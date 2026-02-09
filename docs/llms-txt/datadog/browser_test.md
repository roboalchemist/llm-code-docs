# Source: https://docs.datadoghq.com/getting_started/synthetics/browser_test.md

---
title: Getting Started with Browser Tests
description: >-
  Create Datadog browser tests to monitor user journeys across devices and
  browsers. Record test scenarios, set up alerts, and validate business
  transactions.
breadcrumbs: >-
  Docs > Getting Started > Getting Started with Synthetic Monitoring > Getting
  Started with Browser Tests
---

# Getting Started with Browser Tests

## Overview{% #overview %}

[Browser tests](https://docs.datadoghq.com/synthetics/browser_tests/) are scenarios that Datadog executes on your web applications. You can configure periodic intervals to run tests from multiple locations, devices, and browsers as well as execute them from your CI/CD pipelines. These tests verify that your users can perform **key business transactions** on your applications and that they are not negatively impacted by recent code changes.

## Create a browser test{% #create-a-browser-test %}

The example below demonstrates the creation of a browser test that maps a user's journey from adding an item to a cart to successfully checking out.

### Configure your test details{% #configure-your-test-details %}

1. In the Datadog site, hover over **Digital Experience** in the left hand menu and select **[Tests](https://app.datadoghq.com/synthetics/tests)** (under **Synthetic Monitoring & Testing**).
1. In the top right corner, click **New Test** > **[Browser Test](https://app.datadoghq.com/synthetics/browser/create)**.

You may create a test using one of the following options:

- **Create a test from a template**:

  1. Hover over one of the pre-populated templates and click **View Template**. This opens a side panel displaying pre-populated configuration information, including: Test Details, Alert Conditions, Steps, and optionally Variables.

  1. Click **+Create Test** to open the configuration page, where you can review and edit the pre-populated configuration options. The fields presented are identical to those available when creating a test from scratch.

  1. Click **Save & Quit** in the upper right hand corner to submit your Browser Test.

     {% video
        url="https://datadog-docs.imgix.net/images//synthetics/browser_tests/synthetics_templates_browser.mp4" /%}

- **Build a test from scratch**:

  1. Click the **+** template to start a new Browser Test from scratch.
  1. Add the URL of the website you want to monitor. If you don't know what to start with, you can use `https://www.shopist.io`, a test e-commerce web application.
  1. Select **Advanced Options** to set custom request options, certificates, authentication credentials, and more.
  1. Name your test and set tags to it such as `env:prod` and `app:shopist`. Tags allow you to keep your test suite organized and quickly find tests you're interested in on the homepage.
  1. Choose the browsers and devices you want to test with.
  1. Click **Save & Edit Recording** to submit your Browser Test.

### Select locations{% #select-locations %}

Select one or more **Managed Locations** or **Private Locations** to run your test from.

Managed locations allow you to test public-facing websites and endpoints. To test internal applications or simulate user behavior in discrete geographic regions, use [private locations](https://docs.datadoghq.com/getting_started/synthetics/private_location) instead.

The Shopist application is publicly available at `https://www.shopist.io/`, so you can pick any managed locations to execute your test from.

### Specify test frequency{% #specify-test-frequency %}

Select the frequency at which you want your test to execute. You can leave the default frequency of 1 hour.

In addition to running your Synthetic test on a schedule, you can trigger them manually or directly from your [CI/CD pipelines](https://docs.datadoghq.com/continuous_testing/cicd_integrations).

### Define alert conditions{% #define-alert-conditions %}

You can define alert conditions to ensure your test does not trigger for things like a sporadic network blip, so that you only get alerted in case of real issues with your application.

You can specify the number of consecutive failures that should happen before considering a location failed:

```text
Retry test 2 times after 300 ms in case of failure
```

You can also configure your test to only trigger a notification when your application goes down for a certain amount of time and number of locations. In the below example, the alerting rule is set to send a notification if the test fails for three minutes on two different locations:

```text
An alert is triggered if your test fails for 3 minutes from any 2 of 13 locations
```

### Configure the test monitor{% #configure-the-test-monitor %}

Design your alert message and add an email address you want your test to send alerts to.

{% video
   url="https://datadog-docs.imgix.net/images/getting_started/synthetics/configured-browser-test.mp4" /%}

You can also use [notifications integrations](https://docs.datadoghq.com/integrations/#cat-notification) such as Slack, PagerDuty, Microsoft Teams, and webhooks. In order to trigger a Synthetic alert to these notification tools, you first need to set up the corresponding [integration](https://app.datadoghq.com/account/settings).

When you're ready to save your test configuration and monitor, click **Save & Edit Recording**.

For more information, see [Using Synthetic Test Monitors](https://docs.datadoghq.com/synthetics/guide/synthetic-test-monitors).

## Create recording{% #create-recording %}

Once your test configuration is saved, Datadog prompts you to download and install the [Datadog test recorder](https://chrome.google.com/webstore/detail/datadog-test-recorder/kkbncfpddhdmkfmalecgnphegacgejoa) Chrome extension. (This Chrome extension can also be installed on a Microsoft Edge browser)

Once you have installed the extension, click **Start Recording** to begin recording your test steps.

Navigate through the page in the iframe located on the right of the recorder page. When you select a div, image, or any area of the page, Datadog records and creates the associated step in the browser test.

To end recording your test steps, click **Stop Recording**.

The example below demonstrates how to map a user journey from adding an item to a cart to successfully checking out in `https://www.shopist.io`:

1. Navigate to one of the furniture sections on the example website such as **Chairs** and select **Add to cart**.
1. Click on **Cart** and **Checkout**.
1. Under **Add New**, select **Assertion** and click **"Test that some text is present on the active page"**.
1. To confirm that the words "Thank you!" appear after checking out, enter `Thank you!` in the **Value** field.
1. Press **Save & Quit**.

It is important to finish your browser test with an **Assertion** to ensure your application resulted in the expected state after the defined user journey.

{% video
   url="https://datadog-docs.imgix.net/images/getting_started/synthetics/record-test.mp4" /%}

The example website regularly throws an error causing it to intentionally fail. If you include your email address in the **Configure the monitor for this test** field, you receive an email notification when the test fails and recovers.

## Look at test results{% #look-at-test-results %}

The **Browser Test** details page displays an overview of your test configuration, the global and per location uptime, graphs about time-to-interactive and test duration, sample successful and failed test results, and the list of all test results. Depending on the length of your test, you might have to wait for a few minutes to see the first test results come in.

To troubleshoot a [failed test](https://docs.datadoghq.com/synthetics/browser_tests/test_results#test-failure), select a failed test result and review the screenshots leading up to the failed step. You can also review potential **[Errors & Warnings](https://docs.datadoghq.com/synthetics/browser_tests/test_results#errors)**, **[Resources](https://docs.datadoghq.com/synthetics/browser_tests/test_results#resources)**, and **[Core Web Vitals](https://docs.datadoghq.com/synthetics/browser_tests/test_results#page-performance)** to diagnose the issue.

In the example below, the test failed as the result of a server timeout.

{% video
   url="https://datadog-docs.imgix.net/images/getting_started/synthetics/browser-test-failure.mp4" /%}

Use Datadog's [APM integration with Synthetic Monitoring](https://docs.datadoghq.com/synthetics/apm/) to view traces generated from your backend by the test runs from the **Traces** tab.

## Further Reading{% #further-reading %}

- [Getting Started with Synthetic Browser Testing](https://learn.datadoghq.com/courses/getting-started-with-synthetic-browser-testing)
- [Learn more about browser tests](https://docs.datadoghq.com/synthetics/browser_tests)
- [Learn about private locations](https://docs.datadoghq.com/getting_started/synthetics/private_location)
- [Learn how to trigger Synthetic tests from your CI/CD pipeline](https://docs.datadoghq.com/continuous_testing/cicd_integrations)
- [Learn how to identify Synthetic bots for API tests](https://docs.datadoghq.com/synthetics/identify_synthetics_bots)
- [Learn about Synthetic test monitors](https://docs.datadoghq.com/synthetics/guide/synthetic-test-monitors)

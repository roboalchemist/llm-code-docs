# Source: https://docs.datadoghq.com/getting_started/synthetics/api_test.md

---
title: Getting Started with API Tests
description: >-
  Create Datadog API tests to proactively monitor your endpoints. Build single
  and multistep API tests with assertions, configure alerts, and troubleshoot
  issues.
breadcrumbs: >-
  Docs > Getting Started > Getting Started with Synthetic Monitoring > Getting
  Started with API Tests
---

# Getting Started with API Tests

## Overview{% #overview %}

API tests **proactively monitor** that your **most important services** are available at anytime and from anywhere. [Single API tests](https://docs.datadoghq.com/synthetics/api_tests/) come in eight subtypes that allow you to launch requests on the different network layers of your systems (`HTTP`, `SSL`, `DNS`, `WebSocket`, `TCP`, `UDP`, `ICMP`, and `gRPC`). [Multistep API tests](https://docs.datadoghq.com/synthetics/multistep) enable you to run API tests in sequence to monitor the uptime of key journeys at the API level.

## Create a single API test{% #create-a-single-api-test %}

HTTP tests monitor your API endpoints and alert you when response latency is high or fail to meet any conditions you define, such as expected HTTP status code, response headers, or response body content.

The examples below demonstrate how to create an [HTTP test](https://docs.datadoghq.com/synthetics/api_tests/http_tests), a subtype of [single API tests](https://docs.datadoghq.com/synthetics/api_tests/).

1. In the Datadog site, hover over **Digital Experience** and select **[Tests](https://app.datadoghq.com/synthetics/tests)** (under **Synthetic Monitoring & Testing**).

1. Click **New Test** > **[New API test](https://app.datadoghq.com/synthetics/create)**.

1. You may create a test using one of the following options:

   - **Create a test from a template**:

     1. Hover over one of the pre-populated templates and click **View Template**. This opens a side panel displaying pre-populated configuration information, including: Test Details, Request Details, Assertions, Alert Conditions, and Monitor Settings.
     1. Click **+Create Test** to open the **Define Request** page, where you can review and edit the pre-populated configuration options. The fields presented are identical to those available when creating a test from scratch.
     1. Click **Save Details** to submit your API test.

     {% video
        url="https://datadog-docs.imgix.net/images/getting_started/synthetics/synthetics_templates_api_video.mp4" /%}

   - **Build a test from scratch**:

     1. To build a test from scratch, click the **+ Start from scratch** template, then select the `HTTP` request type.

     1. Add the URL of the endpoint you want to monitor. If you don't know what to start with, you can use `https://www.shopist.io/`, a test e-commerce web application. If you use the test Shopist URL, the name of your test is automatically populated as `Test on shopist.io`.

     1. Optionally, select **Advanced Options** to set custom request options, add certificates and authentication credentials, and create secure [global variables](https://docs.datadoghq.com/synthetics/settings/#global-variables) or [local variables](https://docs.datadoghq.com/synthetics/api_tests/http_tests#variables) for dynamic inputs.

**Note**: Type `{{` in any relevant field to select a variable and inject its value into your test options.

     1. Optionally, set tags such as `env:prod` and `app:shopist` on your test. Tags allow you to keep your test suite organized and quickly find tests you're interested in on the homepage.

     1. Click **Send** to trigger a sample test run.

        {% image
           source="https://datadog-docs.imgix.net/images/getting_started/synthetics/api-test-config-4.7ab513fd164d341c7f31c4749a240ab8.png?auto=format"
           alt="API test configuration" /%}

     1. Click **Create Test** to submit your API test.

### Define assertions{% #define-assertions %}

Clicking **Send** automatically populates basic assertions about your endpoint's response. Assertions define what a successful test run is.

In this example, three default assertions populate after triggering the sample test run:

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/synthetics/assertions-example-2.562bb2c285b25cb409df85212e2cc897.png?auto=format"
   alt="Default assertions" /%}

Assertions are fully customizable. To add a custom assertion, click on elements of the response preview such as the headers or click **New Assertion** to define a new assertion from scratch.

{% video
   url="https://datadog-docs.imgix.net/images/getting_started/synthetics/api-test-configuration-2.mp4" /%}

### Select locations{% #select-locations %}

Select one or more **Managed Locations** or **Private Locations** to run your test from. Datadog's out-of-the-box managed locations allow you to test public-facing websites and endpoints from regions where your customers are located.

**AWS**:

| Americas            | Asia Pacific | EMEA      |
| ------------------- | ------------ | --------- |
| Canada Central      | Hong Kong    | Bahrain   |
| Northern California | Jakarta      | Cape Town |
| Northern Virginia   | Mumbai       | Frankfurt |
| Ohio                | Osaka        | Ireland   |
| Oregon              | Seoul        | London    |
| SÃ£o Paulo           | Singapore    | Milan     |
| Sydney              | Paris        |
| Tokyo               | Stockholm    |

**GCP**:

| Americas    | Asia Pacific | EMEA      |
| ----------- | ------------ | --------- |
| Dallas      | Tokyo        | Frankfurt |
| Los Angeles |
| Oregon      |
| Virginia    |

**Azure**:

| Region   | Location |
| -------- | -------- |
| Americas | Virginia |

The Datadog for Government site (US1-FED) uses the following managed location:

| Region   | Location |
| -------- | -------- |
| Americas | US-West  |

The Shopist application is publicly available at `https://www.shopist.io/`, so you can pick any managed locations to execute your test from. To test internal applications or simulate user behavior in discrete geographic regions, use [private locations](https://docs.datadoghq.com/getting_started/synthetics/private_location) instead.

### Specify test frequency{% #specify-test-frequency %}

Select the frequency at which you want your test to execute. You can leave the default frequency of 1 minute.

In addition to running your Synthetic test on a schedule, you can trigger them manually or directly from your [CI/CD pipelines](https://docs.datadoghq.com/synthetics/ci).

### Define alert conditions{% #define-alert-conditions %}

You can define alert conditions to ensure your test does not trigger for things like a sporadic network blip, so that you only get alerted in case of real issues with your endpoint.

You can specify the number of consecutive failures that should happen before considering a location failed:

```text
Retry test 2 times after 300 ms in case of failure
```

You can also configure your test to only trigger a notification when your endpoint goes down for a certain amount of time and number of locations. In the below example, the alerting rule is set to send a notification if the test fails for three minutes on two different locations:

```text
An alert is triggered if your test fails for 3 minutes from any 2 of 13 locations
```

### Configure the test monitor{% #configure-the-test-monitor %}

Design your alert message and add any email address you want your test to send alerts to. You can also use [notifications integrations](https://docs.datadoghq.com/integrations/#cat-notification) such as Slack, PagerDuty, Microsoft Teams, and webhooks. In order to trigger a Synthetic alert to these notification tools, you first need to set up the corresponding [integration](https://app.datadoghq.com/account/settings).

When you're ready to save your test configuration and monitor, click **Create**.

## Create a multistep API test{% #create-a-multistep-api-test %}

[Multistep API tests](https://docs.datadoghq.com/synthetics/multistep) allow you to monitor key business transactions at the API level.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/synthetics/multistep-api-test.70c5c847b9d8911760b4014bd21dc9b1.png?auto=format"
   alt="Overview of a Mulistep Synthetics API Test" /%}

Similar to [API tests](https://docs.datadoghq.com/synthetics/api_tests/http_tests), multistep API tests alert you when your endpoints become too slow or fail to meet any conditions you defined. You can create variables from individual step responses and re-inject their values in subsequent steps, chaining steps together in a way that mimics the behavior of your application or service.

The example test below demonstrates the creation of a multistep API test that monitors the addition of an item to a cart. This test contains three steps:

- Getting a cart
- Getting a product
- Adding the product to the cart

If you don't know which API endpoints to create your multistep API test on, use the example endpoints below.

To create a new multistep API test, click **New Test** > **[Multistep API test](https://app.datadoghq.com/synthetics/multi-step/create)**. Add a test name such as `Add product to cart`, include tags, and select locations.

### Get a cart{% #get-a-cart %}

1. In **Define steps**, click **Create Your First Step**.

1. Add a name to your step, for example: `Get a cart`.

1. Specify the HTTP method and the URL you want to query. You can enter `POST` and `https://api.shopist.io/carts`.

1. Click **Test URL**. This creates a cart item in the Shopist application's backend.

1. Leave the default assertions or modify them.

1. Optionally, define execution parameters.

Selecting **Continue with test if this step fails** is helpful to ensure a whole endpoint collection is tested or to ensure the last cleanup step is executed, regardless of previous steps' success or failure. The **Retry** step feature is handy in situations where you know your API endpoint may take some time before responding.

In this example, no specific execution parameter is needed.

1. To create a variable out of the value of the cart ID located at the end of the `location` header:

   - Click **Extract a variable from response content**.
   - Name your variable as `CART_ID`.
   - In the **Response Header,** select `location`.
   - In the **Parsing Regex** field, add a regular expression such as `(?:[^\\/](?!(\\|/)))+$`.

   {% image
      source="https://datadog-docs.imgix.net/images/getting_started/synthetics/multistep-test-extract-variables.07cb382bfc1985b98c5395bec17b53b8.png?auto=format"
      alt="Extracted variable from response content" /%}

1. Click **Save Variable**.

1. When you're done creating this test step, click **Save Step**.

### Get a product{% #get-a-product %}

1. In **Define another step**, click **Add Another Step**. By default, you can create up to ten steps.
1. Add a name to your step, for example: `Get a product`.
1. Specify the HTTP method and the URL you want to query. Here, you can add: `GET` and `https://api.shopist.io/products.json`.
1. Click **Test URL**. This retrieves a list of products available in the Shopist application.
1. Leave the default assertions or modify them.
1. Optionally, define execution parameters. In this example, no specific execution parameter is needed.
1. To create a variable out of the product ID located in the response body:
   - Click **Extract a variable from response content**
   - Name your variable as `PRODUCT_ID`.
   - Click the **Response Body** tab.
   - Click on the `$oid` key of any product to generate a JSON Path such as `$[0].id['$oid']`.
1. Click **Save Variable**.
1. When you're done creating this test step, click **Save Step**.

### Add product to cart{% #add-product-to-cart %}

1. Click **Add Another Step** to add the final step, the addition of a product into your cart.

1. Add a name to your step, for example: `Add product to cart`.

1. Specify the HTTP method and the URL you want to query. Here, you can add: `POST` and `https://api.shopist.io/add_item.json`.

1. In the **Request Body** tab, choose the `application/json` body type and insert the following:

   ```java
       {
         "cart_item": {
           "product_id": "{{ PRODUCT_ID }}",
           "amount_paid": 500,
           "quantity": 1
         },
         "cart_id": "{{ CART_ID }}"
       } 
       
```

1. Click **Test URL**. This adds the product you extracted in Step 2 to the cart you created in Step 1 and returns a checkout URL.

1. In **Add assertions (optional)**, click **Response Body** and click the `url` key to have your test assert that the journey finished with a response containing the checkout URL.

1. No execution parameters and variable extractions are needed in this last step.

1. When you're done creating this test step, click **Save Step**.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/synthetics/defined-steps.309a5780de50bf95bbe46752e7d548ad.png?auto=format"
   alt="Created test steps" /%}

You can then configure the rest of your test conditions such as test frequency and alerting conditions, and the test monitor. When you're ready to save your test configuration and monitor, click **Create**.

For more information, see [Using Synthetic Test Monitors](https://docs.datadoghq.com/synthetics/guide/synthetic-test-monitors).

## Look at test results{% #look-at-test-results %}

The **API test** and **Multistep API test detail** pages display an overview of the test configuration, the global uptime associated with the tested endpoints by location, graphs about response time and network timings, and a list of test results and events.

To troubleshoot a failed test, scroll down to **Test Results** and click on a failing test result. Review failed assertions and response details such as status code, response time, and associated headers and body to diagnose the issue.

{% image
   source="https://datadog-docs.imgix.net/images/getting_started/synthetics/api-test-failure-5.a637e745f98c18cf65b9d65d9530f00d.png?auto=format"
   alt="API test failure" /%}

With Datadog's [APM integration with Synthetic Monitoring](https://docs.datadoghq.com/synthetics/apm/), access the root cause of a failed test run by looking at the trace generated from the test run in the **Traces** tab.

## Further Reading{% #further-reading %}

- [Create an API test programmatically](https://docs.datadoghq.com/api/latest/synthetics/#create-an-api-test)
- [Learn more about single API tests](https://docs.datadoghq.com/synthetics/api_tests)
- [Learn about private locations](https://docs.datadoghq.com/getting_started/synthetics/private_location)
- [Learn how to trigger Synthetic tests from your CI/CD pipeline](https://docs.datadoghq.com/continuous_testing/cicd_integrations/)
- [Learn how to identify Synthetic bots for API tests](https://docs.datadoghq.com/synthetics/guide/identify_synthetics_bots)
- [Learn about Synthetic test monitors](https://docs.datadoghq.com/synthetics/guide/synthetic-test-monitors)

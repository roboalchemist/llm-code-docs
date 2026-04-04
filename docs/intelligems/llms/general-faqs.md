# Source: https://docs.intelligems.io/getting-started/general-faqs.md

# General FAQs

## Plan, Capabilities & Access FAQs

<details>

<summary>How much does Intelligems cost?</summary>

Intelligems offers monthly and annual pricing options to meet your organization's needs. Prices vary depending on your store's order volume, what type of tests you'd like to run, and how long you are planning to test with us. Please see our [pricing page](https://intelligems.io/pricing) for more information.

</details>

<details>

<summary>What eCommerce platforms does Intelligems integrate with?</summary>

Currently, Intelligems only supports Shopify stores. However, if you are on another platform and interested in using Intelligems, please [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)! We'd love to keep you updated if this changes in the future.

</details>

<details>

<summary>How long does Intelligems take to set up?</summary>

This depends on a few factors, including:

* What test type or types you are planning to run
* Whether you choose to integrate Intelligems on your own, or have the Intelligems team complete it on your behalf
* What version of Shopify you are on and how many other apps and customizations your store has

That said, if you choose to have Intelligems do the integration, our team typically completes it within 3-5 business days, depending on backlog. If you are starting with something simple like content testing, you can get up and running within about 30 minutes!

</details>

<details>

<summary>What types of tests can I run with Intelligems?</summary>

Intelligems enables organizations to test just about anything on their Shopify store, including themes, page templates, pages, other content, discounts, product pricing, shipping and more.

The types of tests that you can run depend on the plan that you are on, so we recommend checking out our [pricing page](https://intelligems.io/pricing) for a full look at what each plan includes. Please don't hesitate to [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions!

</details>

<details>

<summary>What kind of test should I start with?</summary>

The answer to this depends on your goals! If you are starting with price testing, most of our customers start off by testing the prices across their store or on their most popular product or collection as that will generate the fastest results and the most impact. When running a price test, we usually recommend testing both a lower and a higher price vs. the current price.

If you are more interested in testing around shipping, another popular strategy is to test various free shipping thresholds to see what finds the “sweet spot” of AOV and conversion rate.

You can see more test suggestions [here](https://docs.intelligems.io/getting-started/common-use-cases)!

</details>

<details>

<summary>Can I run multiple tests at once?</summary>

Technically, there is no limit to the number of parallel tests you can have running on Intelligems. Strategically, you run the risk of creating *interference* between your tests if they are running on similar things at similar times.

* For example, maybe you are testing pricing on a particular product while also testing the layout of the PDP. You may see these as two separate tests, but in reality customers are being exposed to both. So you end up with a combination of experiences that you don’t have full visibility into since visitors are being randomly assigned within each test.

To control for interference, you can:

1. Set this up as one large test. Make a group for each combination of variables so that you can properly measure and compare (a multivariate test). You **can** have multiple products in the same test, which would keep users in the same group across all products being tested.
2. Run tests sequentially, one after another
3. Use our [Mutually Exclusive Experiments](https://docs.intelligems.io/content-testing/targeting/mutually-exclusive-experiments) feature (beta). If you don't see this as an option in your test setup, please [contact us](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'll enable it.

Exceptions: You can run tests in parallel if there is *not meaningful overlap in their impact to the customer experience.*

* For example, if you wanted to test a PDP layout for one product, and separately have a test running on a landing page for a completely different product and funnel - that should have minimal interference, as the customers won’t likely experience both.
* Or if you ran a pricing test on women’s underwear at the same time you were testing men’s overcoats - those are likely to be pretty distinct sets of customers who won’t be exposed to both tests.

Note: We do only allow *one shipping test at a time* for technical reasons.

</details>

<details>

<summary>Will Intelligems continue to function if I update to Shopify's One-page checkout?</summary>

Overall, yes. Intelligems will continue to function if you update to Shopify's One-page checkout! That said, the full answer depends on the type of test you are looking at:

**Price Test:** this will continue to work seamlessly! If you are on Shopify Plus, please ensure that your Line Item script still includes our Checkout Script. Note that hiding the added discount on the One-page checkout won't be possible, but we can customize the discount's name to your preference.

**Shipping Test:** Intelligems will continue to operate without issues.

**Content Test:** Running content tests on the One-page checkout isn't possible as it doesn't utilize the checkout.liquid file and doesn't allow third-party alterations. However, you can continue to run content tests on the rest of your site without any issues. You can read further about this [here](https://docs.intelligems.io/faqs/content-testing-faqs#can-i-test-the-new-shopify-checkout-vs.-the-old-shopify-checkout-or-test-specific-components-on-the).

</details>

<details>

<summary>Why does Intelligems need collaborator access to your store?</summary>

Intelligems may ask for Shopify collaborator access for a few reasons:

1. To complete the integration on your behalf. The integration requires a few theme changes or other Shopify configurations to be made, so we need access to your Shopify account to complete those.
2. To help troubleshoot. If something is not working as expected, it is helpful for our team to have access to your Shopify account to solve the issue quickly.
3. To take a look at your analytics. This helps us understand if there are an discrepancies with the data we have captured.

**Permissions Intelligems requires:**

* **Orders:** Necessary to track test impact data such as AOV, product mix, etc.
* **Products:** Necessary to find detail on products and variants that will be part of a test.
* **Apps:** Necessary to access Shopify Checkout Scripts, in addition to apps that may play a role in things like managing the cart, collections pages, reviews, etc., which need to be updated as part of a test.
* **Online Store Themes:** Necessary to duplicate a theme and update the code to integrate a test.
* **Settings & Locations:** Necessary to run shipping tests and install Intelligems as a third party rate carrier.

**Permissions Intelligems prefers to have:**

* **Discounts:** In general, we want to be aware of what discounts may be impacting products that are in the test. Note that this is required if we are duplicating products.
* **Customers/Reports/Dashboards:** Helpful to (a) check our data vs. historical data, and (b) confirm there are no discrepancies between the data we are presenting vs. what you see in Shopify.

**Permissions Intelligems does not request access to:**

* Apps developed for you
* Marketing / gift cards
* Edit Orders / Draft Orders

</details>

<details>

<summary>How can I add or remove users from my Intelligems account?</summary>

The easiest way to access Intelligems is directly through Shopify - you can find us by clicking on Apps in the left hand navigation menu -> searching for Intelligems and selecting our app. Anyone who has the permissions to access apps in Shopify should be able to log in that way - you can add users via the Shopify admin by going to Settings -> Users and Permissions -> Add staff. Be sure to give the user permission to manage Intelligems in the App permissions section. If you need to remove users from Intelligems, you can do so by removing that permission. Please see [Shopify's documentation](https://help.shopify.com/en/manual/your-account/staff-accounts/staff-permissions/staff-permissions-descriptions#apps-and-channels-permissions) for additional details.

In the rare case that you would like to provide a user access to Intelligems, but will not be providing them access to Shopify, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we can help get that set up.

</details>

<details>

<summary>I'm upgrading to Checkout Extensibility, is there anything I need to do to ensure Intelligems continues to operate correctly? And will current test results be impacted at all?</summary>

There are no additional steps you need to take to ensure Intelligems continues to operate as expected when upgrading to Checkout Extensibility.\
\
There'll be no impact to any test results, or any Content, Shipping, or Offers tests when updating.\
\
While there is no impact on price tests or their results, there *will* be a visible discount on the checkout page if using our Checkout Script to manipulate prices.\
\
To remove the discount, you'll need to upgrade to Shopify Functions.\
\
Please reach out to support for help with updating to Shopify Functions at <support@intelligems.io>

</details>

<details>

<summary>I'm changing my site's primary URL domain – what do I need to do in Intelligems?</summary>

As long as your Shopify Shop ID remains the same, the only change in Intelligems that you need to make will be updating your domain name in the settings page of the app. If additional changes are being made to the store that affect the Shop ID, please reach out to our Support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request). Please note that after a domain change all visitors to tests will be considered 'new' for targeting purposes, so we would recommend ending any ongoing tests and restarting them after the domain migration.

</details>

## Testing FAQs

<details>

<summary>Can I schedule tests to start, pause or end at a specific time?</summary>

Yes! Intelligems allows you to schedule start times for all types of tests, including Price, Shipping, Content and Campaigns. Intelligems also allows you to schedule pause and end times for Content and Campaigns tests, but does not currently support scheduling pause or end times for Price or Shipping tests due to rollout requirements for ending those types of tests.

To schedule a start, pause or end time, follow these steps:

1. Click on the More Options menu (the three dots) next to the test you'd like to set up a schedule for.
2. Click "Schedule Test". If you do not see this option, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to request this feature be turned on for your account!

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252Fb1iV3NkWAvi1iCWgT722%252FScreenshot%25202024-04-05%2520at%25202.04.15%2520PM.png%3Falt%3Dmedia%26token%3Dc231fcef-f2b1-4bc8-b57c-8f9d856be711&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=9ed7787376137fbce7ca29d7716e4df4dc83811ffa53bf14eddc6d04a47b66a9" alt="" width="188"><figcaption></figcaption></figure>
3. If you are setting up a schedule for a test that has not yet been started, this will open a modal that will ask you to confirm that you have completed the integration & QA'd your test. If you have not already done so, please be sure to complete both of these items before proceeding.

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FJwGgBJ4bT4PXiWWVkql8%252FScreenshot%25202024-04-05%2520at%25202.06.27%2520PM.png%3Falt%3Dmedia%26token%3Dde83ed63-fb26-440b-8e73-170b8c4edab5&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4a0d2e87a2412702919f5155c98fe4932a63889981c8f0670056415a789bc1fb" alt="" width="188"><figcaption></figcaption></figure>
4. Once you have confirmed those items are complete, you'll be taken to a modal where you can set up a scheduled start, pause, and/or end time.

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FPTOfvHS8CvqNwzUWv1XH%252FScreenshot%25202024-04-05%2520at%25202.07.20%2520PM.png%3Falt%3Dmedia%26token%3D68ee23c6-ae45-4e30-b280-b0089da0f41b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=eb9636b9e695b4376c8c2219ba36eb5275f620eff3905c74f38c564277d42454" alt="" width="188"><figcaption></figcaption></figure>

A few things to keep in mind as you set these up:

1. You must schedule items for times in the future only.
2. Test can only be scheduled at 5 minute increments.
3. The times will be based off of your device's current time zone, which will also be listed at the top of the modal.
4. You can only schedule pause and end times for Content and Campaign tests that are either live, or that have a scheduled start time.
5. Once you have scheduled a test to start, pause or end at a specific time, you'll see a clock symbol next to the status, and will be able to hover over that to get more information on the scheduled times like in the below screenshot.

   <figure><img src="https://docs.intelligems.io/~gitbook/image?url=https%3A%2F%2F2052204893-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F2SvefuMLsJyJPAcVXeWc%252Fuploads%252FKWt85JpzNEkCCzgg1y2X%252FScreenshot%25202024-04-05%2520at%25202.01.38%2520PM.png%3Falt%3Dmedia%26token%3Dc8b909a9-0938-4e8d-8fe3-bcfa395608b6&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f53e04bac5dbbd62ffeb94278f86eb116eb99a28cb541bf4ebba36c72416bd79" alt="" width="188"><figcaption></figcaption></figure>

</details>

<details>

<summary>Can I restart a test that I accidentally ended?</summary>

The Intelligems Support Team can help set your ended Content, Price or Offer test back to a paused status, which will allow you to resume the test. We are not able to restart shipping tests due to technical reasons. Please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help with this!

</details>

<details>

<summary>How long does it take to run a test? When should I end my test?</summary>

Determining how long to run a test relies on 3 major things:

1. How big is the effect of this change? The smaller the effect, the harder it is to detect and be certain that the result is not just noise.
2. How many people visit your website every day, and more specifically, how many orders are being placed in a day?
3. How confident do you want to be? The more confident you want to be, the more data you need.

***Our rule of thumb is that if you want to detect a 10% change in conversion with 90% confidence, you need about 300 orders per group.***

* Smaller changes will likely require more data to pick out the signal from the noise
* Larger changes will likely require less data to see a significant pattern

Here are the steps we recommend you take when your test goes live to monitor results and determine when to end the test:

1. Always check in on your test after \~4 hours to make sure your data is flowing - this can be a helpful time to catch any errors in the test configuration (don't launch a test end of day on a Friday, when you won't be able to monitor it)
2. Try not to end any tests before a full week. This allows you to observe a mix of weekdays and weekends, and early results often change.
3. Take a look at the "Time Series" in the Key Metrics dashboard. Have those charts shown consistent results, or are they still varying from day to day? If there is still a lot of variability, it may make sense to run the test for a few more days.
4. Once a week has passed, you can check the “statistical significance” tab to get a read on the “probability to be best” for each group. Check out our [article on statistical significance](https://docs.intelligems.io/analytics/experiment-analytics/statistical-significance) to understand what you are looking for here!
5. You should have a risk tolerance in your head.

* You can wait for everything to hit 95 or 99% confidence, but for smaller brands, that means a lot of time waiting around for results. Waiting around presents a big *opportunity cost* since you are not running other tests - which could be delivering more value! - during that time
* We wouldn’t recommend making decisions with less than 75% confidence
* Many of our customers look for confidence somewhere around 90%

Some tests will not ever hit confidence - they’ll waffle around in the 40-60% range - that means there is *no real difference between the versions*. At that point, pick one to move forward with based on intuition or other strategic considerations, and move on

***Pro tip***: you’re able to change traffic allocation in the middle of a test. So if you have one group that is a clear loser, you can “shut it off” in the middle of your test and send more traffic to the more viable options.

</details>

<details>

<summary>How do I edit something in a live test?</summary>

There are a few steps to safely edit your live test:

**Step 1: Pause your test.**

The pause button can be found next to the status column within your `A/B Tests` overview tab.

*If you are pausing a shipping test,* we will automatically restore your shipping profiles while the test is paused.

*If you are pausing a price test,* we will ask you to select which prices you would like to roll out while the test is paused.

**Step 2: Make your edits.**

The edit button can be found under the three dots to the right of your test. Select this and make any changes you need, such as adding a new product, removing a test group (you can do this by allocating 0% of traffic to that group), changing a price, or changing a shipping rate. Make sure you click through the entire edit flow and select the save button at the end to save your changes!

**Step 3: Resume your test.**

Now that you've made your edits, you can resume your test and keep getting results! The button to do so is right next to the test status.

Keep your edits in mind when looking at the analytics dashboard if the change may have affected the results. Once a test has started, test group names cannot be changed and you can no longer add/remove test groups, but you can set traffic to 0% for a group to effectively remove that group from the test. We do this so that analytics are maintained for that old group that now has no traffic going to it. You can filter your results by date to see the results before and/or after edits were made.

</details>

<details>

<summary>How does the test status work in the test dashboard?</summary>

There are several different statuses that a test can have:

1. Pending: You've set this test up, but have not yet started it.
2. Gathering Data: You've started this test within the last 21 days.
3. Ready For Analysis: This test has been running for at least 21 days. While this is a good baseline, there is ultimately no general rule on time. That said, we often start seeing significant results after about 300 orders *per group*.
4. Paused: You've paused this test; it is not active on the site, but you can resume it.
5. Ended: You've ended this test.

</details>

<details>

<summary>What will my orders look like in Shopify?</summary>

Customers on your site will not see anything to indicate that an Intelligems test is running, but there are a few ways that Intelligems will show up on orders within your Shopify admin portal:

1. Each visitor gets tagged with a unique id that sorts them into a group. This id is passed to the order via [cart.attribute](https://shopify.dev/api/liquid/objects/cart) for tracking purposes and will show under “Additional Details” on the order page. This is hidden from the customer. If this causes any issues for your order forms, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we are able to remove this.
2. We also add each user's test group IDs to the order via [cart.attribute](https://shopify.dev/api/liquid/objects/cart) for tracking purposes and will show under “Additional Details” on the order page. This is hidden from the customer.
3. For Price Testing, we add a line\_item.property to each item equal to the price of that item for that customer. In most cases, this Line Item Property will be titled "\_igp". This is hidden from the customer.
4. For Shipping Testing, we add a line\_item.property to each item equal to the test group ID so that we are able to provide the correct shipping rate for their test group. This is hidden from the customer.
5. If you are using our Checkout Script integration for Price Testing, the Checkout Script applies a “[line-item discount](https://help.shopify.com/en/manual/sell-in-person/shopify-pos/discount-management/line-item-discount)” in order to generate the correct price for a customer’s product. While this shows as a discount in the admin view, this is always hidden from the customer (i.e. in this case they would just see “$13.99” for the product price).

Here is an example of what an order would look like in Shopify:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0c1cbb373b27d102650d9a530c8c30835c763e8a%2FScreenshot%202025-02-14%20at%2010.16.21%20AM.png?alt=media" alt="" data-size="original">

</details>

<details>

<summary>Why does the "Additional Details" section on my Shopify orders contain a random string of numbers &#x26; letters that starts with "ig_"?</summary>

That is the Intelligems ID that we have assigned to that user as this is what allows us to track the visitor and their activity. We add it as a cart attribute (if you look at an order's JSON on Shopify, its the field ​`note­_attributes`​) - this is something that many apps do when they need to add extra information to an order.

In most cases, this additional note should be harmless. However, if it is impacting another software that you use (such as a fulfillment software), Intelligems only needs the Intelligems ID to be there on order creation - we do not need it to *remain* on the order. Because of this, you can set up a [Shopify Flow](https://help.shopify.com/en/manual/shopify-flow) to remove it, and that would fix the problem while retaining the data for Intelligems.

</details>

<details>

<summary>What happens while a test is paused?</summary>

Visitors who were already part of a test group won't see the content of that test while its paused, but they will remain in the same test group. When the test is unpaused, they will resume seeing the test content. This is true for all test types.\
\
Conversions that take place during a paused period never count even if the test is later unpaused.

</details>

<details>

<summary>Will testing through Intelligems affect my SEO?</summary>

No, Intelligems' tests do not impact your store's SEO. Our platform is designed to run tests without affecting search engine rankings or visibility.

We detect all major bots and will block execution when one is detected - this ensures that the bot will see the page *without* intelligems running, which avoids SEO impact. For Price Tests, it also means the bots will see the price of the item as listed in Shopify and not a particular test group.

</details>

<details>

<summary>Can I test across domains or stores?</summary>

Yes! Intelligems supports registering multiple domains for brands operating several domains under one Shopify account (e.g., yourbrand.com and yourbrand.co.uk).

**To add multiple domains:**

1. Navigate to the Settings page in the Intelligems app
2. In the Domain Settings section, click "Add Domain" to register additional domains
3. All registered domains will appear in a list where you can manage them

**What this enables:**

* Run Split URL tests on any of your registered domains
* Set up subdomain redirects for each domain (e.g., yourbrand.com → try.yourbrand.com AND yourbrand.co.uk → try.yourbrand.co.uk)

**Current limitations:**

* Cross-domain redirects are not supported. Visitors cannot be redirected from one top-level domain to another (e.g., yourbrand.com → yourbrand.co.uk will not work)
* Visitor assignments and tracking do not persist across different domains
* Each domain's tests operate independently

**Alternative approaches:**

* Use subdomains instead of separate domains when possible (e.g., shop.yourbrand.com vs yourbrand.com)
* Focus on single-domain user journeys within each registered domain to get meaningful test results

</details>

<details>

<summary>How to Identify the Test Group of a Live Test</summary>

Use the Intelligems JavaScript API to check which test group a user is assigned to in a live test.

**Key Steps:**

1. Get your experiment ID from the test dashboard (Show Info → Test ID)
2. Open JavaScript Console (`Cmd+Option+J` Mac / `Ctrl+Shift+J` Windows)
3. Use: `window.igData?.user.getTestGroup("your-test-id-here")`
4. Review the returned group assignment

**What to verify:** Function returns the correct test group name or `null` if no assignment.

<https://www.loom.com/share/231ab61adca7484b91417d72b55c765c>

&#x20;

</details>

## Integration FAQs

<details>

<summary>What analytics platforms does Intelligems integrate with?</summary>

While Intelligems' analytics dashboards are quite robust, we also currently have an [integration with GA4](https://docs.intelligems.io/analytics/google-analytics-4-integration) if you prefer to take a look at your testing data there. Additionally, we have [integrations with several heatmapping tools](https://docs.intelligems.io/developer-resources/heatmap-integrations), including Microsoft Clarify, Heatmap.com and Hotjar. You can enable these integrations in the [integrations tab](https://app.intelligems.io/integrations) in the Intelligems app!

</details>

<details>

<summary>What page builders does Intelligems integrate with?</summary>

Intelligems has experience integrating with various page builders for different types of testing. Below are some specific page builders our brands have tested with, along with details on the integration requirements for each. If you are using a page builder that is not listed below, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions on integrating with those pages!

1. **Replo:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file. If there are any files in the layout for Replo, our script should be added there as well. If you will be Price Testing, please follow [this guide](https://docs.intelligems.io/getting-started/pricing-integration-guides/replo-page-builder) to integrate your Replo pages - this step is not necessary if you will only be content testing.
2. **Gempages:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Gempage layout files. These pages are also compatible with Price Testing, and should be integrated by following [these steps](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices) - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you need help completing this.
3. **Shogun:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Shogun layout files. These pages are also compatible with Price Testing, and should be integrated by following [these steps](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices) - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you need help completing this.
4. **Pagedeck:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Head Scripts section in the Pagedeck app. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a Pagedeck page so we can help scope this out!
5. **PageFly:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the PageFly layout files. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a PageFly page so we can help scope this out!
6. **Funnelish:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Custom CSS / JS > Head HTML section in the Funnelish app. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a Funnelish page so we can help scope this out!
7. **Webflow:** Typically works out of the box for Content Testing once the [Intelligems JavaScript](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) has been added to your theme.liquid file & to the Webflow layout files. These pages may not be compatible with Price Testing - please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you are interested in testing prices on a Webflow page so we can help scope this out!
8. **Builder.io:** These pages are typically built using the Storefront API, which is Headless & can cause complexities. If you are using Builder.io, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to discuss what will be possible.

</details>

<details>

<summary>What cart apps does Intelligems integrate with for Price Testing?</summary>

Intelligems has experience integrating with various cart apps for different types of testing. Below are some specific cart apps our brands have tested with, along with details on the integration requirements for each. If you are using a cart app that is not listed below, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions on integrating with that app!

1. **Rebuy:** Rebuy works with Price Testing out of the box. Prices of products that have been added to cart will be updated via a Checkout Script, Shopify Function or Duplicate Product, depending on which integration you are using. If you are using Rebuy upsells in your cart, those prices will need to be [tagged](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices) in order to be updated correctly. If you have any questions on this, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
2. **Monster Cart Upsell:** Monster Cart Upsell is not compatible with Checkout Scripts - because of this, if you are using this cart app, you are only eligible for our Duplicate Product integration. If you have any questions on this, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
3. **UpCart:** UpCart works with Price Testing out of the box. Prices of products that have been added to cart will be updated via a Checkout Script, Shopify Function or Duplicate Product, depending on which integration you are using. That said, there are two limitations when using UpCart:
   1. Compare prices, discount tags, discount percentages & line item properties must either be hidden or shown incorrectly as UpCart does not allow Intelligems to manipulate these items
   2. You will not be eligible for our Checkout Script integration
4. **Slide Cart by AMP:** Slide Cart by AMP does require a few extra integration steps to hide the strikethrough prices & discounts - our guide on these steps can be found [here](https://intelligems.notion.site/Integrations-Slide-Cart-by-AMP-854ccb8e6b024c9d9770d41be78727a2?pvs=4). If you have any questions on this, please reach out to our team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!

</details>

<details>

<summary>I see an error associated with Intelligems under "Checkout Rules" — what does this mean?</summary>

You may see an error under Intelligems' checkout extension that says, "There were errors during checkout. Some customers have abandoned checkout."

This indicates there was at least one recent error in processing that may have caused an issue in completing checkout. While this of course sounds concerning, almost always, there were no issues encountered by real customers.

Many Shopify stores are visited by automated bots that scrape various data, including product inventory. One of the ways they record inventory data is to add very large numbers of each product to cart and attempt to checkout until they get out of stock errors. These large carts, often containing nearly the entire product catalog, can cause timeouts from the Intelligems function that show up here.

If you'd like Intelligems to investigate the errors, please [share error reports](https://shopify.dev/docs/apps/build/functions/monitoring-and-errors#sharing-an-error-report) with Intelligems through the Shopify admin, then [reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'll review the logs.

</details>

## Preview FAQs

<details>

<summary>Can I preview a Shopify theme and Intelligems test at the same time?</summary>

Yes, you can! This is a very common practice we use here at Intelligems. You can do this by entering preview mode for your theme and then entering preview mode for your test. The theme should be cached when you open your test preview.

</details>

<details>

<summary>How to Block Intelligems from Running Locally</summary>

Temporarily disable Intelligems on your browser to troubleshoot issues or test baseline functionality.

**Key Steps:**

1. Open Chrome Developer Tools → Network tab (`F12` or `Cmd+Option+I` Mac / `Ctrl+Shift+I` Windows)
2. Filter for "intelligems" and refresh the page
3. Right-click `bundle.js` and select "Block Request URL"
4. Refresh page to test without Intelligems running
5. **Important:** Unblock when finished testing

**What to verify:** Intelligems widget disappears when blocked, reappears when unblocked.

<https://www.loom.com/share/fbf21e4ba1c642e3b4558feb5817535c>

</details>

## Traffic FAQs

<details>

<summary>How does Intelligems split the traffic and keep users in the same test group for the entirety of the test?</summary>

All of our tests are run as true split tests where we segment your traffic in real time between test variants. Intelligems randomly assigns users to a test group when they visit your site for the first time during a test.

Intelligems then saves a unique string of numbers and letters know as the Intelligems ID in a first-party cookie, which we then use to remember your site visitors and keep them in the same test group(s) for the entirety of your test(s). Because of this, every time they come back to the site on the same browser on the same device, the user will have a consistent experience.

Cookies do expire - when they expire depends somewhat on the browser, since different browsers have different max allowed cookie ages. For example, on Chrome, our cookie life is about 1 year. On Safari (including all iOS browsers), cookies are deleted if the user does not visit the site for 7 days.

</details>

<details>

<summary>How does Intelligems handle customers who switch devices?</summary>

Intelligems randomly assigns users to a test group when they visit your site for the first time during a test. We then use a cookie to ensure they remain in the same test group every time they come back to the site on the same browser and device.

When a user visits your site on a new device, we cannot rely on that cookie to place them in the same group, so there is a chance they will end up in a different group. That said, in our testing, we have found that less than 1% of typical site traffic may be impacted by switching devices during a test.

We recommend making your customer support team aware of any tests you may be running, and in the rare case that a customer does switch devices and notices a differing price, having a plan of action (such as a discount code) to create a positive customer experience.

</details>

## Targeting FAQs

<details>

<summary>Can I filter out blog traffic from my test(s)?</summary>

Yes! Some brands use their blog pages for SEO. This generates a lot of traffic for their site, but does not result in many conversions or revenue. Because of this, blog traffic can create a lot of noise in analytics, therefore it might be better to filter blog traffic out of your tests to keep your results clean and actionable. If you do not have any UTMs set up for your blog pages, this article will walk you through how you can exclude that traffic from your test.

**Step 1: Add snippet to theme.liquid file.**

Add the below code to your theme.liquid file directly above your Intelligems JavaScript snippet. An example Intelligems JavaScript snippet is included at the bottom of the snippet below to illustrate where the new snippet should be placed.

```liquid
<script>
if (window.history.pushState && window.location.pathname.includes('blog')) {
                    const newURL = new URL(window.location.href);
                    newURL.search = '?blog=1';
                    window.history.pushState({ path: newURL.href }, '', newURL.href);
}
</script>
<script src="https://cdn.intelligems.io/<your_customer_id>.js"></script>
```

**Step 2: Set up UTM filter.**

Set up the below Audience Targeting on your test. Note that this will need to be added to **each test that you want to exclude blog traffic**, and **will only exclude that traffic moving forward.**

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5613a70143eca9f422ec29f647d7bfa8967b59cd%2Fimage%20\(37\).png?alt=media)

</details>

<details>

<summary>How can I force myself into a specific test group?</summary>

You can force yourself into a specific test group by adding the below to the end of your site's URL:

`/?igTg=TEST-GROUP-ID`

where `TEST-GROUP-ID` is the ID for the test group you would like to be forced into. You can find the test group ID by heading to the A/B Tests tab in the Intelligems app, clicking on the three dots / more options menu next to the test you are working on, and selecting "Show Info". This will bring up the experiment ID, as well as the test group ID for each test group. Click on the long ID for the group you'd like to be forced into to copy it to your clipboard.

The final results should look something like this:

`www.mywebsite.com/?igTg=44bae2e6-dbc3-4fc1-a68d-4218ac04f99c`

</details>

<details>

<summary>Will Intelligems remove UTM parameters when a visitor lands on my site and is part of a test?</summary>

No, UTM parameters won't be removed from your URLs by Intelligems! While there are a few test types that involve redirects, such as Theme, Template and Split URL Tests, URL parameters are persisted, and therefore traffic attribution is preserved.

</details>

<details>

<summary>How do I target or exclude new vs. returning customers?</summary>

Targeting new vs. returning customers is a bit tricky because Shopify does not share whether a customer is new or returning with Intelligems. There are, however, a few ways you can set up audience targeting to help target or exclude new vs. returning visitors.

The first option is to use UTM parameters. To target only new visitors, we typically recommend applying the test to users visiting the site through specific UTM or media campaigns that you use for targeting new customers. There is a small chance that returning customers could come in through these campaigns.

The second option is to use our New / Returning Visitor targeting. It is important to note that this is looking at whether someone is a new or returning *visitor*, and not necessarily whether they are a new or returning *customer*. It is also important to note that we determine whether a visitor is new or returning based off of whether they have an Intelligems ID assigned to them. We assign all site visitors an Intelligems ID when they come to your site, as long as our JavaScript is in your live site. Because of this, if you have just started working with Intelligems, most visitors will be seen as new since they don't have an Intelligems ID assigned to them yet.

Both of these options can be set up in the Targeting step of test set up, which you can read more about [here](https://docs.intelligems.io/content-testing/targeting#what-is-intelligems-audience-targeting).

</details>

## Uninstalling FAQs

<details>

<summary>Can I remove the Intelligems script once my test is complete?</summary>

While there are technically no issues with removing the Intelligems script from your site once your test is complete, we only recommend doing so in the rare case that the site is experiencing performance issues. Otherwise, we recommend leaving the lightweight script installed in your theme as testing shouldn't be one-and-done. We find that stores that approach testing with a roadmap and plan are the stores that unlock the most value. If you are stuck on coming up with an idea on what to test next, check out [this article!](https://docs.intelligems.io/getting-started/common-use-cases)

Additionally, keeping the Intelligems script installed on your store allows Intelligems to continue assigning users an Intelligems ID - this will make New vs. Returning Visitor targeting much more powerful.

If you do need to remove the Intelligems script from your site, delete or comment it out in your theme.liquid file. For Shopify Plus customers, this may also be located in your checkout.liquid file. The JavaScript to remove or comment out will look something like this:

```
<script src="https://cdn.intelligems.io/<your_customer_id>.js"></script>
```

</details>

<details>

<summary>How do I uninstall Intelligems?</summary>

✨ We'd hate to see you go! If you plan on testing again any time in the future, we recommend moving to a Pause Plan instead of uninstalling. This will allow you to keep the integration live so it's easy to start a new test down the road, as well as maintain access to the analytics from any tests you've already run. If this sounds like a better option, you can do this from the Settings page of the Intelligems app. If you don't see the option there, please reach out to <billing@intelligems.io> to get set up with a Pause Plan.

{% hint style="info" %}
Note: We do *not* recommend uninstalling and reinstalling the app as a technical troubleshooting step, as this will cause you to be charged again for the new installation. If you're experiencing an issue with the app or with a test, please reach out to <support@intelligems.io> for assistance.
{% endhint %}

**Step 1: Stop any tests.**

Confirm that you've stopped any tests or campaigns from within the app! You'll want to make sure you also rolled out the winners while doing this - see more details on how to end a [Price Test](https://help.intelligems.io/how-to-end-price-tests) and a [Shipping Test](https://help.intelligems.io/ending-a-shipping-test) at each of those links.

**Step 2: Uninstall the app via Shopify.**

Follow Shopify's steps [here](https://help.shopify.com/en/manual/apps/uninstalling-apps#uninstall-app) to uninstall the Intelligems app - this will cancel billing.

**Step 3: Remove Intelligems JavaScript.**

During the integration, you or the Intelligems team added JavaScript as a source into your theme.liquid file - you can now remove the Intelligems script from your site. To do so, delete or comment it out in your theme.liquid file. For Shopify Plus customers, this may also be located in your checkout.liquid file. The JavaScript to remove or comment out will look like this:

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-56b581da7daa58252fa1d1c8f05b4455592a9d1f%2FScreenshot%202024-02-06%20at%203.50.14%20PM.png?alt=media" alt="" data-size="original">

❗Note that if you do not complete this step, we will continue to append an igId onto your orders in the 'Additional Details' section in Shopify. Customers will not see this, and it will not cause any issues, but may cause confusion for your team if they do not know where it is coming from!

**Step 4: Remove Checkout Script&#x20;*****or*****&#x20;manage Duplicate Products, if applicable.**

❗This step is only applicable if you have run Price Tests!

***If you are on Shopify Plus and ran your test using a Checkout Script,*** you can now stop that script by either unpublishing the entire Checkout Script (if nothing else is in it), or by removing the Intelligems script if you use the Checkout Script for anything else.

***If you are not on Shopify Plus and ran your test using Duplicate Products,*** confirm those products are archived. See more details on managing Duplicate Products from previous tests [here](https://help.intelligems.io/can-i-delete-duplicate-products-once-a-pricing-test-is-over).

**Step 5: Remove Intelligems as a shipping rate provider, if applicable.**

❗This step is only applicable if you have run Shipping Tests!

Confirm that Intelligems is removed as a shipping rate provider. You can check this by going to your Settings in Shopify → Shipping and delivery → Manage by General Shipping Rates. Once you're there, confirm that 'Intelligems Shipping (Rates provided by app)' is not listed anywhere. If it is, please delete it using the three dots to the right and add your own rate to replace it if needed.

**Step 6: Send us your feedback!**

We are always looking to make improvements to our platform and processes! If there is something we could have done better, you have feature requests, or you just want to chat all things ecomm, please don't hesitate to reach out to <support@intelligems.io>.

</details>

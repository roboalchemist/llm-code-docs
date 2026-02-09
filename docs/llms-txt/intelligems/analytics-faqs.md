# Source: https://docs.intelligems.io/analytics/analytics-faqs.md

# Analytics FAQs

<details>

<summary>I just started an experiment. How long does it take to see results in the analytics dashboard?</summary>

Data will arrive in nearly real-time, but there may be occasional delays. You should see data on visitors within about 30-60 seconds of their entrance into the experiment. Data on orders may take a little bit longer — generally they should appear within about 1 minute of the order being placed.

If you're not seeing data yet and have just started an experiment, the reason may be exclusions. Visitors who started their browsing session before an experiment started (i.e., they were "mid-session" when the experiment started) are excluded from analytics, as are visitors who have opened the experiment in Intelligems' preview mode. See more about these default filters [here](https://docs.intelligems.io/experiment-analytics/filters#default-filters).

</details>

<details>

<summary>Why doesn't the data align with Shopify or Google Analytics?</summary>

There are a few reasons why the data won't align perfectly with Shopify or GA in a given moment in time:

* Intelligems shows data in nearly real-time, while Shopify and Google analytics typically have a lag of up to 1 day
* Intelligems tracks conversion based on *visitors* instead of *sessions.* See more [here](https://docs.intelligems.io/analytics/experiment-analytics/metric-definitions/conversion-funnel)
* By default, Intelligems filters out "outlier" orders (more than 3 standard deviations from the mean) to prevent rare, anomalously large orders skewing experiment results. See more [here](https://docs.intelligems.io/experiment-analytics/filters#filters-pane) under "Z-Score"
* Intelligems includes only orders that are placed by visitors who were exposed to an experiment. This typically excludes orders outside of the "Online Store" sales channel (e.g. draft orders, subscription refills, app orders like Tapcart, etc.)
* Intelligems cannot track orders through some quick checkout buttons, e.g., "Buy with Prime" — see the FAQ below this for more information on this
* The dashboard may be filtered to "orders with target products" (i.e., orders with at least one product targeted by the experiment). See more [here](https://docs.intelligems.io/experiment-analytics/filters#filters-pane) under "Filter Orders by Product"
* If your test uses [audience or page targeting](https://docs.intelligems.io/analytics/experiment-analytics/how-experiment-targeting-affects-analytics), only users who passed the targeting rules would have entered the test, and therefore the results. This includes targeting based on currency or location, UTMs, device types, whether they are new or returning, or whether they have hit a page you are targeting in the test. See more [here](https://docs.intelligems.io/analytics/experiment-analytics/how-experiment-targeting-affects-analytics)
* For Split URL and template tests, which are naturally focused on a specific set of pages, visitors enter the experiment only once they have visited one of the origin pages (typically, this is the control page). Visitors who did not reach one of these pages would not be included in analytics. See more [here](https://docs.intelligems.io/experiment-analytics/how-experiment-targeting-affects-analytics#split-url-and-template-tests)
* For Split URL tests specifically, you may notice a discrepancy between Intelligems and Shopify's "Landing Page" reporting. When a visitor lands on an origin page and redirects them to one of the test pages, that redirect executes client-side. Shopify may register the origin page as the landing page for these visitors, even though they are immediately redirected to a test page. This makes the landing page reporting unreliable during the duration of the experiment, and there it cannot be compared to Intelligems' test group reporting. We strongly recommend relying on Intelligems' reporting, rather than Shopify's, to analyze these experiments in particular

If you still think the numbers don't align, [please send a few screenshots](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) of what you're seeing in Shopify or another analytics app, and what test results you are looking at, and we can help look into it.

</details>

<details>

<summary>How does Intelligems track conversion rate?</summary>

Intelligems tracks our conversion rates based off of *visitors* instead of *sessions*.

Here's the difference between the two:\
In Shopify, sessions are the total number of interaction periods a user has with a store, while visitors are the total number of unique people who access the website:

**Sessions**: A session is counted each time a user interacts with the store, such as by searching or entering the store's URL directly. A session can also be initiated when a user logs in to the website. However, a single user can have multiple sessions if they leave and return to the store, or if they use different devices to interact with the store. A session ends after 30 minutes of inactivity or at midnight UTC. Because of this, the number of sessions is usually higher than the number of visitors.

**Visitors:** Visitors are the total number of people who access the website, regardless of how many times they visit.

Learn more about Intelligems' metric definitions [here](https://docs.intelligems.io/analytics/experiment-analytics/metric-definitions/conversion-funnel).

</details>

<details>

<summary>Can I export the data from an Intelligems test?</summary>

Yes! We support data exports of orders and line item sales. See more information on what’s included in those exports and how to get them [here](https://docs.intelligems.io/analytics/experiment-analytics/exporting-data).

</details>

<details>

<summary>Can Intelligems send data to my data warehouse via API?</summary>

Yes! We integrate with a wide variety of data lakes and warehouses. This requires reaching out to us to setup

</details>

<details>

<summary>Does data from post-purchase upsells get counted in the analytics dashboard?</summary>

In most cases yes, the order will be updated with the upsell and we will count it. See more about order accounting [here](https://docs.intelligems.io/analytics/order-and-revenue-accounting). If you have any questions about this, [contact our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) with information about the app you're using for post-purchase upsells, and include an example Shopify order number if possible.

Note that we cannot track purchases that were created as draft orders.

</details>

<details>

<summary>How does Intelligems determine New vs Returning visitors?</summary>

We assign every visitor an Intelligems ID when they first visit your store (and Intelligems' is live on the site). If a visitor has already been assigned an ID when they start their session, they are considered returning. If Intelligems is assigning them an ID on that visit, they are new.

</details>

<details>

<summary>Are tablets considered a mobile or desktop device?</summary>

For Intelligems Targeting and Analytics filtering, tablets will be included in the mobile device category.

</details>

<details>

<summary>The experiments we have run using Intelligems resulted in uplifts, but we have not seen our performance improve in Shopify since implementing the changes that we tested. Why might that happen?</summary>

The short answer is that Intelligems tests are measuring *incrementality*. For example, the data may confirm that experience B converted better than experience A while the test was running, but there are still a number of exogenous factors that go into overall conversion rate and site performance.

For example, consider site performance for most industries in January. Many brands see lower conversion rates that time of year due to post-holiday demand. If you were to run a test and find a statistically significant result, and then implement the change in January, you may see site performance decline on a week-over-week basis, but this is because of exogenous seasonal factors, not necessarily because the change had a different effect than what was measured in the test.

Similarly, it's possible that your ad campaigns are generating different types of customers who have fundamentally different likelihoods to convert. It still is *incrementally* better, but that natural conversion rate can vary quite a bit.

These are all great reasons to continually test your site! Frequent testing will help to solve for seasonal changes and increase confidence in test results.

</details>

<details>

<summary>How does Intelligems calculate metrics when customers purchase in different currencies?</summary>

In our analytics dashboard, we only use your store's default currency. For example if your store's default currency is in USD and a customer makes a purchase in EUR, Shopify converts this to USD, and Intelligems analytics reflects the USD figure.

</details>

<details>

<summary>What time zone is used in analytics?</summary>

Analytics in Intelligems are based on the timezone in your Shopify store's settings when you installed the app. If you would like to change the timezone, contact to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

</details>

<details>

<summary>How can I exclude an order from my results?</summary>

The best way to exclude orders from results in Intelligems is by using order tags. You can do this by adding the tag "ig-exclude" in Shopify to any orders that you'd like to exclude from test results in Intelligems.

Alternatively, if you'd prefer to use your own tag, you can do so by going to [Intelligems Settings](https://app.intelligems.io/settings) → scroll to Analytics Settings → enter tags in the "Exclude Order Tags" field. You can then add this tag to orders in Shopify to exclude them. We recommend using descriptive tags like "Intelligems Excluded" for clear identification.

</details>

<details>

<summary>How can I exclude internal traffic from my results?</summary>

One way to exclude internal traffic from your results is by excluding your team member's IP addresses. You can do this by navigating to [Settings](https://app.intelligems.io/settings) in Intelligems > Analytics Settings and enter IP addresses in the "Exclude IP Addresses" field. IP addresses must be added one at a time. You will still be able to place orders and interact with tests normally - the data simply won't appear in your results.

</details>

<details>

<summary>How does resetting my test to pending work?</summary>

**Why would I reset my test to pending?**

You might want to reset a test to pending if you:

* Accidentally viewed live groups and contaminated your data
* Made configuration changes after launching and want a clean slate
* Need to troubleshoot issues before collecting real visitor data
* Want to start over with fresh results

**How do I reset my test to pending?**

1. Navigate to your test in the dashboard
2. Click the more options menu (the three dots) on the right
3. Select "Reset to Pending"
4. Confirm that you want to remove existing results

**What happens when I reset?**

Resetting clears all collected data and moves your test back to pending status. Your test configuration remains intact—only the results are removed. You can then relaunch the test to begin collecting fresh data.

**When should I avoid resetting?**

Don't reset if you've already collected meaningful traffic data, as you'll lose all results and need to start over. Instead, consider creating a new test variation if you need to make significant changes.

</details>

<details>

<summary>Why do my test results look so different in the first few days and then stabilize?</summary>

**This is completely normal and expected behavior — it's sample size in action.**

In the first hours or days of a test, you have very few visitors in each group. When sample sizes are small, a single conversion creates huge percentage swings.

**Example:** If 1 out of your first 10 visitors buys, that's a 10% conversion rate. But if another variation happens to get 0 out of 10, it shows 0%. That 10-point "gap" isn't meaningful — it's just randomness with small numbers.

As more visitors flow through, those early fluctuations get diluted by the larger dataset. The curves smooth out because you're now measuring actual behavioral patterns rather than random noise.

#### How long should I wait before reading into the results?

We recommend waiting until you have **at least 300 orders per variation** before drawing conclusions. At that sample size, you have enough data for the metrics to reflect real differences (or lack thereof) rather than statistical noise.

You can also use the statistical significance indicators in the analytics dashboard:

* **Probability to beat control** shows confidence that a variation is outperforming
* **Confidence intervals** narrow as more data accumulates

For more on interpreting results, see [Statistical Significance](https://docs.intelligems.io/analytics/experiment-analytics/statistical-significance).

#### What should I do during the early test period?

* **Don't panic** if you see wild swings — this is expected
* **Don't end tests early** based on early results alone
* **Do check results regularly** to catch any actual issues (like zero traffic to a variation)
* **Do wait** for sufficient sample size before making decisions

#### Pro tip: Use discrete mode to see day-by-day patterns

By default, the analytics time series shows **cumulative** data — a running total up to each point in time. If you want to see how metrics performed on individual days (which makes the early volatility even more visible), you can switch to **discrete mode** by unchecking the "Cumulative" checkbox in the time series chart.

This can help you spot daily patterns and see exactly when results started stabilizing.

Learn more: [Time series - Discrete Mode](https://docs.intelligems.io/analytics/experiment-analytics/timeseries#discrete)

**Bottom line:** Early spikes and gaps are statistical noise, not signal. The smoothed-out data after you've accumulated sufficient orders is what actually tells the story.

</details>

# Source: https://docs.intelligems.io/getting-started/best-practices/test-design-best-practices.md

# Test Design Best Practices

## Create a Testing Roadmap

We recommend creating a testing roadmap as you complete onboarding with Intelligems. Major factors to consider when creating a test roadmap include:

* **Define Clear Objectives:** Before launching an A/B test, identify what you aim to achieve. Whether it's increasing the conversion rate, reducing cart abandonment, or improving click-through rates on product pages, having a clear objective helps in designing the test and measuring its success accurately. A few examples:
  * For businesses with lower margins, an increase in revenue can have a dramatic effect on bottom line.
  * Similarly, for businesses with higher margins, a small change in conversion can significantly boost total profit.
  * Businesses that are early on in their journey may be more focused on increasing conversion rates right away.
* **Intuition or Customer Feedback:** Combine your business objectives with your intuition or customer feedback and use Intelligems tests to confirm and quantify potential changes to your merchandising strategy.
* **Get Creative:** Many test types are possible with Intelligems.
* **Test Timing:** Plan for each test to take about 3 to 4 weeks. We recommend running each test for at least one week to capture any changes in customer behavior related to day of the week. We also recommend running each test for no longer than five weeks due to increased risk of device switching / cache clearing.
  * We typically recommend running a test until each group has 200-300 orders to start to see significant results. Use this rule of thumb as a way to estimate the amount of time required to run each test.
* **Test Frequently:** Market conditions and consumer behavior change frequently. Test new hypotheses and run experiments frequently to make sure you're maximizing your store's potential at all times.
* **Determine Stat Sig before starting the test**: you should focus on the probability that indicates one of your test groups outperforms the control. While we suggest reaching 300 orders per test group, actual requirements can vary depending on the nature of the change and the desired confidence threshold. For example, a higher confidence threshold will require more data than a lower threshold. More importantly, larger changes typically yield results more quickly than subtle adjustments. If you're testing a change that's a small risk to implement and easy to revert if needed, you may be comfortable with a lower threshold (e.g. 85%). If you're resting something more important and riskier, you may prefer a higher threshold (e.g. 90%).
* Before launching tests, **establish clear thresholds** for statistical significance, orders, visitors, and duration. Have a hypothesis and, upon concluding the test, assess whether results align with your expectations. If a test doesn't achieve significance within the expected timeframe, use the available data to make an informed decision, considering the change's risk and reversibility. You can read more about Stat Sig [here](https://docs.intelligems.io/analytics/determining-statistical-significance).

***

## Determining Traffic Allocations Between Groups

We generally recommend allocating traffic evenly between groups, other than in certain circumstances such as:

* You have already decided to change prices and want to hold back a small amount of traffic on prior prices
* You want to allocate most traffic to the control because of customer support concerns
* You have decided to remove allocation of new traffic to certain test groups part-way through the test
  * Note: Changing the allocation of test traffic during a test may result in skewed data. If you remove traffic from one group, we recommend scaling the other groups proportionally to their prior allocations

***

## Determining the Magnitude of Changes to Test

We recommend starting with broad changes and using results to narrow in on more refined tests. For instance, if you're testing:

* **Prices:** start with an 8-10% increase and decrease, simultaneously
  * If traffic allows, testing 3-4 groups simultaneously will yield more insightful data and will give you a sense of your products' elasticities
  * If conditions only allow you to test in one direction (i.e. decreasing prices isn't an option for your business), pick a few points in the direction you wish to test
  * Consider factors such as seasonality: for example, if you sell winter and summer products, running a site-wide price test may not make much sense, since results for those categories are probably very different at any given point in the year. You may focus on running the test over products that will yield more meaningful results.
  * Are products substitutable? If testing individual products, avoid changing the price of one product that could affect the results of a different product.
* **Shipping Rates / Thresholds:** start with an 8-10% increase / decrease, simultaneously

***

## Only Make One Change

* We recommend keeping the existing prices and configurations for the "control group" for the experiment to keep your baseline consistent.
* If there are unique aspects to how you merchandise your products (e.g. if you offer bundle discounts, welcome offers, or subscriptions), consider how these elements of your store might be affected by tests you want to run. In general, we recommend keeping these types of discounts as consistent as possible across groups so these variables do not create noise in the test.
* If you are running a content test, be sure to keep the change limited to one thing. If you change multiple elements in a single test, it'll be difficult to decipher what caused any performance changes.

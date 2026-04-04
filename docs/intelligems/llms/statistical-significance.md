# Source: https://docs.intelligems.io/analytics/experiment-analytics/statistical-significance.md

# Statistical Significance

Intelligems uses a Bayesian statistical model and Monte Carlo simulations to analyze A/B tests. Note that the model does not account for intra-week (daily) seasonality, or other store-specific factors. We recommend that in addition to using Intelligems' provided probabilities to determine the significance of your test, you also ensure the test reaches a pre-defined minimum number visitors, orders, and full weeks live.

**A best practice is to set a minimum number of visitors, orders,&#x20;*****and*****&#x20;time** before ending a test or analyzing results.

Once your test has reached your predefined number of visitors, orders, and run for a minimum of one full week, you can use the Stat Sig information in the analytics dashboard in the app to get a read on confidence in the results.

## Probabilities and Confidence Intervals

Within Intelligems analytics, you’ll see a few metrics derived from this statistical model:

* **Probability to beat control**: this is the probability that a test group is better than the control group, on the basis of the selected metric
* **Probability to be best**: this is the probability that a test group is best, on the basis of the selected metric. In tests with a control group and only one other test group (i.e., A vs. B), the probability to be best will equal the probability to beat control
* **Uplift confidence interval**: this is a 95% confidence interval around the uplift percent (i.e., what percent better or worse a test group is vs. control for a specific metric). For example, in this screenshot, the uplift for profit per visitor is +3.50% +/- 2.50. This means the 95% confidence interval around profit per visitor uplift is \[+1.00%, 6.00%], that is, there is a 95% probability that the “true” profit per visitor difference is between +1.00% and +6.00%.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-2ca5ada5361ade672ed916bc3bdc00f0936ec308%2FCleanShot%202025-03-24%20at%2009.57.43.png?alt=media" alt=""><figcaption></figcaption></figure>

* **Value confidence interval**: this is a 95% confidence interval around the value measurement for a specific metric. There is a 95% probability that the “true” value of the metric for the test group lies in this interval.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-30ac58e7687d4bde3ec741f6f4548f2adccdcf43%2FCleanShot%202025-03-24%20at%2010.02.01.png?alt=media" alt=""><figcaption></figcaption></figure>

As your experiment accumulates more data, the confidence intervals around uplift and value will narrow. Note that your experiment may reach statistical significance (i.e., the probability to be best or beat control is above a threshold, like 95%), but the confidence interval around uplift and value may still be very wide. This is because for a test group to have a high probability to be best/beat control, we only need high confidence that the uplift for that test group is > 0%. We may have high confidence that one test group is better than another, but still need to collect more data to have a good specific estimate of how much better.

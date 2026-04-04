# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/business-impact.md

# Business Impact

### What is the Business Impact page?

Business Impact dashboard allows you to tie app quality with business metrics such as the retention rate and monthly active users (MAU). We help show you your apps retention rate and MAU, along with breaking them down into buckets of good experience and bad experience users to understand how app quality impacts those numbers. It is currently a beta product, learn more about our beta programs [here](https://docs.luciq.ai/product-guides-and-integrations/product-guides/broken-reference).

<figure><img src="https://files.readme.io/f306b54cefceff51824e34f6554b036a7b2c0eb2f74c012294224f9a362f3f71-business-impact-for-flutter-beta-1.png" alt=""><figcaption></figcaption></figure>

**Prerequisites to see meaningful insights:**

1. Available for apps using SDK versions starting 12.0.0
2. You will need to have APM enabled
3. Your app needs to have at least 10k users in the past month to be able to see the retention rate

#### How do we calculate the retention rate?

We calculate the retention rate based on a full month’s data. Meaning - If you’re in February, the page will be showing you the retention rate for the month of January, until the full month of February is over then it will be showing you the retention rate for February.

We check to see how many users had users had sessions two months ago, that returned to have sessions in the past month. We use the following formula:

`Retention rate = intersection / last months total number of users`

**Let’s walk through an example:**

* January: You had 10 monthly active users
* February: You had 15 monthly active users. 8 of them were the same users that had sessions in January

The page during march will show you the following values:

* MAU: 15
* Retention Rate: 53%
  * Intersection: 8 users that had sessions in both months
  * Total users: 15 total users for the month of February
  * Retention rate: 8/15 \* 100 = 53%

#### How do we calculate the number of Monthly Active Users (MAU)?

We use a cardinality estimating algorithm HyperLogLog to estimate the number of unique users having sessions. This calculated after the month is over.

For example:

* During March, you will be seeing the number of MAU you had in February
* Once March is over and we’re in April, you will get to see the number of MAU you had in March

Some useful resources about HyperLogLog:

* [Building a Real Time Metrics Database at Datadog | Datadog](https://www.datadoghq.com/videos/real-time-metrics-database/)
* [HyperLogLog in Presto: A significantly faster way to handle cardinality estimation](https://engineering.fb.com/2018/12/13/data-infrastructure/hyperloglog/https://engineering.fb.com/2018/12/13/data-infrastructure/hyperloglog/)

***

#### Overtime Chart

Use the overtime chart to visually monitor the performance of these key metrics overtime, and easily spot any correlations between them.

You can select/unselect which metrics to visualize from the legend at the bottom:

#### Summary section

We help highlight any correlations for you by showcasing the likelihood of:

* Retaining users with good experiences vs users with bad experiences
  * percentage of users with good experiences retained / percentage of users with bad experiences retained
* Users being active
  * percentage of active users with good experiences / percentage of active users with bad experiences

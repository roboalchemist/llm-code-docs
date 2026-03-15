# Source: https://posthog.com/docs/product-analytics/trends/statistical-analysis.md

# Statistical analysis - Docs

When analyzing data, it's important to understand if your results are statistically significant. In other words, are the trends you're seeing real, or are they just due to random chance?

PostHog helps you answer this question by providing confidence intervals for your trend lines.

## What are confidence intervals?

A [confidence interval](https://en.wikipedia.org/wiki/Confidence_interval) is a range of values that likely contains the true value of a metric. A 95% confidence level means that if you were to run the same analysis again 100 times, 95 of those times the true value would fall within the calculated confidence interval.

In PostHog, confidence intervals are displayed as a shaded area around your trend lines. The wider the shaded area, the less confident we are in the data. The narrower the area, the more confident we are.

![Confidence intervals on a line chart](https://res.cloudinary.com/dmukukwp6/image/upload/ci_light_964273850b.png)![Confidence intervals on a line chart](https://res.cloudinary.com/dmukukwp6/image/upload/ci_dark_70b3c2973c.png)

This is especially useful when you're working with smaller sample sizes (sampling turned on) or when you're trying to detect small changes in your metrics. It helps you avoid making decisions based on noise.

## How to use confidence intervals

To enable confidence intervals, go to **Options** section of your trend insight and toggle the **Show confidence intervals** switch.

![Confidence interval settings](https://res.cloudinary.com/dmukukwp6/image/upload/ci_settings_light_2_ee4aa887f2.png)![Confidence interval settings](https://res.cloudinary.com/dmukukwp6/image/upload/ci_settings_dark_2_cc793838c2.png)

You can also set the [confidence level](https://www.statisticshowto.com/probability-and-statistics/statistics-definitions/confidence-level/), which is 95% by default. A higher confidence level will result in a wider interval, while a lower confidence level will result in a narrower interval. Common confidence levels are 90%, 95%, and 99%.

## Interpreting confidence intervals

When comparing two trend lines with confidence intervals, you can use the overlap of their shaded areas to gauge statistical significance.

-   **If the confidence intervals don't overlap**, the difference between the two trend lines is likely statistically significant.
-   **If the confidence intervals do overlap**, the difference may not be statistically significant. You may need to collect more data to be sure.

Confidence intervals are a powerful tool for making data-informed decisions. They can help you avoid being misled by random fluctuations in your data and focus on the changes that matter.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better
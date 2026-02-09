# Source: https://braintrust.dev/docs/pricing-faq.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pricing FAQ

> Pricing FAQ

### Which plan is right for me?

* **Free**: Ideal for individuals or small teams getting started with Braintrust. It includes enough data ingestion, scoring, and data retention to explore and build small projects.

* **Pro**: Best suited for small teams of up to 5 people who are regularly running experiments or evaluations that require increased usage limits and longer data retention. Additional usage beyond included limits is billed flexibly, making it great for teams with growing or varying workloads.

* **Enterprise**: Recommended for larger organizations or teams with custom needs such as high volumes of data, special security requirements, on-premises deployment, or dedicated support.

If you're unsure which option fits your needs or would like to discuss custom requirements, please [contact our team](https://braintrust.dev/contact) for personalized guidance.

### What does processed data mean?

Processed data refers to the data ingested by Braintrust when you create [logs](/observe/view-logs) or [experiments](/evaluate/run-evaluations). This includes inputs, outputs, prompts, metadata, datasets, traces, and any related information. The cumulative size of this data (measured on disk) counts toward your monthly total, calculated from the first day to the last day of each calendar month.

### What are scores?

[Scores](/evaluate/write-scorers) are used to measure the results of offline or online evaluations run in Braintrust. Each time you record a [score](/evaluate/write-scorers#custom-scorers), the total number of scores counted towards your monthly usage increases by one. Your monthly total is calculated cumulatively from the first to the last day of each calendar month.

### What are trace spans?

Spans are the fundamental units of observability in your traces. Each span represents a discrete operation in your application - like an LLM API call, prompt rendering, or evaluation step. Spans are automatically created when you use Braintrust's instrumentation and contribute to your monthly usage quota, which is calculated per calendar month.

### How do I track my usage?

If you are on the Pro plan, you can track your usage by selecting **View usage details** in **Settings** > **Billing**. This will open your detailed usage report in the Orb usage portal, where you can view your current usage and monitor costs throughout the billing period.

### How does billing work?

The Free plan does not require a credit card to get started. You can upgrade to the Pro plan at any time via the **Upgrade** button in the top-right of your workspace.

When you sign up for the Pro plan, you'll immediately be charged a prorated amount of the monthly \$249 platform fee. For example, if you sign up on the 15th of the month, you'll pay about half of the monthly fee. On the 1st of the following month, you'll be charged the full \$249 fee plus any additional usage-based charges incurred during the previous month. Charges will be processed automatically using the credit card provided at sign-up.

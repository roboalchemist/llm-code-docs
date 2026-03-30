# Source: https://docs.acceldata.io/documentation/score-aggregation-methodology.md

# Score Aggregation Methodology

The **Score Aggregation Methodology** setting in Acceldata Observability Cloud (ADOC) allows you to choose how Data Reliability scores are calculated and aggregated and displayed across your environment. This configuration applies specifically to **Data Quality (DQ)** and **Reconciliation** policies.

By default, ADOC uses a **policy-based simple averaging** approach. In **version 4.7.0**, a new scoring strategy called **Row-Weighted Scoring** has been introduced. This new approach provides a more accurate representation of your data health by considering the **volume of data** (number of rows scanned) associated with each rule.

---

## Why This Matters

Previously, all policies contributed equally to the overall reliability score of the asset, regardless of how much data they processed or how many rules they contained. This meant that:

- A policy scanning 10 rows was treated the same as one scanning 10 million rows.
- High-impact or large data assets could appear less critical in reporting.
- The number of rules inside a policy had no effect on the overall score.

With **Rule-Based Row-Weighted Scoring**, larger and more significant datasets have a proportionally higher influence on your overall score, making your reliability insights more accurate and actionable.

---

## How Rule-Based Row-Weighted Scoring Works

Under the new methodology, each **rule item** becomes the core unit for scoring instead of the policy itself.

### Key Changes

- **Policies act as containers** for rules.
- Each rule has its own **pass percentage** and **row count**.
- The **number of rows scanned** for a rule becomes its **weight** in the final score calculation.

### Calculation Formula

```none
Weighted Score = (Sum of (Rule Score × Rows Scanned)) ÷ (Total Rows Scanned)
```



This formula ensures that rules evaluating larger datasets contribute more to the overall reliability score.

### Example

| Rule | Rows Scanned | Rule Score | Weighted Contribution | 
| ---- | ---- | ---- | ---- | 
| Rule A | 10 | 100% | 1,000 | 
| Rule B | 10,000 | 50% | 500,000 | 
| **Overall Weighted Score** | — | — | **(1,000 + 500,000) / 10,010 = 50%** | 


In this example, the overall reliability score aligns more closely with the rule scanning 10,000 rows, rather than being equally influenced by both.

---

## Configuring Score Aggregation Methodology

You can configure the scoring methodology from the Acceldata UI.

### Steps

1. Navigate to **Settings &gt; Reliability &gt; Score Aggregation Methodology**.
2. Choose one of the available scoring options:
    - **Policy-Based Simple Averaging** _**(default)**_
    - **Rule-Based Row-Weighted Averaging** (recommended for large-scale datasets)

> This is a tenant-level setting. Once configured, all Data Quality and Reconciliation reports, dashboards, and reliability scores across the workspace will reflect the selected methodology.

> Changing the score aggregation methodology does not recalculate scores in the background. All score values are precomputed during rule execution. The system simply displays the relevant field based on your selection.

---

## Where This Setting Impacts

When you enable **Rule-Based Row-Weighted Scoring**, the following areas in the product reflect the change:

### 1. Reports

- The **Rules Report** replaces the traditional policy-level view.
- You can now see performance and reliability metrics grouped by **rules** instead of policies.
- The **Column Report** provides a detailed breakdown of scores by column, including:
    - Number of rules configured per data dimension
    - Rules passed or failed
    - Total rows processed and passed
    - Column-level quality scores

### 2. Dashboards

- Custom dashboard widgets display rule-based and column-level scores.
- Trend charts and summary cards dynamically adjust to show row-weighted results.
- Filters such as _rules executed_ and _rows processed_ become available per asset.

### 3. Asset Detail Page

- The **Reliability Score** for an asset displays a tooltip when hovering over the  info icon, indicating that the score is calculated using a Row-Weighted Scoring method.
- The **Average Reliability Score** for each policy shows the mean of all rule execution scores within the selected time period.

### 4. Policy Editor

- Rule weights manually defined during policy creation are currently **ignored**, since row counts are automatically used as weights during scoring.

---

## Benefits

- **Accuracy:** Reflects true data health by factoring in data volume.
- **Transparency:** Provides rule-level and column-level visibility into quality results.
- **Actionability:** Surfaces large or high-impact assets that need attention first.
- **Consistency:** Ensures score alignment across reports, dashboards, and asset views.

---

## Best Practices

- Use **Row-Weighted Scoring** when monitoring large datasets or data sources with uneven data volumes.
- Continue using **Policy-Based Averaging** if your datasets are uniform in size and you prefer equal weighting across all rules.
- Review **Reports → Rules Report** and **Reports → Column Report** to track rule-level performance trends.
- If you switch methodologies, communicate the change to stakeholders to avoid confusion in historical comparisons.

---

## Additional Information

For more information on configuring Data Reliability settings, see [Data Reliability Settings](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/data-reliability-settings).
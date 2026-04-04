# Source: https://docs.qodo.ai/qodo-documentation/code-review/qodo-merge/learn-more/impact-evaluation.md

# Impact Evaluation

{% hint style="warning" %}
**Git Integration (formerly Qodo Merge)** – AI code review agents for pull requests.\
This documentation describes the Qodo v1 experience. For the Qodo v2 documentation, click [here.](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/)
{% endhint %}

{% hint style="info" %}
**Platforms supported:** GitHub, GitLab, Bitbucket
{% endhint %}

### **Measuring ROI with** Qodo

Demonstrating the return on investment (ROI) of AI-powered development tools is essential for modern engineering organizations. To support this need, Qodo provides advanced **AI impact measurement tools and metric**, helping teams quantify the real benefits of AI-driven code review in their PR workflow.

## **Auto Impact Validator**

### **How It Works**

The Auto Impact Validator is a way for you to track implemented Qodo suggestions in real-time.

When a user pushes a new commit to the pull request, Qodo automatically compares the updated code against the previous suggestions, marking them as implemented if the changes address these recommendations, whether directly or indirectly:

1. **Direct Implementation:** The user directly addresses the suggestion as-is in the PR, either by clicking on the "apply code suggestion" checkbox or by making the changes manually.
2. **Indirect Implementation:** Qodo recognizes when a suggestion's intent is fulfilled, even if the exact code changes differ from the original recommendation. It marks these suggestions as implemented, acknowledging that users may achieve the same goal through alternative solutions.

### Real-Time Visual Feedback <a href="#real-time-visual-feedback" id="real-time-visual-feedback"></a>

Upon confirming that a suggestion was implemented, Qodo automatically adds a ✅ (check mark) to the relevant suggestion, enabling transparent tracking of Qodo's impact analysis.

Qodo will also add, inside the relevant suggestions, an explanation of how the new code was impacted by each suggestion.

<figure><img src="https://codium.ai/images/pr_agent/auto_suggestion_checkmark.png" alt=""><figcaption></figcaption></figure>

### Dashboard Metrics <a href="#dashboard-metrics" id="dashboard-metrics"></a>

The dashboard provides macro-level insights into the overall impact of Qodo on the pull-request process with key productivity metrics.

By offering clear, data-driven evidence of Qodo's impact, it empowers leadership teams to make informed decisions about the tool's effectiveness and ROI.

### Key metrics tracked by the dashboard

#### Qodo **Impacts per 1K Lines**

<figure><img src="https://codium.ai/images/pr_agent/impacts_per_1k_llines.png" alt=""><figcaption></figcaption></figure>

> Explanation: for every 1K lines of code (additions/edits), Qodo had on average \~X suggestions implemented.

**Why This Metric Matters:**

1. **Standardized and Comparable Measurement:** By measuring impacts per 1K lines of code additions, you create a standardized metric that can be compared across different projects, teams, customers, and time periods. This standardization is crucial for meaningful analysis, benchmarking, and identifying where Qodo is most effective.
2. **Accounts for PR Variability and Incentivizes Quality:** This metric addresses the fact that "Not all PRs are created equal." By normalizing against lines of code rather than PR count, you account for the variability in PR sizes and focus on the quality and impact of suggestions rather than just the number of PRs affected.
3. **Quantifies Value and ROI:** The metric directly correlates with the value Qodo is providing, showing how frequently it offers improvements relative to the amount of new code being written. This provides a clear, quantifiable way to demonstrate Qodo's return on investment to stakeholders.

#### **Suggestion Effectiveness Across Categories**

<figure><img src="https://codium.ai/images/pr_agent/impact_by_category.png" alt=""><figcaption></figcaption></figure>

> Explanation: This chart illustrates the distribution of implemented suggestions across different categories, enabling teams to better understand Qodo's impact on various aspects of code quality and development practices.

#### **Suggestion Score Distribution**

<figure><img src="https://codium.ai/images/pr_agent/impacted_score_dist.png" alt=""><figcaption></figcaption></figure>

> Explanation: The distribution of the suggestion score for the implemented suggestions, ensuring that higher-scored suggestions truly represent more significant improvements.

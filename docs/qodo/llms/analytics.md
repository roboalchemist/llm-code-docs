# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/rule-enforcement/analytics.md

# Rule Analytics

Rules analytics  provides visibility into how rules are applied across pull requests in the Qodo Portal. It helps teams understand rule effectiveness, monitor violations, and track how often issues are resolved before code is merged.

All analytics shown reflect activity from the last 30 days.

### Accessing rules analytics

Rule analytics are available at two levels in the Qodo portal:

### Aggregated rules analytics

Aggregated rules analytics provide a high-level view of how rules are applied across pull requests in the Qodo portal. These analytics reflect rule activity from the last 30 days and are available at the top of the Rules page.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FJLFjIbBhLVWDD2qUdlRk%2FMetrics.png?alt=media&#x26;token=69510ba8-5301-416b-bc2f-37df856c64bc" alt=""><figcaption></figcaption></figure>

To access aggregated analytics:

1. Open the [**Qodo portal**](https://app.qodost.st.qodo.ai/)**.**&#x20;
2. Select **Rules** from the left navigation.
3. View the analytics summary displayed at the top of the Rules page.

The metrics are shown as summary cards:

* **Passed (no violations)** – The number of evaluations where no rule violations were detected
* **Detected violations** – The total number of rule violations identified during pull request reviews
* **Merged violations** – The number of PRs that were merged with one or more unresolved rule violations

These metrics help teams understand how frequently rules are triggered, how often violations are resolved before merge, and where rule enforcement may need attention.

#### Exporting analytics

Merged violations analytics can be exported as a CSV file using the **⬇︎ download icon** in the top-right corner of the Rules page.\
The exported file includes merged violations metrics from the last 30 days and can be used to perform offline analysis, share insights with stakeholders, and track trends over time outside the portal.

### Individual rule analytics

Individual Rule Analytics provide detailed insights into how a specific rule behaves across pull requests.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FHTu8IZOVmTm3Ow4GVKvM%2FMetrics%20rule.png?alt=media&#x26;token=25b89717-a547-444d-93a3-9f387a5b5b51" alt=""><figcaption></figcaption></figure>

To access individual rule analytics:

1. Open the [**Qodo portal**](https://app.qodost.st.qodo.ai/)**.**
2. Select **Rules** from the left navigation.
3. Click a rule from the **Rules table.**

This opens the rule’s full definition along with rule-level analytics.

Each rule’s analytics show:

* How often the rule was found compliant
* How often the rule is violated
* How frequently violations are merged

These insights help teams identify noisy or ineffective rules, understand developer behavior around specific rule types, and decide whether a rule requires tuning, disabling, or stronger enforcement.

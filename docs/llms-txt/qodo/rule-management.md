# Source: https://docs.qodo.ai/qodo-documentation/management-portal/rule-management.md

# Rule Management

{% hint style="success" %}
**Rules System availability**

The Rules System is currently available in **beta** and supported on **GitHub** only.\
It is enabled by default for new Qodo customers.\
Existing customers can [**contact Qodo**](https://www.qodo.ai/contact/) to request access.
{% endhint %}

The Rules System lets you define, enforce, and evolve your organization’s code standards, all in one place.

Rules are automatically applied during code reviews, turning best practices and team conventions into consistent, measurable enforcement. In the Qodo portal, you can manage rules, review AI-suggested improvements, and track how rules perform across pull requests.

### Rules overview page

In the Qodo portal, select **Rules** from the left navigation menu. The Rules overview page shows the current state of rule enforcement across your organization.

You’ll see two main tabs:

* ​[**Rules**](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/rule-enforcement/generate-and-manage-rules) — view, edit, and monitor active and inactive rules enforced during code reviews
* ​[**Suggestions**](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/rule-enforcement/suggested-rules) — review and activate proposed rules generated from real code and PR history

<figure><img src="https://2742973941-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FnoDWMoicsI0VwDtqoKja%2Fuploads%2FU9T7rysVbPWT7l8Ax6vo%2FScreenshot%202026-03-10%20163506.png?alt=media&#x26;token=5a02b7e3-dd0d-42bf-90bf-446aeada6953" alt=""><figcaption></figcaption></figure>

#### **Summary cards**

At the top of the Rules page, Qodo displays rule analytics for the last 30 days to help you understand how rules are performing in practice:

* **Passed (no violations)** — evaluations with no rule violations
* **Detected violations** — violations identified during reviews
* **Merged violations** — pull requests merged with at least one rule violation

Use these metrics to identify rules that may need refinement or wider adoption.

#### Rules table <a href="#rules-table" id="rules-table"></a>

Each row represents a single rule and its current configuration. You can sort and filter the table to focus on specific rules, including filtering by status (active or inactive), category, or repository scope.\
Click any rule to review its full definition, enforcement behavior, and historical performance.

#### ​Analytics

Use analytics to understand how rules perform across pull requests and identify trends over time.\
Merged violations metrics can be exported to CSV using the ⬇︎ icon in the top-right corner.\
For deeper insights, see [**Rule Analytics**](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/rule-enforcement/analytics).

### **Next steps**

* Learn how rules are evaluated during code reviews in [**Rule Enforcement**](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/rule-enforcement)**.**
* Explore [**Rule Analytics**](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/rule-enforcement/analytics) to understand rule impact over time.
* Review [**Suggested Rules**](https://app.gitbook.com/s/yXEFCLH7CkXrROa2gOqv/get-started/rule-enforcement/suggested-rules) to expand coverage based on real usage.

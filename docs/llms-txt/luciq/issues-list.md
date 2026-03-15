# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/getting-started-with-luciq/issues-list.md

# Issues List

***

### What Is the Issues List?

The Issues List is a centralized view that consolidates all your app's stability and performance issues into a single list. By combining issues like crashes, app hangs, force restarts, and performance metrics like app launches and screen loads, it provides a comprehensive understanding of the problems affecting your app’s quality.

<figure><img src="https://files.readme.io/2788e1fc681c1b5cde861adc0c782ff5666ae3d2c015ead70793c3308b18eb6b-product-guides-issues-list-1.png" alt=""><figcaption></figcaption></figure>

### How Does It Help?

The issues list is **automatically prioritized based on each issue's impact on your App Frustration-Free Sessions**, reflecting how much the issue contributes to frustrating user sessions. By addressing the highest-impact issues first, you can significantly improve your app's quality, reduce user frustration, and boost satisfaction.

Instead of sifting through raw data or dealing with scattered issues, you can now rely on this prioritized list to efficiently manage and resolve the most critical problems first.

***

### Using the Issues List: A Workflow for Improving App Stability and Performance

#### Step 1: Monitor Your App’s Frustration-Free Sessions

The **App Frustration-Free Sessions** is your most important metric for understanding your app’s overall stability and performance. It gives you a clear signal when users experience frustrating sessions, helping you take action before issues escalate.

If you want to improve your Frustration-Free Sessions, head to the **Issues List**, a prioritized view of every performance and stability issue contributing to the score. This leads us to step 2.

#### Step 2: Identify High-Impact Issues

After monitoring your Frustration-Free Sessions, drill down into the Issues List to pinpoint the most critical problems affecting your app. The list ranks issues by their [**Apdex Impact**](https://docs.luciq.ai/product-guides-and-integrations/product-guides/getting-started-with-luciq/issues-list/frustration-impact), a metric that approximates how much each issue contributes to frustrating user sessions. This is calculated by approximating the percentage:

`(Frustrating Sessions caused by this issue ÷ Total Sessions) × 100`

Issues are grouped into the following categories:

* **High Impact:** Issues affecting ≥0.5% of total sessions. These are critical and require immediate attention.
* **Medium Impact:** Issues affecting between 0.01% and 0.5% of sessions. These should be addressed after high-impact issues.
* **Low Impact:** Issues affecting <0.01% of sessions. These have minimal impact but may still need resolution over time.
* **No Impact:** Issues that don’t affect your Frustration-Free Sessions, including:
  * APM groups where all occurrences are satisfying (Apdex 1).
  * Metrics marked as non-key by your team.

For each issue, review:

* **Issue Count:** Represents the number of negative occurrences.
  * For crashes, app hangs, and force restarts: Total number of occurrences.
  * For APM metrics: Dissatisfying count, which is calculated as:\
    Frustrating Occurrences + (0.5 × Tolerable Occurrences)
* **Detailed Metrics:** Depending on the issue type, detailed metrics on the issue card provide insights into the issue’s scope and severity.

<figure><img src="https://files.readme.io/8e728143ad4373af7abf2065e65220d6b1783bc5f70287e001f30918ef361505-product-guides-issues-list-2.png" alt=""><figcaption></figcaption></figure>

Now that you've identified the issues that are impacting your users the most, the next step is to take action and address them effectively.

#### Step 3: Triage the Issue

Review the prioritized issues to determine the appropriate next steps:

**Forward to Jira**

For critical issues requiring immediate attention, forward them to Jira for tracking and resolution.

* The generated Jira ticket includes relevant context about the issue.
* Once forwarded, a shortcut to the Jira ticket will appear on the issue card for quick access.

<figure><img src="https://files.readme.io/b625cf310e912a0e677d39ad2171f4c14a2b922459f475e97607ffb18ae3c142-product-guides-issues-list-3.png" alt=""><figcaption></figcaption></figure>

**Assign to Teams**

* Assigning ensures accountability and streamlines communication.
* Assigned issues will be reflected in the team’s dashboard for full visibility.

<figure><img src="https://files.readme.io/38b5947ea034dcc91991ce73f38b04db77123d0bdd4de0fe5572e2d3f098ca71-product-guides-issues-list-4.png" alt=""><figcaption></figcaption></figure>

#### Step 4: Fix the Issue

When you’re ready to fix an issue, click on it in the Issues List or open it through the link in your Jira ticket. You’ll be redirected to the issue’s **Details Page**, where you’ll find all the debugging data you need to resolve the problem efficiently.

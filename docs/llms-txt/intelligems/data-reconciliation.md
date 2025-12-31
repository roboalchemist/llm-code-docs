# Source: https://docs.intelligems.io/analytics/experiment-analytics/metric-definitions/data-reconciliation.md

# Data Reconciliation

{% hint style="info" %}
**The Data Reconciliation tab is currently a beta feature within our Analytics dashboard.** If you don’t see it in your account and would like access, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we’d be happy to enable it for you.
{% endhint %}

#### **Introduction**

When analyzing order data in experiment reporting, certain orders may be excluded to ensure accuracy and relevance. This doc includes a breakdown of each exclusion reason and what it means.

#### **Not Excluded**

* **What it means:**\
  The order is included in experiment analytics.
* **Why:**\
  It met all criteria for valid test tracking and attribution.

#### **Subscription Refill**

* **What it means:**\
  The order is part of a recurring subscription (not a new checkout).
* **Why it's excluded:**\
  Subscription refills are not influenced by experiments targeting live user decisions.

#### Is Gift Card Only

* **What it means:**\
  The order only contains gift cards.
* **Why it's excluded:**\
  Revenue from gift cards is realized on redemption, not purchase.

#### Draft Order

* **What it means:**\
  Created as a Shopify draft order.
* **Why it's excluded:**\
  Often times was not placed on the online store, or was done in a way that Intelligems cannot accurately track.

#### Non-Online Store Order

* **What it means:**\
  Originated from a channel outside your Shopify Online Store (e.g., POS, Facebook).
* **Why it's excluded:**\
  These are not affected by site-based experiments.

#### Orders Could Not Be Matched to a Session

* **What it means:**\
  The system couldn’t match the order to a session in the experiment.
* **Why it's excluded:**\
  Session-level tracking is required for attribution.

#### Visitor Has Opened Intelligems Preview Mode

* **What it means:**\
  The visitor placed the order while in preview mode, or has had preview mode open previously.
* **Why it's excluded:**\
  Preview mode likely means the user is an internal employee.

#### Visitor Excluded Due to Mutual Exclusion

* **What it means:**\
  The visitor was already assigned to another mutually exclusive test.
* **Why it's excluded:**\
  To prevent test overlap or interaction bias.

#### Visitor Was Excluded by Audience Targeting

* **What it means:**\
  The visitor didn’t meet the audience targeting rules.
* **Why it's excluded:**\
  Experiment rules prevent inclusion.

#### Visitor Did Not Enter Experiment During the Session When Order Was Created

* **What it means:**\
  The user placed an order during a session where they didn’t enter the test.
* **Why it's excluded:**\
  No valid experiment exposure occurred.

#### Missing Experience Assignment Event

* **What it means:**\
  The visitor entered the experiment but a required event was not sent. This could be because of a data outage.
* **Why it's excluded:**\
  Without this, we can’t determine what experience was shown.

#### Visitor Never Entered the Experiment

* **What it means:**\
  The visitor was never exposed to the test.
* **Why it's excluded:**\
  Orders must be linked to a test experience to be valid for analytics.

#### Order Created Before Visitor Entered Experiment

* **What it means:**\
  The order happened before the test experience was assigned.
* **Why it's excluded:**\
  Test wasn’t influencing behavior at the time.

#### Order Created During Experiment Pause

* **What it means:**\
  The order was placed while the test was paused.
* **Why it's excluded:**\
  Paused tests don’t apply active changes.

#### Session Started During Experiment Pause

* **What it means:**\
  The session began while the test was paused.
* **Why it's excluded:**\
  Visitor never entered the test during their session.

#### Order Was Refunded or Voided

* **What it means:**\
  The order was fully refunded or voided.
* **Why it's excluded:**\
  No net revenue contribution.

#### Net Revenue \</= 0

* **What it means:**\
  The order’s net revenue is zero or negative.
* **Why it's excluded:**\
  These do not reflect real economic impact, and likely were edge case orders.

#### Filtered Out: Outlier

* **What it means:**\
  The order is flagged as being 3 or more standard deviations away from the average order value.
* **Why it's excluded:**\
  To prevent skewing results.

#### Filtered Out: Country

* **What it means:**\
  The visitor’s country was excluded.
* **Why it's excluded:**\
  Based on your country-based filter rules.

#### Filtered Out: Device Type

* **What it means:**\
  The device used (e.g., mobile, desktop) was excluded.
* **Why it's excluded:**\
  Based on your device-based filter rules.

#### Filtered Out: New vs. Returning Visitor

* **What it means:**\
  Visitor type (first-time or returning) was filtered out.
* **Why it's excluded:**\
  Based on your visitor type filter rules.

#### Visitor's IP Address is Excluded

* **What it means:**\
  IP is on an internal/testing exclusion list.
* **Why it's excluded:**\
  To remove internal or non-customer traffic.

#### Filtered Out: Excluded Order Tag

* **What it means:**\
  The order contained a tag that was part of the exclusion list.
* **Why it's excluded:**\
  Based on "Exclude Order Tags" exclusion list in settings page.

#### Filtered Out: Traffic Sources or Channels

* **What it means:**\
  Traffic from certain channels was excluded (e.g., email, paid search).
* **Why it's excluded:**\
  Based on your source or channel-based filter rules.

#### Filtered Out: Query Param Filter

* **What it means:**\
  URL parameters triggered exclusion (e.g., test=true).
* **Why it's excluded:**\
  Based on your query param-based rules.

#### Filtered Out: Custom Event

* **What it means:**\
  Custom event logic excluded the visitor/order.
* **Why it's excluded:**\
  Based on your custom event-based rules.

#### Filtered Out: Added To Cart Filter

* **What it means:**\
  The visitor did not meet custom add-to-cart behavior logic.
* **Why it's excluded:**\
  Based on your add to cart-based rules.

#### **Filtered Out: Did Not Reach Checkout Stage**

* **What it means:**\
  Visitor never reached the checkout funnel.
* **Why it's excluded:**\
  Based on your reached checkout-based rules.

#### **Filtered Out: Order Did Not Include Products From Test**

* **What it means:**\
  The order didn’t include any of the products being tested.
* **Why it's excluded:**\
  The test had no influence on this order.

#### **Associated Test Group Has Been Deleted**

* **What it means:**\
  The test group originally linked to the visitor no longer exists.
* **Why it's excluded:**\
  No valid assignment remains.

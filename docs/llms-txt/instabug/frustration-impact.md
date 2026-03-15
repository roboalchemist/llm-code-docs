# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/getting-started-with-luciq/issues-list/frustration-impact.md

# Frustration Impact

### What is Frustration Impact?

Frustration Impact helps you understand how much each issue in your app contributes to frustrating sessions, affecting both your **Frustration score** and **issue prioritization**. This calculation ensures that the issues causing the most user frustration are ranked higher in the **Issues List**, helping you focus on what matters most.

<figure><img src="https://files.readme.io/2b4eae230a41b811856f0492e32d0f7f99ee602655822f0ff0a16d99f063a59b-apdex-impact-1.png" alt=""><figcaption></figcaption></figure>

***

### Frustration Impact Levels

To better understand the significance of each issue based on its Frustration Impact, issues are classified into the following categories:

* **High Impact:** Issues affecting ≥0.5% of total sessions. These are critical and require immediate attention.
* **Medium Impact:** Issues affecting between 0.01% and 0.5% of sessions. These should be addressed after high-impact issues.
* **Low Impact:** Issues affecting <0.01% of sessions. These have minimal impact but may still need resolution over time.
* **No Impact:** Issues that don’t affect your frustration-free sessions score, including:
  * APM groups where all occurrences are satisfying (Frustration-Free Sessions 1).
  * Metrics marked as non-key by your team.

***

### How is Frustration Impact Calculated?

The Frustration Impact of an issue reflects its effect on your app's frustration-free sessions by estimating the **percentage of frustrating or tolerable sessions it causes.**

#### For performance issues:

**Example 1: Cold App Launch**

We approximate the percentage of sessions that were **frustrating** or **tolerable** due to the **cold app launch**. We calculate this by considering how bad the **cold app launch** is within all app launches, and **how much app launches contribute to frustrating and tolerable sessions** in total.

<figure><img src="https://files.readme.io/63c8179a4263bf091ea7ac67b7e812df9f0db74445e1cc8e85eb89b976f22b57-Screenshot_2025-03-25_at_4.40.26_PM.png" alt=""><figcaption></figcaption></figure>

Where:

<figure><img src="https://files.readme.io/efb66e00632dd6617410205e1ac77aa23ba24b91a810ac4aabddcdeb663c9752-image.png" alt=""><figcaption></figcaption></figure>

**Example 2: Network Requests**

We approximate the percentage of sessions that were **frustrating** or **tolerable** due to this particular **network request**. We calculate this by considering **how bad the network request is** within all networks, and **how much networks are contributing to frustrating and tolerable sessions** in total.

<figure><img src="https://files.readme.io/432fa737d1d79e8bff04ad4e247a076a2a7a002d7e420d8a74e24fc2461ae0c7-Screenshot_2025-03-25_at_4.38.48_PM.png" alt=""><figcaption></figcaption></figure>

Where:

<figure><img src="https://files.readme.io/513af81c9ca1957ab9f4272dc85af54bac0ce02531d95a1c8c8e5c8a395ad615-image.png" alt=""><figcaption></figcaption></figure>

**Example 3: App Hangs**

<figure><img src="https://files.readme.io/e9b552b3d649294f2033b56827a306f031792afae00785479f98a8b7770ab555-Screenshot_2025-04-14_at_4.00.14_PM_1.png" alt=""><figcaption></figcaption></figure>

Where:

<figure><img src="https://files.readme.io/4111cb3d88193e62c09b10e11a370b52bd2ec074fda01a30e30fe7be1a3b6edf-image.png" alt=""><figcaption></figcaption></figure>

**Notes:**

* This calculation applies to **app launch**, **networks**, **screen loading**, **flows**, **UI hangs**, **app hangs**, and **force restarts**.
* When calculating **Frustrating/Tolerable Sessions Caused by an issue, tolerable sessions** are given **half the weight** compared to **frustrating sessions**.
* **Dissat count** = (number of frustrating occurrences) + 0.5 \* (number of tolerable occurrences)

#### For Crashes:

A crash occurrence disrupts the user session completely. So we simply calculate the percentage of sessions this crash impacted.

<figure><img src="https://files.readme.io/5bb918a156bee2a5221f3ac794fef0a993367a8f0ed62137e971204837dda719-Screenshot_2025-03-25_at_4.38.59_PM.png" alt=""><figcaption></figcaption></figure>

**Notes:**

* This calculation applies to fatal crashes, ANRs for Android, and OOMs for iOS.

<br>

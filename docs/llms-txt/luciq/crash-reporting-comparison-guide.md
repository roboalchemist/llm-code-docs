# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/crash-reporting-comparison-guide.md

# How to compare Luciq's Crash Reporter with your current vendor

Comparing two crash reporters can be challenging due to the variability in data collection and reporting. **It's crucial to understand that discrepancies of plus or minus 5-10% are normal and acceptable when analyzing crash reports.**

This variance occurs because crash reporters capture crashes at different points in the application lifecycle, use different symbolication methods, and employ varying network retry logic. Additionally, factors like battery level, network connectivity, and whether the app is restarted can all affect whether a crash is successfully reported.

{% hint style="info" %}
This comparison is more straightforward on Android, where both crash reporters can run simultaneously. On iOS, running multiple crash reporters concurrently can lead to conflicts and unreliable data.
{% endhint %}

### The Goal of the Comparison

It's important to stress that exact matches in numbers between crash reporters are not the goal. The primary objective is to ensure that the types of crashes captured by your current vendor are also identified by Luciq.

A successful comparison has two objectives:

1. **Total captured occurrences are similar but not exact:** Within the comparison criteria mentioned below, crash counts should align within ±10%.
2. **All crash types are detected:** The top crashes and all types of crashes captured by your current vendor should also be identified by Luciq.

Due to the nature of crash reporting, the numbers may not align perfectly, and this is expected. Here's why:

* **Crashes are unpredictable events.** They occur in varying network and device conditions. Sometimes with connectivity, sometimes without; sometimes with low memory, sometimes under extreme resource constraints.
* **Crash capture can be interrupted** by system limitations or immediate app termination
* **SDKs operate with different priorities.** Different crash reporting SDKs hook into the system's crash handler at slightly different priority levels.
* **Network transmission varies** based on connectivity, battery level, and each SDK's retry logic

### Steps for Effective Comparison

1. **Select a Consistent Basis for Comparison:**
   1. Choose one app version.
   2. Pick a specific date range for the comparison. (absolute date range and not last x days)
   3. Focus on fatal crashes that affected your app, excluding system crashes.
2. **Ensure Deobfuscation:**
   1. Make sure that both crash reports are deobfuscated. Grouping accuracy is significantly improved when crashes are deobfuscated.
3. **Sort and Compare:**
   1. Sort your vendor's crash reports by top crashes based on occurrences.
   2. Compare this sorted list with Luciq’s crash reports.
   3. Each vendore groups in a way, combine similar crashes to make the comparison better.

### Limited Rollout vs. Full User Base

Comparing the performance of Luciq rolled out to a limited percentage of users with 100% of the user base isn't an apples-to-apples comparison. Here's why:

1. **Smaller Sample Size:**\
   With only a low percentage of users, you have a smaller data set to analyze. This can lead to statistically insignificant results, making it difficult to draw accurate conclusions about the application's overall performance.
2. **Self-Selection Bias:**\
   In a limited rollout, the percentage of users who receive the new version might not be representative of the entire user base. Early adopters or those with specific interests may be more likely to be included, skewing the performance data. Early adopters often have newer devices, more updated operating systems, and different usage patterns than the general user base—they may encounter fewer compatibility issues but stress-test new features more heavily, potentially experiencing crashes that wouldn't affect typical users, or vice versa.
3. **Unforeseen Issues:**\
   Limited rollouts are often used to identify and fix bugs or compatibility issues before a wider release. Issues encountered by the rolled-out population might not be representative of what the entire user base would experience.

By following these steps, focusing on the types of crashes, and understanding the limitations of limited rollouts, you'll be able to make a more meaningful and accurate comparison between Luciq’s crash reporter and your current vendor.

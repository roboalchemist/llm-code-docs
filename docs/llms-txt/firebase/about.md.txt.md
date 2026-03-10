# Source: https://firebase.google.com/docs/remote-config/rollouts/about.md.txt

# About Remote Config rollouts

This guide provides information about key concepts related to Remote Config rollouts, so
that you can:

- [Understand how rollout group membership works.](https://firebase.google.com/docs/remote-config/rollouts/about#understand-rollout-membership)
- [Know when to use a rollout and when to use an A/B Test.](https://firebase.google.com/docs/remote-config/rollouts/about#when-use)
- [Learn how to interpret rollout results.](https://firebase.google.com/docs/remote-config/rollouts/about#understand-rollout-results)

## Understand rollout group membership

When you create a new rollout and assign a percentage, Firebase places an
equally-sized portion of your audience into a control group for accurate results
when comparing the performance of your enabled feature, resulting in the
following groups.

- **Enabled**: User devices assigned to this group receive the value you configure in your rollout.
- **Control** : User devices assigned to this group receive value they otherwise would have received from Remote Config, not the rollout value.
- **Unassigned:** User devices in this group receive the value they otherwise would have received from Remote Config, but *are not* used in rollout comparison results.

That is, if you roll out to 2% of your users, they are added to the Enabled
group and an additional 2% of your users are added to the Control
group, which is used for comparison. 96% of your users remain in Unassigned.

This approach ensures a fair comparison between the performance of users and
devices that receive your rollout value and those that do not and lets you
effectively determine success or failure of the rollout on the [Rollout
Results](https://firebase.google.com/docs/remote-config/rollouts/about#understand-rollout-results) page.

> [!NOTE]
> **Note:** In order to achieve equally-sized groups, any rollout you create must be exposed to less than or equal to 50% until and unless you roll out to 100% of your users.

Rollout group assignment is consistent across all phases of a rollout. That is,
within the same rollout, if you reduce the percentage to 0%, all users will
revert to receiving the parameter value defined in the Remote Config
template. If you later decide to increase the rollout percentage, users who were
part of the previous Enabled or Control groups will return to the group they
were originally assigned and will receive values consistent with those groups.

When you've verified that your release is successful and decide to fully launch
to 100% of targeted users, Firebase no longer uses the control group and *all*
targeted users and devices receive the rollout value.

## When to use a rollout versus an A/B test?

Remote Config rollouts and A/B Testing are appropriate for slightly different use
cases and can be used in a complementary manner.

**Rollouts** are gradual releases, and are often used to release a new feature
to a select group of users. You might want to target users in a specific
country, or using a specific version of your app. Use rollouts to mitigate risk,
to test new features in a real-world environment, with tight controls, so that
you can see how the feature performs. You can also monitor how your backend
services perform with the added load of the new feature, and approximate usage
to ensure your change is scalable before releasing to a wider audience.

Rollouts are excellent tools for situations where you're implementing new
features that significantly change functionality, changes that may result in
unpredictable results, or changes that may impact your backend infrastructure,
services, or external APIs.

[**A/B Testing**](https://firebase.google.com/docs/ab-testing/ab-concepts) gives you the ability to
present multiple versions of a feature or app element, for example,
updating UI look and feel, changing advertising copy, updating game level
difficulty. You can then expose different variations to your users to learn
which option drives better results based on your chosen metric (like user
engagement, ad clicks, and revenue).

Use A/B Testing for data-driven decision making, optimization, and
understanding your users' preferences. It's perfect for situations where
you have multiple comparable options and very specific goals. For example,
A/B Testing is appropriate for changes where you want to tweak your app
to improve a specific metric, like testing which banner ad placement
results in more clicks.

It's also a good idea to combine Remote Config rollouts and A/B Testing within an
overarching strategy: First, create an A/B Test with a constrained set of
users to determine the variant that produces the optimal results for your
key metrics. Then, after A/B Testing has determined [a
leader](https://firebase.google.com/docs/ab-testing/ab-concepts#leader-determination), create a
rollout with the winning variant. Monitor its stability and key metrics as
you incrementally increase the number of exposed users and, after you're
confident in its performance, roll it out to 100%.

## Understand rollout results

After you publish a rollout, you should start seeing results almost immediately.

You can view results in multiple ways:

- From the **Parameters** page, expand the parameter you configured for the Rollout and, beneath the rollout, click **View results**.
- From the **Rollouts** page, click the rollout name.

The app selector at the top of the Results page lets you select views for
specific apps. Results are divided into multiple sections:

- The **Summary** section, which shows the configured **Rollout percentage** and provides the ability to roll back or edit the rollout. When expanded, it shows an **Overview** of your rollout's configuration details and **Change
  history**.
- The **Users** section, which shows the number of unique app
  installations that have fetched a rollout template in the following
  groups:

  - **Enabled:** Number of app instances that match target rollout condition and have fetched the rollout value.
  - **Control:** Number of app instances that match the target rollout condition and have fetched the unchanged value.
  - **Target**: Estimated total number of instances that match the condition you set in your rollout, which should receive either the rollout or an unchanged value.

  Learn more at
  [Understand rollout group membership](https://firebase.google.com/docs/remote-config/rollouts/about#understand-rollout-membership).
- The [**Crashlytics**](https://firebase.google.com/docs/remote-config/rollouts/about#crashlytics-results) and
  [**Analytics**](https://firebase.google.com/docs/remote-config/rollouts/about#analytics-results) sections, which show comparison data
  for Enabled and Control groups. You can filter the collected data for the
  **Last 24 hours** , **Since last publish** , or **Last 7 days**. Last 24 hours
  is the default view.

### Crashlytics results for rollouts

You can see the total number of **Crashes** , **Non-fatals** , and **ANRs** that
occurred during your rollout. Each result category shows a bar graph that
compares the raw totals of the **Enabled** and **Control** users that met the
condition of the rollout.

- **Crashes:** Shows the number and percentage of crashes, and the number of unique users who experienced crashes for the Enabled and Control groups.
- **Non-fatals:** Shows the number and percentage of non-fatal errors, number of unique users who experienced non-fatal errors.
- **ANRs (Android apps only):** Shows the number and percentage of "Application Not Responding" events, as well as the number of unique users who experienced one or more ANR events.

For more detailed information about crashes, you can click **View more in
Crashlytics** . This opens the Crashlytics page with an active filter for
the rollout whose results you were inspecting. The rollout results on the
Crashlytics page measures all users who have *ever* been exposed to the
respective variant, **Enabled** or **Control**. You can choose to view Control
group crashes, Enabled group crashes, or both.

> [!TIP]
> **Tip:** When viewing results in Crashlytics, you can filter for events that happened while a specific rollout was active by selecting **Filter issues** \> **Rollouts** and then selecting one or more rollout names.

### Google Analytics results for rollouts

The Google Analytics rollout results section compares Analytics
metrics for all users who have ever been exposed to the Enabled or Control
groups in detail and in graph views. Three metrics are provided:

- **Total revenue:** Shows the total amount of revenue, including Ad revenue and Purchase revenue, in USD. You can filter your results to show results specifically for Ad revenue or Purchase revenue.
- **Total conversions:** Shows the raw count of the sum of all conversion events. You can filter your results by the conversion that you want to highlight.
- **Total engagement time:** Shows The total engagement time that your users spent with one of the rollout variants. Total engagement time is displayed in the Hours:Minutes:Seconds format. For example, 01:31:28. The graph shows data from the time period you selected above the Crashlytics section.

## Next steps

- [Get started with Remote Config rollouts](https://firebase.google.com/docs/remote-config/rollouts).
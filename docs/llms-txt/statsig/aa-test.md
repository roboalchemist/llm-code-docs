# Source: https://docs.statsig.com/experiments/types/aa-test.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Running an A/A Test

> Learn how to run A/A tests to validate your experimentation setup and ensure proper metrics configuration.

In this guide, you will create and implement an A/A test on your product in Statsig from end to end. This is commonly used to validate a new experimentation engine you may be integrating with.

For new users just getting started with Statsig, we often recommend running an A/A test to provide a “low-stakes” first test environment to ensure that you have your metrics set up correctly and are seeing exposures flowing through as expected before kicking off your first real A/B test.

By the end of this tutorial, you will have:

* Created a new **Feature Gate** in the Statsig console, set up as an "A/A test"

## Prerequisites

1. You already have a [Statsig account](https://console.statsig.com/sign_up)
2. You already [integrated the Statsig Client SDK](/sdks/quickstart) into an existing application

## Step 1: Create a feature gate in the console

The easiest way to run an A/A test in Statsig is by leveraging a [Feature Gate](/feature-flags/overview). You can also leverage an [Experiment](/guides/abn-tests) to run an A/A, but we chose to use a Feature Gate for this tutorial for simplicity.

Log into the Statsig console at [https://console.statsig.com/](https://console.statsig.com/) and navigate to **Feature Gates** in the left-hand navigation panel.

Click on the **Create** button and enter the name and (optional) description for your feature gate. We will call our feature gate “aatest\_example”. Click **Create**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163246908-24494f12-9d2e-4d8b-8e3e-4fc0ad9c7e41.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=ff488ae925ec3a045ee4c0f43d2873c3" alt="create_new_fg_empty" width="496" height="424" data-path="images/experiments/types/aa-test/163246908-24494f12-9d2e-4d8b-8e3e-4fc0ad9c7e41.png" />
</Frame>

In the Setup tab, define the rules for this feature gate. Tap **+ Add New Rule**. While you could run an A/A test on a specific user-group, platform, etc. the easiest setup is to simply divide all of your traffic 50/50 and deliver the same experience (your default product experience) to each group.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163247089-360857f8-ada3-46af-ac82-e41fc99274b5.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=bc486ec4e9d5a784ac2bc225194fd1bd" alt="add_new_rule_empty" width="497" height="588" data-path="images/experiments/types/aa-test/163247089-360857f8-ada3-46af-ac82-e41fc99274b5.png" />
</Frame>

To do this, under **Criteria** select **Everyone** (you may need to scroll up), name your rule, and then change the **Pass Percentage** to 50%. Click **Add Rule** and that’s it! Tap **Save Changes** in the upper right-hand corner.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163247141-30c96f8a-8257-4b39-aa9f-830bb3c89228.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=378d886566f87789672e7df64da082bb" alt="add_new_rule_filled" width="496" height="546" data-path="images/experiments/types/aa-test/163247141-30c96f8a-8257-4b39-aa9f-830bb3c89228.png" />
</Frame>

Your feature gate setup should now look as follows-

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163247211-aacb2c54-1088-4c4a-ab7b-64e393383bdb.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=f30d32cc2a7726f82256da195ab67a7d" alt="aa_rule_filled_out" width="1327" height="637" data-path="images/experiments/types/aa-test/163247211-aacb2c54-1088-4c4a-ab7b-64e393383bdb.png" />
</Frame>

Check that it is working as expected by typing in some dummy user IDs into the console- roughly 50% of the time your IDs should pass, and 50% of the time they should fail.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163247281-c0fb8089-f418-41af-a3a7-d8e684a3cdf3.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=bb040b04e0e35445fe1a8dcc66a60921" alt="check_rule_pass" width="1322" height="426" data-path="images/experiments/types/aa-test/163247281-c0fb8089-f418-41af-a3a7-d8e684a3cdf3.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163247287-7d565983-8253-4841-a65a-0f74d2e103b2.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=14cbd5e8169ba09e4057cb3cea83319c" alt="check_rule_fail" width="1323" height="426" data-path="images/experiments/types/aa-test/163247287-7d565983-8253-4841-a65a-0f74d2e103b2.png" />
</Frame>

## Step 2: Check the feature gate in your code

Copy the code snippet in the upper right hand corner of your feature gate page under the **\< >** symbol and drop it into your application at the point you want to call the A/A check.

```jsx  theme={null}
statsig.checkGate("aatest_example") 
```

Now when a user renders this page in their client application, you will automatically start to see a live log stream in the Statsig console when you navigate to the **Diagnostics** tab for your feature gate.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163247712-4610d7b4-188f-4418-a696-127b3c2f54da.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=6f06bf5a965611d39ab227072c6e44d0" alt="logstream" width="1306" height="611" data-path="images/experiments/types/aa-test/163247712-4610d7b4-188f-4418-a696-127b3c2f54da.png" />
</Frame>

## Step 3: Review A/A test results

Within 24 hours of starting your experiment, you'll see the cumulative exposures in the **Pulse Results** tab of your feature gate.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163247787-be1e816c-f715-4fd3-ad59-3a6caf48027a.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=880c7a70508afabb17fe426afe24f090" alt="cumulative_exposures" width="997" height="349" data-path="images/experiments/types/aa-test/163247787-be1e816c-f715-4fd3-ad59-3a6caf48027a.png" />
</Frame>

This will break down your logged exposures (as well as the distribution of the logged exposures). If something looks off, check the **Diagnostics** tab for more granular, day-by-day exposure breakdowns at both the Checks and User level.

In the **Metric Lifts** panel, you can see the full picture of how all your tagged metrics are performing.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/163248267-7bd7419a-59e0-4d58-b8e5-8ace95ed74d9.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=f3577e3032d790fae8ce2edafc245bb1" alt="pulse_results_empty" width="987" height="1208" data-path="images/experiments/types/aa-test/163248267-7bd7419a-59e0-4d58-b8e5-8ace95ed74d9.png" />
</Frame>

What should you expect to see?

* **Exposures**- make sure you’re seeing exposures flowing through as expected from your product. If you’re not seeing exposures, use the **Diagnostics** tab and the **Exposure Stream** to debug
* **Pulse results**- roughly 5% of your metrics in Pulse should be showing a statistically significant change due to the 95% confidence interval of Statsig’s stats engine

We recommend running your A/A long enough to reach most of your weekly active users, or at least a week.

## Simulated A/A Tests

We’ve made running A/A tests at scale easy by setting up simulated A/A tests that run every day in the background, for every company on the platform. An A/A test is like an A/B test - but both groups get the same experience. A/A tests help build trust in your experimentation platform (and your metrics!)

A/A tests can be Online or Offline. An [Online A/A test](/guides/aa-test) is run on real users. An engineer instruments your app with the Statsig SDK to check for experiment assignment. Assignment is logged, but there's no difference in experience to the user.

Since there is no effect, you expect to only see statistical noise. When using 95% confidence intervals, only \~1 in 20 metrics will show a stat-sig difference between control and test.

### Offline A/A tests

A single request runs on one unit type, and an offline A/A test works by

1. Querying a representative sample of your data
2. Randomly assigning subjects to Test or Control
3. Computing relevant metrics for Test vs Control and running them through the stats engine
4. You're looking for the % of false positives. If your p-value cutoff is 0.05 (typical), you'd expect a \~5% false positive rate.

You can download the running history of your simulated A/A test performance via the “Tools” menu in your Statsig Console. We run 100 tests per request.

### File Description

| Column Name                          | Description                                                         |
| ------------------------------------ | ------------------------------------------------------------------- |
| metric\_name                         | Name of the Metric                                                  |
| metric\_type                         | Type of Metric                                                      |
| unit\_type                           | The unit used to randomize (e.g. userID)                            |
| n\_tests                             | The number of tests run                                             |
| pct\_ss\_95\_pct\_confidence         | The percentage of tests that have a stat-sig result for this metric |
| avg\_units\_per\_test                | The number of units (often users) sampled into the A/A test         |
| avg\_participating\_units\_per\_test | The number of units in the test with a value for this metric        |

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/HZGmTR51kQF0d2q8/images/experiments/types/aa-test/199562491-84d9b7c4-1cea-4308-a0a9-c04a14a41671.png?fit=max&auto=format&n=HZGmTR51kQF0d2q8&q=85&s=96cde3e80d6431d4c9d938fe783c1e19" alt="A/A test results table showing statistical significance percentages" width="1316" height="1204" data-path="images/experiments/types/aa-test/199562491-84d9b7c4-1cea-4308-a0a9-c04a14a41671.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
# Source: https://docs.statsig.com/statsig-warehouse-native/features/interpreting-results/read-results.md

# Source: https://docs.statsig.com/experiments/interpreting-results/read-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Read Experiment Results (Formerly "Pulse")

## Read Experiment Results

To read the results of your experiment, go to the **Results** tab, where you will see your experiment hypothesis, **exposures**, and **Scorecard**.

### Exposures

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ABt5zTtoVx2ssgdr/images/snippets/pulse/read-results/7a80e74e-140d-4c36-a78e-c9b626e1fee5.png?fit=max&auto=format&n=ABt5zTtoVx2ssgdr&q=85&s=bc6d5ec63fa6734ce31395846f31ec0d" alt="Exposures chart showing cumulative users per experiment group" width="1318" height="530" data-path="images/snippets/pulse/read-results/7a80e74e-140d-4c36-a78e-c9b626e1fee5.png" />
</Frame>

At the top of the Results page is the Exposures Chart. Exposures are the unique experimental units enrolled in the experiment. This is typically the number of unique users, and for device-level experimentation, this is the number of devices. The timeline shows you when the experiment was started, and how many exposures were enrolled on any given day. You can see the rate at which users were added into each group of the experiment, how many total users were exposed, and confirm the target ratio matches what you configured in experiment setup.

### Scorecard

The experiment **Scorecard** shows the metric lifts for all Primary and Secondary metrics you set up at experiment creation.

#### Immediately Post-experiment Start

For up to the first 24 hours after starting your experiment (before our daily metric results run), the **Scorecard** section is calculated hourly (this only applies to Statsig Cloud, for WHN projects you will need to reload results on demand or set up a daily schedule). This more real-time scorecard is designed to enable you to confirm that exposures and metrics are being calculated as expected and debug your experiment or gate setup if needed.

<Note>
  You should **not** make any experiment decisions based on real-time results data in this first 24 hour window after experiment start. Experiments should only be called once the experiment has hit target duration, as set by your primary metric(s) hitting experimental power.
  Read more about target duration [here](/experiments-plus/create-new#target-duration).
</Note>

Given data during this early post-experiment start window is designed for diagnostic, not decision-making purposes, you will notice a few key differences between this real-time view and the results that will start showing after daily runs have initiated:

* Metric lifts do not have confidence intervals
* No time-series view of metric trends
* No projected topline impact analysis
* No option to apply more advanced statistical tactics, such as CUPED or Sequential Testing

All of these are available in daily Results, which will start showing in the next daily run.

#### Post-first Day Scorecard

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/pulse/read-results/8b855f5c-d26f-4185-ac31-5108fbebe18e.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=5438397c57ebdb1ace781aa8bd69fb3c" alt="Experiment scorecard table displaying metric lifts and confidence intervals" width="1377" height="707" data-path="images/snippets/pulse/read-results/8b855f5c-d26f-4185-ac31-5108fbebe18e.png" />
</Frame>

The experiment Results daily run calculates the difference between the comparable randomization groups (eg. test and control) across your company's suite of metrics, and applies a statistical test to the results. You can read more about Statsig's stats engine [here](/stats-engine).

For every metric, we will show you:

* The calculated relative difference (Delta %)
* The confidence interval
* Whether the result is statistically significant
  * Positive lifts are green
  * Negative lifts are red
  * Non-significant results are grey

The formula for calculating lift is:

Delta(%) = (Test - Control) / Control

Confidence intervals are reported at the selected significance level (95% by default). In a typical two-sided Z-test, we show the confidence interval as +/- 1.96 \* standard error.

99.9% winsorization is automatically applied to event\_count, event\_count\_custom, and sum metrics. This caps extreme outlier values to reduce their impact on experiment results. For metrics added to the **Scorecard** or **Monitoring Metrics** sections of your experiment or gate, you can also apply other optional statistical treatments, such as CUPED (pre-experiment bias reduction) and sequential testing adapted confidence intervals. Read more [here](/stats-engine).

* **Experiment results are computed for the first 90 days**: By default, Statsig will compute experiment results for your experiment for only the first 90 days of your experiment. You will be notified via e-mail as you approach the 90 days cap, at which point will be able to extend this compute window for another 30 days at a time. If the experiment runs beyond the compute window, new users will stop getting added into the experiment's result, but analysis for existing users who have been exposed to the experiment will continue to run even if the compute window is not extended, until you make a decision on the experiment.

<Note>
  This experiment result calculation window only affects whether a user is included in the experiment's analysis, and does not affect the treatment each user would receive. New users would still receive the experience for the group they get randomized into.
</Note>

### Experiment Results Views

There are a few different views to see your Scorecard metric lifts, namely:

* **Cumulative results (default view)**: Displays the aggregate difference between experiment groups and visualizes the corresponding confidence intervals
* **Table view**: Displays the same data as the cumulative view but in a table format with additional fields
* **Daily results**: Shows the difference between experiment groups aggregated based on days since start of experiment
* **Days since exposure**: Shows the difference between experiment groups aggregated based on days since exposure to the experiment

Cumulative results includes a detailed view on hover, where you can additionally view the raw statistics used in the metric lift calculations, as well as topline impact.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/pulse/read-results/856c7750-df56-45d9-b253-6b63f336cac7.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=3851b2e97105703ddc10b2ef22715980" alt="Cumulative results view with hover details" width="1378" height="765" data-path="images/snippets/pulse/read-results/856c7750-df56-45d9-b253-6b63f336cac7.png" />
</Frame>

### Dimensions

There are two ways in which we can breakdown a given Scorecard metric - one is by a **User Dimension**, the other is by an **Event Dimension**.

#### User Dimensions

User Dimensions refer to user level attributes that are either part of the user object you log, or additional metadata that Statsig extracts. Examples of these user attributes could be operating system, country, and region.

You can create [custom "explore" queries](/pulse/custom-queries) to *filter on* or *group by* available user dimensions. For example, you could "See results for users in the US", or "See results for users using iOS, grouped by their country". Go to the "explore" tab to draft a custom query

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/pulse/read-results/e3afb526-8f9d-465e-af33-ea9575ac69e7.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=5b3d53523ab45a5da865d578992a6115" alt="custom queries" width="1328" height="773" data-path="images/snippets/pulse/read-results/e3afb526-8f9d-465e-af33-ea9575ac69e7.png" />
</Frame>

#### Event dimensions

Events Dimensions refer to the value or metadata logged as part of a custom event that is used to define the metric. If you want to see results for a metric broken down by categories that are specific to that metric, [specify the dimension](/metrics/metric-dimensions) you want to break down by in the **value** or **metadata** attributes when you log the source event. For example, when you log a "click" event on your web or mobile application, you may also log the target category using the **value** attribute as shown below. Statsig will automatically generate results for each category in addition to the top level metric.

To see breakdowns for all categories within a metric, click on the (+) sign next to the metric.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/ABt5zTtoVx2ssgdr/images/snippets/pulse/read-results/65cbe2a0-d269-4385-a606-c825ff2e8e05.png?fit=max&auto=format&n=ABt5zTtoVx2ssgdr&q=85&s=87463043338fada7844b7c366e7568a5" alt="dimension button" width="379" height="245" data-path="images/snippets/pulse/read-results/65cbe2a0-d269-4385-a606-c825ff2e8e05.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/pulse/read-results/f557dac6-e29f-4cb5-bd6a-19fc2b226193.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=52ac3d2704e2c284a0e7062f2b0c3d0f" alt="dimension results view" width="1326" height="281" data-path="images/snippets/pulse/read-results/f557dac6-e29f-4cb5-bd6a-19fc2b226193.png" />
</Frame>

### Significance Level Settings

These settings can be adjusted at any time to view Scorecard results with different significance levels.

* **Apply Benjamini-Hochberg Procedure per Variant**: Select this option to apply the procedure to reduce the probability of false positives by adjusting the significance level for multiple comparisons - [read more here](/stats-engine/methodologies/benjamini-hochberg-procedure).
* **Confidence Interval**: Changes the confidence interval displayed with the metric deltas.  Choose lower confidence intervals (e.g.: 80%) when there's higher tolerance for false positives and fast iteration with directional results is preferred over longer/larger experiments with increased certainty.
* **CUPED**: Toggle CUPED on/ off via the inline settings above the metric lifts. Note that this setting can only be toggled for **Scorecard** metrics, as CUPED is not applied to non-Scorecard metrics.
* **Sequential Testing**: Applies a correction to the calculate p-values and confidence intervals to reduce false positive rates when evaluating results before the target completion date of the experiment. This helps mitigate the increased false positive rate associated with the "peeking problem". Toggle Sequential Testing on/ off via the inline settings above the metric lifts. Note that this setting is available only for experiments with a set target duration.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/pulse/read-results/d2d7405a-9e86-4317-8f32-51b369c66699.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=321171f661c85c9140fea7bf07f3bc6f" alt="analysis settings" width="583" height="58" data-path="images/snippets/pulse/read-results/d2d7405a-9e86-4317-8f32-51b369c66699.png" />
</Frame>

### Restarting Results

<img width="1062" height="80" alt="Restart results banner" src="https://mintcdn.com/statsig-4b2ff144/ABt5zTtoVx2ssgdr/images/snippets/pulse/read-results/201ab314-9304-43f1-bc11-58dcf9394aa2.png?fit=max&auto=format&n=ABt5zTtoVx2ssgdr&q=85&s=710a2bd3af54951ebbb709e477b5990e" data-path="images/snippets/pulse/read-results/201ab314-9304-43f1-bc11-58dcf9394aa2.png" />

If your experiment has stopped computing results, you can resume updates by clicking the Restart button. There are some important facts to be aware of:

* A Restart is not a [Reset](/experiments/ending/ending-experiment#stopping-an-experiment) of your experiment. A Restart will not re-salt (i.e. re-randomize) units in your experiment, and all users will continue to receive the same group assignments.

* Statsig will begin computing experiment results anew from the restart point, so your metric results will start over. Old results may still be available in timeseries and explore query views, but they will not be carried forward or updated.

* Your Cumulative Exposures chart will update based on new exposures, but the duration of the pause in computations will affect if the chart starts over from zero or your exposure count includes past exposures.

It's best to avoid having to Restart Results by actively extending experiments while they're running. Be sure to look out for email alerts from Statsig and check in your experiments regularly.


Built with [Mintlify](https://mintlify.com).
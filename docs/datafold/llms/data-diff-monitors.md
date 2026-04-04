# Source: https://docs.datafold.com/data-monitoring/monitors/data-diff-monitors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Diff Monitors

> Data Diff monitors compare datasets across or within databases, identifying row and column discrepancies with customizable scheduling and notifications.

## Ways to create a data diff monitor

There are 3 ways to create a data diff monitor:

1. From the **Monitors** page by clicking **Create new monitor** and then selecting **Data diff** as a type of monitor.
2. Clone an existing monitor by clicking **Actions** and then **Clone** in the header menu. This will pre-fill the form with the existing monitor configuration.
3. Create a monitor directly from the data diff results by clicking **Actions** and **Create monitor**. This will pre-fill the configuration with the parent data diff settings, requiring updates only for the **Schedule** and **Notifications** sections.

Once a monitor is created and initial metrics collected, you can set up [thresholds](/data-monitoring/monitors/data-diff-monitors#monitoring) for the two metrics.

## Create a new data diff monitor

Setting up a new diff monitor in Datafold is straightforward. You can configure it with the following parameters and options:

### General

Choose how you want to compare your data and whether the diff type is in-database or cross-database.

Pick your data connections. Then, choose the two datasets you want to compare. This can be a table or a view in your relational database.

If you need to compare just a subset of data (e.g., for a particular city or last two weeks), add a SQL filter.

Select **Materialize inputs** to improve diffing speed when query is heavy on compute, or if filters are applied to non-indexed columns, or if primary keys are transformed using concatenation, coalesce, or another function.

<Frame caption="Data Diff General Settings">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a06294be7daca047c2f4d40d47f2c69f" data-og-width="1497" width="1497" data-og-height="1005" height="1005" data-path="images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=213af5fdb48e1012d925a8be5203943a 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=51eb58c7cfd9012a4e801be46e44880e 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=89639c2d9c761dcfbdabf9d3900f9161 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1f0b0df1baeaa5f720449433d3a2f62a 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=e047642410f555d62c95b5ddc98bdf0d 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_general-bdcc461b033ca6c91e5831339673e522.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=21c33bf84a0a60743205df808fcb2b8d 2500w" />
</Frame>

### Column remapping

When columns are the same data type but are named differently, column remapping allows you to align and compare them. This is useful when datasets have semantically identical columns with different names, such as `userID` and `user_id`. Datafold will surface any differences under the column name used in Dataset A.

<Frame caption="Column Remapping Settings">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=30f8c1dfd4fc510154c421eeb817cc21" data-og-width="1499" width="1499" data-og-height="455" height="455" data-path="images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=0c0a4eed190fa23f92df206b7ea5bfe9 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=bf3a422997eab6ba6643a8c831cfd5dd 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=026c103728585781724d615ac7603092 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=cd3cf76a5f59560645284b636c3a4d72 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=ff1e41e1b13a26651a145972bd981a9e 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_column_remapping-59552ddfda90200e3eba4ab4461757f8.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b5211e308e7986c49164bf9f167beec7 2500w" />
</Frame>

### Diff settings

<Frame caption="Diff Settings">
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=8eabf23bd47e14ba6dcd5337c99c6f20" data-og-width="1494" width="1494" data-og-height="1263" height="1263" data-path="images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=2acf7e0252c0342a0a0d2107b6b11b45 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=b52751b92261f735321ebefe513908a2 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3d13cdec6683755445b58d4a9464169e 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=1ecde098cc2ed4039b19edd30baa294c 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3d37646ea7df295d3e31a9c97e69b04f 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_diff_settings-cd905714f5f522817bcd503f38a1fefc.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=7b749a57785dd6d6d310ed45cad1c7a5 2500w" />
</Frame>

#### Primary key

The primary key is one or more columns used to uniquely identify a row in the dataset during diffing. The primary key (or keys) does not need to be formally defined in the database or elsewhere as it is used for unique row identification during diffing. Multiple columns support compound primary key definitions.

#### Columns to compare

Determine whether to compare all columns or select specific one(s). To optimize performance on large tables, it's recommended to exclude columns known to have unique values for every row, such as timestamp columns like "updated\_at," or apply filters to limit the comparison scope.

#### Materialize diff results

Choose whether to store diff results in a table.

#### Sampling

Use this to compare a subset of your data instead of the entire dataset. This is best for assessing large datasets.

There are two ways to enable sampling in Monitors: [Tolerance](#tolerance) and [% of Rows](#-of-rows).

<Tip>
  **TIP**

  When should I use sampling tolerance instead of percent of rows?

  Each has its specific use cases and benefits, please [see the FAQ section](#sampling-tolerance-vs--of-rows) for a more detailed breakdown.
</Tip>

##### Tolerance

Tolerance defines the allowable margin of error for our estimate. It sets the acceptable percentage of rows with primary key errors (like nulls, duplicates, or primary keys exclusive to one dataset) before disabling sampling.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=4febbf2598a8185c272232032d52de65" data-og-width="1494" width="1494" data-og-height="640" height="640" data-path="images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c6efacf6edb6b8c79ea1b606fcc8a1c6 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=28a2b6ae6a74f6016306275e487447a5 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=34b87a7124ceaeeb1af06576fe24d4a8 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a5ac9fcaf55e9b75177cca0f4acd53f4 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=71c98168b3b65380d590d3925051e87b 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_tolerance-c48e5b3c707d1e6cec2a5cde995c6d01.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=286afa738b16dc2f4f2f9d98d590270d 2500w" />
</Frame>

When sampling tolerance is enabled, not every row is examined, which introduces a probability of missing certain discrepancies. This threshold represents the level of difference we are willing to accept before considering the results unreliable and thereby disabling sampling. It essentially sets a limit on how much variance is tolerable in the sample compared to the complete dataset.

Default: 0.001%

###### Sampling confidence

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset. It represents the minimum confidence level that the rate of primary key errors is below the threshold defined in sampling tolerance.

To put it simply, a 95% confidence level with a 5% tolerance means we are 95% certain that the true value falls within 5% of our estimate.

Default: 99%

###### Sampling threshold

Sampling will be disabled if total row count of the largest table is less that the threshold value.

###### Sample size

This provides an estimated count of the total number of rows included in the combined sample from Datasets A and B, used for the diffing process. It's important to note that this number is an estimate and can vary from the actual sample size due to several factors:

* The presence of duplicate primary keys in the datasets will likely increase this estimate, as it inflates the perceived uniqueness of rows
* Applying filters to the datasets tends to reduce the estimate, as it narrows down the data scope

The number of rows we sample is not fixed; instead, we use a statistical approach called the Poisson distribution. This involves picking rows randomly from an infinite pool of rows with uniform random sampling. Importantly, we don't need to perform a full diff (compare every single row) to establish a baseline.

Example: Imagine there are two datasets we want to compare, Main and Test. Since we prefer not to check every row, we use a statistical approach to determine the number of rows to sample from each dataset. To do so, we set the following parameters:

* Sampling tolerance: 5%
* Sampling confidence: 95%

Sampling confidence reflects our level of certainty that our sample accurately represents the entire dataset, while sampling tolerance defines the allowable margin of error for our estimate. Here, with a 95% sampling confidence and a 5% sampling tolerance, we are 95% confident that the true value falls within 5% of our estimate. Datafold will then estimate the sample size needed (e.g., 200 rows) to achieve these parameters.

##### % of rows

Percent of rows sampling defines the proportion of the dataset to be included in the sample by specifying a percentage of the total number of rows. For example, setting the sampling percentage to 0.1% means that only 0.1% of the total rows will be sampled for analysis or comparison.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c682330c2d754021ef6b20164c2cf3c9" data-og-width="1482" width="1482" data-og-height="498" height="498" data-path="images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=6d14ee08e3e68fec35d1d2f173ddc174 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=edf6b8bb2703d6f79f1d579cb2fd2888 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=97119c1709e2a26dca8df8aa80c5ce5b 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=c9e0b7637dfee4e8d1edba0bf510acf2 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=065ee528210828e9a0d45b26286b27c8 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_settings_sampling_percent-48c1e9b953a45b49213d5a9799842875.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=a55178c8b732905ba9a01585e7da4c12 2500w" />
</Frame>

When percent of rows sampling is enabled, a fixed percentage of rows is selected randomly from the dataset. This method simplifies the sampling process, making it easy to understand and configure without needing to adjust complex statistical parameters. However, it lacks the statistical assurances provided by methods like sampling tolerance.

It doesn't dynamically adjust based on data characteristics or discrepancies but rather adheres strictly to the specified percentage, regardless of the dataset's variability. This straightforward approach is ideal for scenarios where simplicity and quick setup are more important than precision and statistical confidence. It provides a basic yet effective way to estimate the dataset's characteristics or differences, suitable for less critical data validation tasks.

###### Sampling rate

This refers to the percentage of the total number of rows in the largest table that will be used to determine the sample size. This ensures that the sample size is proportionate to the size of the dataset, providing a representative subset for comparison. For instance, if the largest table contains 1,000,000 rows and the sampling rate is set to 1%, the sample size will be 10,000 rows.

###### Sampling threshold

Sampling is automatically disabled when the total row count of the largest table in the comparison falls below a specified threshold value. This approach is adopted because, for smaller datasets, a complete dataset comparison is not only more feasible but also quicker and more efficient than sampling. Disabling sampling in these scenarios ensures comprehensive data coverage and provides more accurate insights, as it becomes practical to examine every row in the dataset without significant time or resource constraints.

###### Sampling size

This parameter is the [same one used in sampling tolerance](#sample-size).

### Add a schedule

You can choose to run your monitor daily, hourly, or even input a cron expression for more complex scheduling:

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=bba568fdc3049b5cf68cf1b8786eb97e" data-og-width="1184" width="1184" data-og-height="304" height="304" data-path="images/monitors/schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=23963e43888a23fa582b2ca0acb14278 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=be1bd4311a6edba905d6b0ac05ed9e40 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=84c1074e12d76ed7e1bb58a5b226f9ab 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=5a23b013dfdd0808925417e2890e5d53 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a46bd2d3dbeeecf2f5371f6549646331 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitors/schedule.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=a1003bb0bc5401af01a645062f9eb279 2500w" />
</Frame>

### Add notifications

You can add notifications, sent through Slack or emails, which indicate whether a monitor has been executed.

Notifications are sent when either or both predefined thresholds are reached during a Diff Monitor. You can set a maximum threshold for the:

* Number of different rows
* Percentage of different rows

<Frame>
  <img src="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=87bfb30d98bd8da832bcdd3192d9c559" data-og-width="1576" width="1576" data-og-height="578" height="578" data-path="images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=280&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=f7d5d2b6c2819122c487d7a25a69ff00 280w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=560&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=9187a82760eb2bf34b8567640887793e 560w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=840&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=aee0c94c2479f59f69ef009adc46bb72 840w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1100&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=8c6ee9ee72739450f84e7a1016f412bd 1100w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=1650&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=4059e04a333762886bff02f601f68fcd 1650w, https://mintcdn.com/datafold/BHI8Zy_v4DyXlmzL/images/monitor_settings_notifications-c4bd20b39b0ec478ae4a5e46a0dce0e8.png?w=2500&fit=max&auto=format&n=BHI8Zy_v4DyXlmzL&q=85&s=da1b7bebb6c322791e71a98bce66a2cf 2500w" />
</Frame>

## Results

The diff monitor run history shows the results from each run.

<Frame>
  <img src="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=d069f23a21e684fb6401fa7502f120a0" data-og-width="3059" width="3059" data-og-height="1502" height="1502" data-path="images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=280&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=74049ae838daa9b01486825d44485e92 280w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=560&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=23712bc34bd61835cc6e57263cddf9ac 560w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=840&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=3aa7dae0bf0f4eaed0d379d0f987c539 840w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=1100&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=6ab08d1c38569298ed0670526706564a 1100w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=1650&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=e916691a3ed08749f8448c03d9c63520 1650w, https://mintcdn.com/datafold/Q7OqZ4fuuETHBSvX/images/data_diff_results-0ed255b70929f8b7a501b59d042d7958.png?w=2500&fit=max&auto=format&n=Q7OqZ4fuuETHBSvX&q=85&s=db0aba8cb426d05c65c76f2e0ca06d58 2500w" />
</Frame>

Each run includes basic stats, along with metrics such as:

* The total rows different: number of different rows according to data diff results.
* Rows with different values: percentage of different rows relative to the total number of rows in dataset A according to data diff results. Note that the status `Different` doesn't automatically map into a notification/alert.

Click the **Open Diff** link for more granular information about a specific Data Diff.

## FAQ

<AccordionGroup>
  <Accordion title="Sampling tolerance vs. % of rows">
    Use sampling tolerance when you need statistical confidence in your results, as it is more efficient and stops sampling once a difference is confidently detected. This method is ideal for critical data validation tasks that require precise accuracy.

    On the other hand, use the percent of rows method for its simplicity and ease of use, especially in less critical scenarios where you just need a straightforward, quick sampling approach without worrying about statistical parameters. This method is perfect for general, easy-to-understand sampling needs.
  </Accordion>

  <Accordion title="Need help?">
    If you have any questions about how to use Data Diff monitors, please reach out to our team via Slack, in-app chat, or email us at [support@datafold.com](mailto:support@datafold.com).
  </Accordion>
</AccordionGroup>

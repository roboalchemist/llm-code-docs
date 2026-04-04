# Source: https://docs.statsig.com/statsig-warehouse-native/features/differential-impact.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Differential Impact Detection

> Learn how Statsig automatically flags experiments with extreme differential impacts on sub-populations.

## What is Differential Impact Detection?

Experiments can have interesting effects on sub-populations that are easily missed. They might have a bug that impacts only a certain browser, OS, or country. If the topline impact isn't significant or is canceled out by other changes - these are missed.

Statsig will automatically flag experiments when extreme differential impacts are detected for any sub-population you have configured. Once configured, experiments are analyzed for differential impact when Pulse is loaded after Day 1, Day 3 and when the Target Duration is met.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/whn/differentialImpact/9783ba7a-812b-4fea-97af-4e3344f8345f.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=efacd728e840091b3dcc13d9d3e4af40" alt="Differential impact detection alert in Pulse results" width="2048" height="1130" data-path="images/snippets/whn/differentialImpact/9783ba7a-812b-4fea-97af-4e3344f8345f.png" />
</Frame>

## Enabling this

Configure the "Segments of Interest" you want automatically evaluated for Differential Impact Detection. On Statsig Cloud, these are user properties in the [User Object](/concepts/user) you configure when using the Statsig SDK. On Statsig Warehouse Native they can be configured as an [Entity Property](/statsig-warehouse-native/features/entity-properties) too.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/whn/differentialImpact/c9bb5e56-dbc8-4fc2-a33b-92974f867120.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=3dede509ab983f630510b63314f1e03c" alt="Segments of Interest configuration interface" width="1292" height="749" data-path="images/snippets/whn/differentialImpact/c9bb5e56-dbc8-4fc2-a33b-92974f867120.png" />
</Frame>

This feature is also referred to as as **Heterogeneous Treatment Effect** or **Segments of Interest**.

## Seeing Differential Impacts

If extreme outliers are found for a segment you have configured, Statsig will flag this when you're looking at Pulse results. You will be able to see the data broken out by segments in the Explore section of your Pulse results.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/whn/differentialImpact/5e5a3907-ff67-404c-a94f-2f986262008e.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=acef5cad29faa65e4df6bccfbe0cd061" alt="Pulse results showing differential impact by segments" width="2177" height="1120" data-path="images/snippets/whn/differentialImpact/5e5a3907-ff67-404c-a94f-2f986262008e.png" />
</Frame>

## Methodology

We use a Welch’s t-test to compare the treatment effect for a particular segment of users to the treatment effect for all other users since we expect to potentially see unequal population variances when comparing user segments.

The average treatment effect is calculated as follows:

$\overline{TE} = \overline{X_t} - \overline{X_c} $

The variance in treatment effect is calculated as follows:

$var(TE) = var(X_t) + var(X_c)$

The n of the treatment effect is calculated as follows:

$n_{TE} = min(n_t, n_c)$

With these calculations, we can determine the t-statistic and degrees of freedom as we would for any experiment using [Welch's t-test](/stats-engine/p-value#welchs-t-test).
We then use a Bonferroni Correction to adjust our alpha to avoid false positives, setting a threshold where we consider there to be a high likelihood of heterogeneous treatment effect or some likelihood of heterogeneous treatment effect. We consider a specific dimension vs the rest calculation for one metric of one test variant vs the control to be one "comparison" for the sake of the Bonferroni Correction.

$\text{high chance of HTE, } \alpha = \frac{0.01}{\text{number of comparisons}}$

$\text{some chance of HTE, } \alpha = \frac{0.05}{\text{number of comparisons}}$

## Viewing Results

You can go to the explore tab of your experiment and filter to the Differential Impact Detection query type to see all historical analyses.

##


Built with [Mintlify](https://mintlify.com).
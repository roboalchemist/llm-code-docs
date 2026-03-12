# Source: https://docs.statsig.com/statsig-warehouse-native/cure/cure-setup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Started With CURE

## Defaults

By default, CURE will run a univariate regression when enabled - the same as the [standard implementation of CUPED](https://www.exp-platform.com/Documents/2013-02-CUPED-ImprovingSensitivityOfControlledExperiments.pdf).

To add additional covariates

## Project Defaults

In project settings under Experimentation, specify default covariates for your company:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/jlb5TRV6XjpxIwsY/images/cure/project_setting.png?fit=max&auto=format&n=jlb5TRV6XjpxIwsY&q=85&s=48b2d3eba50584b66950639f8fda75e4" alt="Project Settings" width="2638" height="258" data-path="images/cure/project_setting.png" />
</Frame>

Covariates can be sourced from the assignment source for the experiment, or from Entity Property Sources.

Properties with an Entity Property Source name attached come from a property source and will always be included on the experiment. Properties without an EPS come from an assignment source, and will be used if the column exists on the assignment source of a given experiment.

## Experiment Settings

Per-experiment, specify additional covariates or remove covariates specific to your analysis:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/jlb5TRV6XjpxIwsY/images/cure/experiment_setting.png?fit=max&auto=format&n=jlb5TRV6XjpxIwsY&q=85&s=89acf369e737f44a8351c45daafc8b8c" alt="Experiment Settings" width="2356" height="666" data-path="images/cure/experiment_setting.png" />
</Frame>

Like with the experiment settings, this list is sourced from the experiment assignment source columns as well as relevant Entity Property Sources.

## Metric:Metric

One tool our framework enables is using metric:metric covariates; for example, using units' pre-experiment clicks as a covariate for units' in-experiment revenue. We decided against using this for several reasons:

* Consistency. It should not be the case that adding a new metric to your analysis significantly alters the results of other metrics
* It's not necessary. If you have key metrics that function as covariates, we recommend **explicitly** providing these - for all metrics - as a covariate in an entity property source. This achieves the same result, without "black box" outputs coming from unknown metric covariances

Statsig has a strong opinion that throwing in arbitrary covariates based on an experiment's metric selection is a bad practice, and it is better to explicitly include key metric covariates as numerical covariates; please reach out in Slack if you would like to discuss!

## Preventing Adjustments

You can turn off CUPED in your pulse results, and can create a project-level setting to enforce this. This will still run CURE, however, which entails some amount of compute cost. To avoid running CURE, you can turn it off on a given metric by un-checking the CUPED option in the metric's setup page.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/jlb5TRV6XjpxIwsY/images/cure/metric_setting.png?fit=max&auto=format&n=jlb5TRV6XjpxIwsY&q=85&s=71734eb70748c3b192b8c8cdaead64b1" alt="Metric Settings" width="1044" height="126" data-path="images/cure/metric_setting.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).
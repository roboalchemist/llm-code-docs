# Source: https://docs.statsig.com/statsig-warehouse-native/features/statistics/methodologies/delta-method.md

# Source: https://docs.statsig.com/experiments/statistical-methods/methodologies/delta-method.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Delta Method

## Delta Method for Ratio Metics

Statsig uses the delta method when calculating the variance for variables that have a numerator and denominator.

The variance of ratio and mean metrics depends upon the numerator and denominator variables, which are typically correlated. For example, consider a *clicks per session* metric. The number of clicks and the number of sessions are two sets of observations coming from the same group of users, so they are not independent from each other. To properly account for this correlation, the variance of a ratio metric *R* is obtained using the delta method:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/stats-methods/delta-method/167956015-cc3f9fca-2c4d-410c-bff1-3f13dd16d105.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=e5a2f29951e5105690521fac7d18ae55" alt="Delta method variance formula" width="694" height="76" data-path="images/snippets/stats-methods/delta-method/167956015-cc3f9fca-2c4d-410c-bff1-3f13dd16d105.png" />
</Frame>

where the variance of the numerator and denominator means are computed in the same way as detailed above for count metrics, and the covariance is

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/stats-methods/delta-method/167956127-c17017ef-07b2-4f76-88c4-00539eec50a7.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=a45c59e3655e874db6112b4a46ee9735" alt="Covariance calculation formula" width="584" height="69" data-path="images/snippets/stats-methods/delta-method/167956127-c17017ef-07b2-4f76-88c4-00539eec50a7.png" />
</Frame>

## Delta Method for Relative Lifts

Statsig may also use the delta method when calculating the confidence interval for relative lifts. The other methodology for calculating confidence intervals for relative lifts is [Fieller Intervals](/experiments/statistical-methods/methodologies/fieller-intervals) - the delta method is a heuristic for Fieller Intervals which converges with a large population.


Built with [Mintlify](https://mintlify.com).
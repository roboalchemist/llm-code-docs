# Source: https://docs.statsig.com/statsig-warehouse-native/features/statistics/methodologies/benjamini-hochberg-procedure.md

# Source: https://docs.statsig.com/experiments/statistical-methods/methodologies/benjamini-hochberg-procedure.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Benjamini–Hochberg Procedure

## What it is

The Benjamini-Hochberg Procedure ("BH" procedure) is a statistical method that reduces the probability of false positives by adjusting the significance level for multiple comparisons. It is not as extreme as a [Bonferroni Correction](/stats-engine/methodologies/bonferroni-correction), because instead of controlling the chance of at least one false positive (Family Wise Error Rate), BH controls the expected value of false positives when the null hypothesis has been rejected (False Discovery Rate).

Like with many other analysis settings, you can enable BH procedure for individual experiments (or configure global Experiment Settings to default it).

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/nWWZ8OL8Q-oTLDq_/images/snippets/stats-methods/benjamini-hochberg-procedure/c865494e-0ae4-489c-a416-45848b4d10bc.png?fit=max&auto=format&n=nWWZ8OL8Q-oTLDq_&q=85&s=125e53ad165a91e7e8c86672324ef919" alt="Benjamini-Hochberg procedure configuration interface" width="1090" height="651" data-path="images/snippets/stats-methods/benjamini-hochberg-procedure/c865494e-0ae4-489c-a416-45848b4d10bc.png" />
</Frame>

## Methodology

The [Benjamini-Hochberg Procedure](https://www.statisticshowto.com/benjamini-hochberg-procedure/) updates the significance level to be used (modifying your pre-set $\alpha$). The new significance level to be applied is calculated by sorting the p-values of metrics in ascending order and comparing with a paired threshold. Each p-value’s paired threshold is the desired False Discovery Rate divided by the number of comparisons being evaluated multiplied by what rank a p-value is in the ordered list. The largest threshold value which is higher than its corresponding p-value is our new significance level ($\alpha$).

The Benjamini-Hochberg Procedure can be applied based on:

* The number of test groups (multiple treatment hypotheses). For each metric aggregate the list of p-values from each variant and complete the Benjamini-Hochberg procedure.
* The number of metrics in the scorecard. For each variant aggregate the list of p-values from each metric and complete the Benjamini-Hochberg procedure.
* Both the number of test groups and number of metrics in the scorecard. All p-values are aggregated to complete the Benjamini-Hochberg procedure.

Statsig does not apply BH procedure when evaluating the p-values of any event-dimension or user-property experiment metric results. Only the top-line metric results are compared to the new significance level.

## How do my experiment metrics look now?

In the experiment scorecard section, confidence intervals will be derived from (1 - adjusted α) for applicable metrics. If you hover over a confidence interval, the adjusted α will be displayed alongside other relevant metric details.

In the experiment explore section, if applicable to the selections you make, a new adjusted α will be calculated and these confidence intervals will use (1 - adjusted α).


Built with [Mintlify](https://mintlify.com).
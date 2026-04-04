# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/rank-your-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Finding the best run

> Learn how to use Automatic Run Ranking to find the best run

When building and evaluating an application, you are going to want to test many different combinations of
parameters - e.g. different prompt templates, models or agent configurations. You're also
likely to look at a combination of metrics: basic system metrics such as cost and latency, Galileo Guardrail
Metrics such as Context Adherence or Completeness, and potentially some of your own custom metrics.

Finding the best run when combing through a large number of runs each containing a lot of different metrics
can be like finding a needle in a haystack. To help you automate this process we built *Automatic Run Ranking*.

<img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/crown-logic-runs-table.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=17dcf18480eac6364481ed02db97d3c3" data-og-width="3004" width="3004" data-og-height="790" height="790" data-path="images/crown-logic-runs-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/crown-logic-runs-table.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=6a167a9f639cc79262e26e0a49d9ee7b 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/crown-logic-runs-table.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=ae296dce5796230e799e0ebcdf6621bf 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/crown-logic-runs-table.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=63e14db2bd89ff52b53cedc51ec93704 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/crown-logic-runs-table.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=fbba686a5cb471b107a62f3a5d55b740 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/crown-logic-runs-table.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=bfae990567f934d7c99dc17f00465ff6 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/crown-logic-runs-table.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=fbe0dbcde934bd76efcb053b69f87b26 2500w" />

### Configuring your Criteria

To configure your Run Ranking, click on **Ranking Criteria** on the top right of your Evaluate project. Set weights
for each of the metrics that were computed for your project, the weights you set will be used in the ranking formula.

Weights are between 0 and 1, give high weights to metrics you want to prioritize highly, low weights to metrics that
you want to have some impact on the rank, and 0 for those that should not be taken into account for your ranking.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-criteria-settings.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=0167991e9b96f4be1a32ac2d19c42b5e" width="300" data-og-width="736" data-og-height="1650" data-path="images/rank-criteria-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-criteria-settings.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=49dc782872a96691943718185e166fb9 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-criteria-settings.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=4fc061b26f30a65d4837d8b45f54ca94 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-criteria-settings.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=cc09c357c2291ac881c0599de13d6ba4 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-criteria-settings.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=b1a7aa2d7fa40fe9f43f5b8a153406c3 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-criteria-settings.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=d4bdd3b721f6c673d34979b6b400ef96 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-criteria-settings.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=72f7bd4ad3e78f18a995b63272be3285 2500w" />
</Frame>

### Ranking Formula

Behind the scenes, the ranking is calculated by taking the sum of every metric normalized between 0 and 1 multiplied by its weight, and dividing
by the sum of all weights:

<Frame>
  $\frac{\sum\limits_{metric \in \text{metrics}} (\text{weight(metric)} \times normalized(metric))}{\sum\limits_{weight \in \text{weights}} weights}$
</Frame>

<Note>Only numerical custom metrics can be used with this feature. Higher numerical values will be treated as positive scores (i.e. good), low values as negative scores (bad).</Note>

### Using the Results

The "Rank" column on your table will show you the ranking order of all your runs. You can sort by Rank, or hover over the rank number to
see the value of the ranking formula.

<Frame>
  <img src="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-tooltip.png?fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ec42775b013127f24ccdd95c86b4f977" width="400" data-og-width="976" data-og-height="638" data-path="images/rank-tooltip.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-tooltip.png?w=280&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=ea1c179e5d7b15e8930405c9b94ca500 280w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-tooltip.png?w=560&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=f2436778391606302fb9186a0155bee9 560w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-tooltip.png?w=840&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=a575b7c6396b16364a5eb101d608fdbc 840w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-tooltip.png?w=1100&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=2f4caf5e16f62b64d554a26150ddfe0c 1100w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-tooltip.png?w=1650&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=8bee19e161a31d0306b9f4ea69ff2869 1650w, https://mintcdn.com/galileo/PnVQRYgzV1f_rIIL/images/rank-tooltip.png?w=2500&fit=max&auto=format&n=PnVQRYgzV1f_rIIL&q=85&s=06210bf60226269e925473b1c47457cf 2500w" />
</Frame>

The winning run will be automatically be crowned. This run performed best according to your ranking criteria, the configuration you used for it is the best configuration you've tried.

# Source: https://docs.galileo.ai/galileo/gen-ai-studio-products/galileo-evaluate/how-to/rank-your-runs.md

# Finding the best run

> Learn how to use Automatic Run Ranking to find the best run

When building and evaluating an application, you are going to want to test many different combinations of
parameters - e.g. different prompt templates, models or agent configurations. You're also
likely to look at a combination of metrics: basic system metrics such as cost and latency, Galileo Guardrail
Metrics such as Context Adherence or Completeness, and potentially some of your own custom metrics.

Finding the best run when combing through a large number of runs each containing a lot of different metrics
can be like finding a needle in a haystack. To help you automate this process we built *Automatic Run Ranking*.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/crown-logic-runs-table.png" />

### Configuring your Criteria

To configure your Run Ranking, click on **Ranking Criteria** on the top right of your Evaluate project. Set weights
for each of the metrics that were computed for your project, the weights you set will be used in the ranking formula.

Weights are between 0 and 1, give high weights to metrics you want to prioritize highly, low weights to metrics that
you want to have some impact on the rank, and 0 for those that should not be taken into account for your ranking.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/rank-criteria-settings.png" width="300" />
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
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/rank-tooltip.png" width="400" />
</Frame>

The winning run will be automatically be crowned. This run performed best according to your ranking criteria, the configuration you used for it is the best configuration you've tried.

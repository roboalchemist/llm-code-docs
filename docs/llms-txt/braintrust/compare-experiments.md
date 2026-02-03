# Source: https://braintrust.dev/docs/evaluate/compare-experiments.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Compare experiments

> Identify improvements and regressions across evaluation runs

Comparing experiments helps you understand which changes improve performance and which cause regressions. Braintrust automatically highlights differences and makes it easy to drill into specific test cases.

## Automatic comparison

When you run multiple experiments on the same dataset, Braintrust automatically compares them. The UI shows:

* Score differences for each test case
* Improvements highlighted in green
* Regressions highlighted in red
* Percentage changes in summary metrics

Enable diff mode with the toggle to focus on changes.

## Compare in the UI

### Select baseline

Choose which experiment to use as the baseline for comparison. The current experiment's scores will be compared against the baseline.

### Sort by changes

Sort the table by improvements or regressions to quickly identify which test cases changed the most:

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/sort-by-comparison-poster.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/sort-by-comparison.mov?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=9cc8744675ef3631185bee2cd49d7400" type="video/mp4" data-path="images/core/experiments/sort-by-comparison.mov" />
</video>

### View side-by-side diffs

Select any row to see detailed diffs for each field:

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/diff-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/diff.mov?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=74ffaa4441e76afc7184f83e985fee57" type="video/mp4" data-path="images/core/experiments/diff.mov" />
</video>

The diff view shows:

* Input (should be identical)
* Output differences highlighted
* Score changes with delta values
* Metadata and timing comparisons

## Compare multiple experiments

Add multiple experiments as comparisons to see how changes evolve over time:

1. Select an experiment
2. Click **Add comparison**
3. Choose additional experiments
4. View all in grid or summary layout

### Grid layout

See outputs side-by-side in a table. Select which fields to display from the **Fields** dropdown. This is perfect for spot-checking specific test cases across experiments.

### Summary layout

View aggregate metrics across all experiments in a reporting-friendly format. Both layouts respect filters and groupings.

## Match test cases

Braintrust matches test cases across experiments using the `input` field by default. Test cases with identical inputs are considered the same example.

### Custom comparison keys

If your `input` includes additional data, configure a custom comparison key:

1. Go to project **Configuration**
2. Define a SQL expression for matching
3. Save the comparison key

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=395cdce8f0459bbbd4ac591d9d8e0650" alt="Create comparison key" data-og-width="1552" width="1552" data-og-height="282" height="282" data-path="images/guides/projects/comparison-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=f2a0d804e9bf494fd2e3e51846fab6e3 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=3fc8632c4a7bb7df4ff10dc664c74409 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=77c6e881a1c686ed1c28df376b5d87ea 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=eba38a4ed439e35a85d70c894c5639b9 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=4726778c4a41ad4e0553b17de24af3e5 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=88204b9577364076cd496d701868e626 2500w" />

For example, use `input.user_query` instead of the entire `input` object if other fields vary.

## Compare trials

When you run multiple trials (repeated evaluations of the same input), group by input to see aggregate results:

1. Select **Input** from the **Group** dropdown
2. View average scores across trials
3. Identify variance and reliability issues

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/trials-comparison-poster.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trials-comparison.mp4?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=474c1825d5d19c1bf35d873b59299f97" type="video/mp4" data-path="images/core/experiments/trials-comparison.mp4" />
</video>

## Compare programmatically

Access comparison data through the SDK:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { init } from "braintrust";

  const experiment = init("My Project", {
    experiment: "new-experiment",
    baseExperiment: "baseline-experiment",
  });

  // Run your evaluation
  const summary = await experiment.summarize();

  console.log("Improvements:", summary.improvements);
  console.log("Regressions:", summary.regressions);
  console.log("Score delta:", summary.scoreDelta);
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  from braintrust import init

  experiment = init(
      project="My Project",
      experiment="new-experiment",
      base_experiment="baseline-experiment",
  )

  # Run your evaluation
  summary = experiment.summarize()

  print("Improvements:", summary.improvements)
  print("Regressions:", summary.regressions)
  print("Score delta:", summary.score_delta)
  ```
</CodeGroup>

## Analyze differences

When comparing experiments, look for:

### Consistent improvements

Test cases that improve across all scorers indicate a genuine enhancement. These are your wins.

### Consistent regressions

Test cases that regress across scorers indicate a problem. Investigate and fix before deploying.

### Mixed results

Cases that improve on some scorers but regress on others require careful analysis. You may need to adjust scorer weights or accept trade-offs.

### Edge case changes

Look for patterns in which types of inputs improved or regressed. Group by metadata to identify systematic issues.

## Use comparison in CI/CD

Set score thresholds in CI to automatically catch regressions:

```yaml  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
- name: Run Evals
  uses: braintrustdata/eval-action@v1
  with:
    api_key: ${{ secrets.BRAINTRUST_API_KEY }}
    runtime: node
    fail_on_regression: true
    min_score: 0.7
```

The action will fail the build if scores drop below thresholds or show significant regressions.

## Next steps

* [Interpret results](/evaluate/interpret-results) in detail
* [Use playgrounds](/evaluate/playgrounds) for rapid iteration
* [Write scorers](/evaluate/write-scorers) to measure what matters
* [Run evaluations](/evaluate/run-evaluations) in CI/CD

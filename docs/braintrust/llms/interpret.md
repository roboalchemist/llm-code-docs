# Source: https://braintrust.dev/docs/core/experiments/interpret.md

# Interpret evals

Running an eval from the API or SDK will return a link to the corresponding experiment in Braintrust's UI. When you open the link, you'll land on a detailed view of the eval run that you selected. The detailed view includes:

* **Diff mode toggle** - Allows you to compare eval runs to each other. If you select the toggle, you will see the results of your current eval compared to the results of the baseline.
* **Filter bar** - Allows you to focus in on a subset of test cases. You can filter by typing natural language or [BTQL](https://www.braintrust.dev/docs/reference/btql).
* **Column visibility** - Allows you to toggle column visibility. You can also order columns by regressions to hone in on problematic areas.
* **Table** - Shows the data for every test case in your eval run.

<img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-run.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=ce6ce5916ba938ea92e1624f063c151d" alt="One eval run" data-og-width="2162" width="2162" data-og-height="1498" height="1498" data-path="images/core/experiments/eval-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-run.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=44a2c50aabda3936c25cc169fd60e80f 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-run.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=8fb625d9b0457ff7caedc46a88263f3d 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-run.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=aed86cc792fdd26b4312727e900093d2 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-run.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=f1a47c882c89b8d2447b39110ff3465a 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-run.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=5369df837f1b6d0fa6884b826845841b 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/eval-run.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=8387f531c8d13a8dc1965f0a1cca234b 2500w" />

### Experiment summaries

When you select an experiment, you'll get a summary of the comparisons, scorers, datasets, and metadata.
<img src="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-summary.png?fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=4be8b9c556118d5fc0f3c9472d0c6628" alt="Experiment summary" data-og-width="2162" width="2162" data-og-height="1498" height="1498" data-path="core/experiments/experiment-summary.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-summary.png?w=280&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=d80efa085c157c9777263e1a6392c293 280w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-summary.png?w=560&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=067b08834dd2dfbdae75660fc0a8db9b 560w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-summary.png?w=840&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=e15f688a258f2837c7e7348b196ffc07 840w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-summary.png?w=1100&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=cd8f731ce5240abad4439ed91d591df4 1100w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-summary.png?w=1650&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=86efca71b4e8dcd9ef148072b810db7f 1650w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-summary.png?w=2500&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=8fd985ca4247991c87af6a4e57d446d2 2500w" />

You can also view and copy the experiment ID from the bottom of the summary pane.
<img src="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-id.png?fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=c702e7ea330e8588f8949b9bd9fb9afc" alt="Experiment ID" data-og-width="2162" width="2162" data-og-height="1498" height="1498" data-path="core/experiments/experiment-id.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-id.png?w=280&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=15d809ce137054862992762f3abb4e1a 280w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-id.png?w=560&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=2ae2e93ff3f9a1ba5cbe7c1ea1e752ae 560w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-id.png?w=840&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=6342fcb0e9b38f9a81a34419a33e823c 840w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-id.png?w=1100&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=17cad3b5029205f9c5553a6767726a9c 1100w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-id.png?w=1650&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=ab492a3053c341a5f474e58af9087996 1650w, https://mintcdn.com/braintrust/WfF7RkpYE_1CNyf3/core/experiments/experiment-id.png?w=2500&fit=max&auto=format&n=WfF7RkpYE_1CNyf3&q=85&s=332c8ae1141af9c407455fa8a638d6fd 2500w" />

### Table header summaries

Summaries will appear for score and metric columns. To find test cases to focus on, use column header summaries to filter by improvements or regressions (test cases that decreased in score). This allows you to see the scorers with the biggest issues. You can also group the table to view summaries across metadata fields or inputs. For example, if you use separate datasets for distinct types of usecases, you can group by dataset to see which usecases are having the biggest issues.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/column-grouping-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/column-grouping.gif?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=d509d82bfe255ccf825327fd01a789e7" type="video/mp4" data-path="images/core/experiments/column-grouping.gif" />
</video>

## Group summaries

By default, group rows will show one experiment's summary data, and you can switch between them by selecting your desired aggregation.

<img src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/summary-experiment-aggregation.png?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=246b3dfdbb1bc3cc9977d03130d926ff" alt="Summary experiment aggregations" data-og-width="2372" width="2372" data-og-height="1516" height="1516" data-path="images/core/experiments/summary-experiment-aggregation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/summary-experiment-aggregation.png?w=280&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=18796d6513b329bdf05fd861dcd15cbc 280w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/summary-experiment-aggregation.png?w=560&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=f1b2309e61a6830337c4b3e8190aaff6 560w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/summary-experiment-aggregation.png?w=840&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=09ae974d373452b2ac21a2437454ffe7 840w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/summary-experiment-aggregation.png?w=1100&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=5bdba6df88c8fc07a5b1a19afcc4fe04 1100w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/summary-experiment-aggregation.png?w=1650&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=cf849aeab86f777d51bb37b433b73aea 1650w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/summary-experiment-aggregation.png?w=2500&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=ada8cb28c8638cc3c1952d8496ffea65 2500w" />

If you would like to view the summary data for all experiments, select **Include comparisons in group**.

<img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/include-comparisons-group.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=d14409d847406a6e648e2e8d320893ea" alt="Include comparisons in group" data-og-width="2372" width="2372" data-og-height="1516" height="1516" data-path="images/core/experiments/include-comparisons-group.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/include-comparisons-group.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=8eb186f5de99531efb3f10c5e9ae41f7 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/include-comparisons-group.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=bd29d7e09d05bbf65417d2dfe97d3e29 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/include-comparisons-group.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=8dd2bc527599c2f25f4961f9560e3888 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/include-comparisons-group.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=80e31223d77dd18aa62a061e24b38906 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/include-comparisons-group.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=ebb16b417c6738d9cbf772ec1fc4d433 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/include-comparisons-group.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=bb16f620c4b1bb2c70472dac78a76015 2500w" />

Within a grouped table, you can also sort rows by regressions of a specific score relative to a comparison experiment.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/sort-by-regression-poster.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/sort-by-regression.gif?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=004826e040294a6482cae5e52fe9d8f7" type="video/mp4" data-path="images/core/experiments/sort-by-regression.gif" />
</video>

Now that you've narrowed your test cases, you can view a test case in detail by selecting a row.

### Trace view

Selecting a row will open the trace view. Here you can see all of the data for the trace for this test case, including input, output, metadata, and metrics for each span inside the trace.

Look at the scores and the output and decide whether the scores seem "right". Do good scores correspond to a good output? If not, you'll want to improve your evals by updating [scorers](/core/experiments/write#scorers) or [test cases](https://www.braintrust.dev/blog/eval-feedback-loops).

<img src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=533697a2e36b8aa1e54cefa4e152b432" alt="Trace view" data-og-width="2372" width="2372" data-og-height="1516" height="1516" data-path="images/core/experiments/trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=280&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=e9a2a837755dda8f762a11e85f0ea67d 280w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=560&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=cf7592a569f31dcef51baeb71ce4bf70 560w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=840&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=6b2cff2f3b365e8369a93a18eb7ad12c 840w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=1100&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=79af603c7015a4f7fd48661d080daf91 1100w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=1650&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=c751837ad787d8b7b7ff0cc8c0602a94 1650w, https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trace.png?w=2500&fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=64b969d78c6a090c1264c1c2d2c2099a 2500w" />

### Create custom columns

You can create custom columns to extract values from the root span.
To do this, use the **Add custom column** option at the bottom of the **Columns** dropdown or select the **+** icon at the end of the table headers.

<img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=9d1e23a6419c38c10244d0a24bf58beb" alt="Create column action" data-og-width="2372" width="2372" data-og-height="1516" height="1516" data-path="images/core/experiments/create-column.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=ec2dd3895ff134d517f4bba629a9a17c 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=7f94fb086678b0328c8e9065af2c6d1a 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=ea5192d04a6dd8c643dfaec515f62cc6 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=c03aea5dc7de9c5863e9b2e897a64f03 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=9314236b4e94a266269e0e45da0b49f5 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=601068ead1cd289a9c2278d299f3b205 2500w" />

After naming your custom column, you can either choose from the inferred fields in the dropdown or enter a custom [BTQL](https://www.braintrust.dev/docs/reference/btql) statement.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/create-column-dialog-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/create-column-dialog.mp4?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=2b3f0a5192b81954f205f7caf295c3a0" type="video/mp4" data-path="images/core/experiments/create-column-dialog.mp4" />
</video>

Once created, you can filter and sort the table using your custom columns.

## Score experiments

You can manually apply scorers to test cases in your experiments. When applied, scores show up as additional spans within the trace for a test case. There are two ways to manually score test cases.

* **Multiple test cases**: Select the rows of an experiment you'd like to score, then select <Icon icon="percent" /> **Score** to apply the chosen scorers.
* **Single test case**: Select any row of an experiment and use the <Icon icon="percent" /> **Score** button in the trace view to apply scorers to that specific test case.

## Interpret results

### How metrics are calculated

Along with the scores you track, Braintrust tracks a number of metrics about your LLM calls that help you assess and understand performance. For example, if you're trying to figure out why the average duration increased substantially when you change a model,
it's useful to look at both duration and token metrics to diagnose the underlying issue.

Wherever possible, metrics are computed on the `task` subspan, so that LLM-as-a-judge calls are excluded. Specifically:

* `Duration` is the duration of the `"task"` span.
* `Offset` is the time elapsed since the trace start time.
* `Prompt tokens`, `Completion tokens`, `Total tokens`, `LLM duration`, and `Estimated LLM cost` are averaged over every span
  that is not marked with `span_attributes.purpose = "scorer"`, which is set automatically in autoevals.

If you are using the logging SDK, or API, you will need to follow these conventions to ensure that metrics are computed correctly.

<Note>
  To compute LLM metrics (like token counts), make sure you [wrap your LLM calls](/guides/traces/customize#wrapping-llm-clients).
</Note>

### Diff mode

When you run multiple experiments, Braintrust will automatically compare the results of experiments to each other. This allows you to
quickly see which test cases improved or regressed across experiments.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/sort-by-comparison-poster.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/sort-by-comparison.mov?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=9cc8744675ef3631185bee2cd49d7400" type="video/mp4" data-path="images/core/experiments/sort-by-comparison.mov" />
</video>

You can also select any individual row in an experiment to see diffs for each field in a span.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/diff-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/diff.mov?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=74ffaa4441e76afc7184f83e985fee57" type="video/mp4" data-path="images/core/experiments/diff.mov" />
</video>

#### How rows are matched

By default, Braintrust considers two test cases to be the same if they have the same `input` field. This is used both to match test cases across experiments
and to bucket equivalent cases together in a [trial](./write#trials).

### View data across trials

To group by [trials](./write#trials), or multiple rows with the same `input` value, select **Input** from the **Group** dropdown menu.
This will consolidate each trial for a given input and display aggregate data, showing comparisons for each unique input across all experiments.

If Braintrust detects that any rows have the same `input` value within the same experiment, diff mode will show a **Trials** column where you can select matching trials in your comparison experiments.
You can also step through the relevant trial rows in your comparison experiment by selecting a specific trace.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/trials-comparison-poster.png">
  <source src="https://mintcdn.com/braintrust/FJKP8dcMkQrpeBHe/images/core/experiments/trials-comparison.mp4?fit=max&auto=format&n=FJKP8dcMkQrpeBHe&q=85&s=474c1825d5d19c1bf35d873b59299f97" type="video/mp4" data-path="images/core/experiments/trials-comparison.mp4" />
</video>

### Customize the comparison key

However, sometimes your `input` may include additional data, and you need to use a different
expression to match test cases. You can configure the comparison key in your project's **Configuration** page.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=395cdce8f0459bbbd4ac591d9d8e0650" alt="Create comparison key" data-og-width="1552" width="1552" data-og-height="282" height="282" data-path="images/guides/projects/comparison-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=f2a0d804e9bf494fd2e3e51846fab6e3 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=3fc8632c4a7bb7df4ff10dc664c74409 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=77c6e881a1c686ed1c28df376b5d87ea 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=eba38a4ed439e35a85d70c894c5639b9 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=4726778c4a41ad4e0553b17de24af3e5 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=88204b9577364076cd496d701868e626 2500w" />

### Experiment view layouts

#### Grid layout

When you run multiple experiments, you can also compare experiment outputs side-by-side in the table by selecting the **Grid layout**. In the grid layout, select which fields to display in cells by selecting from the **Fields** dropdown menu.

#### Summary layout

The **Summary layout** summarizes scores and metrics across the base experiment and all comparison experiments, in a reporting-friendly format with large type. Both summary and grid layouts respect all view filters.

### Aggregate (weighted) scores

It's often useful to compute many, even hundreds, of scores in your experiments, but when reporting on an experiment, or comparing
experiments over time, it's often useful to have a single score that represents the experiment as a whole.

Braintrust allows you to do this with aggregate scores, which are formulas that combine multiple scores. To create an aggregate score, go to your project's **Configuration** page,
and select **Add aggregate score**.

<img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=04e0cfcc3540ccd8f96c75b0f6d3c59d" alt="Add aggregate score" data-og-width="1136" width="1136" data-og-height="1012" height="1012" data-path="images/core/experiments/add-aggregate-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=5dd7274a5f0929f25b89d3eb61c45d5f 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=411833a6bf9b3280a3cbdcbe0c4c8042 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=bb763140b615fd285dbcf0b3ac59f9bc 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=95ad65a931300136b5cee76f008fac00 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=f7a65f4528a6a037174a804b67304294 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=003b53a2981c4aaa86d64dd2fba7a632 2500w" />

Braintrust currently supports three types of aggregate scores:

* **Weighted average** - A weighted average of selected scores.
* **Minimum** - The minimum value among the selected scores.
* **Maximum** - The maximum value among the selected scores.

## Analyze across experiments

Braintrust allows you to analyze data across experiments to, for example, compare the performance of different models.

### Bar chart

On the Experiments page, you can view your scores as a bar chart by selecting **Score comparison** from the X axis selector:

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/bar-score-comparison-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/bar-score-comparison.mp4?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=b25cb61270d179bd0a54ff73a1039167" type="video/mp4" data-path="images/core/experiments/bar-score-comparison.mp4" />
</video>

You can also select the metadata fields you want to group by to create bar charts:

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/group-by-dataset-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/group-by-dataset.mov?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=31e804217b233da7a4ad8e91de1839b7" type="video/mp4" data-path="images/core/experiments/group-by-dataset.mov" />
</video>

### Scatter plot

Select a metric on the x-axis to construct a scatter plot. Here's an example comparing the relationship between accuracy and duration.

<video className="border rounded-md" loop autoPlay muted poster="/images/core/experiments/scatterplot-poster.png">
  <source src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/scatterplot.gif?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=88b9ccd8f7e748c2d70e61e9cb0d047a" type="video/mp4" data-path="images/core/experiments/scatterplot.gif" />
</video>

## Export experiments

### UI

To export an experiment's results, open the menu next to the experiment name. You can export as `CSV` or `JSON`, and choose if you'd like to download all fields.

<img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=c9d392fe5158555fa7547107c478ee4e" alt="Export experiments" data-og-width="2198" width="2198" data-og-height="1496" height="1496" data-path="images/core/experiments/exporting-experiments.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=eeb59d6a70a7b33e6661e46120719c56 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=fa9380daa3d79bad13d74ba638f585bc 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=db8ab9c4f1464a59d7f37b91ba85ed77 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=cb2f3c5a357b0d4eb444eef87b82888d 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=c7d91686711eeff3b2f30bcd494d5bfb 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/exporting-experiments.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=038b655e9fdc2682ec9d60d05bd73bb7 2500w" />

### API

To fetch the events in an experiment via the API, see [Fetch experiment (POST form)](https://www.braintrust.dev/docs/api-reference#fetch-experiment-post-form) or [Fetch experiment (GET form)](https://www.braintrust.dev/docs/api-reference#fetch-experiment-get-form).

### SDK

If you need to access the data from a previous experiment, you can pass the `open` flag into
`init()` and then just iterate through the experiment object:

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { init } from "braintrust";

  async function openExperiment() {
    const experiment = init(
      "Say Hi Bot", // Replace with your project name
      {
        experiment: "my-experiment", // Replace with your experiment name
        open: true,
      },
    );
    for await (const testCase of experiment) {
      console.log(testCase);
    }
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import braintrust

  def open_experiment():
      experiment = braintrust.init(
          project="Say Hi Bot",  # Replace with your project name
          experiment="my-experiment",  # Replace with your experiment name
          open=True,
      )
      for test in experiment:
          print(test_case)
  ```
</CodeGroup>

You can use the the `asDataset()`/`as_dataset()` function to automatically convert the experiment into the same
fields you'd use in a dataset (`input`, `expected`, and `metadata`).

<CodeGroup dropdown>
  ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import { init } from "braintrust";

  async function openExperiment() {
    const experiment = init(
      "Say Hi Bot", // Replace with your project name
      {
        experiment: "my-experiment", // Replace with your experiment name
        open: true,
      },
    );

    for await (const testCase of experiment.asDataset()) {
      console.log(testCase);
    }
  }
  ```

  ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  import braintrust

  def open_experiment():
      experiment = braintrust.init(
          project="Say Hi Bot",  # Replace with your project name
          experiment="my-experiment",  # Replace with your experiment name
          open=True,
      )
      for test in experiment.as_dataset():
          print(test_case)
  ```
</CodeGroup>

For a more advanced overview of how to reuse experiments as datasets, see [Hill climbing](/core/experiments/write#hill-climbing).


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
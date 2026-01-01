# Source: https://braintrust.dev/docs/core/logs/score.md

# Score logs

Scoring logs in Braintrust allows you to evaluate the quality of your AI application's performance in real-time through online evaluations. Unlike experiments that evaluate pre-defined datasets, online scoring automatically runs evaluations on your production logs as they are generated, providing continuous monitoring and quality assurance.

To score historical logs manually rather than automatically in real-time as they are generated, see [manual scoring](#manual-scoring).

## What is online scoring?

Online scoring, also known as online evaluations, runs evaluations on traces as they are logged in production. This enables you to:

* **Monitor quality continuously** without manually running evaluations
* **Catch regressions** in production performance immediately
* **Evaluate at scale** across all your production traffic
* **Get insights** into real user interactions and edge cases

Online scoring runs asynchronously in the background, so it doesn't impact your application's latency or performance.

## Set up online scoring

Online scoring is configured at the project level through the **Configuration** page. You can set up multiple scoring rules with different sampling rates and filters.

### Create online scoring rules

Navigate to **Configuration > <Icon icon="radio" /> Online scoring > + Create rule**.

<img src="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/configure-score.png?fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=567388ff52548416505a46592ccb6370" alt="Configure score" data-og-width="1204" width="1204" data-og-height="1576" height="1576" data-path="images/cookbook/assets/Realtime/configure-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/configure-score.png?w=280&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=6b1e72318bc134a57535e84dcdd24d14 280w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/configure-score.png?w=560&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=bac8c2ef902b6ad089ab1e7b996ba899 560w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/configure-score.png?w=840&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=68d1fd32301b8960b8021c6bf0ae3f35 840w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/configure-score.png?w=1100&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=f938538100f4a1488142cb61aee4a640 1100w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/configure-score.png?w=1650&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=74791c8bd8ec593c914abf7ce8947704 1650w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/configure-score.png?w=2500&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=bade918c0eb03951c076b54b6150cb61 2500w" />

### Configure online scoring rule parameters

For each online scoring rule, you can configure:

* **Rule name**: Unique identifier for the rule

* **Description**: Explanation of what the rule does and why it exists

* **Scorers**: Choose from [autoevals](https://github.com/braintrustdata/autoevals) or any custom scorers in the current project or in another project

* **Sampling rate**: Percentage of logs to evaluate (for example, 10% for high-volume applications)

* **BTQL filter clause**: Filter spans based on their data (input, output, metadata, etc.) using a [BTQL filter clause](https://www.braintrust.dev/docs/reference/btql#filter). Only spans where the BTQL filter clause evaluates to true are considered for scoring.

  <Note>
    The `!=` operator is not supported in this specific context (fails silently). Use `IS NOT` instead.
  </Note>

* **Apply to spans**: Among spans that pass the BTQL filter (if any), choose which span types to actually score:

  * Root spans toggle: Score root spans (top-level spans with no parent)
  * Span names field: Score spans with specific names (comma-separated list)

  If both options are enabled, spans matching either criterion are scored. If neither option is enabled, all spans that pass the BTQL filter are scored.

### Test online scoring rules

Preview how your online scoring rule will perform by selecting **Test rule** at the bottom of the configuration dialog. This allows you to see sample results before enabling the rule.

## Types of scorers for online evaluation

Online scoring supports the same types of scorers you can use in experiments. You can use pre-built scorers from the [autoevals](https://github.com/braintrustdata/autoevals) library or create custom code-based scorers written in TypeScript or Python that implement your specific evaluation logic. For more information on creating scorers, check out the [scorers guide](/core/functions/scorers).

## View online scoring results

### In logs view

Online scoring results appear automatically in your logs. Each scored span shows:

* **Score value**: The numerical result (0-1 or 0-100 depending on scorer)
* **Scoring span**: A child span containing the evaluation details
* **Scorer name**: Which scorer generated the result

<img src="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=9bd610b169cf14f2ab57775781c5a867" alt="Scoring span" data-og-width="2792" width="2792" data-og-height="2010" height="2010" data-path="images/cookbook/assets/Realtime/scoring-span.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=280&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=9b94ff81b8e3158f1b65bdf4ce798cf2 280w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=560&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=44b67a41c7e574f7121fc1d6b5458dcf 560w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=840&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=ca6890865cb8dfa3dbde9eff11d23342 840w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=1100&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=1f8edc00273dc234c01448bc197d89d6 1100w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=1650&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=af8236f4e8099817c0d4dd2e82c8db40 1650w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=2500&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=6479f417d4add98a28306e132ce09671 2500w" />

## Best practices for online scoring

Choose your sampling rate based on application volume and criticality. High-volume applications should use lower sampling rates (1-10%) to manage costs, while low-volume or critical applications can afford higher rates (50-100%) for comprehensive coverage. Since online scoring runs asynchronously, it won't impact your application's latency, though LLM-as-a-judge scorers can have higher latency and costs than code-based alternatives.

Online scoring works best as a complement to offline experimentation, helping you validate experiment results in production, monitor deployed changes for quality regressions, and identify new test cases from real user interactions.

## Troubleshooting common issues

### Low or inconsistent scores

* **Review scorer logic**: Ensure scoring criteria match expectations
* **Check input/output format**: Verify scorers receive expected data structure
* **Test with known examples**: Validate scorer behavior on controlled inputs
* **Refine evaluation prompts**: Make LLM-as-a-judge criteria more specific

### Missing scores

* **Check Apply to spans settings in online scoring rule**: Ensure the root spans toggle and/or span names field target the correct span types
* **Check BTQL filter clause in online scoring rule**: Confirm your logs' data (input, output, metadata) passes the BTQL filter clause. Also see [note about unsupported BTQL operators](#btql-operator-note)
* **Check sampling rate in online scoring rule**: Low sampling can result in sparse scoring
* **Check token permissions**: Ensure your API key or service token has access to scorer projects and has 'Read' and 'Update' permissions on the project and project logs
* **Check span data completeness at end time**:
  * Online scoring currently triggers when `span.end()` is called (or automatically when using `wrapTraced()` in TypeScript or `@traced` decorator in Python)
  * The online scoring rule's BTQL filter clause evaluates only the data present at the moment when `span.end()` is called
  * If a span is updated after calling `end()` (e.g., logging output after ending), the update won't be evaluated by the BTQL filter clause. For example, if your filter requires `output IS NOT NULL` but output is logged after `span.end()`, the span won't be scored

## Manual scoring

You can manually apply scorers to historical logs. When applied, scores show up as additional spans within the log's trace. There are three ways to manually score logs:

* **Specific logs**: Select the logs you'd like to score, then select <Icon icon="percent" /> **Score** to apply the chosen scorers
* **Individual logs**: Navigate into any individual log and use the <Icon icon="percent" /> **Score** button in the trace view to apply scorers to that specific log
* **Bulk filtered logs**: Use filters to narrow your view, then select **Score past logs** under <Icon icon="radio" /> **Online scoring** to apply scorers to the 50 most recent logs matching your filters

<img src="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=c555137224ceb2ca0927780735058e61" alt="Apply score" data-og-width="914" width="914" data-og-height="420" height="420" data-path="images/cookbook/assets/Realtime/apply-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=280&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=316f87000add2494449621b6c5ccbe0a 280w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=560&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=637ff88137d499c0c88e863dfb674863 560w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=840&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=4abb413f10d809a7fc01fe953e6d9334 840w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=1100&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=12f48b4d4ff7f739ec8f23977a6ee790 1100w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=1650&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=c6d9ca410e09cf70387df15726ce288c 1650w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=2500&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=b5a2216bcf6300e90b1afe9ec110a5d5 2500w" />


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
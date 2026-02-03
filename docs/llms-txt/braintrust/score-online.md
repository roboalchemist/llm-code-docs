# Source: https://braintrust.dev/docs/observe/score-online.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Score production traces

> Run evaluations automatically on production logs

Online scoring evaluates production traces automatically as they're logged, running evaluations asynchronously in the background to provide continuous quality monitoring without affecting your application's latency or performance.

This enables you to:

* Monitor quality continuously across all production traffic
* Catch regressions immediately when they occur
* Evaluate at scale without manual intervention
* Get insights into real user interactions and edge cases

## Create scoring rules

Online scoring rules are defined at the project level and specify which scorers to run, how often, and on which logs. Once configured, these rules automatically evaluate production traces as they arrive.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    In the Braintrust UI, create a scoring rule in project settings, when setting up a scorere, or when testing a scorer.

    * **Project settings**: Go to <Icon icon="settings-2" /> **Settings** > **Project** > <Icon icon="radio" /> **Online scoring** and click **Add rule**.

      See [Manage projects](/admin/projects#set-up-online-scoring) for more details.

    * **Scorer setup**: When creating or editing a scorer, click <Icon icon="radio" /> **Online scoring** and either select an existing scoring rule or create a new rule. This workflow allows you to configure both the scorer and its scoring rules together.

      See [Write scorers](/evaluate/write-scorers) for more details.

    * **Scorer testing**: When testing a scorer with logs in the <Icon icon="play" /> **Run** section, filter logs to find relevant examples, then click <Icon icon="radio" /> **Online scoring** to create a new online scoring rule with filters automatically prepopulated from your current log filters. This enables rapid iteration from logs to scoring rules.

      See [Test with logs](/evaluate/write-scorers#test-with-logs) for more details.

    <Tip>
      Select **Test rule** to preview how your rule will perform before enabling it.
    </Tip>
  </Tab>

  <Tab title="SDK" icon="terminal">
    Create scorers using the SDK, then configure online scoring rules in the UI:

    1. [Write and push your scorer](/evaluate/write-scorers#create-scorers) to Braintrust.
    2. In the UI, go to <Icon icon="settings-2" /> **Settings** > **Project** > <Icon icon="radio" /> **Online scoring**.
    3. Click **Add rule**, select your scorer, and configure when it runs.
  </Tab>
</Tabs>

## Rule parameters

Configure each rule with:

* **Rule name**: Unique identifier.

* **Description**: Explanation of the rule's purpose.

* **Project**: Select which project the rule belongs to. When creating from a scorer page, you can choose any project.

* **Scorers**: Choose from [autoevals](https://github.com/braintrustdata/autoevals) or custom scorers from the current project or any other project in your organization. When creating from a scorer page, the current scorer is automatically selected.

* **Sampling rate**: Percentage of logs to evaluate (e.g., 10% for high-volume apps).

* **SQL filter**: Filter spans based on input, output, metadata, etc. using a [SQL filter clause](/reference/sql#filter). Only spans matching the filter are scored. When creating from logs browser, filters are automatically prepopulated.

  <Note>
    The `!=` operator is not supported in SQL filters for online scoring. Use `IS NOT` instead.
  </Note>

* **Apply to spans**: Choose which span types to score:

  * Root spans (top-level spans with no parent)
  * Specific span names (comma-separated list)

  If both options are enabled, spans matching either criterion are scored. If neither is enabled, all spans passing the SQL filter are scored.

## View scoring results

Scores appear automatically in your logs. Each scored span shows:

* Score value (0-1 or 0-100 depending on scorer)
* Scoring span containing evaluation details
* Scorer name that generated the result

<img src="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=9bd610b169cf14f2ab57775781c5a867" alt="Scoring span" data-og-width="2792" width="2792" data-og-height="2010" height="2010" data-path="images/cookbook/assets/Realtime/scoring-span.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=280&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=9b94ff81b8e3158f1b65bdf4ce798cf2 280w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=560&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=44b67a41c7e574f7121fc1d6b5458dcf 560w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=840&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=ca6890865cb8dfa3dbde9eff11d23342 840w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=1100&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=1f8edc00273dc234c01448bc197d89d6 1100w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=1650&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=af8236f4e8099817c0d4dd2e82c8db40 1650w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/scoring-span.png?w=2500&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=6479f417d4add98a28306e132ce09671 2500w" />

## Score manually

Apply scorers to historical logs in three ways:

* **Specific logs**: Select logs and use <Icon icon="percent" /> **Score** to apply chosen scorers
* **Individual logs**: Open any log and use <Icon icon="percent" /> **Score** in the trace view
* **Bulk filtered logs**: Filter logs, then use **Score past logs** under <Icon icon="radio" /> **Online scoring** to score the 50 most recent matching logs

<img src="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=c555137224ceb2ca0927780735058e61" alt="Apply score" data-og-width="914" width="914" data-og-height="420" height="420" data-path="images/cookbook/assets/Realtime/apply-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=280&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=316f87000add2494449621b6c5ccbe0a 280w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=560&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=637ff88137d499c0c88e863dfb674863 560w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=840&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=4abb413f10d809a7fc01fe953e6d9334 840w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=1100&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=12f48b4d4ff7f739ec8f23977a6ee790 1100w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=1650&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=c6d9ca410e09cf70387df15726ce288c 1650w, https://mintcdn.com/braintrust/e0-dTi9KCLeMOpZ4/images/cookbook/assets/Realtime/apply-score.png?w=2500&fit=max&auto=format&n=e0-dTi9KCLeMOpZ4&q=85&s=b5a2216bcf6300e90b1afe9ec110a5d5 2500w" />

## Best practices

**Choose sampling rates wisely**: High-volume applications should use lower rates (1-10%) to manage costs. Low-volume or critical applications can use higher rates (50-100%) for comprehensive coverage.

**Complement offline evaluation**: Use online scoring to validate experiment results in production, monitor deployed changes, and identify new test cases from real interactions.

**Consider scorer costs**: LLM-as-a-judge scorers have higher latency and costs than code-based alternatives. Factor this into your sampling rate decisions.

## Troubleshoot issues

### Low or inconsistent scores

* Review scorer logic to ensure criteria match expectations.
* Verify scorers receive the expected data structure.
* Test scorer behavior on controlled inputs.
* Make LLM-as-a-judge criteria more specific.

### Missing scores

* Check **Apply to spans** settings to ensure correct span types are targeted (root spans or specific span names).
* Verify logs pass the SQL filter clause. Confirm your logs' data (input, output, metadata) matches the filter criteria.
* Confirm sampling rate isn't too low for your traffic volume.
* Ensure API key or service token has proper permissions (Read and Update on project and project logs). If using scorers from other projects, ensure permissions on those projects as well.
* Verify span data is complete when `span.end()` is called:
  * Online scoring triggers when `span.end()` is called (or automatically when using `wrapTraced()` in TypeScript or `@traced` decorator in Python)
  * The SQL filter clause evaluates only the data present at the moment `span.end()` is called
  * If a span is updated after calling `end()` (e.g., logging output after ending), the update won't be evaluated by the filter. For example, if your filter requires `output IS NOT NULL` but output is logged after `span.end()`, the span won't be scored

## Next steps

* [Create dashboards](/observe/dashboards) to monitor score trends
* [Build datasets](/annotate/datasets) from scored production traces
* [Run experiments](/evaluate/run-evaluations) to validate scoring criteria
* Learn about [creating scorers](/evaluate/write-scorers)

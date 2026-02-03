# Source: https://braintrust.dev/docs/observe/loop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use Loop

> Ask questions and get AI-powered insights about your logs

<Icon icon="blend" /> **Loop** is Braintrust's AI assistant that helps you query, analyze, and understand your production logs through natural language. Use Loop to search logs semantically, generate filters, identify patterns, extract insights, and analyze individual traces without writing queries.

## Open Loop

Select <Icon icon="blend" /> **Loop** in the bottom right corner of the <Icon icon="activity" /> **Logs** page to open the chat window. Loop keeps track of your queries in a queue, so you can ask multiple follow-ups while it's running. Use the Enter key to interrupt the current operation and execute the next query in the queue.

Loop is also available when [viewing individual traces](/observe/view-logs#view-a-specific-trace). Select a trace from the logs table and open it in fullscreen or in a separate page, then select <Icon icon="blend" /> **Loop** in the bottom right corner.

Loop maintains conversation history, letting you edit and re-run earlier messages and make inline model adjustments.

## Configure Loop

### Select a model

Change the AI model in the dropdown at the bottom of the Loop chat window.

Supported models:

* `claude-4.5-sonnet` (recommended)
* `claude-4.5-haiku`
* `claude-4.5-opus`
* `claude-4-sonnet`
* `claude-4.1-opus`
* `gpt-5.1`
* `gpt-5.2`

<Note>
  Only models from organization-level AI providers are available to Loop. Administrators can [configure AI providers at the organization level](/admin/organizations#configure-ai-providers) and [select which models are available to Loop](/admin/organizations#select-models-for-loop).
</Note>

### Toggle auto-accept

By default, Loop asks for confirmation before executing certain actions. To enable auto-accept, select <Icon icon="settings-2" /> settings in your Loop chat window and select **Auto-accept edits**.

### Select data sources

Loop can access different parts of your project. Select <Icon icon="file-plus-2" /> add context and search for the data sources you want Loop to query, such as specific datasets or experiments.

## Analyze logs

Select <Icon icon="blend" /> **Loop** in the bottom right corner of the <Icon icon="activity" /> **Logs** page to open the chat window. Use Loop to analyze patterns across all your logs, generate SQL filters from natural language, find similar traces semantically, create datasets from log patterns, and generate scorers based on identified issues.

Example queries:

* "What are the most common errors?"
* "Show me traces where users were frustrated"
* "Find requests that took longer than 60 seconds"
* "Create a dataset from logs with errors"
* "What user retention trends do you see?"
* "Find common failure modes"
* "What patterns do you see in high-latency requests?"

## Generate filters

Use Loop to create [SQL queries](/observe/filter#write-sql-queries) from natural language descriptions:

1. Select <Icon icon="list-filter" /> **Filter** to open the filter editor.
2. Switch to **SQL** mode.
3. Select <Icon icon="blend" /> **Generate** and describe the filter you want.

Example queries:

* "Only LLM spans"
* "From user John Smith"
* "Logs from the last 5 days where factuality score is less than 0.5"
* "Traces that took longer than 60 seconds"

## Find similar traces

Select rows in the logs table and use <Icon icon="glasses" /> **Find similar traces**. Loop analyzes the selected traces to identify common traits and returns [semantically similar traces](/observe/deep-search).

This helps you:

* Discover patterns across different user interactions
* Find edge cases with similar characteristics
* Group related issues together
* Build datasets from similar examples

## Analyze individual traces

When [viewing a single trace](/observe/view-logs#view-a-specific-trace) in fullscreen or a separate page, select <Icon icon="blend" /> **Loop** to analyze that specific trace. Loop can summarize trace execution, identify errors and performance issues, search project logs for similar patterns, and generate custom visualizations.

<Accordion title="Understand trace execution">
  Ask Loop to summarize or explain what happened in a specific trace:

  Example queries:

  * "Summarize this trace"
  * "What are the errors that are happening in this trace?"
  * "What was the total latency and where was time spent?"
  * "Explain the tool calls that were made"
</Accordion>

<Accordion title="Find patterns across logs">
  Loop on trace pages can search your project logs to find similar patterns or related issues:

  Example queries:

  * "Find logs where users showed frustration"
  * "Find logs where the agent failed to answer the user's question"
  * "Are there other traces with similar errors?"
  * "Show me traces with comparable latency patterns"
</Accordion>

<Accordion title="Create custom trace visualizations">
  Generate [custom visualizations](/observe/view-logs#create-custom-trace-views) for your trace data using natural language:

  Example queries:

  * "Create a view that renders a list of all tools available in this trace and their outputs"
  * "Show a timeline of all LLM calls with their token counts"
</Accordion>

<Note>
  Loop on trace pages has a focused set of tools optimized for single-trace analysis. For broader log analysis and dataset generation, use Loop from the main <Icon icon="activity" /> **Logs** page.
</Note>

## Generate datasets

Create [datasets](/annotate/datasets) from your logs based on specific criteria:

<img src="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=37336e72e52b9f902fd94930efe6c3b2" alt="Generate dataset from logs" data-og-width="2196" width="2196" data-og-height="1440" height="1440" data-path="images/core/loop/generate-dataset-from-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=280&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=785ed8b42659598dda1691b56f699551 280w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=560&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=24ec8f783bf99431a47667810d6b5142 560w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=840&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=1faf0cd0f303fe9cd24f0b6de0b67818 840w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=1100&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=0865dfcd4958a651495a7567ddab5355 1100w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=1650&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=c0f7badaa8b6b2f3d501f542651f458c 1650w, https://mintcdn.com/braintrust/UtXR-Wt0mdWPIYU5/images/core/loop/generate-dataset-from-logs.png?w=2500&fit=max&auto=format&n=UtXR-Wt0mdWPIYU5&q=85&s=29a88190e99b6b806bb29b005b154ad7 2500w" />

Example queries:

* "Create a dataset from the most common inputs in the logs"
* "Generate a dataset from logs with errors"
* "Build a dataset from high-scoring examples"

## Generate scorers

Create [scorers](/evaluate/write-scorers) based on patterns you identify in logs:

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=71ed0861ebcbe0efe5dfc62327d0733e" alt="Generate scorer from logs" data-og-width="4177" width="4177" data-og-height="1304" height="1304" data-path="images/guides/loop/logsToScorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=ba2ad7a61ee28807763d5e0aa7f01a76 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=11df4f1cabda854bd415892aa26c4238 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2da287fde7e248781d29e17cba7f50d3 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=3f7c2fb6057edecbe1701dcd775f9eb8 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=a8884e5ff20430dda77ac604e9a08243 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/logsToScorer.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2e38430332b79f948faa92f8fca1ca4f 2500w" />

Example queries:

* "Generate a code-based scorer based on project logs"
* "Write a scorer that detects the errors I just identified"
* "Create an LLM-as-a-judge scorer for helpfulness based on these logs"

## Search documentation

Ask Loop to search through Braintrust documentation for relevant information and guidance:

<img src="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=59fde0c8eb4fa1f61a248f2321689750" alt="Search docs with loop" data-og-width="2884" width="2884" data-og-height="1798" height="1798" data-path="images/guides/loop/docs-search-loop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=280&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=e5d2b2c3402c50bf96e80e6d5add0645 280w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=560&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=2197518b3fa4dae33bf3a94fd7b54cb8 560w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=840&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=7148f6467517014ac541f83318c4c611 840w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=1100&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=64e307da353d97c14ef130a8a88b5795 1100w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=1650&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=48fc06ca101300dc912d78ca02cdd3c9 1650w, https://mintcdn.com/braintrust/b11zJxKLgN0Qiq8B/images/guides/loop/docs-search-loop.png?w=2500&fit=max&auto=format&n=b11zJxKLgN0Qiq8B&q=85&s=48fa33f193e019744d6c27d5dfc291ad 2500w" />

Example queries:

* "How do I use the Braintrust SDK?"
* "What is the difference between a prompt and a scorer?"
* "How do I configure online scoring?"

## Next steps

* [Build datasets](/annotate/datasets) from patterns you identify
* [Create scorers](/evaluate/write-scorers) based on log analysis
* [Run experiments](/evaluate/run-evaluations) to validate improvements
* [View individual traces](/observe/view-logs#view-a-specific-trace) to analyze specific executions
* Try the [Loop cookbook](/cookbook/recipes/Loop) for more examples

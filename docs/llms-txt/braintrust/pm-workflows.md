# Source: https://braintrust.dev/docs/best-practices/pm-workflows.md

# Product manager workflows

This guide is for product managers and subject matter experts using Braintrust. It covers best practices, core workflows, and tips to help you quickly become effective. Braintrust is designed to make AI feature development measurable, iterative, and collaborative for both technical and nontechnical teammates.

## What Braintrust enables for PMs

Braintrust empowers product managers to:

* **Make qualitative bets measurable**: Replace "feels better" with data-driven decisions.
* **Test and iterate without engineering dependencies**: Evaluate AI features independently using the UI.
* **Collaborate in a shared platform**: Work directly with engineers and stakeholders using the same tools and visibility.
* **Ship faster with confidence**: Catch regressions early and continuously improve AI quality through systematic evaluation.

## The continuous improvement loop

Use the following workflow to continuously improve your AI features. Each step is supported by Braintrust's integrated tools.

<Steps>
  <Step title="Spot patterns in production">
    Review [logs](/core/logs) to identify recurring issues, user pain points, or behavioral patterns in your AI system.

    Use [Loop](/core/loop), [filters](/core/loop#generate-and-run-btql-queries), or [deep search](/core/logs/use-deep-search) to surface interesting logs. Each log includes the full [trace](/guides/traces) for additional context.
  </Step>

  <Step title="Curate targeted datasets">
    Create small, focused [datasets](/core/playground#datasets) from your real application logs as test data to use for iteration and evaluation. A good dataset contains 10 to 200 examples and target particular behavioral patterns from your users.

    Use [tags](/core/logs/view#tags) to organize examples from real user interactions and add logs directly to datasets for rapid curation.

    <Note>
      Avoid maintaining large, static "golden datasets." Models and prompts evolve quickly, so your test data should evolve alongside them.
    </Note>
  </Step>

  <Step title="Iterate in playgrounds">
    Use [playgrounds](/core/playground) to compare prompt and model changes side-by-side on the same dataset.

    For subjective qualities like tone, empathy, and conversational feel, rely on human judgment. For objective checks like accuracy or format compliance, use [automated scorers or LLM-as-judge](/best-practices/scorers).
  </Step>

  <Step title="Apply human review where it matters">
    Use the [review](/core/human-review) UI for batch review with keyboard shortcuts, sliders, and freeform notes.

    Treat human labels as first-class signals that you can filter, revisit, and use to gate releases.
  </Step>

  <Step title="Deploy and monitor">
    Once a change passes evaluation, deploy it directly without engineering handoffs for prompt or dataset updates.

    After shipping, [monitor](/core/monitor) live logs and re-run targeted datasets to catch regressions, especially after model upgrades.
  </Step>
</Steps>

## Best practices

The Braintrust toolset is powerful and provides flexibility to support many workflows. These best practices help you get the most out of the platform.

### Treat production as the source of truth

Continuously feed real user logs into Braintrust. You can add any trace to a dataset with one button. Use production data to decide what to test and improve.

### Keep datasets small and fresh

Curate datasets for each new issue or edge case. Ten to two hundred examples is usually enough to identify and fix patterns. Avoid relying on static golden datasets that grow stale as your system evolves.

### Use human review for subjective quality

For qualities like tone, empathy, and conversational feel, manual review is essential. Use [keyboard shortcuts](/core/human-review#focused-review-mode) and batch actions to review efficiently. Human review scores and notes become filterable signals for analysis and release gating.

### Automate only what is deterministic

Use [automated scorers](/core/experiments/write#online-evaluation) for binary or easily measurable checks like accuracy and latency. For subjective work, rely on domain experts and manual review rather than forcing automated evaluations.

### Version control everything

Braintrust automatically versions prompts, datasets, and experiments. Use this to compare different prompt versions on the same dataset and identify which performs better. Always document changes and avoid overwriting test cases without review.

### Make Braintrust a team visibility tool

Share [dashboards](/core/monitor#create-custom-dashboards) and experiment results in sprint demos and product reviews. Give PMs, engineers, and stakeholders access to the same data, metrics, and logs to eliminate silos.

### Iterate quickly and ship often

Move from idea to tested prototype in hours rather than sprints. Use playgrounds and human review to validate changes before shipping. After each deployment, rerun evaluations, inspect results, and roll back if necessary.

## UI workflow tips

**[Playgrounds](/core/playground)**: Test prompts and models without code. Run A/B comparisons and share results with engineers for productionization.

**[Human review](/core/human-review)**: Use keyboard shortcuts to label outputs rapidly. Mark good and bad examples, add contextual notes, and build datasets as you review.

**[Monitor page](/core/monitor#monitor-custom-dashboards)**: Use built-in dashboards to track quality, regressions, and improvements over time. These visualizations help communicate impact to stakeholders.

**Collaboration**: Team members can [comment](/core/human-review#leave-comments), tag, and share experiments. PMs can operate independently or work in tandem with engineering.

## AI-assisted workflows with Loop

Use [Loop](/core/loop) to accelerate common PM tasks:

* Find patterns in recent failures and generate [BTQL filters from natural language](/core/loop#generate-and-run-btql-queries)
* Collect examples of specific issues into new datasets for targeted evaluations
* Bulk-generate examples that vary user persona and length, or draft expected outputs
* Summarize which prompts regress on specific criteria or group failures by score
* Create LLM-judge scorers with custom rubrics and examples
* Write [BTQL](https://www.braintrust.dev/docs/reference/btql) queries for common analyses like listing top error types

<Note>
  If your organization has Loop disabled, ask an admin to enable it in Settings. Hybrid deployments require version v0.0.74+.
</Note>

## Why Braintrust works for PMs

**No-code and UI-based**: Run evaluations, review outputs, and manage datasets without writing code.

**Human in the loop**: Manual review is as important as automated metrics, especially for subjective qualities.

**Integrated workflow**: [Logs](/core/logs), [datasets](/core/playground#datasets), [experiments](/core/experiments), and [reviews](/core/human-review) live in one place, supporting rapid iteration and collaboration.

**Direct deployment**: Nontechnical users can ship [prompt](/core/functions/prompts) and dataset changes directly to production, accelerating iteration velocity.

## Additional resources

* [Getting started](/start)
* [Cookbook](/cookbook)
* [Access control](/guides/access-control)
* [All guides](/guides)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
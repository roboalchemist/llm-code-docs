# Source: https://braintrust.dev/docs/core/projects.md

# Projects

> Create and configure projects

A project is analogous to an AI feature in your application. Some customers create separate projects for development and production to help track workflows. Projects contain all [experiments](/core/experiments), [logs](/core/logs), [datasets](/core/datasets) and [playgrounds](/core/playground) for the feature.

Projects house configuration settings shared across the project.

## Create a project

You can create projects through the UI or programmatically via the SDK.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    To create a new project in the UI, navigate to your organization's project list and select **+ Project**. Enter a project name and click **Create**.
  </Tab>

  <Tab title="SDK" icon="terminal">
    To create a project in code, use the `projects.create()` method.

    <Note>
      If a project already exists, `projects.create()` returns a handle. There is no separate `.get()` method.
    </Note>

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as braintrust from "braintrust";

      // Get a handle to the project (creates if it doesn't exist)
      const project = braintrust.projects.create({ name: "my-project" });

      // Use the project to create functions, log data, etc.
      project.tools.create({...});
      project.prompts.create({...});
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      # Get a handle to the project (creates if it doesn't exist)
      project = braintrust.projects.create(name="my-project")

      # Use the project to create functions, log data, etc.
      project.tools.create(...)
      project.prompts.create(...)
      ```
    </CodeGroup>

    You can also create projects when initializing experiments or loggers:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import * as braintrust from "braintrust";

      // Creates project "my-project" if it doesn't exist
      const experiment = braintrust.init("my-project", {
        experiment: "my-experiment"
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import braintrust

      # Creates project "my-project" if it doesn't exist
      experiment = braintrust.init(project="my-project", experiment="my-experiment")
      ```
    </CodeGroup>

    For more details, see the SDK reference for [Python](/reference/sdks/python#projectbuilder) or [TypeScript](/reference/sdks/typescript#projectbuilder).
  </Tab>
</Tabs>

## Tags

Braintrust supports tags that you can use throughout your project to curate logs, datasets, and even experiments. You can filter based on tags in the UI to track various kinds of data across your application, and how they change over time. Tags can be created in the **Configuration** tab by selecting **Add tag** and entering a tag name, selecting a color, and adding an optional description.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/tags.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=8f260cc34d0f4fc1bb5eab1f0f2c6e2f" alt="Create tag" width="568" height="307" data-og-width="1136" data-og-height="614" data-path="images/guides/projects/tags.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/tags.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=73ab129d8c94f9b603f8e8f08c7c1249 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/tags.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=abde1a808502397bda4082b1d7257058 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/tags.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=3e3dc349ed62231fd1f4f61436c47527 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/tags.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=b1d5674eb94123b0eb853bc11ea6c3cf 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/tags.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=ae1e50fbcc1bdf1813763968f931c6a0 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/tags.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=bf1afdd76c6e33442e9ce07f51304b5c 2500w" />

For more information about using tags to curate logs, check out the [logging guide](/core/logs#tags-and-queues).

## Human review

You can define scores and labels for manual human review, either as feedback from your users (through the API) or directly through the UI. Scores you define on the **Configuration** page will be available in every experiment and log in your project.

To create a new score, select **Add human review score** and enter a name and score type. You can add multiple options and decide if you want to allow writing to the expected field instead of the score, or multiple choice.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/human-review.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=f83f0b9810e5f678f6f3ce0b958122dd" alt="Create human review score" width={1124 / 2} height={976 / 2} data-og-width="1124" data-og-height="976" data-path="images/guides/projects/human-review.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/human-review.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=2277a93f7d403cf103d848e0c23e0821 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/human-review.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=68edcbafd1c48741db00462b9244ece1 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/human-review.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=45146e63f6ecf1a8c3a82613e903fce1 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/human-review.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=1302c18c9d5ae7cb7ef98af3060507b0 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/human-review.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=095d96ae3c7753761584702edc70b82f 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/human-review.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=8f276072e13d5814b8038f39e852d972 2500w" />

To learn more about human review, check out the [full guide](/core/human-review).

## Aggregate scores

Aggregate scores are formulas that combine multiple scores into a single value. This can be useful for creating a single score that represents the overall experiment.

To create an aggregate score, select **Add aggregate score** and enter a name, formula, and description. Braintrust currently supports three types of aggregate scores:

<img src="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=04e0cfcc3540ccd8f96c75b0f6d3c59d" alt="Add aggregate score" width={1136 / 2} height={1012 / 2} data-og-width="1136" data-og-height="1012" data-path="images/core/experiments/add-aggregate-score.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=280&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=5dd7274a5f0929f25b89d3eb61c45d5f 280w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=560&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=411833a6bf9b3280a3cbdcbe0c4c8042 560w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=840&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=bb763140b615fd285dbcf0b3ac59f9bc 840w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=1100&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=95ad65a931300136b5cee76f008fac00 1100w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=1650&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=f7a65f4528a6a037174a804b67304294 1650w, https://mintcdn.com/braintrust/286-LRz_qGMfyggP/images/core/experiments/add-aggregate-score.png?w=2500&fit=max&auto=format&n=286-LRz_qGMfyggP&q=85&s=003b53a2981c4aaa86d64dd2fba7a632 2500w" />

Braintrust currently supports three types of aggregate scores:

* **Weighted average** - A weighted average of selected scores.
* **Minimum** - The minimum value among the selected scores.
* **Maximum** - The maximum value among the selected scores.

To learn more about aggregate scores, check out the [experiments guide](/core/experiments/interpret#aggregate-weighted-scores).

## Online scoring

Braintrust supports server-side online evaluations that are automatically run asynchronously as you upload logs. To create an online evaluation, select **Add rule** and input the rule name, description, and which scorers and sampling rate you'd like to use. You can choose from custom scorers available in this project and others in your organization, or built-in scorers. Decide if you'd like to apply the rule to the root span or any other spans in your traces.

For more information about online evaluations, check out the [logging guide](/core/logs#online-evaluation).

## Span iframes

You can configure span iframes from your project settings. For more information, check out the [extend traces](/guides/traces/extend/#custom-rendering-for-span-fields) guide.

## Comparison key

When comparing multiple experiments, you can customize the expression you're using to evaluate test cases by changing the comparison key. It defaults to "input," but you can change it in your project's **Configuration** tab.

<img src="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=395cdce8f0459bbbd4ac591d9d8e0650" alt="Create comparison key" width={1552 / 2} height={282 / 2} data-og-width="1552" data-og-height="282" data-path="images/guides/projects/comparison-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=280&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=f2a0d804e9bf494fd2e3e51846fab6e3 280w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=560&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=3fc8632c4a7bb7df4ff10dc664c74409 560w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=840&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=77c6e881a1c686ed1c28df376b5d87ea 840w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=1100&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=eba38a4ed439e35a85d70c894c5639b9 1100w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=1650&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=4726778c4a41ad4e0553b17de24af3e5 1650w, https://mintcdn.com/braintrust/tQWbJcq__mTOHSpB/images/guides/projects/comparison-key.png?w=2500&fit=max&auto=format&n=tQWbJcq__mTOHSpB&q=85&s=88204b9577364076cd496d701868e626 2500w" />

For more information about the comparison key, check out the [evaluation guide](/core/experiments/interpret#customizing-the-comparison-key).

## Edit project name and description

To edit the name and description of a project, do the following:

1. Navigate to the project overview.
2. Click **Edit project**.
3. Edit the name and description.
4. Click **Save**.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
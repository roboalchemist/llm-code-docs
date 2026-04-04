# Source: https://braintrust.dev/docs/annotate/labels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add labels and corrections

> Annotate traces with tags, comments, and expected values

Beyond numeric scores, you can annotate traces with tags, comments, expected values, and metadata to provide context and build better datasets. These annotations flow between logs, datasets, and experiments.

After reviewing and scoring traces, use tags, comments, and corrections to further organize and enrich your data for dataset creation.

## Apply tags

Tags categorize and organize traces across your project. Use tags to mark traces for review, indicate status, or group related examples. Tags flow between logs, datasets, and experiments.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    ### Configure tags

    Set up tags at the project level:

    1. Navigate to the **Configuration** tab in your project.
    2. Add, modify, or delete tags with custom names, colors, and descriptions.

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=bdc9c2ee34d75b6fcd6f3354ba27309b" alt="Configure tags" data-og-width="2918" width="2918" data-og-height="1238" height="1238" data-path="images/guides/logs/Configure-Tags.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=adb11b09d20b0bced71877cb1b74c307 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=113b56a6abe379fe51cea3fb303f0644 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=6f5d221b6cfa3a5fd216ab9ead6165bd 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=136e984e7a41f7c8c0ac85a4a943ce0f 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=eff122d9321a6c8960fc4a564c39c486 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=8b553ff0749653c4fe90931b52e41696 2500w" />

    ### Add tags

    Select traces and apply tags from the table or trace view:

    <video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/logs/Add-Tag-Poster.png">
      <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Add-Tag.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=9c076d5466b0f153f642f18ceb63b9b8" type="video/mp4" data-path="images/guides/logs/Add-Tag.mp4" />
    </video>
  </Tab>

  <Tab title="SDK" icon="terminal">
    Include tags when logging or providing feedback:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger } from "braintrust";

      const logger = initLogger({ projectName: "My Project" });

      // When logging
      logger.traced(async (span) => {
        span.log({
          input,
          output: result,
          tags: ["user-action", "triage"],
        });
      });

      // When logging feedback
      logger.logFeedback({
        id: spanId,
        scores: { correctness: score },
        tags: ["needs-review"],
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import init_logger

      logger = init_logger(project="My Project")

      # When logging
      with logger.start_span() as span:
          span.log(input=input, output=result, tags=["user-action", "triage"])

      # When logging feedback
      logger.log_feedback(
          id=span_id,
          scores={"correctness": score},
          tags=["needs-review"],
      )
      ```
    </CodeGroup>

    <Note>
      Tags can be applied to any span in a trace. When viewing traces, tags from all spans are aggregated and displayed together at the trace level. When you log additional tags, they are automatically merged (union), rather than replaced.
    </Note>
  </Tab>
</Tabs>

## Add comments

Comments provide free-form context and explanations. Use comments to explain why a trace succeeded or failed, note patterns or edge cases, share insights with teammates, or document corrections.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    Open any trace and add comments in the trace view:

    <video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/human-review/comment-poster.png">
      <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/comment.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=b8aeec14bc3456cc40591c3e3a1e085c" type="video/mp4" data-path="images/guides/human-review/comment.mp4" />
    </video>

    Copy links to comments to share with teammates. Comments are searchable using the filter menu.
  </Tab>

  <Tab title="SDK" icon="terminal">
    Include comments when logging feedback:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      logger.logFeedback({
        id: spanId,
        comment: "User reported incorrect information in the response",
        scores: { correctness: 0 },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      logger.log_feedback(
          id=span_id,
          comment="User reported incorrect information in the response",
          scores={"correctness": 0},
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Update expected values

Expected values define the correct or ideal output for a given input. Update expected values to provide ground truth for evaluation, document user corrections, specify multiple acceptable answers, or label categorical data.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    Click any expected field in a trace to edit it directly. You can:

    * Enter structured JSON data
    * Use form-based editing (if schemas are defined)
    * Write categorical labels via human review scores
    * Copy expected values from other spans

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=406359641fc9f3de4f70086d56f236dd" alt="Write to expected" data-og-width="1852" width="1852" data-og-height="966" height="966" data-path="images/guides/human-review/expected-fields.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=74c2817c643f44e6bf10b5c872ad988b 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2504bd28d1b54f4430d7458fd407be25 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=5691362eca4b4c03f9b2dbf32873bb51 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=2d93b28ed1d8d7f62d65c15b4786a762 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=e2ee18d7f67b4b4f89c08d765a7734bb 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/human-review/expected-fields.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=a44f9ea41167ce86f27a572aac1c3f7d 2500w" />

    <Tip>
      You can also [create human review scores](/annotate/human-review#configure-review-scores) when reviewing traces.
    </Tip>
  </Tab>

  <Tab title="SDK" icon="terminal">
    Include expected values when logging feedback or updating datasets:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      // Update via feedback
      logger.logFeedback({
        id: spanId,
        expected: { answer: "The correct answer is 42" },
        comment: "User provided correction",
      });

      // Update dataset record
      dataset.update({
        id: recordId,
        expected: { answer: "Updated expected value" },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # Update via feedback
      logger.log_feedback(
          id=span_id,
          expected={"answer": "The correct answer is 42"},
          comment="User provided correction",
      )

      # Update dataset record
      dataset.update(
          id=record_id,
          expected={"answer": "Updated expected value"},
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Add metadata

Metadata provides structured context for filtering and analysis. Common metadata includes user IDs and session IDs, feature flags or A/B test variants, geographic or demographic information, request source or client type, and custom business context.

<Tabs>
  <Tab title="SDK" icon="terminal">
    Add metadata when logging or via feedback:

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      // When logging
      span.log({
        input,
        output: result,
        metadata: {
          user_id: userId,
          feature_variant: "test-a",
          request_source: "mobile-app",
        },
      });

      // Via feedback
      logger.logFeedback({
        id: spanId,
        metadata: {
          reviewer: "jane@company.com",
          review_date: new Date().toISOString(),
          category: "edge-case",
        },
      });
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      # When logging
      span.log(
          input=input,
          output=result,
          metadata={
              "user_id": user_id,
              "feature_variant": "test-a",
              "request_source": "mobile-app",
          },
      )

      # Via feedback
      logger.log_feedback(
          id=span_id,
          metadata={
              "reviewer": "jane@company.com",
              "review_date": datetime.now().isoformat(),
              "category": "edge-case",
          },
      )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Filter by annotations

Use filters to find annotated traces:

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE tags INCLUDES "needs-review"
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter: tags includes "needs-review"
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE comment IS NOT NULL
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter: comment IS NOT NULL
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE metadata.category = "edge-case"
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter: metadata.category = "edge-case"
  ```
</CodeGroup>

<CodeGroup>
  ```sql SQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  WHERE expected IS NOT NULL
  ```

  ```sql BTQL syntax theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
  filter: expected IS NOT NULL
  ```
</CodeGroup>

Combine filters to build precise queries for dataset curation.

## Next steps

* [Build datasets](/annotate/datasets) from annotated traces
* [Add human feedback](/annotate/human-review) for structured scoring
* [Run evaluations](/evaluate/run-evaluations) using labeled datasets
* [Export data](/annotate/export) with annotations intact

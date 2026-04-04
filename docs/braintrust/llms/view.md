# Source: https://braintrust.dev/docs/guides/traces/view.md

# Source: https://braintrust.dev/docs/core/logs/view.md

# View logs

> Browse, filter, and analyze your production traces

To view logs from your application in real-time, go to your project in the Braintrust UI and select <Icon icon="activity" /> **Logs**.

## Browse traces and spans

By default, logs display as a table of traces, where each row represents a complete trace with its root span. To view all logged spans individually instead, select **Spans** in dropdown at the top of the page.

This is useful when you want to:

* Analyze individual operations within traces
* Find specific function calls or API requests
* Examine timing for particular operations

<video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/logs/spans-table-poster.png">
  <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/spans-table.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=116e31dc58f8c0dbbeb80c99cf105af2" type="video/mp4" data-path="images/guides/logs/spans-table.mp4" />
</video>

## Group related traces

View multiple related traces together based on shared metadata or tags. This helps you understand the full context of multi-step operations and related requests.

1. On the <Icon icon="activity" /> **Logs** page, select <Icon icon="stretch-horizontal" /> **Group** and a tag or metadata path to group by.
2. Select a trace. If the trace includes the grouped attribute, the trace tree shows the trace with all other relevant traces, and the corresponding rows in the table are highlighted.
3. In the trace panel, select <Icon icon="square-chart-gantt" /> **Timeline** to view the timing of operations or <Icon icon="messages-square" /> **Thread** to view the entire session.

<img src="https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=c7e24aafec4ae062eacd8ae5e7e7d3fa" alt="Group related traces" data-og-width="1219" width="1219" data-og-height="793" height="793" data-path="images/core/logs/group-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=280&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=5f5713a12deae26798ebcc6c65d36691 280w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=560&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=66366826dfd0c5717552e9145d73741e 560w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=840&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=c6d4ffd3678f8faad179dbc7ee6f9666 840w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=1100&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=ff9300f61745d0ebb7e90fbba73a677d 1100w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=1650&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=9454d087828a8a8a11aca56aadbddcb5 1650w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=2500&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=988cbd7f890ec7696365d6278eb29f63 2500w" />

## Create custom columns

Extract and display specific values from your traces as table columns. Custom columns let you surface important metadata, scores, or nested values directly in the logs table.

To create custom columns:

1. Select the column dropdown in the logs table.
2. Click **+ Add custom column**.
3. Enter a name and either choose from the inferred fields or enter a [BTQL](/reference/btql) expression to extract the value.

For example, create a column named `User ID` with the expression `metadata.user_id` to display the user ID for each trace.

Custom columns work the same way in both logs and experiments. For more details, see [Create custom columns](/core/experiments/interpret#create-custom-columns).

## Filter and search logs

You can filter logs three ways:

* **Filter menu**: Quick filters and [BTQL](/reference/btql) queries for precise field matching
* **Loop and deep search**: Natural language queries and AI-powered semantic search
* **API**: Programmatic access for integrations and automation

### Filter menu

Select <Icon icon="list-filter" /> **Filter** to filter logs by tags, time range, comments, and other fields.

Use the **Basic** tab for quick filters, or select **BTQL** to write a BTQL query. Add your own query or select <Icon icon="blend" /> **Generate** to create a query from a natural language description.

### Filter using Loop and deep search

Use [Loop](/core/loop) <Icon icon="blend" /> to ask questions about your logs and get AI-powered insights. Loop understands your data structure and can answer questions, identify patterns, and help you find specific traces.

* **Find similar traces**: Select rows in the logs table and use <Icon icon="glasses" /> **Find similar traces**. Loop analyzes the selected traces to identify common traits and returns similar traces.

* **Deep search**: Use [deep search](/core/logs/use-deep-search) to find traces based on semantic meaning rather than exact keywords. Deep search helps you discover patterns, sentiment, and edge cases that traditional filtering might miss.

### Filter through the API

For basic filters and programmatic access, use the [project logs](/api-reference) endpoint. This endpoint supports the same query syntax as the UI and allows you to specify additional fields to return.

For advanced queries, use the [BTQL](/reference/btql#api-access) endpoint.

## Iterate on prompts in playgrounds

Extract prompts and dataset inputs from logs to quickly iterate on them in playgrounds.

1. On the <Icon icon="activity" /> **Logs** page, select the rows you want to extract.
2. Select <Icon icon="shapes" /> **Iterate in playground**.
3. Customize your playground settings, optionally appending the extracted resources to existing resources.
4. Select **Create playground**.

## Apply tags to organize traces

Braintrust supports organizing logs with tags. Tags flow between logs, datasets, and experiments, so you can track specific types of data across your application and how they change over time.

Tags are configured at the project level.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    To configure tags:

    1. Navigate to the **Configuration** tab in your project.
    2. Add, modify, or delete tags with custom names, colors, and descriptions.

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=bdc9c2ee34d75b6fcd6f3354ba27309b" alt="Configure tags" data-og-width="2918" width="2918" data-og-height="1238" height="1238" data-path="images/guides/logs/Configure-Tags.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=adb11b09d20b0bced71877cb1b74c307 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=113b56a6abe379fe51cea3fb303f0644 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=6f5d221b6cfa3a5fd216ab9ead6165bd 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=136e984e7a41f7c8c0ac85a4a943ce0f 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=eff122d9321a6c8960fc4a564c39c486 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=8b553ff0749653c4fe90931b52e41696 2500w" />

    <video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/logs/Add-Tag-Poster.png">
      <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Add-Tag.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=9c076d5466b0f153f642f18ceb63b9b8" type="video/mp4" data-path="images/guides/logs/Add-Tag.mp4" />
    </video>
  </Tab>

  <Tab title="SDK" icon="terminal">
    Specify the `tags` field when logging data to add tags programmatically.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { wrapOpenAI, initLogger } from "braintrust";
      import { OpenAI } from "openai";

      const logger = initLogger({
        projectName: "My Project",
        apiKey: process.env.BRAINTRUST_API_KEY,
      });
      const client = wrapOpenAI(new OpenAI({ apiKey: process.env.OPENAI_API_KEY }));

      export async function POST(req: Request) {
        return logger.traced(async (span) => {
          const input = await req.text();
          const result = await client.chat.completions.create({
            model: "gpt-3.5-turbo",
            messages: [{ role: "user", content: input }],
          });
          span.log({ input, output: result, tags: ["user-action"] });
          return {
            result,
            requestId: span.id,
          };
        });
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import init_logger

      logger = init_logger(project="My Project")

      def my_route_handler(req):
          with logger.start_span() as span:
              body = req.body
              result = some_llm_function(body)
              span.log(input=body, output=result, tags=["user-action"])
              return {
                  "result": result,
                  "request_id": span.span_id,
              }
      ```
    </CodeGroup>

    <Note>
      Tags can only be applied to top-level spans, e.g., those created via `traced()`
      or `logger.startSpan()`/ `logger.start_span()`. You cannot apply tags to
      subspans (those created from another span) because they are properties of the
      whole trace, not individual spans.
    </Note>

    You can also apply tags while capturing feedback via the `logFeedback()` / `log_feedback()` method.

    <CodeGroup dropdown>
      ```typescript  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger } from "braintrust";

      const logger = initLogger({
        projectName: "My project",
        apiKey: process.env.BRAINTRUST_API_KEY,
      });

      export async function POSTFeedback(req: Request) {
        const { spanId, comment, score, userId } = await req.json();
        logger.logFeedback({
          id: spanId, // Use the newly created span's id, instead of the original request's id
          comment,
          scores: {
            correctness: score,
          },
          metadata: {
            user_id: userId,
          },
          tags: ["user-feedback"],
        });
      }
      ```

      ```python  theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import init_logger

      logger = init_logger(project="My Project")

      def my_feedback_handler(req):
          logger.log_feedback(
              id=req.body.request_id,
              scores={
                  "correctness": req.body.score,
              },
              comment=req.body.comment,
              metadata={
                  "user_id": req.user.id,
              },
              tags=["user-feedback"],
          )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Next steps

* Learn how to [write logs to Braintrust](/core/logs/write)
* Use [deep search](/core/logs/use-deep-search) to find traces semantically
* Explore [Loop](/core/loop) for AI-powered insights
* Write advanced queries with [BTQL](/reference/btql)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt
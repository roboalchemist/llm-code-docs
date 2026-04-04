# Source: https://braintrust.dev/docs/observe/view-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# View your logs

> Browse traces, create custom columns, and organize with tags

To view logs from your application in real-time, go to your project in the Braintrust UI and select <Icon icon="activity" /> **Logs**.

## Browse traces or spans

By default, logs display as a table of traces where each row represents a complete trace with its root span.

Select <Icon icon="settings-2" /> **Display** > <Icon icon="rows-3" /> **Row type** > <Icon icon="diamond" /> **Spans** view to see all logged spans individually.

View individual spans when you want to:

* Analyze specific operations within traces
* Find particular function calls or API requests
* Examine timing for individual operations

## Filter traces

Each project provides default table views with common filters, including:

* **Default view**: Shows all records
* **Non-errors**: Shows only records without errors
* **Errors**: Shows only records with errors
* **Unreviewed**: Hides items that have been human-reviewed
* **Assigned to me**: Shows only records assigned to the current user for human review

Use the <Icon icon="layers-2" /> menu to switch the table view.

You can also use the <Icon icon="list-filter" /> **Filter** menu to add custom filtering. See [Filter and search logs](/observe/filter) for more details.

<Tip>
  Default table views cannot be modified, but you can create [custom table views](#create-custom-table-views) based on custom filters and display settings.
</Tip>

## Group related traces

Group related traces by shared metadata or tags to understand multi-step operations.

1. Select <Icon icon="settings-2" /> **Display** > **Group trace by** and choose a tag or metadata path.
2. Select a trace with the grouped attribute to see it alongside all related traces
3. Switch to <Icon icon="square-chart-gantt" /> **Timeline** view to see operation timing or <Icon icon="messages-square" /> **Thread** view for the entire session.

<img src="https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=c7e24aafec4ae062eacd8ae5e7e7d3fa" alt="Group related traces" data-og-width="1219" width="1219" data-og-height="793" height="793" data-path="images/core/logs/group-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=280&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=5f5713a12deae26798ebcc6c65d36691 280w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=560&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=66366826dfd0c5717552e9145d73741e 560w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=840&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=c6d4ffd3678f8faad179dbc7ee6f9666 840w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=1100&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=ff9300f61745d0ebb7e90fbba73a677d 1100w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=1650&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=9454d087828a8a8a11aca56aadbddcb5 1650w, https://mintcdn.com/braintrust/UMUFxoAjk7qVjzj5/images/core/logs/group-logs.png?w=2500&fit=max&auto=format&n=UMUFxoAjk7qVjzj5&q=85&s=988cbd7f890ec7696365d6278eb29f63 2500w" />

## View a specific trace

Select any trace from the logs table to open it in a panel on the right side of your screen. The trace shows all spans that make up the request, with detailed information about inputs, outputs, timing, and metadata.

Use the <Icon icon="fullscreen" /> button to expand the trace to fullscreen or the <Icon icon="arrow-up-right" /> button to open it in a separate page.

### View as a timeline

While viewing a trace, select <Icon icon="square-chart-gantt" /> **Timeline** to visualize the trace as a gantt chart. This view shows spans as horizontal bars where the width represents duration. Bars are color-coded by span type, making it easy to identify performance bottlenecks and understand the execution flow.

### View as a thread

While viewing a trace, select <Icon icon="messages-square" /> **Thread** to view the trace as a conversation thread. This view displays messages, tool calls, and scores in chronological order, ideal for debugging LLM conversations and multi-turn interactions.

Use <Icon icon="search" /> **Find** or press `Cmd/Ctrl+F` to search within the thread view and quickly locate specific content such as message text and score rationale. Matches are highlighted in-place using your browser's native highlighting.

<Note>
  Thread view searches only within the currently open trace, not across all traces in your project.
</Note>

### Create custom trace views

While viewing a trace, select <Icon icon="layers-2" /> **Views** to create custom visualizations using natural language. Describe how you want to view your trace data and [Loop](/observe/loop) will generate the code.

For example:

* "Create a view that renders a list of all tools available in this trace and their outputs"
* "Render the video url from the trace's metadata field and show simple thumbs up/down buttons"

By default, a custom trace view is only visible and editable by the user who created it. To share your view with all users in the project, select **Save** > **Save as new view version** > **Update**.

<Note>
  Self-hosted deployments: If you restrict outbound access, allowlist `https://www.braintrustsandbox.dev` to enable custom views. This domain hosts the sandboxed iframe that securely renders custom view code.
</Note>

### Change span data format

When viewing a trace, each span field (input, output, metadata, etc.) displays data in a specific format. Change how a field displays by selecting the view mode dropdown in the field's header.

Available views:

* **Pretty** - Parses objects deeply and renders values as Markdown (optimized for readability)
* **JSON** - JSON highlighting and folding
* **YAML** - YAML highlighting and folding
* **Tree** - Hierarchical tree view for nested data structures

Additional format-specific views appear automatically for certain data types:

* **LLM** - Formatted AI messages and tool calls with Markdown
* **LLM Raw** - Unformatted AI messages and tool calls
* **HTML** - Rendered HTML content

Your view mode selection is remembered per field type. To set a default view mode for all fields, go to <Icon icon="settings-2" /> **Settings** > **Personal** > <Icon icon="square-user-round" /> **Profile** and select your preferred data view. See [Personal settings](/admin/personal-settings#default-data-display-format) for more details.

### View raw trace data

When viewing a trace, select a span and then select the <Icon icon="braces" /> button in the span's header to view the complete JSON representation. The raw data view shows all fields including metadata, inputs, outputs, and internal properties that may not be visible in other views.

The raw data view has two tabs:

* **This span** - Shows the complete JSON for the selected span only
* **Full trace** - Shows the complete JSON for the entire trace

Use the search bar at the top of the dialog to find specific content within the data.

Raw span data is useful when you need to:

* Inspect the complete span structure for debugging
* Find specific fields in large or deeply nested spans
* Verify exact values and data types
* Export or copy the full span for reproduction

## Analyze with Loop

Use <Icon icon="blend" /> **Loop** to query and analyze your logs through natural language. Loop is available on both the main <Icon icon="activity" /> **Logs** page and when viewing individual traces.

See [Analyze logs](/observe/loop#analyze-logs) and [Analyze individual traces](/observe/loop#analyze-individual-traces) for more details.

## Iterate in playgrounds

Extract prompts and inputs from logs to quickly test variations in playgrounds.

1. Select the rows you want to extract.
2. Select <Icon icon="shapes" /> **Iterate in playground**.
3. Customize settings and optionally append to existing resources.
4. Select **Create playground**.

## Organize with tags

Tags help you categorize and track specific types of data across logs, datasets, and experiments.

<Tabs>
  <Tab title="UI" icon="mouse-pointer-2">
    Configure tags in your project:

    1. Navigate to the **Configuration** tab
    2. Add, modify, or delete tags with custom names, colors, and descriptions

        <img src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=bdc9c2ee34d75b6fcd6f3354ba27309b" alt="Configure tags" data-og-width="2918" width="2918" data-og-height="1238" height="1238" data-path="images/guides/logs/Configure-Tags.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=280&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=adb11b09d20b0bced71877cb1b74c307 280w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=560&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=113b56a6abe379fe51cea3fb303f0644 560w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=840&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=6f5d221b6cfa3a5fd216ab9ead6165bd 840w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=1100&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=136e984e7a41f7c8c0ac85a4a943ce0f 1100w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=1650&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=eff122d9321a6c8960fc4a564c39c486 1650w, https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Configure-Tags.png?w=2500&fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=8b553ff0749653c4fe90931b52e41696 2500w" />

    <video className="border rounded-md" loop autoPlay muted playsInline poster="/images/guides/logs/Add-Tag-Poster.png">
      <source src="https://mintcdn.com/braintrust/ORZ9J5LROFjITLRP/images/guides/logs/Add-Tag.mp4?fit=max&auto=format&n=ORZ9J5LROFjITLRP&q=85&s=9c076d5466b0f153f642f18ceb63b9b8" type="video/mp4" data-path="images/guides/logs/Add-Tag.mp4" />
    </video>
  </Tab>

  <Tab title="SDK" icon="terminal">
    Add tags programmatically when logging:

    <CodeGroup dropdown>
      ```typescript {14} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { wrapOpenAI, initLogger } from "braintrust";
      import { OpenAI } from "openai";

      const logger = initLogger({ projectName: "My Project" });
      const client = wrapOpenAI(new OpenAI());

      export async function POST(req: Request) {
        return logger.traced(async (span) => {
          const input = await req.text();
          const result = await client.chat.completions.create({
            model: "gpt-4o",
            messages: [{ role: "user", content: input }],
          });
          span.log({ input, output: result, tags: ["user-action"] });
          return { result, requestId: span.id };
        });
      }
      ```

      ```python {8} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import init_logger

      logger = init_logger(project="My Project")

      def my_route_handler(req):
          with logger.start_span() as span:
              result = some_llm_function(req.body)
              span.log(input=req.body, output=result, tags=["user-action"])
              return {"result": result, "request_id": span.id}
      ```
    </CodeGroup>

    <Note>
      Tags can be applied to any span in a trace. When viewing traces, tags from all spans are aggregated and displayed together at the trace level. This means you can add contextual tags to specific operations while still being able to filter traces by any of their contained tags.
    </Note>

    Add tags when logging feedback:

    <CodeGroup dropdown>
      ```typescript {12} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      import { initLogger } from "braintrust";

      const logger = initLogger({ projectName: "My Project" });

      export async function POSTFeedback(req: Request) {
        const { spanId, comment, score, userId } = await req.json();
        logger.logFeedback({
          id: spanId,
          comment,
          scores: { correctness: score },
          metadata: { user_id: userId },
          tags: ["user-feedback"],
        });
      }
      ```

      ```python {11} theme={"theme":{"light":"github-light","dark":"github-dark-dimmed"}}
      from braintrust import init_logger

      logger = init_logger(project="My Project")

      def my_feedback_handler(req):
          logger.log_feedback(
              id=req.body.request_id,
              scores={"correctness": req.body.score},
              comment=req.body.comment,
              metadata={"user_id": req.user.id},
              tags=["user-feedback"],
          )
      ```
    </CodeGroup>
  </Tab>
</Tabs>

## Customize the logs table

### Show and hide columns

Select <Icon icon="settings-2" /> **Display** > **Columns** and then:

* Show or hide columns to focus on relevant data
* Reorder columns by dragging them
* Pin important columns to the left

All column settings are automatically saved when you save a view.

### Create custom columns

Surface important metadata, scores, or nested values directly in the logs table by creating custom columns:

1. Select <Icon icon="settings-2" /> **Display** > **+ Add custom column**.
2. Name your column.
3. Choose from inferred fields or write a SQL expression.

For example, create a column named `User ID` with the expression `metadata.user_id` to display the user ID for each trace.

Custom columns work the same way in both logs and experiments. For more details, see [Create custom columns](/evaluate/interpret-results#create-custom-columns).

### Adjust table layout

To change the table density to see more or less detail per row, select <Icon icon="settings-2" /> **Display** > **Row height** > **Compact** or **Tall**.

To switch between different layouts, select <Icon icon="settings-2" /> **Display** > **Layout** and one of the following:

* List: Default table view.
* Grid: Compare outputs side-by-side.
* Summary: Large-type summary of scores and metrics across all experiments.

Layouts respect view filters and are automatically saved when you save a view.

### Create custom table views

Custom table views save your table configurations including filters, column order, column visibility, and display settings. This lets you quickly switch between different ways of analyzing your logs.

To create a custom table view:

1. Apply the filters and display settings you want.
2. Select **Save as** in the toolbar.
3. Enter a view name.

Custom table views are accessible and configurable by any member of the organization. Table views update dynamically with new rows matching saved criteria.

## Next steps

* [Analyze with Loop](/observe/loop) using natural language queries
* [Filter and search](/observe/filter) to find specific traces
* [Use deep search](/observe/deep-search) for semantic queries
* [Score online](/observe/score-online) to evaluate production data
* [Create dashboards](/observe/dashboards) to monitor metrics

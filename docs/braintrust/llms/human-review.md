# Source: https://braintrust.dev/docs/annotate/human-review.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add human feedback

> Review traces with structured scores

Review traces and provide structured scores to begin the annotation process. You can efficiently evaluate large batches with keyboard navigation, or use the kanban layout to visualize review progress across backlog, pending, and complete states.

## Configure review scores

Review scores let you collect structured feedback on spans and label dataset rows.

Configure scores in <Icon icon="settings-2" /> **Settings** > **Project** > <Icon icon="list-checks" /> **Human review**. See [Configure human review](/admin/projects#configure-human-review) for details on score types and options.

## Score traces and datasets

Go to the <Icon icon="list-checks" /> **Review** page and select the type of data to review:

* **Log spans**: production traces and debugging sessions
* **Experiment spans**: Evaluation results and test runs
* **Dataset rows**: Test cases and examples

Then select a row and set scores. You can also [add comments and tags](/annotate/labels) while reviewing.

When finished reviewing, click **Complete review and continue** to move to the next item in the queue, or use the **Next row** and **Previous row** buttons.

<Note>
  Not all score types appear on dataset rows. Only categorical/slider scores configured to "write to expected" and free-form scores are available for dataset reviews, since datasets store test data (input/expected pairs) rather than subjective quality assessments.
</Note>

## Filter review data

Each project provides default table views with common filters, including:

* **Default view**: Shows all records
* **Awaiting review**: Shows only records flagged for review but not yet started
* **Assigned to me**: Shows only records assigned to you for review
* **Completed**: Shows only records that have finished review

Use the <Icon icon="layers-2" /> **View** menu to switch between views.

You can also use the [<Icon icon="list-filter" /> **Filter**](/observe/filter) menu to focus on specific subsets for review. Use the **Basic** tab for point-and-click filtering, or switch to **SQL** to write precise queries. For example, filter by scores (e.g., `scores.Preference > 0.75`) to find highly-rated examples.

<Tip>
  Default table views cannot be modified, but you can create [custom table views](#create-custom-table-views) based on custom filters and display settings.
</Tip>

<Tip>
  Use [tags](/observe/view-logs#organize-with-tags) to mark items for "Triage", then review them all at once.
</Tip>

## Change the trace layout

While reviewing log and experiment traces, you see detailed information about the flagged span by default.

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

## Create and edit scores inline

While reviewing, create new score types or edit existing configurations without navigating to settings:

* To create a new score, click **+ Human review score**.
* To edit an existing score, select the <Icon icon="pencil" /> edit icon next to the score name.

Changes apply immediately across your project.

<Note>
  Editing a score configuration affects how that score works going forward. Existing score values on traces remain unchanged.
</Note>

## Capture production feedback

In addition to internal reviews, capture feedback directly from production users. Production feedback helps you understand real-world performance and build datasets from actual user interactions.

See [Capture user feedback](/instrument/user-feedback) for implementation details and [Build datasets from user feedback](/annotate/datasets#from-user-feedback) to learn how to turn feedback into evaluation datasets. You can also use [dashboards](/observe/dashboards) to monitor user satisfaction trends and correlate automated scores with user feedback.

## Customize the review table

### Show and hide columns

Select <Icon icon="settings-2" /> **Display** > **Columns** and then:

* Show or hide columns to focus on relevant data
* Reorder columns by dragging them
* Pin important columns to the left

All column settings are automatically saved when you save a view.

### Use kanban layout

The kanban layout organizes flagged spans into three columns based on their review status:

* **Backlog**: Spans flagged for review but not yet started
* **Pending**: Spans currently being reviewed
* **Complete**: Spans that have finished review

To use the kanban layout:

1. On the <Icon icon="list-checks" /> **Review** page, select <Icon icon="settings-2" /> **Display** > **Layout** > **Kanban**.
2. Drag cards between columns to update review status. Changes save automatically.
3. Click any card to open the full trace for detailed review.

Each card displays the span name, creation date, assignees, and a preview of the input and output.

### Create custom table views

Custom table views save your table configurations including filters, column order, column visibility, and display settings. This lets you quickly switch between different ways of reviewing your data.

To create a custom table view:

1. Apply the filters and display settings you want.
2. Select **Save as** in the toolbar.
3. Enter a view name.

Custom table views are accessible and configurable by any member of the organization. Table views update dynamically with new rows matching saved criteria.

## Next steps

* [Add labels and corrections](/annotate/labels) to categorize and tag traces
* [Build datasets](/annotate/datasets) from reviewed logs
* [Capture user feedback](/instrument/user-feedback) from production
* [Run evaluations](/evaluate/run-evaluations) with human-reviewed datasets

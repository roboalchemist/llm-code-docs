# Source: https://docs.wandb.ai/weave/guides/tracking/annotation-queues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Set up annotation queues

> Create annotation queues, route traces to domain experts, and export structured feedback.

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

export const ColabLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="colab-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M14.25.18l.9.2.73.26.59.3.45.32.34.34.25.34.16.33.1.3.04.26.02.2-.01.13V8.5l-.05.63-.13.55-.21.46-.26.38-.3.31-.33.25-.35.19-.35.14-.33.1-.3.07-.26.04-.21.02H8.77l-.69.05-.59.14-.5.22-.41.27-.33.32-.27.35-.2.36-.15.37-.1.35-.07.32-.04.27-.02.21v3.06H3.17l-.21-.03-.28-.07-.32-.12-.35-.18-.36-.26-.36-.36-.35-.46-.32-.59-.28-.73-.21-.88-.14-1.05-.05-1.23.06-1.22.16-1.04.24-.87.32-.71.36-.57.4-.44.42-.33.42-.24.4-.16.36-.1.32-.05.24-.01h.16l.06.01h8.16v-.83H6.18l-.01-2.75-.02-.37.05-.34.11-.31.17-.28.25-.26.31-.23.38-.2.44-.18.51-.15.58-.12.64-.1.71-.06.77-.04.84-.02 1.27.05zm-6.3 1.98l-.23.33-.08.41.08.41.23.34.33.22.41.09.41-.09.33-.22.23-.34.08-.41-.08-.41-.23-.33-.33-.22-.41-.09-.41.09zm13.09 3.95l.28.06.32.12.35.18.36.27.36.35.35.47.32.59.28.73.21.88.14 1.04.05 1.23-.06 1.23-.16 1.04-.24.86-.32.71-.36.57-.4.45-.42.33-.42.24-.4.16-.36.09-.32.05-.24.02-.16-.01h-8.22v.82h5.84l.01 2.76.02.36-.05.34-.11.31-.17.29-.25.25-.31.24-.38.2-.44.17-.51.15-.58.13-.64.09-.71.07-.77.04-.84.01-1.27-.04-1.07-.14-.9-.2-.73-.25-.59-.3-.45-.33-.34-.34-.25-.34-.16-.33-.1-.3-.04-.25-.02-.2.01-.13v-5.34l.05-.64.13-.54.21-.46.26-.38.3-.32.33-.24.35-.2.35-.14.33-.1.3-.06.26-.04.21-.02.13-.01h5.84l.69-.05.59-.14.5-.21.41-.28.33-.32.27-.35.2-.36.15-.36.1-.35.07-.32.04-.28.02-.21V6.07h2.09l.14.01.21.03zm-6.47 14.25l-.23.33-.08.41.08.41.23.33.33.23.41.08.41-.08.33-.23.23-.33.08-.41-.08-.41-.23-.33-.33-.23-.41-.08-.41.08z" />
    </svg>
    Try in Colab
  </a>;

## Overview

Annotation queues let you route selected traces to domain experts for structured review without requiring them to navigate the full Weave UI. You define what feedback is collected, select which traces require review, and later can export completed annotations for analysis or dataset creation. Use cases can include:

* **Manual trace scoring**: Have SMEs rate model outputs on correctness, quality, or style.
* **Failure analysis**: Annotate failure modes (hallucinations, refusals, loops) to understand where your model breaks.
* **Domain expert review**: Enable medical, legal, or safety experts to review content with a task-focused interface.
* **Dataset creation**: Turn annotated traces into evaluation or training datasets.

## End-to-end workflow

The following workflow summarizes how to use annotation queues to obtain reviews:

1. Define annotation fields.
2. Create an annotation queue.
3. Load traces into the queue for review.
4. Monitor progress while domain experts complete reviews.
5. Filter and export completed annotations.

## Define annotation fields

To start creating an annotation queue, you must define your annotation fields first so that they can be selected during queue setup. Annotation fields define the feedback that the annotator provides for each trace item. Fields are reusable across queues and projects.

Field types include:

* Boolean judgments such as correctness or acceptability.
* Numeric or integer values such as quality or confidence.
* Categorical labels such as failure mode or intent.
* Free-form text for qualitative feedback.

To create an annotation field:

1. Navigate to [wandb.ai](https://wandb.ai) and select your project.
2. In the Weave project sidebar, click **Annotate**.  If you don't see **Annotate**, it might be nested in the menu under **More**.
3. In the tab bar, click the **Fields** tab.
4. In the Fields table toolbar, click **New Field**.
5. In the **Create annotation field** modal dialog, configure:
   * **Type**: Boolean, Integer, Number, String, or categorical options.
   * **Name**: Name of field to be displayed to the annotator.
   * **Description** (Optional): Details for evaluating this field to be displayed to the annotator.
6. Click **Create annotation field** to save the field.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/i_jfLHt7AV9D6HiI/weave/guides/tracking/imgs/AnnotationCreateField.png?fit=max&auto=format&n=i_jfLHt7AV9D6HiI&q=85&s=fd636409bf7960b67612a352f7bbc593" alt="Annotation field creation dialog with inputs for name, description, and field type, used to define the schema annotators complete when reviewing trace items." width="1331" height="528" data-path="weave/guides/tracking/imgs/AnnotationCreateField.png" />
</Frame>

Fields cannot be edited after creation to ensure annotation consistency.

## Create an annotation queue

An annotation queue consists of:

* A set of annotation fields.
* Guidelines that provide task instructions for annotators.
* A collection of trace items awaiting review.

To create an annotation queue:

1. In the Weave project sidebar, click **Annotate**.
2. In the tab bar, click the **Queues** tab.
3. In the Queues table toolbar, click **Create Queue**.
4. In the **Create Annotation Queue** modal dialog, configure:
   * **Queue name**: This is the queue name the annotator selects to complete their work.
   * **Guidelines** (Optional): Any additional instructions for the annotator.
5. Click **Next**.
6. Click **Manage fields** and choose what Annotation Fields to include in this review work. All existing Annotation Fields for the Project are available for selection.
7. After you have selected all the Fields for the queue, click **Create Queue** to save the queue.

All annotation queues for the project are listed in the Annotation Queues page.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/i_jfLHt7AV9D6HiI/weave/guides/tracking/imgs/AnnotationQueues.png?fit=max&auto=format&n=i_jfLHt7AV9D6HiI&q=85&s=13e99209cb1fe8ad9f0e9894dc0190af" alt="Annotation Queues page displaying a table of queues in the project, including queue names, descriptions, and review progress to track annotation workflows." width="1334" height="395" data-path="weave/guides/tracking/imgs/AnnotationQueues.png" />
</Frame>

Creating an annotation queue defines the fields and guidelines for evaluation, but you still need to add traces to the queue to identify what data should be evaluated.

### Add traces to a queue

Add traces to an annotation queue directly from the **Traces** page.

To add traces to an annotation queue:

1. In the Weave project sidebar, click **Traces**.
2. In the Traces table toolbar, filter traces as needed (such as by hallucination scores, failure modes, or specific ops).
3. In the table, select the traces you want annotated.
4. In the table's action bar, click **Add to queue** to add the selected rows to an annotation queue.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/i_jfLHt7AV9D6HiI/weave/guides/tracking/imgs/AnnotationAddTraces.png?fit=max&auto=format&n=i_jfLHt7AV9D6HiI&q=85&s=32e139c2b3d6df85a2676fe31aeff2d0" alt="Traces table with multiple rows selected and a bulk action bar showing actions that apply to the selected rows, such as Add to queue and Add to dataset." width="1346" height="862" data-path="weave/guides/tracking/imgs/AnnotationAddTraces.png" />
</Frame>

5. In the **Add to annotation queue** modal dialog, configure:
   * **Queue Name**: In the list, select the name of the existing queue to add these traces to.
   * **Select trace data to display**: Select the Weave trace data elements to display to the annotator as they are evaluating the results.
     * **Inputs**: Select which trace input fields to show during annotation.
     * **Outputs**: Select which trace output fields to show during annoation.
6. Click **Add ***\[Count]*** traces to annotation queue** to assign these traces as a part of the annotation queue review.

When adding traces, you control which trace inputs and which outputs or model responses are reviewed. This way you can present annotators with only the context needed to make accurate judgments.

## Monitor review progress

Once you have created the annotation queue and added traces to it, share the queue name with your annotator for them to begin their review. See [Review items in an annotation queue](/weave/guides/tracking/annotation-review) for details on the review process.

To share a direct link to the annotation queue with an annotator:

1. In the Weave project sidebar, click **Annotate**.
2. In the tab bar, click the **Queues** tab.
3. In the Annotation Queues table, click the name of your queue to open the queue items.
4. In the Queue header bar, click the link button to copy a direct link to this queue.  You can also copy the URL from the browser address bar.

<img src="https://mintcdn.com/wb-21fd5541/i_jfLHt7AV9D6HiI/weave/guides/tracking/imgs/AnnotationLinkToQueue.png?fit=max&auto=format&n=i_jfLHt7AV9D6HiI&q=85&s=2359b84131a5569c537d49d0a471fd2d" alt="Copy link to the annotation queue in the Annotation Queue header bar" width="1036" height="100" data-path="weave/guides/tracking/imgs/AnnotationLinkToQueue.png" />

In the Annotation Queues table, the **State** column indicates reviewing progress:

* **Not started**: Queue has items but no annotations have been submitted.
* **In progress**: At least one item has been reviewed.
* **Completed**: All items have been reviewed.

In the Annotation Queues table, the **Calls with responses** column indicates the percent of items (out of the total number of **Calls**) that have at least one submitted review.

## Filter and export annotations

Weave stores completed annotations as structured metadata on traces.

You can:

* Filter traces by queue assignment and annotation completion.
* Save filtered views for reuse.
* Export annotated traces to datasets for evaluation or training workflows.

This connects expert human feedback directly to model evaluation and iteration.

### Filter annotated traces

You can use the filter controls of the **Traces** page to display only traces with annotations.

To view only traces with annotations:

1. In the Weave project sidebar, click **Traces**.
2. In the Traces table toolbar, click **Filter**.
3. Add three values to a filter row:
   * For **Column**, type "Queue", then press **Enter**.
   * For the second list, choose **Text: "is"**.
   * For **Select a queue**, choose your annotation queue name.
4. To also filter on 'completed' queue items only, click **+ Add Filter**:
   * For **Column**, type "feedback".  A dialog will populate with Annotations and includes your Annotation Field names.  Choose a required Field from your queue.
   * For the second list, choose **Other: "is not empty"**.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/i_jfLHt7AV9D6HiI/weave/guides/tracking/imgs/AnnotationTracesFilter.png?fit=max&auto=format&n=i_jfLHt7AV9D6HiI&q=85&s=f30682ff2fdf01a1c2532ff39ecb9fd7" alt="Traces table configuring a filter to select traces belonging to specific annotation queue." width="1340" height="273" data-path="weave/guides/tracking/imgs/AnnotationTracesFilter.png" />
</Frame>

4. Filter rows are automatically applied; click elsewhere in the page for the filter entry to close.
5. (Optional) Save as a view for quick access. In the Traces table header, click **Save View**.

### Export annotated traces to datasets

You can export annotated traces either through the UI or programmatically, depending on how you plan to use the data.

#### Add annotated traces to a dataset

Select annotated traces and click **Add to Dataset** to include expert labels in your eval or training data.

To add annotated traces to a dataset:

1. In the Weave project sidebar, click **Traces**.
2. In the Traces table, select the traces that you want to export.
3. In the table toolbar, click **Add to dataset**. Follow the on-screen prompts to complete the addition.

To learn more about using datasets, see [Collect and track datasets](/weave/guides/core-types/datasets).

## Access annotations programmatically

If you want to integrate annotations programmatically, you must know your project name and queue ID:

* **Project**: The W\&B project name (can be project or team/project). If you don’t specify a W\&B team (such as "team/project"), your default team is used.
* **Queue ID**: The annotation queue's unique identifier.

To find the queue ID:

1. In the **Annotation Queues** table, select the name of the queue to open its items.
2. Copy the ID from the end of the page URL.

**Example**

```
https://wandb.ai/.../annotation-queues/019c0f63-7acb-7497-8f87-08873368fcd4
```

In this example, the queue ID is:

019c0f63-7acb-7497-8f87-08873368fcd4

You can iterate through the traces (calls) in your queue using the following code.

```python lines theme={null}
import weave
from weave.trace_server.trace_server_interface import AnnotationQueueItemsQueryReq

# Update project and queue identifiers to your own values.
PROJECT = "your-team-name/your-project-name"
QUEUE_ID = "019c0f63-7acb-7497-8f87-08873368fcd4"

# Initialize Weave.
client = weave.init(PROJECT)

# Get call IDs from calls in a queue.
calls = client.server.annotation_queue_items_query(
    AnnotationQueueItemsQueryReq(
        project_id=PROJECT,
        queue_id=QUEUE_ID,
    )
)

# Iterate through calls and get feedback.
for i, item in enumerate(calls.items):
    call = client.get_call(call_id=item.call_id, include_feedback=True)
    feedback = call.feedback or {}

    # Count total feedback items for call.
    total_feedback_items = len(feedback)

    print(f"\nItem {i} — call_id: {item.call_id} — total feedback items: {total_feedback_items}")

    if not feedback:
        print("No feedback for item")
        continue

    # Get the first annotation value. 
    # Field annotations are not added in repeatable order - thus the first field will vary.
    field_name = next(iter(feedback))
    field_value = feedback[0]

    print(f"  {field_name}: {field_value}")
```

The following Google Colab notebook provides an in-depth example of programmatically accessing annotation data and collecting an analytics report:

<div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
  <ColabLink url="https://colab.research.google.com/github/wandb/docs/blob/main/weave/cookbooks/source/weave_annotations_v2.ipynb" />

  <GitHubLink url="https://github.com/wandb/docs/blob/main/weave/cookbooks/source/weave_annotations_v2.ipynb" />
</div>

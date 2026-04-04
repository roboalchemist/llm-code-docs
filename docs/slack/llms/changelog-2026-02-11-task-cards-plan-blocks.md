Source: https://docs.slack.dev/changelog/2026/02/11/task-cards-plan-blocks

# Apps can now display thinking steps to users

February 11, 2026

Display your apps' and agents' actions with three new Block Kit components:

* The [`task_card`](/reference/block-kit/blocks/task-card-block) block displays a single task.
* The [`url source`](/reference/block-kit/block-elements/url-source-element) element displays clickable URL references within a task card.
* The [`plan`](/reference/block-kit/blocks/plan-block) block displays multiple of those tasks together in a unified view.

How tasks are displayed is set with a new parameter in the text-streaming API methods: `task_display_mode`. Use this to choose whether your app's tasks appear individually or in a comprehensive plan.

Then update the task cards and plan via the new `chunks` parameter. The parameter also supports plain markdown.

Ready to test it out? Check out our guide on [developing AI apps](/ai/developing-agents#streaming), or jump straight to the text-streaming methods' reference pages:

* [`chat.startStream`](/reference/methods/chat.startStream)
* [`chat.appendStream`](/reference/methods/chat.appendStream)
* [`chat.stopStream`](/reference/methods/chat.stopStream)

**Tags:**

* [New Feature](/changelog/tags/new-feature)
* [Block Kit](/changelog/tags/block-kit)

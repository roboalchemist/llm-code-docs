# Source: https://trigger.dev/docs/bulk-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Bulk actions

> Perform actions like replay and cancel on multiple runs at once.

Bulk actions allow you to perform replaying and canceling on multiple runs at once. This is especially useful when you need to retry a batch of failed runs with a new version of your code, or when you need to cancel multiple in-progress runs.

<video src="https://content.trigger.dev/bulk-actions.mp4" preload="auto" controls={true} loop muted autoPlay={true} width="100%" height="100%" />

## How to create a new bulk action

<Icon icon="circle-1" iconType="solid" color="#FF2D6B" size="20" /> Open the bulk action panel from the top right of the runs page

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/bulk-action-open-panel.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=e514c6b6e2c85aa8dc9bbb2cc6604f21" alt="Access bulk actions" width="964" height="603" data-path="images/bulk-action-open-panel.png" />

<Icon icon="circle-2" iconType="solid" color="#FF2D6B" size="20" /> Filter the runs table to show the runs you want to bulk action

<Icon icon="circle-3" iconType="solid" color="#FF2D6B" size="20" /> Alternatively, you can select individual runs

<Icon icon="circle-4" iconType="solid" color="#FF2D6B" size="20" /> Choose the runs you want to bulk action

<Icon icon="circle-5" iconType="solid" color="#FF2D6B" size="20" /> Name your bulk action (optional)

<Icon icon="circle-6" iconType="solid" color="#FF2D6B" size="20" /> Choose the action you want to perform, replay or cancel

<Icon icon="circle-7" iconType="solid" color="#FF2D6B" size="20" /> Click the "Replay" or "Cancel" button and confirm in the dialog

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/bulk-action-create.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=defba18d2817528b5cbbfbdac1b01552" alt="Access bulk actions" width="2259" height="1367" data-path="images/bulk-action-create.png" />

<Icon icon="circle-8" iconType="solid" color="#FF2D6B" size="20" /> You'll now view the bulk action processing from the bulk action page

<Icon icon="circle-9" iconType="solid" color="#FF2D6B" size="20" /> You can replay or view the runs from this page

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/bulk-action-page.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=a796b724494a8c0cce3883d2befc5b46" alt="Access bulk actions" width="2257" height="1361" data-path="images/bulk-action-page.png" />

<Note>
  You can only cancel runs that are in states that allow cancellation (like QUEUED or EXECUTING).
  Runs that are already completed, failed, or in other final states by the time the bulk action process gets to them, cannot be canceled.
</Note>


Built with [Mintlify](https://mintlify.com).
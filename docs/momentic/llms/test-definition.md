# Source: https://momentic.ai/docs/editor/test-definition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Test definition

> How to tell Momentic what to do

The test definition is the core of your Momentic test. It describes what actions
to perform, what elements to interact with, and how to verify the results. You
can write the test definition in natural language, and Momentic will convert it
into browser interactions at runtime.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/editor/definition.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=c96f689ad45209a392881a939e20c5f5" width="3630" height="2450" data-path="images/editor/definition.png" />
</Frame>

## Test actions

There is a toolbar at the top of the editor that provides various actions to
manage your test definition.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/editor/test-actions.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=a5d6edf7fc0f5366dd430ce96905a4c3" width="3620" height="2440" data-path="images/editor/test-actions.png" />
</Frame>

Here are the available actions:

* **Add new step**: Create a new step in your test definition.
* **Record**: Start recording a new test definition. This will open the browser
  in recording mode, allowing you to interact with the app and automatically
  generate steps based on your actions.
* **Create module**: Create a reusable module from selection of steps. This
  allows you to share logic across multiple tests.
* **Run from start**: Execute the test definition from the beginning. This will
  reset the browser and run all steps in order.

## Step actions

If you hover over each step, you will see action buttons that allow you to
execute, edit, delete, or move the step.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/editor/action-buttons.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=e4a27a037be6c17f310e257020ff1fd0" width="3626" height="2446" data-path="images/editor/action-buttons.png" />
</Frame>

Here are the available actions (from left to right):

* **Run**: Execute the step immediately.
* **Run to**: Execute the step and all previous steps.
* **Run from**: Execute the step and all subsequent steps.
* **Edit**: Modify the step's content.
* **Duplicate**: Create a copy of the step.
* **Move up**: Move the step one position up in the list.
* **Move to top**: Move the step to the top of the list.
* **Move down**: Move the step one position down in the list.
* **Move to bottom**: Move the step to the bottom of the list.
* **Add before**: Insert a new step before the current one.
* **Add after**: Insert a new step after the current one.
* **Delete**: Remove the step from the test definition.

## Editing steps

You can edit a step by clicking on the **Edit** button. This will open a text
editor where you can modify the step's content. Hover over labels to see
tooltips with more information about each option.

<Frame>
  <img src="https://mintcdn.com/momentic-docs/N47HcAM-4dLVFPuL/images/editor/edit-step.png?fit=max&auto=format&n=N47HcAM-4dLVFPuL&q=85&s=fc9092e851f9491af69342c50939e840" width="3626" height="2450" data-path="images/editor/edit-step.png" />
</Frame>

## Keyboard shortcuts

<Info>All `Cmd` keys can be replaced with `Ctrl` on Windows.</Info>

| Shortcut                       | Action                         |
| ------------------------------ | ------------------------------ |
| <kbd>Cmd + Enter</kbd>         | Save the currents step         |
| <kbd>Cmd + Shift + Enter</kbd> | Save and run the currents step |
| <kbd>Esc</kbd>                 | Discard edits                  |


Built with [Mintlify](https://mintlify.com).
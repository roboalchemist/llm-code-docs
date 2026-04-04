Source: https://docs.slack.dev/changelog/2020/09/01/full-state-on-view-submisson-and-block-actions

# A full state on view submission and block actions

September 1, 2020

If you rely or want to rely on stateful Block Kit views, we have some exciting news for you. The payloads for [`view_submission`](/reference/interaction-payloads/view-interactions-payload#view_submission) and [`block_actions`](/reference/interaction-payloads/block_actions-payload) will have some new additions. Read on to learn more.

## What's changing {#changed}

### Changes to view_submission payloads {#changes-to-view_submission-payloads}

Previously, when your app received a `view_submission` payload, the `state` value would only contain the state of any input blocks in the view. This meant that you were missing the state of any stateful elements in _other_ interactive blocks from that view.

From September 29, 2020, `view_submission` and `block_action` payloads will include a full `state` property that will include all stateful elements, not just input blocks.

Below is a sample payload from a modal with a `multi_conversations_select` element in a section block and a `plain_text_input` element in an input block:

```json
{ "state": {  "values": {   "section_block_id": {    "multi_convos": {     "type": "multi_conversations_select",     "selected_conversations": ["G12345"]    }   },   "input_block_id": {    "plain_text_action_id": {     "type": "plain_text_input",     "value": "test123"    }   }  } }}
```text

You'll notice how the `multi_conversations_select` is present now, even though it’s in a section block.

### Changes to block_actions payloads {#changes-to-block_actions-payloads}

We will also include the `state` field in all `block_actions` payloads. You will no longer need to wait for a `view_submission` to see the full state of your modals, messages, or App Home tabs.

In the example below, this sample payload will be sent when a user selects a conversation, firing a `block_actions` call:

```json
{ "actions": [  {   "type": "multi_conversations_select",   "action_id": "multi_convos",   "block_id": "test123",   "selected_conversations": ["G12345"]  } ], "container": {  "type": "view",  "view_id": "V12345" }, "state": {  "values": {   "section_block_id": {    "multi_convos": {     "type": "multi_conversations_select",     "selected_conversations": ["G12345"]    }   },   "other_block_id": {    "other_action_id": {     "type": "plain_text_input",     "value": "test123"    }   }  } }}
```text

### Changes to empty state in all payloads {#changes-to-empty-state-in-all-payloads}

We’ll send `null` as the value when users have deselected or deleted their entry in an input or action block.

`multi_select` elements and `checkboxes` are exceptions—if you deselect everything in those elements, we send it as `[]` — an empty array.

You will see these changes in `view_submission` and `block_actions` payloads.

In this example, this sample payload will be sent if a user submits a form without selecting any conversations or entering any text:

```json
{ "state": {  "values": {   "section_block_id": {    "multi_convos": {     "type": "multi_conversations_select",     "selected_conversations": []    }   },   "other_block_id": {    "other_action_id": {     "type": "plain_text_input",     "value": null    }   }  } }}
```text

Notice the explicit `null` and empty `[]` array.

## How to prepare {#prepare}

We don't anticipate this change to break any existing apps—however you should still prepare your app for the addition of the state field in `view_submission` and `block_actions` payloads.

Note: It's safe to rely on `state` for all inputs now, especially if you've used `private_metadata` as a stand-in for maintaining their state.

## What happens if I do nothing? {#happens}

Since this change is additive it should be backwards-compatible, because it's not changing the existing structure of the payload. If your app assumes `state` will only be included in user-modified input blocks, you may want to verify how your app will respond to these changes.

## When is this happening? {#when}

The updated payloads mentioned above will be sent to apps from September 29, 2020.

## Tags:

* [New feature](/changelog/tags/new-feature)

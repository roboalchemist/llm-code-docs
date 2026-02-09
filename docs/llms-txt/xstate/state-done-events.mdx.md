# Source: https://stately.ai/docs/state-done-events.mdx

# State done events (/docs/state-done-events)
AÂ **state done event**Â transitions from a parent state when one of its child states reaches its final state. State done events are labeled âonDone.â

State done events are useful when you want to:

* Model sequential flows where one process must complete before moving to the next
* Coordinate between parent and child states in a hierarchical state machine
* Handle cleanup or transition logic after a subprocess completes
* Automatically transition to a new state when all child states are complete

For example, in a coffee machine, you might use an `onDone` event to transition from the "preparation" state to "brewing" only after all preparation steps (grinding beans, heating water, etc.) are complete. This ensures proper sequencing of operations.

State done events also help maintain separation of concerns by allowing child states to focus on their specific tasks while the parent state handles the overall flow coordination.

<Callout>
  Watch our [âWhat are state done events?â video on YouTube](https://www.youtube.com/watch?v=3laC3gWBLnM\&list=PLvWgkXBB3dd4I_l-djWVU2UGPyBgKfnTQ\&index=11) (1m16s).
</Callout>

In the video player above, when the video player reaches theÂ *Stopped*Â state, theÂ *Opened*Â state transitions through theÂ *onDone*Â state done event to theÂ *Closed*Â state.

## How to add a state done event to a parent state

1. Check the final child state has its state type set toÂ **Final**. If the parent state doesnât contain a final child state, the state done event type will not be available for transitions from the parent state.
2. Select the parent state.
3. Drag from the handles on the left, right and bottom sides of the selected state, and release to create a connecting transition, event and new state.
4. Select the newly-created event. Thenâ¦

### Using theÂ **quick actions**Â menu

1. Right-click the state to open theÂ **quick actions**Â menu.
2. ChooseÂ **State done event**Â from theÂ **Event type**Â options.

### Using theÂ **Transition details**Â panel

1. Open theÂ **Transition details**Â panel from the right tool menu.
2. ChooseÂ **State done event**Â from theÂ **Event type**Â dropdown menu.

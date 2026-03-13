# Source: https://uat.rive.app/docs/scripting/api-reference/interfaces/transition-condition.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# TransitionCondition

A condition to evaluate for a transition between state machine states to be taken.

For more information, see [Transition Condition Scripts](/scripting/protocols/transition-condition-scripts).

## Methods

### `init`

Called once when the transition condition is created or attached.

```lua highlight={4,5,6,14} theme={null}
type MyTransitionCondition = {}

-- Called once when the script initializes.
function init(self: MyTransitionCondition, context: Context): boolean
  return true
end

function evaluate(self: MyTransitionCondition): boolean
  return false
end

return function(): TransitionCondition<MyTransitionCondition>
  return {
    init = init,
    evaluate = evaluate,
  }
end
```

### `evaluate`

Called every frame while the transition is active.

```lua highlight={4,5,6,14} theme={null}
type MyTransitionCondition = {10,11,12,17}

function init(self: MyTransitionCondition, context: Context): boolean
  return true
end

-- Add your transition logic here.
-- `evaluate` is fired every frame while the transition is active.
-- Returning false prevents a transition, true allows a transition.
function evaluate(self: MyTransitionCondition): boolean
  return false
end

return function(): TransitionCondition<MyTransitionCondition>
  return {
    init = init,
    evaluate = evaluate,
  }
end
```

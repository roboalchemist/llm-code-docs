# Source: https://uat.rive.app/docs/scripting/protocols/transition-condition-scripts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Transition Condition Scripts

> Create custom state machine transitions using scripts

[Conditions](/editor/state-machine/transitions#conditions) are the rules that determine when the State Machine transitions from one state to another. Transition Condition Scripts let you define custom conditions when built-in comparisons aren’t enough—such as transitions that depend on complex logic or multiple view model properties evaluated together.

## Creating a Transition Condition Script

[Create a new script](/scripting/creating-scripts) and select **Transition Condition Script** as the type.

## Anatomy of a Transition Condition

```lua  theme={null}
type MyTransitionCondition = {
  context: Context,
}

-- Called once when the script initializes.
function init(self: MyTransitionCondition, context: Context): boolean
  -- Context gives you access to your main view model and other data.
  self.context = context

  return true
end

-- Add your transition logic here.
-- `evaluate` is fired every frame while the transition is active.
-- Returning false prevents a transition, true allows a transition.
function evaluate(self: MyTransitionCondition): boolean
  return false
end

-- Return a factory function that Rive uses to build the Transition Condition instance.
return function(): TransitionCondition<MyTransitionCondition>
  return {
    init = init,
    evaluate = evaluate,
    context = late(),
  }
end
```

<Note>
  `evaluate` runs every frame while the transition is active.

  It should be fast and side-effect free, and only return whether the transition is allowed.
</Note>

## Adding your Transition Condition

<Steps>
  <Step title="Select a Transition" />

  <Step title="Click + to add a new Condition" />

  <Step title="Select your Script" />
</Steps>

<img src="https://mintcdn.com/rive/JjU0q55-K2f1gZny/images/scripting/add-transition-condition.gif?s=e4d72b842a1076948b2429c65f84faf2" alt="Add a custom transition" width="480" height="169" data-path="images/scripting/add-transition-condition.gif" />

## Script Inputs

Inputs let you add parameters a transition without changing script logic—making the same condition reusable across different transitions or states. For more information on adding inputs to your scripts, see [Script Inputs](/scripting/script-inputs).

<Note>
  Inputs can control scripts, but scripts can't change the value of inputs.

  If you need to control a view model property from your script, access the [Main View model through context](/scripting/data-binding#accessing-the-main-view-model) or [View Model Inputs](/scripting/script-inputs#view-model-inputs).
</Note>

### Setting an Input

To set the value of an input, select the Properties icon next to the transition.

<img src="https://mintcdn.com/rive/I7V7AMXE2CuuPyMc/images/scripting/transition-condition-input.png?fit=max&auto=format&n=I7V7AMXE2CuuPyMc&q=85&s=f5b3028a2c126c9a828cc548d71122a3" alt="transition script inputs" width="850" height="295" data-path="images/scripting/transition-condition-input.png" />

### Data Binding an Input

Right-click your property and select Data Bind to bind your input to a view model property.

<img src="https://mintcdn.com/rive/I7V7AMXE2CuuPyMc/images/scripting/transition-condition-input-binding.png?fit=max&auto=format&n=I7V7AMXE2CuuPyMc&q=85&s=047fe0158fbc5f7070d4123ad39a50a6" alt="data binding transition script inputs" width="847" height="300" data-path="images/scripting/transition-condition-input-binding.png" />

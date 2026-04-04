# Source: https://uat.rive.app/docs/scripting/protocols/listener-action-scripts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Listener Action Scripts

> Run custom logic when a state machine listener fires

[Listeners](/editor/state-machine/listeners) fire when a specific event occurs in a State Machine.
Listener Action Scripts let you run custom logic in response to those events.

Use Listener Action Scripts when you need to perform side effects—such as updating view model values, responding to pointer input, or triggering external behavior—without changing state.

## Creating a Listener Action Script

[Create a new script](/scripting/creating-scripts) and select **Listener Action Script** as the type.

## Anatomy of a Listener Action

```lua  theme={null}
type MyListenerAction = {
  context: Context,
}

-- Called once when the script initializes.
function init(self: MyListenerAction, context: Context): boolean
  -- Context gives you access to your main view model and other data.
  self.context = context
  return true
end

-- Called when the Listener fires.
-- Use this to perform side effects (no return value).
function perform(self: MyListenerAction, pointerEvent: PointerEvent)

end

-- Return a factory function that Rive uses to build the Listener Action instance.
return function(): ListenerAction<MyListenerAction>
  return {
    init = init,
    perform = perform,
    context = late(),
  }
end

```

## Adding your Listener Action

<Steps>
  <Step title="Select a Listener" />

  <Step title="Click + and select Scripted Action" />

  <Step title="From the Run dropdown, select your script" />
</Steps>

<img src="https://mintcdn.com/rive/c6Shdr6bTbiqaAny/images/scripting/add-listener-action.gif?s=072cbfbb2c2681d30edc891ca8ed46b9" alt="Add a custom listener action" width="480" height="120" data-path="images/scripting/add-listener-action.gif" />

## Script Inputs

Inputs let you add parameters to a listener action without changing script logic—making the same script reusable across different listeners. For more information on adding inputs to your scripts, see [Script Inputs](/scripting/script-inputs).

<Note>
  Inputs can control scripts, but scripts can't change the value of inputs.

  If you need to control a view model property from your script, access the [Main View model through context](/scripting/data-binding#accessing-the-main-view-model) or [View Model Inputs](/scripting/script-inputs#view-model-inputs).
</Note>

### Setting an Input

To set the value of an input, select the Properties icon next to the listener script.

<img src="https://mintcdn.com/rive/G2J2SST696k_ww2Y/images/scripting/listener-action-script-input.png?fit=max&auto=format&n=G2J2SST696k_ww2Y&q=85&s=bf62790188304ae9e34a197422daa0d1" alt="listener action script inputs" width="2362" height="604" data-path="images/scripting/listener-action-script-input.png" />

### Data Binding an Input

Right-click your property and select Data Bind to bind your input to a view model property.

<img src="https://mintcdn.com/rive/G2J2SST696k_ww2Y/images/scripting/listener-action-script-input-binding.png?fit=max&auto=format&n=G2J2SST696k_ww2Y&q=85&s=b1478ea2796ad18a565659288986e0ad" alt="listener action script inputs" width="2370" height="608" data-path="images/scripting/listener-action-script-input-binding.png" />

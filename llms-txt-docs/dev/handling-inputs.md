# Source: https://dev.writer.com/framework/handling-inputs.md

# Handling inputs

There are two, complementary, ways to handle inputs in Framework: via event handlers and via binding.

## Event handlers

Input components have *change* events that are dispatched when the value changes. The new value is provided as a payload in the event handler. Change events have slightly different names across components, reflecting the payloads they provide. For example, *Number Input* and *Slider Input* use the event `wf-number-change` while *Text Input* and *Text Area Input* use the generic `wf-change`.

As discussed in the [Event handlers](/framework/event-handlers) section, the payload can be accessed via the `payload` argument in the event handler.

```py  theme={null}
# This event handler takes the payload and assigns it
# to the state element "name"
def handle_input_change(state, payload):
    state["name"] = payload
```

## Two-way bindings

Writing event handlers for every input component can be tedious. In most cases, you'll only need to update a single element of state when the value changes, akin to the example above. You can achieve this by binding a component to a state element.

Bindings automatically handle the *change* event for the component and set the value of the state element to the payload. Furthermore, bindings are two-way. If the state element is updated from the back-end, the front-end component is updated to reflect the new value.

As mentioned in the [Builder basics](/framework/builder-basics) section of the guide, bindings can be configured in the component settings.

<img src="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/handling-inputs.binding.png?fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=bcb3fe9fc8d61fe1f7302f98a35b4099" alt="Repeater example" data-og-width="1704" width="1704" data-og-height="479" height="479" data-path="framework/images/handling-inputs.binding.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/handling-inputs.binding.png?w=280&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=30286a1280fbb6857684e8b7df39ea4b 280w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/handling-inputs.binding.png?w=560&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=5fcd4e09500b5f515e3da035d56ecb30 560w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/handling-inputs.binding.png?w=840&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=07d449ad6f6684fc6a8bfb345cddf328 840w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/handling-inputs.binding.png?w=1100&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=4a01e06896f46ab476c478efbc93197c 1100w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/handling-inputs.binding.png?w=1650&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=7d36df5998e1d3b122f16f1f1082c26d 1650w, https://mintcdn.com/writer/eBiCs3I5_-mSTcT-/framework/images/handling-inputs.binding.png?w=2500&fit=max&auto=format&n=eBiCs3I5_-mSTcT-&q=85&s=9e78b799744a7e6f3d51982eb132fedb 2500w" />

The binding above establishes a two-way link between the component and the state element `name`. If `name` changes in the back-end, the component changes. If the component changes, the value of `name` changes.

## Using events and bindings simultaneously

Bindings can be used together with events. This is useful for triggering recalculations or applying dynamic filters. For example, you may want to have three *Number Input* components bound to `a`, `b` and `c` and display a value `n`. This easily done by binding the components and linking the same recalculation event handler to all three components.

```py  theme={null}
def recalculate(state):
    state["n"] = state["a"]*state["b"]*state["c"]
```

## Handling inputs safely

Framework automatically sanitises the payloads it provides for its built-in events, those that start with `wf-`.

For example, if a *Dropdown Input* component lists options `high` and `low`, you're guaranteed you won't get a value like `"Robert'); DROP TABLE students;--"` when handling `wf-option-change`. You'll get `"high"`, `"low"` or `None`.

<Warning>
  Inputs are sanitised, but you should still be careful

  As with any application, it's important to be familiar with the risks associated with handling user input, especially SQL injections. If you're using any custom HTML and mixing it with user generated content, make sure you understand XSS.
</Warning>

## Creating forms

Input components can be combined with *Message* and *Button* components to create forms with messages, indicating whether the submission was successful.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/handling-inputs.form.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=d60aee2c6edda91f55808ee2d678c288" alt="Form example" data-og-width="1704" width="1704" data-og-height="762" height="762" data-path="framework/images/handling-inputs.form.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/handling-inputs.form.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=64e26040ef3e8d68b4637bd5fea22701 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/handling-inputs.form.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b88b74e0aaaafaa15bcb9badf0a36259 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/handling-inputs.form.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=394e066d339f3c59aa6b3f9d8aba1a39 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/handling-inputs.form.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=fa7381a45e5660ce96e304161feeddcf 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/handling-inputs.form.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=be882a73798bc6b47612e77b06e08086 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/handling-inputs.form.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b5e3d32164e295da0c49afcd40e4b927 2500w" />

# Source: https://reactnative.dev/docs/the-new-architecture/direct-manipulation-new-architecture.md

# Direct Manipulation

It is sometimes necessary to make changes directly to a component without using state/props to trigger a re-render of the entire subtree. When using React in the browser for example, you sometimes need to directly modify a DOM node, and the same is true for views in mobile apps. `setNativeProps` is the React Native equivalent to setting properties directly on a DOM node.

caution

Use `setNativeProps` when frequent re-rendering creates a performance bottleneck!

Direct manipulation will not be a tool that you reach for frequently. You will typically only be using it for creating continuous animations to avoid the overhead of rendering the component hierarchy and reconciling many views. `setNativeProps` is imperative and stores state in the native layer (DOM, UIView, etc.) and not within your React components, which makes your code more difficult to reason about.

Before you use it, try to solve your problem with `setState` and [`shouldComponentUpdate`](https://react.dev/reference/react/Component#shouldcomponentupdate).

## setNativeProps to edit TextInput value[​](#setnativeprops-to-edit-textinput-value "Direct link to setNativeProps to edit TextInput value")

Another very common use case of `setNativeProps` is to edit the value of the TextInput. The `controlled` prop of TextInput can sometimes drop characters when the `bufferDelay` is low and the user types very quickly. Some developers prefer to skip this prop entirely and instead use `setNativeProps` to directly manipulate the TextInput value when necessary.

For example, the following code demonstrates editing the input when you tap a button:

* TypeScript
* JavaScript

You can use the [`clear`](/docs/textinput.md#clear) method to clear the `TextInput` which clears the current input text using the same approach.

## Avoiding conflicts with the render function[​](#avoiding-conflicts-with-the-render-function "Direct link to Avoiding conflicts with the render function")

If you update a property that is also managed by the render function, you might end up with some unpredictable and confusing bugs because anytime the component re-renders and that property changes, whatever value was previously set from `setNativeProps` will be completely ignored and overridden.

# Source: https://reactnative.dev/docs/handling-text-input.md

# Handling Text Input

[`TextInput`](/docs/textinput.md#content) is a [Core Component](/docs/intro-react-native-components.md) that allows the user to enter text. It has an `onChangeText` prop that takes a function to be called every time the text changed, and an `onSubmitEditing` prop that takes a function to be called when the text is submitted.

For example, let's say that as the user types, you're translating their words into a different language. In this new language, every single word is written the same way: 🍕. So the sentence "Hello there Bob" would be translated as "🍕 🍕 🍕".

In this example, we store `text` in the state, because it changes over time.

There are a lot more things you might want to do with a text input. For example, you could validate the text inside while the user types. For more detailed examples, see the [React docs on controlled components](https://react.dev/reference/react-dom/components/input#controlling-an-input-with-a-state-variable), or the [reference docs for TextInput](/docs/textinput.md).

A `TextInput` is one of many ways for the user to interact with your app. For examples of other ways to handle input, see the documentation on [how to handle touches](/docs/handling-touches.md).

Now, let's take a look at [ScrollView](/docs/using-a-scrollview.md), another Core Component.

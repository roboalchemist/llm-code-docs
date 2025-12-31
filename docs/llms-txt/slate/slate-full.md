# Slate Documentation

Source: https://docs.slatejs.org/llms-full.txt

---

# Introduction

[Slate](http://slatejs.org) is a *completely* customizable framework for building rich text editors.

Slate lets you build rich, intuitive editors like those in [Medium](https://medium.com/), [Dropbox Paper](https://www.dropbox.com/paper) or [Google Docs](https://www.google.com/docs/about/)—which are becoming table stakes for applications on the web—without your codebase getting mired in complexity.

It can do this because all of its logic is implemented with a series of plugins, so you aren't ever constrained by what *is* or *isn't* in "core". You can think of it like a pluggable implementation of `contenteditable` built on top of [React](https://facebook.github.io/react/) and [Immutable](https://immutable-js.github.io/immutable-js/). It was inspired by libraries like [Draft.js](https://facebook.github.io/draft-js/), [Prosemirror](http://prosemirror.net/) and [Quill](http://quilljs.com/).

> 🤖 **Slate is currently in beta**. Its core API is usable now, but you might need to pull request fixes for advanced use cases. Some of its APIs are not "finalized" and will (breaking) change over time as we find better solutions.

## Why?

Why create Slate? Well... *(Beware: this section has a few of* [*my*](https://github.com/ianstormtaylor) *opinions!)*

Before creating Slate, I tried a lot of the other rich text libraries out there—[**Draft.js**](https://facebook.github.io/draft-js/), [**Prosemirror**](http://prosemirror.net/), [**Quill**](http://quilljs.com/), etc. What I found was that while getting simple examples to work was easy enough, once you started trying to build something like [Medium](https://medium.com/), [Dropbox Paper](https://www.dropbox.com/paper) or [Google Docs](https://www.google.com/docs/about/), you ran into deeper issues...

* **The editor's "schema" was hardcoded and hard to customize.** Things like bold and italic were supported out of the box, but what about comments, or embeds, or even more domain-specific needs?
* **Transforming the documents programmatically was very convoluted.** Writing as a user may have worked, but making programmatic changes, which is critical for building advanced behaviors, was needlessly complex.
* **Serializing to HTML, Markdown, etc. seemed like an afterthought.** Simple things like transforming a document to HTML or Markdown involved writing lots of boilerplate code, for what seemed like very common use cases.
* **Re-inventing the view layer seemed inefficient and limiting.** Most editors rolled their own views, instead of using existing technologies like React, so you had to learn a whole new system with new "gotchas".
* **Collaborative editing wasn't designed for in advance.** Often the editor's internal representation of data made it impossible to use it for a realtime, collaborative editing use case without basically rewriting the editor.
* **The repositories were monolithic, not small and reusable.** The code bases for many of the editors often didn't expose the internal tooling that could have been re-used by developers, leading to having to reinvent the wheel.
* **Building complex, nested documents was impossible.** Many editors were designed around simplistic "flat" documents, making things like tables, embeds and captions difficult to reason about and sometimes impossible.

Of course not every editor exhibits all of these issues, but if you've tried using another editor you might have run into similar problems. To get around the limitations of their APIs and achieve the user experience you're after, you have to resort to very hacky things. And some experiences are just plain impossible to achieve.

If that sounds familiar, you might like Slate.

Which brings me to how Slate solves all of that...

## Principles

Slate tries to solve the question of "[Why?](#why)" with a few principles:

1. **First-class plugins.** The most important part of Slate is that plugins are first-class entities—the core editor logic is even implemented as its own plugin. That means you can *completely* customize the editing experience, to build complex editors like Medium's or Dropbox's, without having to fight against the library's assumptions.
2. **Schema-less core.** Slate's core logic doesn't assume anything about the schema of the data you'll be editing, which means that there are no assumptions baked into the library that'll trip you up when you need to go beyond the most basic use cases.
3. **Nested document model.** The document model used for Slate is a nested, recursive tree, just like the DOM itself. This means that creating complex components like tables or nested block quotes are possible for advanced use cases. But it's also easy to keep it simple by only using a single level of hierarchy.
4. **Parallel to the DOM.** Slate's data model is based on the DOM—the document is a nested tree, it uses selections and ranges, and it exposes all the standard event handlers. This means that advanced behaviors like tables or nested block quotes are possible. Pretty much anything you can do in the DOM, you can do in Slate.
5. **Stateless views and immutable data.** By using React and Immutable.js, the Slate editor is built in a stateless fashion using immutable data structures, which leads to much easier to reason about code, and a much easier time writing plugins.
6. **Intuitive changes.** Slate documents are edited using "changes", that are designed to be high-level and extremely intuitive to write and read, so that custom functionality is as expressive as possible. This greatly increases your ability to reason about your code.
7. **Collaboration-ready data model.** The data model Slate uses—specifically how changes are applied to the document—has been designed to allow for collaborative editing to be layered on top, so you won't need to rethink everything if you decide to make your editor collaborative.
8. **Clear "core" boundaries.** With a plugin-first architecture, and a schema-less core, it becomes a lot clearer where the boundary is between "core" and "custom", which means that the core experience doesn't get bogged down in edge cases.

## Demo

Check out the [**live demo**](http://slatejs.org) of all of the examples!

## Examples

To get a sense for how you might use Slate, check out a few of the examples:

* [**Plain text**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/plain-text) — showing the most basic case: a glorified `<textarea>`.
* [**Rich text**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/rich-text) — showing the features you'd expect from a basic editor.
* [**Auto-markdown**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/markdown-preview) — showing how to add key handlers for Markdown-like shortcuts.
* [**Links**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/links) — showing how wrap text in inline nodes with associated data.
* [**Images**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/images) — showing how to use void (text-less) nodes to add images.
* [**Hovering menu**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/hovering-menu) — showing how a contextual hovering menu can be implemented.
* [**Tables**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/tables) — showing how to nest blocks to render more advanced components.
* [**Paste HTML**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/paste-html) — showing how to use an HTML serializer to handle pasted HTML.
* [**Code Highlighting**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples/code-highlighting) — showing how to use decorations to dynamically mark text.
* [**See all the examples...**](https://github.com/ianstormtaylor/slate/tree/v0.47/examples)

If you have an idea for an example that shows a common use case, pull request it!

## Plugins

Slate encourages you to write small, reusable modules. Check out the public ones you can use in your project!

* [`slate-auto-replace`](https://github.com/ianstormtaylor/slate-auto-replace) auto-replaces text as the user types. Useful for "smart" typography!
* [`slate-collapse-on-escape`](https://github.com/ianstormtaylor/slate-collapse-on-escape) simply collapses the selection when `escape` is pressed.
* [`slate-paste-linkify`](https://github.com/ianstormtaylor/slate-paste-linkify) wraps the selected text in a link when a URL is pasted from the clipboard.
* [`slate-soft-break`](https://github.com/ianstormtaylor/slate-soft-break) adds a soft break when `enter` is pressed.
* [`slate-drop-or-paste-images`](https://github.com/ianstormtaylor/slate-drop-or-paste-images) lets users drop or paste images to insert them!
* [**View all plugins...**](https://docs.slatejs.org/general/plugins)

## Documentation

If you're using Slate for the first time, check out the [Getting Started](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/walkthroughs/installing-slate/README.md) walkthroughs and the [Guides](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/guides/README.md) to familiarize yourself with Slate's architecture and mental models. Once you've gotten familiar with those, you'll probably want to check out the full [API Reference](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/slate-core/README.md).

* [**Walkthroughs**](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/walkthroughs/README.md)
* [**Guides**](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/guides/README.md)
* [**Reference**](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/slate-core/README.md)
* [**FAQ**](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/general/faq/README.md)
* [**Resources**](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/general/resources/README.md)

If even that's not enough, you can always [read the source itself](https://github.com/ianstormtaylor/slate/tree/v0.47/packages/slate), which is heavily commented.

There are also translations of the documentation into other languages:

* [中文](https://doodlewind.github.io/slate-doc-cn/)

If you're maintaining a translation, feel free to pull request it here!

## Contributing!

All contributions are super welcome! Check out the [Contributing instructions](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/docs/general/contributing/README.md) for more info!

Slate is [MIT-licensed](https://github.com/ianstormtaylor/slate/blob/v0.47/License.md).


# Installing Slate

Slate is a monorepo divided up into multi npm packages, so to install it you do:

```
npm install slate slate-react
```

You'll also need to be sure to install Slate's peer dependencies:

```
npm install react react-dom immutable
```

*Note, if you'd rather use a pre-bundled version of Slate, you can `npm install slate` and retrieve the bundled `dist/slate.js` file! Check out the* [*Using the Bundled Source*](https://github.com/ianstormtaylor/slate/tree/a0b7976cb9a2812d8d96361e9993fe8853a2cc64/docs/walkthroughs/using-the-bundled-source.md) *guide for more information.*

Once you've installed Slate, you'll need to import it.

Slate exposes a set of modules that you'll use to build your editor. The most important of which is an `Editor` component.

```javascript
// Import the Slate editor.
import { Editor } from 'slate-react'
```

In addition to rendering the editor, you need to give Slate a "initial value" to render as content. We'll use the `Value` model that ships with Slate to create a new initial value that just contains a single paragraph block with some text in it:

```javascript
// Import the `Value` model.
import { Editor } from 'slate-react'
import { Value } from 'slate'

// Create our initial value...
const initialValue = Value.fromJSON({
  document: {
    nodes: [
      {
        object: 'block',
        type: 'paragraph',
        nodes: [
          {
            object: 'text',
            text: 'A line of text in a paragraph.',
          },
        ],
      },
    ],
  },
})
```

And now that we've created our initial value, we define our `App` and pass it into Slate's `Editor` component, like so:

```javascript
// Import React!
import React from 'react'
import { Editor } from 'slate-react'
import { Value } from 'slate'

const initialValue = Value.fromJSON({
  document: {
    nodes: [
      {
        object: 'block',
        type: 'paragraph',
        nodes: [
          {
            object: 'text',
            text: 'A line of text in a paragraph.',
          },
        ],
      },
    ],
  },
})

// Define our app...
class App extends React.Component {
  // Set the initial value when the app is first constructed.
  state = {
    value: initialValue,
  }

  // On change, update the app's React state with the new editor value.
  onChange = ({ value }) => {
    this.setState({ value })
  }

  // Render the editor.
  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

You'll notice that the `onChange` handler passed into the `Editor` component just updates the app's state with the newest changed value. That way, when it re-renders the editor, the new value is reflected with your changes.

And that's it!

That's the most basic example of Slate. If you render that onto the page, you should see a paragraph with the text `A line of text in a paragraph.`. And when you type, you should see the text change!

**Next:**\
[Adding Event Handlers](https://docs.slatejs.org/walkthroughs/adding-event-handlers) <br>


# Adding Event Handlers

**Previous:**\
[Installing Slate](https://docs.slatejs.org/walkthroughs/installing-slate) <br>

## Adding Event Handlers

Okay, so you've got Slate installed and rendered on the page, and when you type in it, you can see the changes reflected. But you want to do more than just type a plaintext string.

What makes Slate great is how easy it is to customize. Just like other React components you're used to, Slate allows you to pass in handlers that are triggered on certain events. You've already seen how the `onChange` handler can be used to store the changed editor value, but let's try adding more...

Let's use the `onKeyDown` handler to change the editor's content when we press a key.

Here's our app from earlier:

```javascript
class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

Now we add an `onKeyDown` handler:

```javascript
class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  // Define a new handler which prints the key that was pressed.
  onKeyDown = (event, editor, next) => {
    console.log(event.key)
    return next()
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
      />
    )
  }
}
```

Cool, now when a key is pressed in the editor, its corresponding keycode is logged in the console.

Now we want to make it actually change the content. For the purposes of our example, let's implement turning all ampersand, `&`, keystrokes into the word `and` upon being typed.

Our `onKeyDown` handler might look like this:

```javascript
class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    // Return with no changes if the keypress is not '&'
    if (event.key !== '&') return next()

    // Prevent the ampersand character from being inserted.
    event.preventDefault()

    // Change the value by inserting 'and' at the cursor's position.
    editor.insertText('and')
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
      />
    )
  }
}
```

With that added, try typing `&`, and you should see it suddenly become `and` instead!

This offers a sense of what can be done with Slate's event handlers. Each one will be called with the `event` object, and the `editor` that lets you perform commands. Simple!

**Next:**\
[Defining Custom Block Nodes](https://docs.slatejs.org/walkthroughs/defining-custom-block-nodes) <br>


# Defining Custom Block Nodes

**Previous:**\
[Adding Event Handlers](https://docs.slatejs.org/walkthroughs/adding-event-handlers) <br>

## Defining Custom Block Nodes

In our previous example, we started with a paragraph, but we never actually told Slate anything about the `paragraph` block type. We just let it use its internal default renderer, which uses a plain old `<div>`.

But that's not all you can do. Slate lets you define any type of custom blocks you want, like block quotes, code blocks, list items, etc.

We'll show you how. Let's start with our app from earlier:

```javascript
class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    if (event.key != '&') return next()
    event.preventDefault()
    editor.insertText('and')
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
      />
    )
  }
}
```

Now let's add "code blocks" to our editor.

The problem is, code blocks won't just be rendered as a plain paragraph, they'll need to be rendered differently. To make that happen, we need to define a "renderer" for `code` nodes.

Node renderers are just simple React components, like so:

```javascript
// Define a React component renderer for our code blocks.
function CodeNode(props) {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}
```

Pretty simple.

See the `props.attributes` reference? Slate passes attributes that should be rendered on the top-most element of your blocks, so that you don't have to build them up yourself. You **must** mix the attributes into your component.

And see that `props.children` reference? Slate will automatically render all of the children of a block for you, and then pass them to you just like any other React component would, via `props.children`. That way you don't have to muck around with rendering the proper text nodes or anything like that. You **must** render the children as the lowest leaf in your component.

Now, let's add that renderer to our `Editor`:

```javascript
function CodeNode(props) {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    if (event.key != '&') return next()
    event.preventDefault()
    editor.insertText('and')
  }

  render() {
    return (
      // Pass in the `renderBlock` prop...
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
        renderBlock={this.renderBlock}
      />
    )
  }

  // Add a `renderBlock` method to render a `CodeNode` for code blocks.
  renderBlock = (props, editor, next) => {
    switch (props.node.type) {
      case 'code':
        return <CodeNode {...props} />
      default:
        return next()
    }
  }
}
```

Okay, but now we'll need a way for the user to actually turn a block into a code block. So let's change our `onKeyDown` function to add a \`control-\`\` shortcut that does just that:

```javascript
function CodeNode(props) {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    // Return with no changes if it's not the "`" key with ctrl pressed.
    if (event.key != '`' || !event.ctrlKey) return next()

    // Prevent the "`" from being inserted by default.
    event.preventDefault()

    // Otherwise, set the currently selected blocks type to "code".
    editor.setBlocks('code')
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
        renderBlock={this.renderBlock}
      />
    )
  }

  renderBlock = (props, editor, next) => {
    switch (props.node.type) {
      case 'code':
        return <CodeNode {...props} />
      default:
        return next()
    }
  }
}
```

Now, if you press \`control-\`\` the block your cursor is in should turn into a code block! Magic!

*Note: The Edge browser does not currently support `control-...` key events (see* [*issue*](https://developer.microsoft.com/en-us/microsoft-edge/platform/issues/742263/)*), so this example won't work on it.*

But we forgot one thing. When you hit \`control-\`\` again, it should change the code block back into a paragraph. To do that, we'll need to add a bit of logic to change the type we set based on whether any of the currently selected blocks are already a code block:

```javascript
function CodeNode(props) {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    if (event.key != '`' || !event.ctrlKey) return next()

    event.preventDefault()

    // Determine whether any of the currently selected blocks are code blocks.
    const isCode = editor.value.blocks.some(block => block.type == 'code')

    // Toggle the block type depending on `isCode`.
    editor.setBlocks(isCode ? 'paragraph' : 'code')
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
        renderBlock={this.renderBlock}
      />
    )
  }

  renderBlock = (props, editor, next) => {
    switch (props.node.type) {
      case 'code':
        return <CodeNode {...props} />
      default:
        return next()
    }
  }
}
```

And there you have it! If you press \`control-\`\` while inside a code block, it should turn back into a paragraph!

**Next:**\
[Applying Custom Formatting](https://docs.slatejs.org/walkthroughs/applying-custom-formatting) <br>


# Applying Custom Formatting

**Previous:**\
[Defining Custom Block Nodes](https://docs.slatejs.org/walkthroughs/defining-custom-block-nodes) <br>

## Applying Custom Formatting

In the previous guide we learned how to create custom block types that render chunks of text inside different containers. But Slate allows for more than just "blocks".

In this guide, we'll show you how to add custom formatting options, like **bold**, *italic*, `code` or ~~strikethrough~~.

So we start with our app from earlier:

```javascript
class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    if (event.key != '`' || !event.ctrlKey) return next()
    event.preventDefault()
    const isCode = editor.value.blocks.some(block => block.type == 'code')

    editor.setBlocks(isCode ? 'paragraph' : 'code')
    return true
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
        renderBlock={this.renderBlock}
      />
    )
  }

  renderBlock = (props, editor, next) => {
    switch (props.node.type) {
      case 'code':
        return <CodeNode {...props} />
      default:
        return next()
    }
  }
}
```

And now, we'll edit the `onKeyDown` handler to make it so that when you press `control-B`, it will add a "bold" mark to the currently selected text:

```javascript
class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    if (!event.ctrlKey) return next()

    // Decide what to do based on the key code...
    switch (event.key) {
      // When "B" is pressed, add a "bold" mark to the text.
      case 'b': {
        event.preventDefault()
        editor.addMark('bold')
        break
      }
      // When "`" is pressed, keep our existing code block logic.
      case '`': {
        const isCode = editor.value.blocks.some(block => block.type == 'code')
        event.preventDefault()
        editor.setBlocks(isCode ? 'paragraph' : 'code')
        break
      }
      // Otherwise, let other plugins handle it.
      default: {
        return next()
      }
    }
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
        renderBlock={this.renderBlock}
      />
    )
  }

  renderBlock = (props, editor, next) => {
    switch (props.node.type) {
      case 'code':
        return <CodeNode {...props} />
      default:
        return next()
    }
  }
}
```

Okay, so we've got the hotkey handler setup... but! If you happen to now try selecting text and hitting `control-B`, you won't notice any change. That's because we haven't told Slate how to render a "bold" mark.

For every mark type you want to add to your schema, you need to give Slate a "renderer" for that mark, just like nodes. So let's define our `bold` mark:

```javascript
// Define a React component to render bold text with.
function BoldMark(props) {
  return <strong>{props.children}</strong>
}
```

Pretty simple, right?

And now, let's tell Slate about that mark. To do that, we'll pass in the `renderMark` prop to our editor. Also, let's allow our mark to be toggled by changing `addMark` to `toggleMark`.

```javascript
function BoldMark(props) {
  return <strong>{props.children}</strong>
}

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    if (!event.ctrlKey) return next()

    switch (event.key) {
      case 'b': {
        event.preventDefault()
        editor.toggleMark('bold')
        break
      }
      case '`': {
        const isCode = editor.value.blocks.some(block => block.type == 'code')
        event.preventDefault()
        editor.setBlocks(isCode ? 'paragraph' : 'code')
        break
      }
      default: {
        return next()
      }
    }
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
        renderBlock={this.renderBlock}
        // Add the `renderMark` prop...
        renderMark={this.renderMark}
      />
    )
  }

  renderBlock = (props, editor, next) => {
    switch (props.node.type) {
      case 'code':
        return <CodeNode {...props} />
      default:
        return next()
    }
  }

  // Add a `renderMark` method to render marks.
  renderMark = (props, editor, next) => {
    switch (props.mark.type) {
      case 'bold':
        return <BoldMark {...props} />
      default:
        return next()
    }
  }
}
```

Now, if you try selecting a piece of text and hitting `control-B` you should see it turn bold! Magic!

**Next:**\
[Using Plugins](https://docs.slatejs.org/walkthroughs/using-plugins) <br>


# Using Plugins

**Previous:**\
[Applying Custom Formatting](https://docs.slatejs.org/walkthroughs/applying-custom-formatting) <br>

## Using Plugins

Up until now, everything we've learned has been about how to write one-off logic for your specific Slate editor. But one of the most beautiful things about Slate is actually its plugin system and how it lets you write less one-off code.

In the previous guide, we actually wrote some pretty useful code for adding **bold** formatting to ranges of text when a key is pressed. But most of that code wasn't really specific to **bold** text; it could just as easily have applied to *italic* text or `code` text if we switched a few variables.

So let's break that logic out into a reusable plugin that can toggle *any* mark on *any* key press.

Starting with our app from earlier:

```javascript
class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  onKeyDown = (event, editor, next) => {
    if (event.key != 'b' || !event.ctrlKey) return next()
    event.preventDefault()
    editor.toggleMark('bold')
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        onKeyDown={this.onKeyDown}
        renderMark={this.renderMark}
      />
    )
  }

  renderMark = (props, editor, next) => {
    switch (props.mark.type) {
      case 'bold':
        return <strong {...props.attributes}>{props.children}</strong>
      default:
        return next()
    }
  }
}
```

Let's write a new function that takes a set of options: the mark `type` to toggle and the `key` to press.

```javascript
function MarkHotkey(options) {
  // Grab our options from the ones passed in.
  const { type, key } = options
}
```

Okay, that was easy. But it doesn't do anything.

To fix that, we need our plugin function to return a "plugin object" that Slate recognizes. Slate's plugin objects are just plain JavaScript objects whose properties map to the same handlers on the `Editor`.

In this case, our plugin object will have one property, an `onKeyDown` handler, with its logic copied right from our current app's code:

```javascript
function MarkHotkey(options) {
  const { type, key } = options

  // Return our "plugin" object, containing the `onKeyDown` handler.
  return {
    onKeyDown(event, editor, next) {
      // If it doesn't match our `key`, let other plugins handle it.
      if (!event.ctrlKey || event.key != key) return next()

      // Prevent the default characters from being inserted.
      event.preventDefault()

      // Toggle the mark `type`.
      editor.toggleMark(type)
    },
  }
}
```

Boom! Now we're getting somewhere. That code is reusable for any type of mark.

Now that we have our plugin, let's remove the hard-coded logic from our app and replace it with our brand new `MarkHotkey` plugin instead, passing in the same options that will keep our **bold** functionality intact:

```javascript
// Initialize our bold-mark-adding plugin.
const boldPlugin = MarkHotkey({
  type: 'bold',
  key: 'b',
})

// Create an array of plugins.
const plugins = [boldPlugin]

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  render() {
    return (
      // Add the `plugins` property to the editor, and remove `onKeyDown`.
      <Editor
        plugins={plugins}
        value={this.state.value}
        onChange={this.onChange}
        renderMark={this.renderMark}
      />
    )
  }

  renderMark = (props, editor, next) => {
    switch (props.mark.type) {
      case 'bold':
        return <strong>{props.children}</strong>
      default:
        return next()
    }
  }
}
```

Awesome. If you test out the editor now, you'll notice that everything still works just as it did before. But the beauty of the logic being encapsulated in a plugin is that we can add more mark types *extremely* easily now!

Let's add *italic*, `code`, ~~strikethrough~~ and underline marks:

```javascript
// Initialize a plugin for each mark...
const plugins = [
  MarkHotkey({ key: 'b', type: 'bold' }),
  MarkHotkey({ key: '`', type: 'code' }),
  MarkHotkey({ key: 'i', type: 'italic' }),
  MarkHotkey({ key: '~', type: 'strikethrough' }),
  MarkHotkey({ key: 'u', type: 'underline' }),
]

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  render() {
    return (
      <Editor
        plugins={plugins}
        value={this.state.value}
        onChange={this.onChange}
        renderMark={this.renderMark}
      />
    )
  }

  renderMark = (props, editor, next) => {
    switch (props.mark.type) {
      case 'bold':
        return <strong>{props.children}</strong>
      // Add our new mark renderers...
      case 'code':
        return <code>{props.children}</code>
      case 'italic':
        return <em>{props.children}</em>
      case 'strikethrough':
        return <del>{props.children}</del>
      case 'underline':
        return <u>{props.children}</u>
      default:
        return next()
    }
  }
}
```

And there you have it! We just added a ton of functionality to the editor with very little work. And we can keep all of our mark hotkey logic tested and isolated in a single place, making the code easier to maintain.

That's why plugins are awesome. They let you get really expressive while also making your codebase easier to manage. And since Slate is built with plugins as a primary consideration, using them is dead simple!

**Next:**\
[Saving to a Database](https://docs.slatejs.org/walkthroughs/saving-to-a-database) <br>


# Saving to a Database

**Previous:**\
[Using Plugins](https://docs.slatejs.org/walkthroughs/using-plugins) <br>

## Saving to a Database

Now that you've learned the basics of how to add functionality to the Slate editor, you might be wondering how you'd go about saving the content you've been editing, such that you can come back to your app later and have it load.

In this guide, we'll show you how to add logic to save your Slate content to a database for storage and retrieval later.

Let's start with a basic editor:

```javascript
import { Editor } from 'slate-react'
import { Value } from 'slate'

const initialValue = Value.fromJSON({
  document: {
    nodes: [
      {
        object: 'block',
        type: 'paragraph',
        nodes: [
          {
            object: 'text',
            text: 'A line of text in a paragraph.',
          },
        ],
      },
    ],
  },
})

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

That will render a basic Slate editor on your page, and when you type things will change. But if you refresh the page, everything will be reverted back to its original value—nothing saves!

What we need to do is save the changes you make somewhere. For this example, we'll just be using [Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), but it will give you an idea for where you'd need to add your own database hooks.

So, in our `onChange` handler, we need to save the `value`. But the `value` argument that `onChange` receives is an immutable object, so we can't just save it as-is. We need to serialize it to a format we understand first, like JSON!

```javascript
const initialValue = Value.fromJSON({
  document: {
    nodes: [
      {
        object: 'block',
        type: 'paragraph',
        nodes: [
          {
            object: 'text',
            text: 'A line of text in a paragraph.',
          },
        ],
      },
    ],
  },
})

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    // Save the value to Local Storage.
    const content = JSON.stringify(value.toJSON())
    localStorage.setItem('content', content)

    this.setState({ value })
  }

  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

Now whenever you edit the page, if you look in Local Storage, you should see the `content` value changing.

But... if you refresh the page, everything is still reset. That's because we need to make sure the initial value is pulled from that same Local Storage location, like so:

```javascript
// Update the initial content to be pulled from Local Storage if it exists.
const existingValue = JSON.parse(localStorage.getItem('content'))
const initialValue = Value.fromJSON(
  existingValue || {
    document: {
      nodes: [
        {
          object: 'block',
          type: 'paragraph',
          nodes: [
            {
              object: 'text',
              text: 'A line of text in a paragraph.',
            },
          ],
        },
      ],
    },
  }
)

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    const content = JSON.stringify(value.toJSON())
    localStorage.setItem('content', content)

    this.setState({ value })
  }

  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

Now you should be able to save changes across refreshes!

However, if you inspect the change handler, you'll notice that it's actually saving the Local Storage value on *every* change to the editor, even when only the selection changes! This is because `onChange` is called for *every* change. For Local Storage, this doesn't really matter, but if you're saving things to a database via HTTP request, this would result in a lot of unnecessary requests. You can fix this by checking against the previous `document` value.

```javascript
const existingValue = JSON.parse(localStorage.getItem('content'))
const initialValue = Value.fromJSON(
  existingValue || {
    document: {
      nodes: [
        {
          object: 'block',
          type: 'paragraph',
          nodes: [
            {
              object: 'text',
              text: 'A line of text in a paragraph.',
            },
          ],
        },
      ],
    },
  }
)

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    // Check to see if the document has changed before saving.
    if (value.document != this.state.value.document) {
      const content = JSON.stringify(value.toJSON())
      localStorage.setItem('content', content)
    }

    this.setState({ value })
  }

  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

Now your content will be saved only when the content itself changes!

Success—you've got JSON in your database.

But what if you want something other than JSON? Well, you'd need to serialize your value differently. For example, if you want to save your content as plain text instead of JSON, you can use the `Plain` serializer that ships with Slate, like so:

```javascript
// Switch to using the Plain serializer.
import { Editor } from 'slate-react'
import Plain from 'slate-plain-serializer'

const existingValue = localStorage.getItem('content')
const initialValue = Plain.deserialize(
  existingValue || 'A string of plain text.'
)

class App extends React.Component {
  state = {
    value: initialValue,
  }

  onChange = ({ value }) => {
    if (value.document != this.state.value.document) {
      const content = Plain.serialize(value)
      localStorage.setItem('content', content)
    }

    this.setState({ value })
  }

  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

That works! Now you're working with plain text.

However, sometimes you may want something a bit more custom, and a bit more complex... good old fashioned HTML. In that case, check out the next guide...

**Next:**\
[Saving and Loading HTML Content](https://docs.slatejs.org/walkthroughs/saving-and-loading-html-content) <br>


# Saving and Loading HTML Content

**Previous:**\
[Saving to a Database](https://docs.slatejs.org/walkthroughs/saving-to-a-database) <br>

## Saving and Loading HTML Content

In the previous guide, we looked at how to serialize the Slate editor's content and save it for later. What if you want to save the content as HTML? It's a slightly more involved process, but this guide will show you how to do it.

Let's start with a basic editor:

```javascript
import { Editor } from 'slate-react'
import Plain from 'slate-plain-serializer'

class App extends React.Component {
  state = {
    value: Plain.deserialize(''),
  }

  onChange = ({ value }) => {
    this.setState({ value })
  }

  render() {
    return <Editor value={this.state.value} onChange={this.onChange} />
  }
}
```

That will render a basic Slate editor on your page.

Now\... we need to add the [`Html`](https://docs.slatejs.org/other-packages/index) serializer. And to do that, we need to tell it a bit about the schema we plan on using. For this example, we'll work with a schema that has a few different parts:

* A `paragraph` block.
* A `code` block for code samples.
* A `quote` block for quotes...
* And `bold`, `italic` and `underline` formatting.

By default, the `Html` serializer knows nothing about our schema, just like Slate itself. To fix this, we need to pass it a set of `rules`. Each rule defines how to serialize and deserialize a Slate object.

To start, let's create a new rule with a `deserialize` function for paragraph blocks.

```javascript
const rules = [
  // Add our first rule with a deserializing function.
  {
    deserialize(el, next) {
      if (el.tagName.toLowerCase() == 'p') {
        return {
          object: 'block',
          type: 'paragraph',
          data: {
            className: el.getAttribute('class'),
          },
          nodes: next(el.childNodes),
        }
      }
    },
  },
]
```

The `el` argument that the `deserialize` function receives is just a DOM element. And the `next` argument is a function that will deserialize any element(s) we pass it, which is how you recurse through each node's children.

Okay, that's `deserialize`, now let's define the `serialize` property of the paragraph rule as well:

```javascript
const rules = [
  {
    deserialize(el, next) {
      if (el.tagName.toLowerCase() == 'p') {
        return {
          object: 'block',
          type: 'paragraph',
          data: {
            className: el.getAttribute('class'),
          },
          nodes: next(el.childNodes),
        }
      }
    },
    // Add a serializing function property to our rule...
    serialize(obj, children) {
      if (obj.object == 'block' && obj.type == 'paragraph') {
        return <p className={obj.data.get('className')}>{children}</p>
      }
    },
  },
]
```

The `serialize` function should also feel familiar. It's just taking [Slate models](https://github.com/ianstormtaylor/slate/tree/a0b7976cb9a2812d8d96361e9993fe8853a2cc64/docs/reference/slate/README.md) and turning them into React elements, which will then be rendered to an HTML string.

The `obj` argument of the `serialize` function will either be a [`Node`](https://docs.slatejs.org/slate-core/node), a [`Mark`](https://docs.slatejs.org/slate-core/mark) or a special immutable [`String`](https://github.com/ianstormtaylor/slate/tree/a0b7976cb9a2812d8d96361e9993fe8853a2cc64/docs/reference/serializers/html.md#ruleserialize) object. And the `children` argument is a React element describing the nested children of the object in question, for recursing.

Okay, so now our serializer can handle `paragraph` nodes.

Let's add the other types of blocks we want:

```javascript
// Refactor block tags into a dictionary for cleanliness.
const BLOCK_TAGS = {
  p: 'paragraph',
  blockquote: 'quote',
  pre: 'code',
}

const rules = [
  {
    // Switch deserialize to handle more blocks...
    deserialize(el, next) {
      const type = BLOCK_TAGS[el.tagName.toLowerCase()]
      if (type) {
        return {
          object: 'block',
          type: type,
          data: {
            className: el.getAttribute('class'),
          },
          nodes: next(el.childNodes),
        }
      }
    },
    // Switch serialize to handle more blocks...
    serialize(obj, children) {
      if (obj.object == 'block') {
        switch (obj.type) {
          case 'paragraph':
            return <p className={obj.data.get('className')}>{children}</p>
          case 'quote':
            return <blockquote>{children}</blockquote>
          case 'code':
            return (
              <pre>
                <code>{children}</code>
              </pre>
            )
        }
      }
    },
  },
]
```

Now each of our block types is handled.

You'll notice that even though code blocks are nested in a `<pre>` and a `<code>` element, we don't need to specifically handle that case in our `deserialize` function, because the `Html` serializer will automatically recurse through `el.childNodes` if no matching deserializer is found. This way, unknown tags will just be skipped over in the tree, instead of their contents omitted completely.

Okay. So now our serializer can handle blocks, but we need to add our marks to it as well. Let's do that with a new rule...

```javascript
const BLOCK_TAGS = {
  blockquote: 'quote',
  p: 'paragraph',
  pre: 'code',
}

// Add a dictionary of mark tags.
const MARK_TAGS = {
  em: 'italic',
  strong: 'bold',
  u: 'underline',
}

const rules = [
  {
    deserialize(el, next) {
      const type = BLOCK_TAGS[el.tagName.toLowerCase()]
      if (type) {
        return {
          object: 'block',
          type: type,
          data: {
            className: el.getAttribute('class'),
          },
          nodes: next(el.childNodes),
        }
      }
    },
    serialize(obj, children) {
      if (obj.object == 'block') {
        switch (obj.type) {
          case 'code':
            return (
              <pre>
                <code>{children}</code>
              </pre>
            )
          case 'paragraph':
            return <p className={obj.data.get('className')}>{children}</p>
          case 'quote':
            return <blockquote>{children}</blockquote>
        }
      }
    },
  },
  // Add a new rule that handles marks...
  {
    deserialize(el, next) {
      const type = MARK_TAGS[el.tagName.toLowerCase()]
      if (type) {
        return {
          object: 'mark',
          type: type,
          nodes: next(el.childNodes),
        }
      }
    },
    serialize(obj, children) {
      if (obj.object == 'mark') {
        switch (obj.type) {
          case 'bold':
            return <strong>{children}</strong>
          case 'italic':
            return <em>{children}</em>
          case 'underline':
            return <u>{children}</u>
        }
      }
    },
  },
]
```

Great, that's all of the rules we need! Now let's create a new `Html` serializer and pass in those rules:

```javascript
import Html from 'slate-html-serializer'

// Create a new serializer instance with our `rules` from above.
const html = new Html({ rules })
```

And finally, now that we have our serializer initialized, we can update our app to use it to save and load content, like so:

```javascript
// Load the initial value from Local Storage or a default.
const initialValue = localStorage.getItem('content') || '<p></p>'

class App extends React.Component {
  state = {
    value: html.deserialize(initialValue),
  }

  onChange = ({ value }) => {
    // When the document changes, save the serialized HTML to Local Storage.
    if (value.document != this.state.value.document) {
      const string = html.serialize(value)
      localStorage.setItem('content', string)
    }

    this.setState({ value })
  }

  render() {
    return (
      <Editor
        value={this.state.value}
        onChange={this.onChange}
        // Add the ability to render our nodes and marks...
        renderBlock={this.renderNode}
        renderMark={this.renderMark}
      />
    )
  }

  renderNode = (props, editor, next) => {
    switch (props.node.type) {
      case 'code':
        return (
          <pre {...props.attributes}>
            <code>{props.children}</code>
          </pre>
        )
      case 'paragraph':
        return (
          <p {...props.attributes} className={props.node.data.get('className')}>
            {props.children}
          </p>
        )
      case 'quote':
        return <blockquote {...props.attributes}>{props.children}</blockquote>
      default:
        return next()
    }
  }

  // Add a `renderMark` method to render marks.
  renderMark = (props, editor, next) => {
    const { mark, attributes } = props
    switch (mark.type) {
      case 'bold':
        return <strong {...attributes}>{props.children}</strong>
      case 'italic':
        return <em {...attributes}>{props.children}</em>
      case 'underline':
        return <u {...attributes}>{props.children}</u>
      default:
        return next()
    }
  }
}
```

And that's it! When you make any changes in your editor, you should see the updated HTML being saved to Local Storage. And when you refresh the page, those changes should be carried over.


# Commands & Queries

All commands to a Slate editor's value, whether it's the `selection`, `document`, `history`, etc. happen via "commands".

Under the covers, Slate takes care of converting each command into a set of low-level [operations](https://docs.slatejs.org/slate-core/operation) that are applied to produce a new value. This is what makes collaborative editing implementations possible. But you don't have to worry about that, because it happens automatically.

You just need to understand commands...

## Expressiveness is Key

Commands in Slate are designed to prioritize expressiveness above almost all else.

If you're building a powerful editor, it's going to be somewhat complex, and you're going to be writing code to perform all different kinds of programmatic commands. You'll be removing nodes, inserting fragments, moving the selection around, etc.

And if the API for commands was verbose, or if it required lots of in between steps to be continually performed, your code would balloon to be impossible to understand very quickly.

To solve this, Slate has very expressive, chainable commands. Like this:

```javascript
editor
  .focus()
  .moveToRangeOfDocument()
  .delete()
  .insertText('A bit of rich text, followed by...')
  .moveTo(10)
  .moveFocusForward(4)
  .addMark('bold')
  .moveToEndOfBlock()
  .insertBlock({
    type: 'image',
    data: {
      src: 'http://placekitten.com/200/300',
      alt: 'Kittens',
      className: 'img-responsive',
    },
  })
  .insertBlock('paragraph')
```

Hopefully from reading that you can discern that those commands result in... the entire document's content being selected and deleted, some text being written, a word being bolded, and finally an image block and a paragraph block being added.

Of course you're not usually going to chain that much.

Point is, you can get pretty expressive in just a few lines of code.

That way, when you're scanning to see what behaviors are being triggered, you can understand your code easily. You don't have to sit there and try to parse out a bunch of interim variables to figure out what you're trying to achieve.

To that end, Slate defines *lots* of commands.

The commands are the one place in Slate where overlap and near-duplication isn't stomped out. Because sometimes the exact-right command is the difference between one line of code and ten. And not just ten once, but ten repeated everywhere throughout your codebase.

## Command Categories

There are a handful of different categories of commands that ship with Slate by default, and understanding them may help you understand which methods to reach for when trying to write your editor's logic...

### At a Specific Range

These are commands like `deleteAtRange()`, `addMarkAtRange()`, `unwrapBlockAtRange()`, etc. that take in a [`Range`](https://docs.slatejs.org/slate-core/range) argument and apply a change to the document for all of the content in that range. These aren't used that often, because you'll usually be able to get away with using the next category of commands instead...

### At the Current Selection

These are commands like `delete()`, `addMark()`, `insertBlock()`, etc. that are the same as the `*AtRange` equivalents, but don't need to take in a range argument, because they apply their edits based on where the user's current selection is. These are often what you want to use when programmatically editing "like a user".

### On the Selection

These are commands like `blur()`, `moveToStart()`, `moveToRangeOfNode()`, etc. that change the `value.selection` model and update the user's cursor without affecting the content of the document.

### On a Specific Node

There are two types of commands referring to specific nodes, either by `path` or by `key`. These are often what you use when making programmatic commands from inside your custom node components, where you already have a reference to `props.node.key`.

Path-based commands are ones like `removeNodeByPath()`, `insertNodeByPath()`, etc. that take a `path` pinpointing the node in the document. And key-based commands are ones like `removeNodeByKey()`, `setNodeByKey()`, `removeMarkByKey()`, etc. that take a `key` string referring to a specific node, and then change that node in different ways.

### On the Top-level Value

These are commands like `setData()`, `setDecorations()`, etc. that act on the other top-level properties of the [`Value`](https://docs.slatejs.org/slate-core/value) object. These are more advanced.

### On the History

These are commands like `undo()`, `redo()`, etc. that use the operation history and redo or undo commands that have already happened. You generally don't need to worry about these, because they're already bound to the keyboard shortcuts you'd expect, and the user can use them.

## Running Commands

When you decide you want to make a change to the Slate value, you're almost always in one of four places...

### 1. In Slate Handlers

The first place, is inside a Slate-controlled event handler, like `onKeyDown` or `onPaste`. These handlers take a signature of `event, editor, next`. For example...

```javascript
function onKeyDown(event, editor, next) {
  if (event.key == 'Enter') {
    editor.splitBlock()
  } else {
    return next()
  }
}
```

Any commands you call will be applied immediately to the `editor` object, and flushed to the `onChange` handler on the next tick.

### 2. From Custom Node Components

The second place is inside a custom node component. For example, you might have an `<Image>` component and you want to make a change when the image is clicked. For example...

```javascript
class Image extends React.Component {
  onClick = event => {
    const { editor, node } = this.props
    editor.removeNodeByKey(node.key)
  }

  render() {
    return <img {...this.props.attributes} onClick={this.onClick} />
  }
}
```

The `<Image>` node component will be passed the `editor` and the `node` it represents as props, so you can use these to trigger commands.

### 3. From Schema Rules

The third place you may perform change operations—for more complex use cases—is from inside a custom normalization rule in your editor's [`Schema`](https://github.com/ianstormtaylor/slate/tree/a0b7976cb9a2812d8d96361e9993fe8853a2cc64/docs/references/slate/schema.md). For example...

```javascript
{
  blocks: {
    list: {
      nodes: [{
        match: { type: 'item' }
      }],
      normalize: (editor, error) => {
        if (error.code == 'child_type_invalid') {
          editor.wrapBlockByKey(error.child.key, 'item')
        }
      }
    }
  }
}
```

When a rule's validation fails, Slate passes the editor to the `normalize` function of the rule, if one exists. You can use these normalizing functions to apply the commands necessary to make your document valid on the next normalization pass.

### 4. From Outside Slate

The last place is from outside of Slate. Sometimes you'll have components that live next to your editor in the render tree, and you'll need to explicitly pass them a reference to the Slate `editor` to run changes. In React you do this with the `ref={}` prop...

```javascript
<Editor
  ref={editor => this.editor = editor}
  ...
/>
```

Which gives you a reference to the Slate editor. And from there you can use the same commands syntax from above to apply changes.

## Running Queries

Queries are similar to commands, but instead of manipulating the current value of the editor, they return information about the current value, or a specific node, etc.

By default, Slate only defines two queries: `isAtomic` for marks and decorations, and `isVoid` for nodes. You can access them directly on the editor:

```javascript
const isVoid = editor.isVoid(node)
```

But you can also define your own queries that are specific to your schema. For example, you might use a query to determine whether the "bold" mark is active...

```javascript
const isBold = editor.isBoldActive(value)
```

And then use that information to mark the bold button in your editor's toolbar as active or not.

## Reusing Commands and Queries

In addition to using the built-in commands, if your editor is of any complexity you'll want to write your own reusable commands. That way, you can reuse a single `insertImage` change instead of constantly writing `insertBlock(...args)`.

To do that, you can define commands in your own Slate plugin, which will be made available as methods on the `editor` object. For example, here are two simple block inserting commands...

```javascript
const yourPlugin = {
  commands: {
    insertParagraph(editor) {
      editor.insertBlock('paragraph')
    },

    insertImage(editor, src) {
      editor.insertBlock({
        type: 'image',
        data: { src },
      })
    },
  },
}
```

Notice how rewriting that image inserting logic multiple times without having it encapsulated in a single function would get tedious. Now with those change functions defined, you can reuse them!

```javascript
editor.insertImage('https://google.com/logo.png')
```

And any arguments you pass in are sent to your custom command functions.

The same thing goes for queries, which can be defined in plugins and re-used across your entire codebase. To do so, define a `queries` object:

```javascript
const yourPlugin = {
  queries: {
    getActiveListItem(editor) {
      ...
    }
  }
}
```

And then you can use them right from the `editor` instance:

```javascript
editor.getActiveListItem()
```

This reusability is key to being able to organize your commands and queries, and compose them together to create more advanced behaviors.


# Data Model

Slate is based on an immutable data model that closely resembles the DOM. When you start using Slate, one of the most important things to do is familiarize yourself with this data model. This guide will help you do just that!

## Slate Mirrors the DOM

One of the main principles of Slate is that it tries to mirror the native DOM API's as much as possible.

Mirroring the DOM is an intentional decision given Slate is a richer implementation of `contenteditable,` which uses the DOM. And people use the DOM to represent documents with rich-text-like structures all the time. Mirroring the DOM helps make the library familiar for new users, and it lets us reuse battle-tested patterns without having to reinvent them ourselves.

Because it mirrors the DOM, Slate's data model features a [`Document`](https://docs.slatejs.org/slate-core/document) with [`Block`](https://docs.slatejs.org/slate-core/block), [`Inline`](https://docs.slatejs.org/slate-core/inline) and [`Text`](https://docs.slatejs.org/slate-core/text) nodes. You can reference parts of the document with a [`Range`](https://docs.slatejs.org/slate-core/range). And there is a special range-like object called a [`Selection`](https://docs.slatejs.org/slate-core/selection) that represents the user's current cursor selection.

> The following content on Mozilla's Developer Network may help you learn more about the corresponding DOM concepts:
>
> * [Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)
> * [Block Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements)
> * [Inline elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements)
> * [Text elements](https://developer.mozilla.org/en-US/docs/Web/API/Text)

## Immutable Objects

Slate's data model is implemented using [`Immutable.js`](https://immutable-js.github.io/immutable-js/) objects to allow more performant rendering and ensure objects cannot be accidentally modified (which are especially tricky bugs to track down).

Specifically, Slate's models are [`Immutable.Record`](https://immutable-js.github.io/immutable-js/docs/#/Record) objects, which makes them very similar to JavaScript objects for retrieving values:

```javascript
const block = Block.create({ type: 'paragraph' })

block.object // "block"
block.type // "paragraph"
```

Changing values requires you to use the [`Immutable.Record` API](https://immutable-js.github.io/immutable-js/docs/#/Record/set).

Collections of Slate objects are represented as immutable `Lists`, `Sets`, `Stacks`, etc, which means we enjoy expressive methods like `filter`, `includes`, `take`, `skip`, `rest` and `last`.

If you haven't used [`Immutable.js`](https://immutable-js.github.io/immutable-js/) before, there is definitely a learning curve. Before you dive into Slate, you are encouraged to become familiar the [Immutable.js documentation](https://immutable-js.github.io/immutable-js/docs/#/). Once you get the hang of the Immutable JS API you'll be quite productive. It might take a few days to get used to Immutable JS. And, you might write some suboptimal code at first. Don't let this discourage you! Learning Immutable JS is well worth the investment!

## The "Value"

The top-level object in Slate—the object encapsulating the entire value of a Slate editor—is called a [`Value`](https://docs.slatejs.org/slate-core/value).

Value consists of the document which contains all content, and a `selection` representing the user's current cursor selection. Value also has a few other advanced properties such as `decorations` and `data`.

> 📋 For more info, check out the [`Value` reference](https://docs.slatejs.org/slate-core/value).

The following example illustrates a simple Slate value which has been serialized and logged to the console. Continue reading to learn more about the data types represented.

```javascript
{
  "object": "value",
  "document": {
    "object": "document",
    "data": {},
    "nodes": [
      {
        "object": "block",
        "type": "paragraph",
        "data": {},
        "nodes": [
          {
            "object": "text",
            "leaves": [
              {
                "object": "leaf",
                "text": "A line of text in a paragraph.",
                "marks": []
              }
            ]
          }
        ]
      }
    ]
  }
}
```

## Documents and Nodes

A Slate document is a nested and recursive structure. In a document block nodes can have child nodes—all which may have child nodes without limit. The nested and recursive structure enable you to model simple behaviors such as user mentions and hashtags or complex behaviors such as tables and figures with captions.

Unlike the DOM, Slate offers some constraints to prevent "impossible" situations from occurring. Slate's constraints include:

* **Documents must have block nodes as direct children.** This constraint mirrors how rich-text editors work. The top-most elements are blocks that may be split when pressing Enter.
* **Blocks may contain either only block nodes, or a combination of inline and text nodes.** This constraint helps you avoid boilerplate `if` statements. You can trust blocks either wrap (a) exclusively blocks, or (b) a combination of non-block nodes made up of inline and/or text nodes.
* **Inlines can only contain inline or text nodes.** This constraint helps you avoid boilerplate code. When working within the context of an inline you can trust the contents do not contain blocks.
* **Text nodes cannot be adjacent to other text nodes.** Any two adjacent text nodes will automatically be merged into one by Slate which prevents ambiguous cases where a cursor could be at the end of one text node or at the start of the next. However, you may have an inline node surrounded by two texts.
* **Blocks and inlines must always contain at least one text node.** This constraint ensures that the user's cursor can always "enter" the nodes and that ranges can be created referencing them.

Slate enforces all of these constraints for you automatically. As you [run commands](https://docs.slatejs.org/guides/commands-and-queries) to manipulate the document, Slate will normalize the value if it determines the document violates any of these constraints.

> 🙃 Fun fact: "normalizing" is actually based on the DOM's [`Node.normalize()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/normalize)!

In addition to documents, blocks and inlines, Slate introduces one other type of markup that the DOM does not have natively, the [`Mark`](https://docs.slatejs.org/slate-core/mark) which is used for formatting.

## Marks

Marks are how Slate represents formatting data that is attached to the characters in the text itself. Standard formatting such as **bold**, *italic*, `code`, or custom formatting for your application can be implemented using marks.

There are multiple techniques you might choose to format or style text. You can implement styling based on inlines or marks. Unlike inlines, marks do not affect the structure of the nodes in the document. Marks simply attach themselves to the characters.

Marks may be easier to reason about and manipulate because marks do not affect the structure of the document and are associated to the characters. Marks can be applied to characters no matter how the characters are nested in the document. If you can express it as a `Range`, you can add marks to it. Working with marks instead of inlines does not require you to edit the document's structure, split existing nodes, determine where nodes are in the hierarchy, or other more complex interactions.

When marks are rendered, the characters are grouped into "leaves" of text that each contain the same set of marks applied to them. One disadvantage of marks is that you cannot guarantee how a set of marks will be ordered.

This limitation with respect to the ordering of marks is similar to the DOM, where this is invalid:

```markup
<em>t<strong>e</em>x</strong>t
```

Because the elements in the above example do not properly close themselves they are invalid. Instead, you would write the above HTML as follows:

```markup
<em>t</em><strong><em>e</em>x</strong>t
```

If you happened to add another overlapping section of `<strike>` to that text, you might have to rearrange the closing tags yet again. Rendering marks in Slate is similar—you can't guarantee that even though a word has one mark applied that that mark will be contiguous, because it depends on how it overlaps with other marks.

Of course, this mark ordering stuff sounds pretty complex. But, you do not have to think about it much, as long as you use marks and inlines for their intended purposes:

* Marks represent **unordered**, character-level formatting.
* Inlines represent **contiguous**, semantic elements in the document.

## Ranges, Points and "The Selection"

Just like the DOM, you can reference a part of the document using a `Range`. Slate keeps track of a the user's current cursor selection using a range called the `Selection`.

Ranges are defined by two `Point`s:

* **Anchor point** is where the range starts
* **Focus point** is where the range ends

> Note: The terms "anchor" and "focus" are borrowed from the DOM API (see [anchor](https://developer.mozilla.org/en-US/docs/Web/API/Selection/anchorNode) and [focus](https://developer.mozilla.org/en-US/docs/Web/API/Selection/focusNode)).

Each point is a combination of a "path" or "key" referencing a specific node, and an "offset". This ends up looking like this:

```javascript
const range = Range.create({
  anchor: {
    key: 'node-a',
    path: [0, 2, 1],
    offset: 0,
  },
  focus: {
    key: 'node-b',
    path: [0, 3, 2],
    offset: 4,
  },
})
```

> Note: Every node has a unique `key` property. The above psuedocode references `node-a` and `node-b`; however, Slate uses auto-incrementing numerical strings by default—`'1', '2', '3', ...`.

An anchor and focus are established by a user interaction. The anchor point isn't always *before* the focus point in the document. Just like in the DOM, the ordering of an anchor and selection point depend on whether the range is backwards or forwards.

Here's how Mozilla Developer Network explains it:

> A user may make a selection from left to right (in document order) or right to left (reverse of document order). The anchor is where the user began the selection and the focus is where the user ends the selection. If you make a selection with a desktop mouse, the anchor is placed where you pressed the mouse button and the focus is placed where you released the mouse button. Anchor and focus should not be confused with the start and end positions of a selection, since anchor can be placed before the focus or vice versa, depending on the direction you made your selection. — [`Selection`, MDN](https://developer.mozilla.org/en-US/docs/Web/API/Selection)

To make working with ranges easier, `Range` objects also provide both `start` and `end` point properties that consider whether the range is forward or backward into account. The `start.key` and `start.path` will always be before the `end.key` and `end.path` in the document to provide you with intuitive methods of working with ranges.

Typically, you will utilize `start` and `end` points since you rarely care which side of the selection is "extendable".

One important thing to note is that the anchor and focus points of ranges **always reference the "leaf-most" text nodes** in a document and never reference blocks or inlines. Said differently ranges always reference child text nodes. This range behavior is different than the DOM API and simplifies working with ranges as there are fewer edge cases for you to handle.

> 📋 For more info, check out the [`Range` reference](https://docs.slatejs.org/slate-core/range).

The `Selection` model contains slightly more information than the `Range` model because it is responsible for tracking the "focus" and "marks" for the user. Example:

```javascript
const selection = Selection.create({
  anchor: {
    key: 'node-a',
    path: [0, 2, 1],
    offset: 0,
  },
  focus: {
    key: 'node-b',
    path: [0, 3, 2],
    offset: 4,
  },
  isFocused: true,
  marks: [{ type: 'bold' }],
})
```

However, keeping the `key` and `path` of ranges or selections synchronized yourself is tedious. Instead, you can create selections using either option and have the other automatically be inferred by the document. To do so, you use the `createRange` and `createSelection` methods:

```javascript
const selection = document.createSelection({
  anchor: {
    key: 'node-a',
    offset: 0,
  },
  focus: {
    key: 'node-b',
    offset: 4,
  },
  isFocused: true,
  marks: [{ type: 'bold' }],
})
```

The resulting `selection` will have a both the `key` and `path` set for its points, with the `key` being used to look up the `path` in the document.


# Plugins

With Slate, *all* of your editor's logic is controlled by "plugins".

Plugins have complete control over the schema, the behaviors, and the rendering of the editor—they can add any kind of functionality they want. So much so that even the core logic of Slate is defined by its own plugins.

Slate encourages you to break up code into small, reusable modules that can be shared with others, and easily reasoned about.

## What Are Plugins?

Slate's plugins are plain JavaScript objects containing a collection of functions that all contribute to a shared behavior—each with a specific name and set of arguments. For a full list of the arguments, check out the [Plugins](https://docs.slatejs.org/slate-core/plugins) and [React Plugins](https://docs.slatejs.org/slate-react/plugins) references.

When building a plugin module, it should always export a function that takes options. This way even if it doesn't take any options now, it won't be a breaking API change to take more options in the future.

So a basic plugin might look like this:

```javascript
export default function MySlatePlugin(options) {
  return {
    onKeyDown(event, editor, next) {
      if (event.key == options.key) {
        editor.blur()
      } else {
        return next()
      }
    },
    onClick(event, editor, next) {
      if (editor.value.selection.isBlurred) {
        editor.moveToRangeOfDocument().focus()
      } else {
        return next()
      }
    },
  }
}
```

It focuses the editor and selects everything when it is clicked, and it blurs the editor when `options.key` is pressed.

Notice how it's able to define a set of behaviors, reacting to different events, that work together to form a single "feature" in the editor. That's what makes Slate's plugins a powerful form of encapsulation.

## The Plugins "Stack"

Slate's editor takes a list of plugins as one of its arguments. We refer to this list as the plugins "stack". It is very similar to "middleware" from Express or Koa, except instead of just a single stack of handler functions, there are multiple stacks for each type of request.

```javascript
const plugins = [
  ...
]

<Editor
  plugins={plugins}
  ...
/>
```

When the editor needs to handle a DOM event, or decide what to render, it will loop through the plugins stack, invoking each plugin in turn. Plugins can choose to handle the request, in which case the editor will break out of the loop. Or they can ignore it, and they will be skipped as the editor proceeds to the next plugin in the stack.

Because of this looping, plugins are **order-sensitive**! This is very important. The earlier in the stack, the more preference the plugin has, since it can react before the others after it. If two plugins both try to handle the same event, the earlier plugin will "win".

## "Core" Plugins

If you put Slate on the page without adding any of your own plugins, it will still behave like you'd expect a rich-text editor to. That's because it has its own "core" logic. And that core logic is implemented with its own core plugins.

The core plugins doesn't have any assumptions about your schema, or what types of formatting you want to allow. But they do define common editing behaviors like splitting the current block when enter is pressed, or inserting a string of text when the user pastes from their clipboard.

These are behaviors that all rich-text editors exhibit, and that don't make sense for userland to have to re-invent for every new editor.

For the most part you don't need to worry about the core plugins.

*To learn more, check out the* [*Core Plugin reference*](https://docs.slatejs.org/slate-core/plugins)*.*

## The "Editor" Plugin

If you've read through the [`<Editor>` reference](https://docs.slatejs.org/slate-react/editor) you'll notice that the editor itself has handlers like `onKeyDown`, `onClick`, etc. just like plugins.

```javascript
const plugins = [
  ...
]

<Editor
  onClick={...}
  onKeyDown={...}
  plugins={plugins}
/>
```

This is nice because it makes the editor feel like a proper React component, it makes writing simple editors easier, and nicely mimics the native DOM API of `<input>` and `<textarea>`.

But under the covers, those editor handlers are actually just a convenient way of writing a plugin. Internally, the editor grabs all of those plugin-like properties, and turns them into an "editor" plugin that it places at the beginning of its plugins array. So that example above is actually equivalent to...

```javascript
const plugins = [
  { onClick: ..., onKeyDown: ... },
  ...
]

<Editor
  plugins={plugins}
/>
```

This isn't something you need to remember, but it's helpful to know that even the top-level editor props are just another plugin!

## Helper Plugins vs. Feature Plugins

Plugins *can* do anything and everything. But that doesn't mean you should build a single plugin that is thousands of lines long that implements every single feature in your editor—your codebase would be hell to maintain. Instead, just like all modules, you should split them up into pieces with separate concerns.

A distinction that helps with this is to consider two different types of plugins: "helper plugins" and "feature plugins".

This distinction is very similar to any other type of packages. You have things like [`chalk`](https://yarnpkg.com/en/package/chalk), [`is-url`](https://yarnpkg.com/en/package/is-url) and [`isomorphic-fetch`](https://yarnpkg.com/en/package/isomorphic-fetch) that are open-source helpers that you compose together to form larger features in your app.

### Helper Plugins

Helper plugins are usually very small, and just serve to easily encapsulate a specific piece of logic that gets re-used in multiple places—often in multiple "feature" plugins.

For example, you may have a simple `Hotkey` plugin that makes binding behaviors to hotkeys a lot simpler:

```javascript
function Hotkey(hotkey, fn) {
  return {
    onKeyDown(event, editor, next) {
      if (isHotkey(hotkey, event)) {
        editor.command(fn)
      } else {
        return next()
      }
    },
  }
}
```

That pseudo-code allows you to encapsulate the hotkey-binding logic in one place, and re-use it anywhere else you want, like so:

```javascript
const plugins = [
  ...,
  Hotkey('cmd+b', editor => editor.addMark('bold')),
]
```

These types of plugins are critical to keeping your code maintainable. And they're good candidates for open-sourcing for others to use. A few examples of plugins like this in the wild are [`slate-auto-replace`](https://github.com/ianstormtaylor/slate-plugins/tree/master/packages/slate-auto-replace), [`slate-collapse-on-escape`](https://github.com/ianstormtaylor/slate-plugins/tree/master/packages/slate-collapse-on-escape), etc.

There's almost no piece of logic too small to abstract out and share, as long as it's reusable and not opinionated about the editor's schema.

But hotkey binding logic by itself isn't a "feature". It's just a small helper that makes building more complex features a lot more expressive.

### Feature Plugins

Feature plugins are larger in scope, and serve to define an entire series of behaviors that make up a single "feature" in your editor. They're not as concrete as helper plugins, but they make reasoning about complex editors much simpler.

For example, you maybe decide you want to allow **bold** formatting in your editor. To do that, you need a handful of different behaviors.

You could just have a single, long `plugins.js` file that contained all of the plugins for all of the features in your editor. But figuring out what was going on in that file would get confusing very quickly.

Instead, it can help to split up your plugins into features. So you might have a `bold.js`, `italic.js`, `images.js`, etc. Your bold plugin might look like...

```javascript
function Bold(options) {
  return [
    Hotkey('cmd+b', addBoldMark),
    RenderMark('bold', props => <BoldMark {...props} />),
    RenderButton(props => <BoldButton {...props} />),
    ...
  ]
}
```

This is just pseudo-code, but you get the point.

You've created a single plugin that defines the entire bold "feature". If you go to your editor and you removed the `Bold` plugin, the entire bold "feature" would be removed. Having it encapsulated like this makes it much easier to maintain.

Feature plugins are usually app-specific, so they don't make great open-source candidates.

### Framework Plugins

That said, there might be another type of plugins that kind of straddle the line. Continuining our analogy to the JavaScript package landscape, you might call these "framework" plugins.

These are plugins that bundle up a set of logic, similar to how a feature might, but in a way that is re-usable across codebases. Some examples of these would be [`slate-edit-code`](https://github.com/GitbookIO/slate-edit-code), [`slate-edit-list`](https://github.com/GitbookIO/slate-edit-list), [`slate-edit-table`](https://github.com/GitbookIO/slate-edit-table), etc.

Framework plugins will often define their own commands, queries and even schema—ideally letting you customize these as needed. And they'll use these commands to provide some larger behavior that's common to many apps, like editing lists or tables.

You'll often want to encapsulate framework plugins in your own feature plugins, but they can go a long way in terms of reducing your codebase size.

## Best Practices

When you're writing plugins, there are a few patterns to follow that will make your plugins more flexible, and more familiar for others.

If you think of another good pattern, feel free to pull request it!

### Write Plugins as Functions

You should always write plugins as functions that take `options`.

```javascript
function YourPlugin(options) {
  return {
    ...
  }
}
```

This is easy to do, and it means that even if you don't have any options now you won't have to break the API to add them in the future. It also makes it easier to use plugins because you just always assume they're functions.

### Register Commands and Queries

This was alluded to in the previous section, but if your plugin defines queries like `hasBoldMark` or commands like `addBoldMark`, it can be helpful to expose those to the user so they can use the same functions in their own code.

```javascript
function YourBoldPlugin(options) {
  return {
    queries: {
      hasBoldMark,
      ...
    },
    commands: {
      addBoldMark,
      ...
    },
    ...
  }
}
```

Even better is to have a default behavior for these commands and queries, but to allow the user to override them, or provide their own command string to use instead. This way you make the default easy, but still allow for use cases with slightly different needs.

For example, when you want to write a plugin that adds a mark when a hotkey is pressed.

If you write this in the naive way as taking a mark `type` string, users won't be able to add data associated with the mark in more complex cases. And if you accept a string or an object, what happens if the user wants to actually add two marks at once, or perform some other piece of logic. You'll have to keep adding esoteric options which make the plugin hard to maintain.

Instead, let the user pass in a command name, like so:

```javascript
const plugins = [
  AddMark({
    hotkey: 'cmd+b',
    command: 'addBoldMark',
  }),
]
```

That way they can choose exactly what logic adding a bold mark entails.


# Rendering

One of the best parts of Slate is that it's built with React, so it fits right into your existing application. It doesn't re-invent its own view layer that you have to learn. It tries to keep everything as React-y as possible.

To that end, Slate gives you control over the rendering behavior of every node and mark in your document, and even the top-level editor itself.

You can define these behaviors by passing `props` into the editor, or you can define them in Slate plugins.

## Nodes & Marks

Using custom components for the nodes and marks is the most common rendering need. Slate makes this easy to do. In case of nodes, you just define a function and pass it to the `renderBlock` or `renderInline` prop of `Editor` component.

The function is called with the node's props, including `props.node` which is the node itself. You can use these to determine what to render. For example, you can render nodes using simple HTML elements:

```javascript
function renderBlock(props, editor, next) {
  const { node, attributes, children } = props

  switch (node.type) {
    case 'paragraph':
      return <p {...attributes}>{children}</p>
    case 'quote':
      return <blockquote {...attributes}>{children}</blockquote>
    case 'image': {
      const src = node.data.get('src')
      return <img {...attributes} src={src} />
    }
    default:
      return next()
  }
}

function renderInline(props, editor, next) {
  ...
}

<Editor
  renderBlock={renderBlock}
  renderInline={renderInline}
  ...
/>
```

> 🤖 Be sure to mix in `props.attributes` and render `props.children` in your node components! The attributes are required for utilities like Slate's `findDOMNode`, and the children are the actual text content of your nodes.

You don't have to use simple HTML elements, you can use your own custom React components too:

```javascript
function renderBlock(props, editor, next) {
  switch (props.node.type) {
    case 'paragraph':
      return <ParagraphComponent {...props} />
    case 'quote':
      return <QuoteComponent {...props} />
    case 'image':
      return <ImageComponent {...props} />
    default:
      return next()
  }
}
```

And you can just as easily put that `renderBlock` or `renderInline` logic into a plugin, and pass that plugin into your editor instead:

```javascript
function SomeRenderingPlugin() {
  return {
    renderBlock(props, editor, next) {
      ...
    }
  }
}

const plugins = [
  SomeRenderingPlugin(),
  ...
]

<Editor
  plugins={plugins}
  ...
/>
```

Marks work the same way, except they invoke the `renderMark` function. Like so:

```javascript
function renderMark(props, editor, next) {
  const { children, mark, attributes } = props
  switch (mark.type) {
    case 'bold':
      return <strong {...{ attributes }}>{children}</strong>
    case 'italic':
      return <em {...{ attributes }}>{children}</em>
    case 'code':
      return <code {...{ attributes }}>{children}</code>
    case 'underline':
      return <u {...{ attributes }}>{children}</u>
    case 'strikethrough':
      return <s {...{ attributes }}>{children}</s>
    default:
      return next()
  }
}
```

Be sure to mix `props.attributes` in your `renderMark`. `attributes` provides `data-*` dom attributes for spell-check in non-IE browsers.

That way, if you happen to have a global stylesheet that defines `strong`, `em`, etc. styles then your editor's content will already be formatted!

> 🤖 Be aware though that marks aren't guaranteed to be "contiguous". Which means even though a **word** is bolded, it's not guaranteed to render as a single `<strong>` element. If some of its characters are also italic, it might be split up into multiple elements—one `<strong>wo</strong>` and one `<em><strong>rd</strong></em>`.

## The Editor Itself

Not only can you control the rendering behavior of the components inside the editor, but you can also control the rendering of the editor itself.

This sounds weird, but it can be pretty useful if you want to render additional top-level elements from inside a plugin. To do so, you use the `renderEditor` function:

```javascript
function renderEditor(props, editor, next) {
  const { editor } = props
  const wordCount = countWords(editor.value.text)
  const children = next()
  return (
    <React.Fragment>
      {children}
      <span className="word-count">{wordCount}</span>
    </React.Fragment>
  )
}

<Editor
  renderEditor={renderEditor}
  ...
/>
```

Here we're rendering a small word count number underneath all of the content of the editor. Whenever you change the content of the editor, `renderEditor` will be called, and the word count will be updated.

This is very similar to how higher-order components work! Except it allows each plugin in Slate's plugin stack to wrap the editor's children.

> 🤖 Be sure to remember to render `children` in your `renderEditor` functions, because that contains the editor's own elements!


# Schemas

One of Slate's principles is that it doesn't assume anything about the type of content you're building an editor for. Some editors will want **bold**, *italic*, ~~strikethrough~~, and some won't. Some will want comments and highlighting, some won't. You *can* build all of these things with Slate, but Slate doesn't assume anything out of the box.

This turns out to be extremely helpful when building complex editors, because it means you have full control over your content—you are never fighting with assumptions that the "core" library has made.

That said, just because Slate is agnostic doesn't mean you aren't going to need to enforce a "schema" for your documents.

To that end, Slate lets you define validations for the structure of your documents, and to fix them if the document ever becomes invalid. This guide will show you how they work.

> 🤖 To see a full example of a schema in affect, check out the [Forced Layout](https://github.com/ianstormtaylor/slate/blob/405cef0225c314b4162d587c74cfce6b65a7b257/examples/forced-layout/index.js#L62) example.

## Basic Schemas

Slate schemas are defined as JavaScript objects, with properties that describe the document, block nodes, and inline nodes in your editor. Here's a simple schema:

```jsx
const schema = {
  document: {
    nodes: [
      {
        match: [{ type: 'paragraph' }, { type: 'image' }],
      },
    ],
  },
  blocks: {
    paragraph: {
      nodes: [
        {
          match: { object: 'text' },
        },
      ],
    },
    image: {
      isVoid: true,
      data: {
        src: v => v && isUrl(v),
      },
    },
  },
}

<Editor
  schema={schema}
  value={this.state.value}
  ...
/>
```

Hopefully just by reading this definition you'll understand what kinds of blocks are allowed in the document and what properties they can have—schemas are designed to prioritize legibility.

This schema defines a document that only allows `paragraph` and `image` blocks. In the case of `paragraph` blocks, they can only contain text nodes. And in the case of `image` blocks, they are void nodes with a `data.src` property that is a URL. Simple enough, right?

The magic is that by passing a schema like this into your editor, it will automatically "validate" the document when changes are made, to make sure the schema is being adhered to. If it is, great. But if it isn't, and one of the nodes in the document is invalid, the editor will automatically "normalize" the node, to make the document valid again.

This way you can guarantee that the data is in a format that you expect, so you don't have to handle tons of edge-cases or invalid states in your own code.

> 🤖 Internally, Slate converts those schema definitions into plugins that enforce certain behaviors when changes are applied to the document.

## Custom Normalizers

By default, Slate will normalize any invalid states to ensure that the document is valid again. However, since Slate doesn't have that much information about your schema, its default normalization techniques might not always be what you want.

For example, with the above schema, if a block that isn't a `paragraph` or an `image` is discovered in the document, Slate will simply remove it.

But you might want to preserve the node, and instead just convert it to a `paragraph`-this way you aren't losing whatever the node's content was. Slate doesn't know those kinds of specifics about your data model, and trying to express all of these types of preferences in a declarative schema is a huge recipe for complexity.

Instead, Slate lets you define your own custom normalization logic.

```javascript
const schema = {
  document: {
    nodes: [{
      match: [{ type: 'paragraph' }, { type: 'image' }],
    }],
    normalize: (editor, error) => {
      if (error.code == 'child_type_invalid') {
        editor.setNodeByKey(error.child.key, { type: 'paragraph' })
      }
    }
  },
  ...
}
```

That's an example of defining your own custom `normalize` option for the document validation. If the invalid reason is `child_type_invalid`, it will set the child to be a `paragraph`.

When Slate discovers an invalid child, it will first check to see if your custom normalizer handles that case; if your normalizer handles it, then Slate won't run any of its default behavior. This way, you can opt-in to customizing the normalization logic for specific cases without having to re-implement all of the defaults yourself.

This gives you the best of both worlds. You can write simple, terse, declarative validation rules that can be highly optimized. But you can still define fine-grained, imperative normalization logic for when invalid states occur.

> 🤖 For a full list of error `code` types, check out the [`Schema` reference](https://docs.slatejs.org/slate-core/schema).

## Low-level Normalizations

Sometimes though, the declarative validation syntax isn't fine-grained enough to handle a specific piece of validation. That's okay, because you can actually define schema validations in Slate as regular functions when you need more control, using the `normalizeNode` property of plugins and editors.

> 🤖 Actually, under the covers the declarative schemas are all translated into `normalizeNode` functions too!

When you define a `normalizeNode` function, you either return nothing if the node's already valid, or you return a normalizer function that will make the node valid if it isn't. Here's an example:

```javascript
function normalizeNode(node, editor, next) {
  const { nodes } = node
  if (node.object !== 'block') return next()
  if (nodes.size !== 3) return next()
  if (nodes.first().object !== 'text') return next()
  if (nodes.last().object !== 'text') return next()
  return () => editor.removeNodeByKey(node.key)
}
```

This validation defines a very specific (honestly, useless) behavior, where if a node is a block and has three children, the first and last of which are text nodes, it is removed. I don't know why you'd ever do that, but the point is that you can get very specific with your validations this way. Any property of the node can be examined.

When you need this level of specificity, using the `normalizeNode` property of the editor or plugins is handy.

However, only use it when you absolutely have to. And when you do, make sure to optimize the function's performance. `normalizeNode` will be called **every time the node changes**, so it should be as performant as possible. That's why the example above returns early, so that the smallest amount of work is done each time it is called.


# Plugins

Here's a list of Slate plugins, organized by category, so that they're easier to find than searching NPM or Yarn.

## Behavior

Plugins that add specific behaviors to your editor.

| **Plugin**                                                                                | **Description**                                                 | **Downloads**                                                                                  |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [`slate-auto-replace`](https://yarnpkg.com/en/package/slate-auto-replace)                 | Automatically transform certain input as a user types.          | ![](https://img.shields.io/npm/dm/slate-auto-replace.svg?maxAge=3600\&label=%E2%AC%87)         |
| [`slate-code`](https://yarnpkg.com/en/package/@convertkit/slate-code)                     | Adds code block editing behaviors to an editor                  | ![](https://img.shields.io/npm/dm/@convertkit/slate-code.svg?maxAge=3600\&label=%E2%AC%87)     |
| [`slate-collapse-on-escape`](https://yarnpkg.com/en/package/slate-collapse-on-escape)     | Collapse the selection when users hit esc.                      | ![](https://img.shields.io/npm/dm/slate-collapse-on-escape.svg?maxAge=3600\&label=%E2%AC%87)   |
| [`slate-drop-or-paste-images`](https://yarnpkg.com/en/package/slate-drop-or-paste-images) | Allows users to insert images by drag-dropping or copy-pasting. | ![](https://img.shields.io/npm/dm/slate-drop-or-paste-images.svg?maxAge=3600\&label=%E2%AC%87) |
| [`slate-lists`](https://yarnpkg.com/en/package/@convertkit/slate-lists)                   | Adds ordered and unordered list editing behaviors to an editor. | ![](https://img.shields.io/npm/dm/@convertkit/slate-lists.svg?maxAge=3600\&label=%E2%AC%87)    |
| [`slate-mark-hotkeys`](https://yarnpkg.com/en/package/slate-mark-hotkeys)                 | Adds common hotkey formatting utils to an editor.               | ![](https://img.shields.io/npm/dm/slate-mark-hotkeys.svg?maxAge=3600\&label=%E2%AC%87)         |
| [`slate-no-empty`](https://yarnpkg.com/en/package/slate-no-empty)                         | Prevents documents from being empty.                            | ![](https://img.shields.io/npm/dm/slate-no-empty.svg?maxAge=3600\&label=%E2%AC%87)             |
| [`slate-paste-linkify`](https://yarnpkg.com/en/package/slate-paste-linkify)               | Automatically linkify URLs when they are pasted.                | ![](https://img.shields.io/npm/dm/slate-paste-linkify.svg?maxAge=3600\&label=%E2%AC%87)        |
| [`slate-soft-break`](https://yarnpkg.com/en/package/slate-soft-break)                     | Adds soft breaks when users hit enter.                          | ![](https://img.shields.io/npm/dm/slate-soft-break.svg?maxAge=3600\&label=%E2%AC%87)           |
| [`slate-sticky-inlines`](https://yarnpkg.com/en/package/slate-sticky-inlines)             | Changes the inline node behavior to allow editing at the edges. | ![](https://img.shields.io/npm/dm/slate-sticky-inlines.svg?maxAge=3600\&label=%E2%AC%87)       |
| [`slate-suggestions`](https://yarnpkg.com/en/package/slate-suggestions)                   | Displays inline auto-completed suggestions.                     | ![](https://img.shields.io/npm/dm/slate-suggestions.svg?maxAge=3600\&label=%E2%AC%87)          |
| [`slate-trailing-block`](https://yarnpkg.com/en/package/slate-trailing-block)             | Ensure that documents end in a specific kind of block.          | ![](https://img.shields.io/npm/dm/slate-trailing-block.svg?maxAge=3600\&label=%E2%AC%87)       |
| [`slate-instant-replace`](https://www.npmjs.com/package/slate-instant-replace)            | Automatically transform last word typed.                        | ![](https://img.shields.io/npm/dm/slate-instant-replace.svg?maxAge=3600\&label=%E2%AC%87)      |

Find more plugins on [npm](https://www.npmjs.com/search?q=slate%20plugin\&page=0\&perPage=20) or [yarn](https://yarnpkg.com/en/packages?q=slate%20plugin\&p=1).

## Components

Components for building Slate editors.

| **Plugin**                                                                | **Description**                            | **Downloads**                                                                          |
| ------------------------------------------------------------------------- | ------------------------------------------ | -------------------------------------------------------------------------------------- |
| [`slate-editor-icons`](https://yarnpkg.com/en/package/slate-editor-icons) | A set of icons for using in toolbars, etc. | ![](https://img.shields.io/npm/dm/slate-editor-icons.svg?maxAge=3600\&label=%E2%AC%87) |

## Serializers

Serializers for handling Slate data.

| **Plugin**                                                                          | **Description**                                 | **Downloads**                                                                               |
| ----------------------------------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [`slate-base64-serializer`](https://yarnpkg.com/en/package/slate-base64-serializer) | A base64 string serializer for Slate documents. | ![](https://img.shields.io/npm/dm/slate-base64-serializer.svg?maxAge=3600\&label=%E2%AC%87) |
| [`slate-html-serializer`](https://yarnpkg.com/en/package/slate-html-serializer)     | An HTML serializer for Slate documents.         | ![](https://img.shields.io/npm/dm/slate-html-serializer.svg?maxAge=3600\&label=%E2%AC%87)   |
| [`slate-plain-serializer`](https://yarnpkg.com/en/package/slate-plain-serializer)   | A plain text serializer for Slate documents.    | ![](https://img.shields.io/npm/dm/slate-plain-serializer.svg?maxAge=3600\&label=%E2%AC%87)  |

## Utils

Useful utilities when working with Slate documents and components.

| **Plugin**                                                              | **Description**                                             | **Downloads**                                                                         |
| ----------------------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| [`slate-hyperprint`](https://yarnpkg.com/en/package/slate-hyperprint)   | Prints Slate documents in their `slate-hyperscript` format. | ![](https://img.shields.io/npm/dm/slate-hyperprint.svg?maxAge=3600\&label=%E2%AC%87)  |
| [`slate-hyperscript`](https://yarnpkg.com/en/package/slate-hyperscript) | Allows you to express Slate documents in JSX.               | ![](https://img.shields.io/npm/dm/slate-hyperscript.svg?maxAge=3600\&label=%E2%AC%87) |
| [`slate-prop-types`](https://yarnpkg.com/en/package/slate-prop-types)   | A set of prop types to use in your Slate components.        | ![](https://img.shields.io/npm/dm/slate-prop-types.svg?maxAge=3600\&label=%E2%AC%87)  |


# Resources

A few resources that are helpful for building with Slate.

## Libraries

These libraries are helpful when developing with Slate:

* [`is-hotkey`](https://github.com/ianstormtaylor/is-hotkey) is a simple way to check whether an `onKeyDown` handler should fire for a given hotkey, handling cross-platform concerns like cmd vs. ctrl keys for you automatically.
* [`react-broadcast`](https://github.com/ReactTraining/react-broadcast) works well when you need to have your custom node components re-render based on state that lives outside the `document`. It's the same pattern that `react-router` uses to update `<Link>` components.

## Tools

These tools are helpful when developing with Slate:

* [Immutable.js Console Extension](https://github.com/mattzeunert/immutable-object-formatter-extension) greatly improves the `console.log` output when working with [Immutable.js](https://immutable-js.github.io/immutable-js/) objects, which Slate's data model is based on.

## Products

These products use Slate, and can give you an idea of what's possible:

* [Cake](https://www.cake.co/)
* [Archbee](https://archbee.io)
* [Chatterbug](https://chatterbug.com)
* [GitBook](https://www.gitbook.com/)
* [Grafana](https://grafana.com/)
* [Guilded](https://www.guilded.gg)
* [Guru](https://www.getguru.com/)
* [Netlify CMS](https://www.netlifycms.org)
* [Outline](https://www.getoutline.com/)
* [Prezly](https://www.prezly.com/)
* [Sanity.io](https://www.sanity.io)
* [Taskade](https://www.taskade.com/)
* [Yuque](https://www.yuque.com/)
* [Thoughts](https://thoughts.teambition.com)

## Editors

These pre-packaged editors are built on top of Slate, and can be helpful to see how you might structure your code:

* [Canner Editor](https://github.com/Canner/canner-slate-editor) is a rich text editor.
* [French Press Editor](https://github.com/roast-cms/french-press-editor) is a customizeable editor with offline support.
* [Nossas Editor](http://slate-editor.bonde.org/) is a drop-in WYSIWYG editor.
* [ORY Editor](https://editor.ory.am/) is a self-contained, inline WYSIWYG editor library.
* [Outline Editor](https://github.com/outline/rich-markdown-editor) is the editor that powers the [Outline](https://www.getoutline.com/) wiki.
* [Chatterslate](https://github.com/chatterbugapp/chatterslate) helps teach language grammar and more at [Chatterbug](https://chatterbug.com).

(Or, if you have their exact use case, can be a drop-in editor for you.)


# Contributing

Want to contribute to Slate? That would be awesome!

* [Reporting Bugs](#reporting-bugs)
* [Asking Questions](#asking-questions)
* [Submitting Pull Requests](#submitting-pull-requests)
* [Running Examples](#running-examples)
* [Running Tests](#running-tests)
* [Running Benchmarks](#running-benchmarks)
* [Adding Browser Support](#adding-browser-support)
* [Testing Input Methods](#testing-input-methods)
* [Debugging Slate Methods](#debugging-slate-methods)
* [Publishing Releases](#publishing-releases)

## Reporting Bugs

If you run into any weird behavior while using Slate, feel free to open a new issue in this repository! Please run a **search before opening** a new issue, to make sure that someone else hasn't already reported or solved the bug you've found.

Any issue you open must include:

* A [JSFiddle](https://jsfiddle.net/fj9dvhom/1/) that reproduces the bug with a minimal setup.
* A GIF showing the issue in action. (Using something like [RecordIt](http://recordit.co/).)
* A clear explanation of what the issue is.

Here's a [JSFiddle template for Slate](https://jsfiddle.net/fj9dvhom/1/) to get you started:

[![](https://3865473779-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-Kuki-R9UbW5PP_Bubk1%2Fsync%2F66396f019726dbba2a0d3ac51c6646bf0d2ac7c8.png?generation=1617228083280473\&alt=media)](https://jsfiddle.net/fj9dvhom/1/)

## Asking Questions

We've also got a [Slate Slack team](https://slate-slack.herokuapp.com) where you can ask questions and get answers from other people using Slate:

[![](https://3865473779-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-Kuki-R9UbW5PP_Bubk1%2Fsync%2F716e1274ecb5f8affb0be7c427024c196195340b.png?generation=1617228087526642\&alt=media)](https://slate-slack.herokuapp.com)

Please use the Slack instead of asking questions in issues, since we want to reserve issues for keeping track of bugs and features. We close questions in issues so that maintaining the project isn't overwhelming.

## Submitting Pull Requests

All pull requests are super welcomed and greatly appreciated! Issues in need of a solution are marked with a [`♥ help please`](https://github.com/ianstormtaylor/slate/issues?q=is%3Aissue+is%3Aopen+label%3A%22%E2%99%A5+help+please%22) label if you're looking for somewhere to start.

Please include tests and docs with every pull request!

## Running Examples

Check out the [Examples readme](https://github.com/ianstormtaylor/slate/tree/73a0b6024d9fc57e94ccc4037ca780df4b25bf12/examples/Readme.md) to see how to get the examples running locally!

## Running Tests

To run the tests, you need to have the Slate repository cloned to your computer. After that, you need to `cd` into the directory where you cloned it, and install the dependencies with `yarn` and build the monorepo:

```
yarn install
yarn build
```

Then run the tests with:

```
yarn test
```

To keep the source rebuilding on every file change, you need to run an additional watching command in a separate process:

```
yarn watch
```

If you need to debug something, you can add a `debugger` line to the source, and then run `yarn test debug`.

If you only want to run a specific test or tests, you can run `yarn test --fgrep="slate-react rendering"` flag which will filter the tests being run by grepping for the string in each test.

## Running Benchmarks

To run the benchmarks, first make some changes to the source that you want to benchmark. Now that you're ready, you need to save a "baseline" for what the performance was before you made you change.

To do that, stash your changes and save the benchmarks:

```
git stash
yarn benchmark:save
```

Then once the reference has been saved, unstash your changes and run the benchmarks to see a comparison:

```
git stash pop
yarn benchmark
```

There will be some subtle changes in iteration speed always, but the comparison reporter will highlight any changes that seem meaningful. You can run `benchmark` multiple times to ensure the speed up persists.

### Run Selected Benchmarks

To run selected benchmarks, create `tmp/benchmark-config.js` with `module.exports.include`. For example, to run slate-core benchmarks only with `get-*`, we can create a `tmp/benchmark-config.js` as

```
module.exports.include = {
  slate: /^get/
}
```

## Adding Browser Support

Slate aims to targeted all of the modern browsers, and eventually the modern mobile platforms. Right now browser support is limited to the latest versions of [Chrome](https://www.google.com/chrome/browser/desktop/), [Firefox](https://www.mozilla.org/en-US/firefox/new/), and [Safari](http://www.apple.com/safari/), but if you are interested in adding support for another modern platform, that is welcomed!

## Testing Input Methods

[Here's a helpful page](https://github.com/Microsoft/vscode/wiki/IME-Test) detailing how to test various input scenarios on Windows, Mac and Linux.

## Debugging Slate Methods

Slate makes use of [debug](https://github.com/visionmedia/debug) to log information about various methods. You can [enable the logger in the browser](https://github.com/visionmedia/debug#browser-support) by setting `localStorage.debug = "*"` (to log methods on all modules) or to a single namespace (e.g. `slate:editor`). Look for `const debug = Debug('<namespace>')` to get the namespace of various modules.

## Publishing Releases

Since we use [Lerna](https://lernajs.io) to manage the Slate packages this is fairly easy, **but** you must make sure you are using `npm` to run the release script, because using `yarn` results in failures. So just run:

```javascript
npm run release
```

And follow the prompts Lerna gives you.


# Changelog

Since Slate is a monorepo with many packages that are versioned separately, we maintain a changelog for each individual package:

* [`slate`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate/Changelog.md)
* [`slate-base64-serializer`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate-base64-serializer/Changelog.md)
* [`slate-html-serializer`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate-html-serializer/Changelog.md)
* [`slate-hyperscript`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate-hyperscript/Changelog.md)
* [`slate-plain-serializer`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate-plain-serializer/Changelog.md)
* [`slate-prop-types`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate-prop-types/Changelog.md)
* [`slate-react`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate-react/Changelog.md)
* [`slate-simulator`](https://github.com/ianstormtaylor/slate/tree/master/packages/slate-simulator/Changelog.md)


# FAQ

A series of common questions people have about Slate:

* [Why is content pasted as plain text?](#why-is-content-is-pasted-as-plain-text)
* [What can a `Block` node have as its children?](#what-can-a-block-node-have-as-its-children)
* [What browsers and devices does Slate support?](#what-browsers-and-devices-does-slate-support)

## Why is content pasted as plain text?

One of Slate's core principles is that, unlike most other editors, it does **not** prescribe a specific "schema" to the content you are editing. This means that Slate's core has no concept of "block quotes" or "bold formatting".

For the most part, this leads to increased flexbility without many downsides, but there are certain cases where you have to do a bit more work. Pasting is one of those cases.

Since Slate knows nothing about your schema, it can't know how to parse pasted HTML content (or other content). So, by default whenever a user pastes content into a Slate editor, it will parse it as plain text. If you want it to be smarter about pasted content, you need to define an [`onPaste`](https://docs.slatejs.org/slate-react/editor#onpaste) handler that parses the content as you wish.

## What can a `Block` node have as its children?

With Slate, you can use `Block` node to created complex nested structures. Block nodes may contain nested block nodes (both void and non-void), inline nodes, text nodes and just regular DOM elements (with `contentEditable = {false}`).

If you have an element that is not going to be editable, you can choose between a `void` node or just a DOM element with `contentEditable = {false}`. Opt for the `void` node if you would like it represented in the Slate schema, and for Slate to be aware of it.

## What browsers and devices does Slate support?

Slate's goal is to support all the modern browsers on both desktop and mobile devices.

However, right now Slate is in beta and is community-driven, so its support is not as robust as it could be. It's currently tested against the latest few versions of Chrome, Firefox and Safari on desktops. It isn't currently tested against Internet Explorer or Edge, or against mobile devices. If you want to add more browser or device support, we'd love for you to submit a pull request!

For older browsers, such as IE11, a lot of the now standard native APIs aren't available. Slate's position on this is that it is up to the user to bring polyfills (like <https://polyfill.io>) when needed for things like `el.closest`, etc. Otherwise we'd have to bundle and maintain lots of polyfills that others may not even need in the first place.


# Glossary

A glossary explaining the terms commonly used in Slate:

## Anchor

An *"anchor point"* is a point where a range starts.

![Anchor Point](https://3865473779-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-Kuki-R9UbW5PP_Bubk1%2Fsync%2F121a812f4dfd647acb41631642d69286deb42023.gif?generation=1617228084460636\&alt=media)

## Block

## Blur

## Change

## Character

A *"character"* is the smallest element that makes up a text node in Slate.

## Collapsed

A selection is *"collapsed"* when text is deselected. A collapse occurs when a range's start and end points are the same.

![Deselection](https://3865473779-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-Kuki-R9UbW5PP_Bubk1%2Fsync%2F0b3650972071ba3e9d2457a1725a1083f3425076.gif?generation=1617228086409042\&alt=media)

## Core

## Data

## Decoration

## Document

The *"document"* is the top-level ["node"](#node) that contains all other nodes that make up the content of the Slate editor.

## Editor

## Extend

## Focus

Focus is defined differently based on your context:

### Focus Point

A *"focus point"* is where a range ends. Unlike a anchor point, a focus point can be expanded.

![Focus Point](https://3865473779-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-Kuki-R9UbW5PP_Bubk1%2Fsync%2Fc1b6fa24a0f157988d3a80a41b79bed2b18d8601.gif?generation=1617228083437675\&alt=media)

### Focus Block

The editor value provides a reference to the current *"focus block"* as a convenience. For example, you access the words within the block a user is focused on like so: `const words = editor.value.focusBlock.text.split(' ');`

## Fragment

## History

## Inline

## Key

A *"keys"* is a unique identifier assigned to a node in Slate and is used to reference a node uniquely. As as the document changes, new unique keys are issued to avoid collisions within the data model.

## Mark

A *"mark"* represents formatting data that is attached to characters within text. Standard formatting such as **bold**, *italic*, `code`, or custom formatting for your application can be implemented using marks.

## Match

A `match`, is an object with possible fields of `type` and `object` that are used to *match* `Nodes` when defining rules in a [Schema](https://docs.slatejs.org/slate-core/schema). An example of `match` could be `{type: 'paragraph'}`, `{objet: 'inline', type: '@-tag'}`, etc.

## Merge

## Model

## Node

## Normalize

## Offset

An *"offset"* is a distance from the start of a text node, measured in ["characters"](#character).

## Operation

## Placeholder

## Plugin

A *"plugin"* is a reusable object that implements one or more of Slate's plugin hooks to add specific behavior to your editor. A plugin helps you express your application while keeping it easy to maintain and reason about.

## Point

A *"point"* represents a specific location in a document, where a user's cursor could be placed. It is represented by the `key` of the node in the document, and the `offset` of characters into a node.

## Range

A *"range"* is a way to represent a specific section of a document between two ["points"](#point). It is modelled after the [DOM Range](https://developer.mozilla.org/en-US/docs/Web/API/Range) concept.

## Redo

## Rule

## Schema

A Slate *"schema"* is a JavaScript object with properties that describe the document, block nodes, and inline nodes in your editor. Every Slate editor has a "schema" associated with it, which contains information about the structure of its content. For the most basic cases, you'll just rely on Slate's default core schema. But for advanced use cases, you can enforce rules about what the content of a Slate document can contain. Read [Schema reference](https://docs.slatejs.org/slate-core/schema) to learn more.

## Selection

## Serializer

## Split

## Stack

## Text

## Undo

## Unwrap

To *"unwrap"* is the opposite of to ["wrap"](#wrap), removing a surrounding node from a selection.

## Validate

## Value

A Slate *"value"* is the top-level object in Slate and is an object encapsulating the entire value of a Slate editor. Read the [Data Model guide](https://docs.slatejs.org/guides/data-model#the-value) to learn more.

## Wrap

To *"wrap"* is to surround a piece of text or a node in another node. For example, if you select the text `Google` and want to turn it into a link, you'd "wrap" it with an inline link node.


# Block

```javascript
import { Block } from 'slate'
```

A block node in a Slate [`Document`](https://docs.slatejs.org/slate-core/document). Block nodes implement the [`Node`](https://docs.slatejs.org/slate-core/node) interface.

Block nodes may contain nested block nodes, inline nodes, and text nodes—just like in the DOM. They always contain at least one text node child.

## Properties

```javascript
Block({
  data: Data,
  key: String,
  nodes: Immutable.List<Node>,
  type: String
})
```

### `data`

`Immutable.Map`

Arbitrary data associated with the node. Defaults to an empty `Map`.

### `key`

`String`

A unique identifier for the node.

### `object`

`String`

An immutable string value of `'block'` for easily separating this node from [`Inline`](https://docs.slatejs.org/slate-core/inline) or [`Text`](https://docs.slatejs.org/slate-core/text) nodes.

### `nodes`

`Immutable.List`

A list of child nodes. Defaults to a list with a single text node child.

### `type`

`String`

The custom type of the node (eg. `blockquote` or `list-item`).

## Computed Properties

### `text`

`String`

A concatenated string of all of the descendant [`Text`](https://docs.slatejs.org/slate-core/text) nodes of this node.

## Static Methods

### `Block.create`

`Block.create(properties: Object) => Block`

Create a block from a plain JavaScript object of `properties`.

### `Block.createList`

`Block.createList(array: Array) => List`

Create a list of block nodes from a plain JavaScript `array`.

### `Block.fromJSON`

`Block.fromJSON(object: Object) => Block`

Create a block from a JSON `object`.

### `Block.isBlock`

`Block.isBlock(maybeBlock: Any) => Boolean`

Returns a boolean if the passed in argument is a `Block`.

## Node Methods

Blocks implement the [`Node`](https://docs.slatejs.org/slate-core/node) interface. For information about all of the node methods, see the [`Node` reference](https://docs.slatejs.org/slate-core/node).

## Instance Methods

### `toJSON`

`toJSON() => Object`

Returns a JSON representation of the block.


# Commands

The core `Editor` ships with a bunch of built-in commands that provide common behaviors for rich text editors.

## Current Selection Commands

These commands act on the `document` based on the current `selection`. They are equivalent to calling the [Document Range Commands](#document-range-commands) with the current selection as the `range` argument, but they are there for convenience, since you often want to act with the current selection, as a user would.

### `addMark`

`addMark(mark: Mark) => Editor` \
&#x20;`addMark(properties: Object) => Editor` \
&#x20;`addMark(type: String) => Editor`

Add a [`Mark`](https://docs.slatejs.org/slate-core/mark) to the characters in the current selection. For convenience, you can pass a `type` string or `properties` object to implicitly create a [`Mark`](https://docs.slatejs.org/slate-core/mark) of that type.

### `delete`

`delete() => Editor`

Delete everything in the current selection.

### `insertBlock`

`insertBlock(block: Block) => Editor` \
&#x20;`insertBlock(properties: Object) => Editor` \
&#x20;`insertBlock(type: String) => Editor`

Insert a new block at the same level as the current block, splitting the current block to make room if it is non-empty. If the selection is expanded, it will be deleted first.

### `deleteBackward`

`deleteBackward(n: Number) => Editor`

Delete backward `n` characters at the current cursor. If the selection is expanded, this method is equivalent to a regular [`delete()`](#delete). `n` defaults to `1`.

### `deleteForward`

`deleteForward(n: Number) => Editor`

Delete forward `n` characters at the current cursor. If the selection is expanded, this method is equivalent to a regular [`delete()`](#delete). `n` defaults to `1`.

### `insertFragment`

`insertFragment(fragment: Document) => Editor`

Insert a [`fragment`](https://docs.slatejs.org/slate-core/document) at the current selection. If the selection is expanded, it will be deleted first.

### `insertInline`

`insertInline(inline: Inline) => Editor` \
&#x20;`insertInline(properties: Object) => Editor`

Insert a new inline at the current cursor position, splitting the text to make room if it is non-empty. If the selection is expanded, it will be deleted first.

### `insertText`

`insertText(text: String) => Editor`

Insert a string of `text` at the current selection. If the selection is expanded, it will be deleted first.

### `setBlocks`

`setBlocks(properties: Object) => Editor` \
&#x20;`setBlocks(type: String) => Editor`

Set the `properties` of the [`Blocks`](https://docs.slatejs.org/slate-core/block) in the current selection. For convenience, you can pass a `type` string to set the blocks' type only.

### `setInlines`

`setInlines(properties: Object) => Editor` \
&#x20;`setInlines(type: String) => Editor`

Set the `properties` of the [`Inlines`](https://docs.slatejs.org/slate-core/inline) nodes in the current selection. For convenience, you can pass a `type` string to set the inline nodes' type only.

### `splitBlock`

`splitBlock(depth: Number) => Editor`

Split the [`Block`](https://docs.slatejs.org/slate-core/block) in the current selection by `depth` levels. If the selection is expanded, it will be deleted first. `depth` defaults to `1`.

### `splitInline`

`splitInline(depth: Number) => Editor`

Split the [`Inline`](https://docs.slatejs.org/slate-core/inline) node in the current selection by `depth` levels. If the selection is expanded, it will be deleted first. `depth` defaults to `Infinity`.

### `removeMark`

`removeMark(mark: Mark) => Editor` \
&#x20;`removeMark(properties: Object) => Editor` \
&#x20;`removeMark(type: String) => Editor`

Remove a [`Mark`](https://docs.slatejs.org/slate-core/mark) from the characters in the current selection. For convenience, you can pass a `type` string or `properties` object to implicitly create a [`Mark`](https://docs.slatejs.org/slate-core/mark) of that type.

### `replaceMark`

`replaceMark(oldMark: Mark, newMark: Mark) => Editor` \
&#x20;`replaceMark(oldProperties: Object, newProperties: Object) => Editor` \
&#x20;`replaceMark(oldType: String, newType: String) => Editor`

Replace a [`Mark`](https://docs.slatejs.org/slate-core/mark) in the characters in the current selection. For convenience, you can pass a `type` string or `properties` object to implicitly create a [`Mark`](https://docs.slatejs.org/slate-core/mark) of that type.

### `toggleMark`

`toggleMark(mark: Mark) => Editor` \
&#x20;`toggleMark(properties: Object) => Editor` \
&#x20;`toggleMark(type: String) => Editor`

Add or remove a [`Mark`](https://docs.slatejs.org/slate-core/mark) from the characters in the current selection, depending on it already exists on any or not. For convenience, you can pass a `type` string or `properties` object to implicitly create a [`Mark`](https://docs.slatejs.org/slate-core/mark) of that type.

### `unwrapBlock`

`unwrapBlock(type: String) => Editor` \
&#x20;`unwrapBlock(properties: Object) => Editor` <br>

Unwrap all [`Block`](https://docs.slatejs.org/slate-core/block) nodes in the current selection that match a `type` and/or `data`.

### `unwrapInline`

`unwrapInline(type: String) => Editor` \
&#x20;`unwrapInline(properties: Object) => Editor` <br>

Unwrap all [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in the current selection that match a `type` and/or `data`.

### `wrapBlock`

`wrapBlock(type: String) => Editor` \
&#x20;`wrapBlock(properties: Object) => Editor` <br>

Wrap the [`Block`](https://docs.slatejs.org/slate-core/block) nodes in the current selection with a new [`Block`](https://docs.slatejs.org/slate-core/block) node of `type`, with optional `data`.

### `wrapInline`

`wrapInline(type: String) => Editor` \
&#x20;`wrapInline(properties: Object) => Editor` <br>

Wrap the [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in the current selection with a new [`Inline`](https://docs.slatejs.org/slate-core/inline) node of `type`, with optional `data`.

### `wrapText`

`wrapText(prefix: String, [suffix: String]) => Editor`

Surround the text in the current selection with `prefix` and `suffix` strings. If the `suffix` is ommitted, the `prefix` will be used instead.

## Selection Commands

These commands change the current `selection`, without touching the `document`.

### `blur`

`blur() => Editor`

Blur the current selection.

### `deselect`

`deselect() => Editor`

Unset the selection.

### `flip`

`flip() => Editor`

Flip the selection.

### `focus`

`focus() => Editor`

Focus the current selection.

### `move{Point}Backward`

`move{Point}Backward(n: Number) => Editor`

Move the `{Point}` of the selection backward `n` characters. Where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}Forward`

`move{Point}Forward(n: Number) => Editor`

Move the `{Point}` of the selection forward `n` characters. Where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To`

`moveTo(path: List, offset: Number) => Editor` `moveTo(key: String, offset: Number) => Editor` `moveTo(offset: Number) => Editor`

Move the `{Point}` of the selection to a new `path` or `key` and `offset`. Where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `moveTo{Point}`

`moveTo{Point}() => Editor`

Collapse the current selection to one of its points. Where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`.

### `move{Point}To{Edge}OfBlock`

`move{Point}To{Edge}OfBlock() => Editor`

Move the current selection to the `{Edge}` of the closest block parent. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To{Edge}OfDocument`

`move{Point}To{Edge}OfDocument() => Editor`

Move the current selection to the `{Edge}` of the document. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To{Edge}OfInline`

`move{Point}To{Edge}OfInline() => Editor`

Move the current selection to the `{Edge}` of the closest inline parent. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To{Edge}OfNode`

`move{Point}To{Edge}OfNode(node: Node) => Editor`

Move the current selection to the `{Edge}` of a `node`. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To{Edge}OfText`

`move{Point}To{Edge}OfText() => Editor`

Move the current selection to the `{Edge}` of the current text node. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To{Edge}Of{Direction}Block`

`move{Point}To{Edge}Of{Direction}Block() => Editor`

Move the current selection to the `{Edge}` of the closest block parent. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To{Edge}Of{Direction}Inline`

`move{Point}To{Edge}Of{Direction}Inline() => Editor`

Move the current selection to the `{Edge}` of the closest inline parent. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `move{Point}To{Edge}Of{Direction}Text`

`move{Point}To{Edge}Of{Direction}Text() => Editor`

Move the current selection to the `{Edge}` of the current text node. Where `{Edge}` is either `Start` or `End`. And where `{Point}` is either `Anchor`, `Focus`, `Start` or `End`. You can also omit `{Point}` to move both the anchor and focus points at the same time.

### `moveToRangeOfNode`

`moveToRangeOfNode(node: Node) => Editor`

Move the current selection's anchor point to the start of a `node` and its focus point to the end of the `node`.

### `moveToRangeOfDocument`

`moveToRangeOfDocument() => Editor`

Move the current selection's anchor point to the start of the document and its focus point to the end of the document, selecting everything.

### `select`

`select(properties: Range || Object) => Editor`

Set the current selection to a range with merged `properties`. The `properties` can either be a [`Range`](https://docs.slatejs.org/slate-core/range) object or a plain JavaScript object of selection properties.

## Document Range Commands

These commands act on a specific [`Range`](https://docs.slatejs.org/slate-core/range) of the document.

### `addMarkAtRange`

`addMarkAtRange(range: Range, mark: Mark) => Editor` \
&#x20;`addMarkAtRange(range: Range, properties: Object) => Editor` \
&#x20;`addMarkAtRange(range: Range, type: String) => Editor`

Add a [`Mark`](https://docs.slatejs.org/slate-core/mark) to the characters in a `range`. For convenience, you can pass a `type` string or `properties` object to implicitly create a [`Mark`](https://docs.slatejs.org/slate-core/mark) of that type.

### `deleteAtRange`

`deleteAtRange(range: Range, ) => Editor`

Delete everything in a `range`.

### `deleteBackwardAtRange`

`deleteBackwardAtRange(range: Range, n: Number) => Editor`

Delete backward `n` characters at a `range`. If the `range` is expanded, this method is equivalent to a regular [`delete()`](#delete). `n` defaults to `1`.

### `deleteForwardAtRange`

`deleteForwardAtRange(range: Range, n: Number) => Editor`

Delete forward `n` characters at a `range`. If the `range` is expanded, this method is equivalent to a regular [`delete()`](#delete). `n` defaults to `1`.

### `insertBlockAtRange`

`insertBlockAtRange(range: Range, block: Block) => Editor` \
&#x20;`insertBlockAtRange(range: Range, properties: Object) => Editor` \
&#x20;`insertBlockAtRange(range: Range, type: String) => Editor`

Insert a new block at the same level as the leaf block at a `range`, splitting the current block to make room if it is non-empty. If the selection is expanded, it will be deleted first.

### `insertFragmentAtRange`

`insertFragmentAtRange(range: Range, fragment: Document) => Editor`

Insert a [`fragment`](https://docs.slatejs.org/slate-core/document) at a `range`. If the selection is expanded, it will be deleted first.

### `insertInlineAtRange`

`insertInlineAtRange(range: Range, inline: Inline) => Editor` \
&#x20;`insertInlineAtRange(range: Range, properties: Object) => Editor`

Insert a new inline at a `range`, splitting the text to make room if it is non-empty. If the selection is expanded, it will be deleted first.

### `insertTextAtRange`

`insertTextAtRange(range: Range, text: String) => Editor`

Insert a string of `text` at a `range`. If the selection is expanded, it will be deleted first.

### `setBlocksAtRange`

`setBlocksAtRange(range: Range, properties: Object) => Editor` \
&#x20;`setBlocks(range: Range, type: String) => Editor`

Set the `properties` of the [`Blocks`](https://docs.slatejs.org/slate-core/block) in a `range`. For convenience, you can pass a `type` string to set the blocks' type only.

### `setInlinesAtRange`

`setInlinesAtRange(range: Range, properties: Object) => Editor` \
&#x20;`setInlines(range: Range, type: String) => Editor`

Set the `properties` of the [`Inlines`](https://docs.slatejs.org/slate-core/inline) nodes in a `range`. For convenience, you can pass a `type` string to set the inline nodes' type only.

### `splitBlockAtRange`

`splitBlockAtRange(range: Range, depth: Number) => Editor`

Split the [`Block`](https://docs.slatejs.org/slate-core/block) in a `range` by `depth` levels. If the selection is expanded, it will be deleted first. `depth` defaults to `1`.

### `splitInlineAtRange`

`splitInlineAtRange(range: Range, depth: Number) => Editor`

Split the [`Inline`](https://docs.slatejs.org/slate-core/inline) node in a `range` by `depth` levels. If the selection is expanded, it will be deleted first. `depth` defaults to `Infinity`.

### `removeMarkAtRange`

`removeMarkAtRange(range: Range, mark: Mark) => Editor` \
&#x20;`removeMarkAtRange(range: Range, properties: Object) => Editor` \
&#x20;`removeMarkAtRange(range: Range, type: String) => Editor`

Remove a [`Mark`](https://docs.slatejs.org/slate-core/mark) from the characters in a `range`. For convenience, you can pass a `type` string or `properties` object to implicitly create a [`Mark`](https://docs.slatejs.org/slate-core/mark) of that type.

### `toggleMarkAtRange`

`toggleMarkAtRange(range: Range, mark: Mark) => Editor` \
&#x20;`toggleMarkAtRange(range: Range, properties: Object) => Editor` \
&#x20;`toggleMarkAtRange(range: Range, type: String) => Editor`

Add or remove a [`Mark`](https://docs.slatejs.org/slate-core/mark) from the characters in a `range`, depending on whether any of them already have the mark. For convenience, you can pass a `type` string or `properties` object to implicitly create a [`Mark`](https://docs.slatejs.org/slate-core/mark) of that type.

### `unwrapBlockAtRange`

`unwrapBlockAtRange(range: Range, properties: Object) => Editor` \
&#x20;`unwrapBlockAtRange(range: Range, type: String) => Editor`

Unwrap all [`Block`](https://docs.slatejs.org/slate-core/block) nodes in a `range` that match `properties`. For convenience, you can pass a `type` string or `properties` object.

### `unwrapInlineAtRange`

`unwrapInlineAtRange(range: Range, properties: Object) => Editor` \
&#x20;`unwrapInlineAtRange(range: Range, type: String) => Editor`

Unwrap all [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in a `range` that match `properties`. For convenience, you can pass a `type` string or `properties` object.

### `wrapBlockAtRange`

`wrapBlockAtRange(range: Range, properties: Object) => Editor` \
&#x20;`wrapBlockAtRange(range: Range, type: String) => Editor`

Wrap the [`Block`](https://docs.slatejs.org/slate-core/block) nodes in a `range` with a new [`Block`](https://docs.slatejs.org/slate-core/block) node with `properties`. For convenience, you can pass a `type` string or `properties` object.

### `wrapInlineAtRange`

`wrapInlineAtRange(range: Range, properties: Object) => Editor` \
&#x20;`wrapInlineAtRange(range: Range, type: String) => Editor`

Wrap the [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in a `range` with a new [`Inline`](https://docs.slatejs.org/slate-core/inline) node with `properties`. For convenience, you can pass a `type` string or `properties` object.

### `wrapTextAtRange`

`wrapTextAtRange(range: Range, prefix: String, [suffix: String]) => Editor`

Surround the text in a `range` with `prefix` and `suffix` strings. If the `suffix` is ommitted, the `prefix` will be used instead.

## Node Commands

These commands are lower-level, and act on a specific node by its `key` or `path`. They're often used in your custom components because you'll have access to `props.node`.

### `addMarkByKey/Path`

`addMarkByKey(key: String, offset: Number, length: Number, mark: Mark) => Editor` `addMarkByPath(path: List, offset: Number, length: Number, mark: Mark) => Editor`

Add a `mark` to `length` characters starting at an `offset` in a [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`.

### `insertNodeByKey/Path`

`insertNodeByKey(key: String, index: Number, node: Node) => Editor` `insertNodeByPath(path: List, index: Number, node: Node) => Editor`

Insert a `node` at `index` inside a parent [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`.

### `insertFragmentByKey/Path`

`insertFragmentByKey(key: String, index: Number, fragment: Fragment) => Transform` `insertFragmentByPath(path: list, index: Number, fragment: Fragment) => Transform`

Insert a [`Fragment`](https://github.com/ianstormtaylor/slate/tree/a0b7976cb9a2812d8d96361e9993fe8853a2cc64/docs/reference/slate/fragment.md) at `index` inside a parent [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`.

### `insertTextByKey/Path`

`insertTextByKey(key: String, offset: Number, text: String, [marks: Set]) => Editor` `insertTextByPath(path: List, offset: Number, text: String, [marks: Set]) => Editor`

Insert `text` at an `offset` in a [`Text Node`](https://docs.slatejs.org/slate-core/text) by its `key` with optional `marks`.

### `mergeNodeByKey/Path`

`mergeNodeByKey(key: String) => Editor` `mergeNodeByPath(path: List) => Editor`

Merge a [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path` with its previous sibling.

### `moveNodeByKey/Path`

`moveNodeByKey(key: String, newKey: String, newIndex: Number) => Editor` `moveNodeByPath(path: List, newKey: String, newIndex: Number) => Editor`

Move a [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path` to a new parent node with its `newKey` and at a `newIndex`.

### `removeMarkByKey/Path`

`removeMarkByKey(key: String, offset: Number, length: Number, mark: Mark) => Editor` `removeMarkByPath(path: List, offset: Number, length: Number, mark: Mark) => Editor`

Remove a `mark` from `length` characters starting at an `offset` in a [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`.

### `removeNodeByKey/Path`

`removeNodeByKey(key: String) => Editor` `removeNodeByPath(path: List) => Editor`

Remove a [`Node`](https://docs.slatejs.org/slate-core/node) from the document by its `key` or `path`.

### `replaceNodeByKey/Path`

`replaceNodeByKey(key: String, node: Node) => Editor` `replaceNodeByPath(path: List, node: Node) => Editor`

Replace a [`Node`](https://docs.slatejs.org/slate-core/node) in the document with a new [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`.

### `removeTextByKey/Path`

`removeTextByKey(key: String, offset: Number, length: Number) => Editor` `removeTextByPath(path: List, offset: Number, length: Number) => Editor`

Remove `length` characters of text starting at an `offset` in a [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`.

### `setMarkByKey/Path`

`setMarkByKey(key: String, offset: Number, length: Number, properties: Object, newProperties: Object) => Editor` `setMarkByPath(path: List, offset: Number, length: Number, properties: Object, newProperties: Object) => Editor`

Set a dictionary of `newProperties` on a [`Mark`](https://docs.slatejs.org/slate-core/mark) on a [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`.

### `setNodeByKey/Path`

`setNodeByKey(key: String, properties: Object) => Editor` \
&#x20;`setNodeByKey(key: String, type: String) => Editor` `setNodeByPath(path: List, properties: Object) => Editor` \
&#x20;`setNodeByPath(path: List, type: String) => Editor`

Set a dictionary of `properties` on a [`Node`](https://docs.slatejs.org/slate-core/node) by its `key` or `path`. For convenience, you can pass a `type` string or `properties` object.

### `splitNodeByKey/Path`

`splitNodeByKey(key: String, offset: Number) => Editor` `splitNodeByPath(path: List, offset: Number) => Editor`

Split a node by its `key` or `path` at an `offset`.

### `unwrapInlineByKey/Path`

`unwrapInlineByKey(key: String, properties: Object) => Editor` \
&#x20;`unwrapInlineByKey(key: String, type: String) => Editor` `unwrapInlineByPath(path: List, properties: Object) => Editor` \
&#x20;`unwrapInlineByPath(path: List, type: String) => Editor`

Unwrap all inner content of an [`Inline`](https://docs.slatejs.org/slate-core/inline) node by its `key` or `path` that match `properties`. For convenience, you can pass a `type` string or `properties` object.

### `unwrapBlockByKey/Path`

`unwrapBlockByKey(key: String, properties: Object) => Editor` \
&#x20;`unwrapBlockByKey(key: String, type: String) => Editor` `unwrapBlockByPath(path: List, properties: Object) => Editor` \
&#x20;`unwrapBlockByPath(path: List, type: String) => Editor`

Unwrap all inner content of a [`Block`](https://docs.slatejs.org/slate-core/block) node by its `key` or `path` that match `properties`. For convenience, you can pass a `type` string or `properties` object.

### `unwrapNodeByKey/Path`

`unwrapNodeByKey(key: String) => Editor` `unwrapNodeByPath(path: List) => Editor`

Unwrap a single node from its parent. If the node is surrounded with siblings, its parent will be split. If the node is the only child, the parent is removed, and simply replaced by the node itself. Cannot unwrap a root node.

### `wrapBlockByKey/Path`

`wrapBlockByKey(key: String, properties: Object) => Editor` \
&#x20;`wrapBlockByKey(key: String, type: String) => Editor` `wrapBlockByPath(path: List, properties: Object) => Editor` \
&#x20;`wrapBlockByPath(path: List, type: String) => Editor`

Wrap the given node in a [`Block`](https://docs.slatejs.org/slate-core/block) node that match `properties`. For convenience, you can pass a `type` string or `properties` object.

### `wrapInlineByKey/Path`

`wrapInlineByKey(key: String, properties: Object) => Editor` \
&#x20;`wrapInlineByKey(key: String, type: String) => Editor` `wrapInlineByPath(path: List, properties: Object) => Editor` \
&#x20;`wrapInlineByPath(path: List, type: String) => Editor`

Wrap the given node in a [`Inline`](https://docs.slatejs.org/slate-core/inline) node that match `properties`. For convenience, you can pass a `type` string or `properties` object.

### `wrapNodeByKey/Path`

`wrapNodeByKey(key: String, parent: Node) => Editor` \
&#x20;`wrapNodeByPath(path: List, parent: Node) => Editor` <br>

Wrap the node with the specified key with the parent [`Node`](https://docs.slatejs.org/slate-core/node). This will clear all children of the parent.

## History Commands

These commands use the history to undo/redo previously made changes.

### `redo`

`redo() => Editor`

Move forward one step in the history.

### `undo`

`undo() => Editor`

Move backward one step in the history.

### `snapshotSelection`

`snapshotSelection() => Editor`

Snapshot `value.selection` for `undo` purposes, useful with delete operations like `editor.removeNodeByKey(focusBlock.key).undo()`.

## Miscellaneous Commands

### `normalize`

`normalize() => Editor`

This method normalizes the document with the value's schema. This should run automatically-you should not need to call this method unless you have manually disabled normalization (and you should rarely, if ever, need to manually disable normalization). The vast majority of changes, whether by the user or invoked programmatically, will run `normalize` by default to ensure the document is always in adherence to its schema.

> 🤖 If you must use this method, use it sparingly and strategically. Calling this method can be very expensive as it will run normalization on all of the nodes in your document.

### `withoutNormalizing`

`withoutNormalizing(fn: Function) => Editor`

This method calls the provided function with the current instance of the `Change` object as the first argument. Normalization does not occur while the fuction is executing, and is instead deferred to be be run immediately after it completes.

This method can be used to allow a sequence of change operations that should not be interrupted by normalization. For example:

```javascript
editor.withoutNormalizing(() => {
  node.nodes.filter(n => n.object != 'block').forEach(child => {
    editor.removeNodeByKey(child.key)
  })
})
```

### `withoutSaving`

`withoutSaving(fn: Function) => Editor`

By default all new operations are saved to the editor's history. If you have changes that you don't want to show up in the history when the user presses cmd+z, you can use `withoutSaving` to skip those changes.

```javascript
editor.withoutSaving(() => {
  editor.setDecorations(decorations)
})
```

However, be sure you know what you are doing because this will create changes that cannot be undone by the user, and might result in confusing behaviors.

### `withoutMerging`

`withoutMerging(fn: Function) => Editor`

Usually, all of the operations in a `Change` are grouped into a single save point in the editor's history. However, sometimes you may want more control over this, to be able to create distinct save points in a single change. To do that, you can use the `withoutMerging` helper.


# Data

```javascript
import { Data } from 'slate'
```

Data is simply a thin wrapper around [`Immutable.Map`](https://immutable-js.github.io/immutable-js/docs/#/Map), so that you don't need to ever depend on Immutable directly, and for future compatibility.

A data object can have any properties associated with it.

## Static Methods

### `Data.create`

`Data.create(properties: Object) => Data`

Create a data object from a plain JavaScript object of `properties`.

### `Data.fromJSON`

`Data.fromJSON(object: Object) => Data`

Create a data object from a JSON `object`.


# Decoration

```javascript
import { Decoration } from 'slate'
```

A decoration is a range of the document that has a specific [`Mark`](https://docs.slatejs.org/slate-core/mark) dynamically applied to it based on its content or some other external state. It is not actually reflected in the document's structure itself. This can be useful for cases like syntax highlighting, or search result highlighting.

Decorations implement the [`Range`](https://docs.slatejs.org/slate-core/range) interface, but also contain a `mark`.

## Properties

```javascript
Decoration({
  anchor: Point,
  focus: Point,
  mark: Mark,
})
```

### `mark`

`Mark`

The mark associated with the decoration.

### `object`

`String`

A string with a value of `'decoration'`.

## Static Methods

### `Decoration.create`

`Decoration.create(properties: Object) => Decoration`

Create a new `Decoration` instance with `properties`.

### `Decoration.createProperties`

`Decoration.createProperties(object: Object|Decoration) => Object`

Create a new dictionary of range properties from an `object`.

### `Decoration.fromJSON`

`Decoration.fromJSON(object: Object) => Decoration`

Create a range from a JSON `object`.

### `Decoration.isDecoration`

`Decoration.isDecoration(value: Any) => Boolean`

Check whether a `value` is a `Decoration`.

## Instance Methods

### `toJSON`

`toJSON() => Object`

Return a JSON representation of the range.

## Mutating Methods

### `setMark`

`setMark(mark: Mark) => Decoration`

Return a new decoration with a new `mark`.


# Document

```javascript
import { Document } from 'slate'
```

The top-level node in Slate's document model.

Documents are made up of block nodes, inline nodes, and text nodes—just like in the DOM. Note that direct descendants of a document node have to be block nodes.

In some places, you'll see mention of "fragments", which are also `Document` objects, just that aren't attached to the main `Value`. For example, when cutting-and-pasting a selection of content, that content will be referred to as a document "fragment".

## Properties

```javascript
Document({
  nodes: Immutable.List<Node>,
})
```

### `data`

`Immutable.Map`

Arbitrary data associated with the document. Defaults to an empty `Map`.

### `object`

`String`

An immutable string value of `'document'` for easily separating this node from [`Block`](https://docs.slatejs.org/slate-core/block), [`Inline`](https://docs.slatejs.org/slate-core/inline) or [`Text`](https://docs.slatejs.org/slate-core/text) nodes.

### `nodes`

`Immutable.List`

A list of child nodes.

## Computed Properties

### `text`

`String`

A concatenated string of all of the descendant [`Text`](https://docs.slatejs.org/slate-core/text) nodes of this node.

## Static Methods

### `Document.create`

`Document.create(properties: Object) => Document`

Create a document from a plain JavaScript object of `properties`.

### `Document.fromJSON`

`Document.fromJSON(object: Object) => Document`

Create a document from a JSON `object`.

### `Document.isDocument`

`Document.isDocument(maybeDocument: Any) => Boolean`

Returns a boolean if the passed in argument is a `Document`.

## Node Methods

Documents implement the [`Node`](https://docs.slatejs.org/slate-core/node) interface. For information about all of the node methods, see the [`Node` reference](https://docs.slatejs.org/slate-core/node).

## Instance Methods

### `toJSON`

`toJSON() => Object`

Returns a JSON representation of the document.


# Editor

```javascript
import { Editor } from 'slate'
```

The top-level controller that holds a [`Value`](https://docs.slatejs.org/slate-core/value) over time, and contains all of the plugins that determine the editor's behavior.

> 🤖 In `slate-react`, the [`<Editor>`](https://docs.slatejs.org/slate-react/editor) component creates an instance of the `Editor` controller which manages its value under the covers.

## Properties

```javascript
new Editor({
  onChange: Function,
  plugins: Array,
  readOnly: Boolean,
  value: Value,
})
```

### `onChange`

`Function onChange(change: Change)`

A change handler that will be called asynchronously with the `change` that applied the change. When the `onChange` handler is called, the `editor.value` will already reflect the new state.

### `operations`

`List<Operation>`

An immutable list of [`Operation`](https://docs.slatejs.org/slate-core/operation) models that have already been applied to the editor in the current change. As soon as the first operation is added, the `onChange` is queued to run on the next tick.

### `plugins`

`Array`

An array of [`Plugins`](https://docs.slatejs.org/slate-core/plugins) that define the editor's behavior. These plugins are only definable when an instance of `Editor` is constructed, and are constant throught the editor's lifecycle.

> 🤖 In `slate-react`, when the `plugins` prop to the [`<Editor>`](https://docs.slatejs.org/slate-react/editor) component changes, an entirely new `Editor` controller is created under the covers. This is why plugins should not be defined inline in the render function.

### `readOnly`

`Boolean`

Whether the editor is in "read-only" mode, where the user is prevented from editing the editor's content.

### `value`

`Value`

A [`Value`](https://docs.slatejs.org/slate-core/value) object representing the current value of the editor.

## Methods

### `command`

`command(type: String, ...args) => Editor` `command(fn: Function, ...args) => Editor`

```javascript
editor.command('insertText', 'word')
editor.command((editor, text) => { ... }, 'word')
```

Invoke a command by `type` on the editor with `args`.

Alternatively, the `type` argument can be a function, which will be invoked with `(editor, ...args)`. This is helpful in situations where you want write one-off commands with customized logic.

### `flush`

`flush() => Editor`

```javascript
editor.flush()
```

Synchronously flush the current changes to editor, calling `onChange`.

> 🤖 In normal operation you never need to use this method! However, it can be helpful for writing tests to be able to keep the entire test synchronous.

### `hasCommand`

`hasCommand(type: String) => Boolean`

```javascript
editor.hasCommand('insertLink')
```

Checks if a command by `type` has been registered.

### `hasQuery`

`hasQuery(type: String) => Boolean`

```javascript
editor.hasQuery('isLinkActive')
```

Checks if a query by `type` has been registered.

### `query`

`query(type: String, ...args) => Any` `query(fn: Function, ...args) => Editor`

```javascript
editor.query('isLinkActive')
editor.query(editor => { ... })
```

Invoke a query by `type` on the editor with `args`, returning its result.

Alternatively, the `type` argument can be a function, which will be invoked with `(editor, ...args)`. This is helpful in situations where you want write one-off queries with customized logic.

### `registerCommand`

`registerCommand(type: String) => Void`

```javascript
editor.registerCommand('insertLink')
```

Add a new command by `type` with the editor. This will make the command available as a top-level method on the `editor`.

> 🤖 Note that this method only registers the command with the editor, creating the top-level command method. It does not define the queries behaviors, which are defined with the `onCommand` middleware.

### `registerQuery`

`registerQuery(type: String) => Void`

```javascript
editor.registerQuery('isLinkActive')
```

Add a new query by `type` with the editor. This will make the query available as a top-level method on the `editor`.

> 🤖 Note that this method only registers the query with the editor, creating the top-level query method. It does not define the queries behaviors, which are defined with the `onQuery` middleware.

### `run`

`run(key, ...args) => Any`

```javascript
editor.run('onKeyDown', { key: 'Tab', ... })
```

Run the middleware stack by `key` with `args`, returning its result.

> 🤖 In normal operation you never need to use this method! However, it's useful for writing tests to be able to simulate plugin behaviors.

### `setReadOnly`

`setReadOnly(readOnly: Boolean) => Editor`

```javascript
editor.setReadOnly(true)
```

Set the editor's `readOnly` state.

### `setValue`

`setValue(value: Value, options: Object) => Editor`

```javascript
editor.setValue(value)
```

Set the editor's `value` state.

You can optionally provide a `normalize` option to either for the editor to completely re-normalize the new value based on its schema or not. By default, the editor will re-normalize only if the value is not equal to its previously seen value (which it knows was normalized).


# Inline

```javascript
import { Inline } from 'slate'
```

A inline node in a Slate [`Document`](https://docs.slatejs.org/slate-core/document). Inline nodes implement the [`Node`](https://docs.slatejs.org/slate-core/node) interface.

Inline nodes may contain nested inline nodes and text nodes—just like in the DOM. They always contain at least one text node child.

## Properties

```javascript
Inline({
  data: Data,
  key: String,
  nodes: Immutable.List<Node>,
  type: String
})
```

### `data`

`Immutable.Map`

Arbitrary data associated with the node. Defaults to an empty `Map`.

### `key`

`String`

A unique identifier for the node.

### `object`

`String`

An immutable string value of `'inline'` for easily separating this node from [`Block`](https://docs.slatejs.org/slate-core/block) or [`Text`](https://docs.slatejs.org/slate-core/text) nodes.

### `nodes`

`Immutable.List`

A list of child nodes. Defaults to a list with a single text node child.

### `type`

`String`

The custom type of the node (eg. `link` or `hashtag`).

## Computed Properties

### `text`

`String`

A concatenated string of all of the descendant [`Text`](https://docs.slatejs.org/slate-core/text) nodes of this node.

## Static Methods

### `Inline.create`

`Inline.create(properties: Object) => Inline`

Create an inline from a plain JavaScript object of `properties`.

### `Inline.createList`

`Inline.createList(array: Array) => List`

Create a list of inline nodes from a plain JavaScript `array`.

### `Inline.fromJSON`

`Inline.fromJSON(object: Object) => Inline`

Create an inline from a JSON `object`.

### `Inline.isInline`

`Inline.isInline(maybeInline: Any) => Boolean`

Returns a boolean if the passed in argument is a `Inline`.

## Node Methods

Inlines implement the [`Node`](https://docs.slatejs.org/slate-core/node) interface. For information about all of the node methods, see the [`Node` reference](https://docs.slatejs.org/slate-core/node).

## Instance Methods

### `toJSON`

`toJSON() => Object`

Returns a JSON representation of the inline.


# Mark

```javascript
import { Mark } from 'slate'
```

A formatting mark that can be associated with characters. Marks are how Slate represents rich formatting like **bold** or *italic*.

## Properties

```javascript
Mark({
  data: Data,
  type: String,
})
```

### `data`

`Data`

A map of [`Data`](https://docs.slatejs.org/slate-core/data).

### `object`

`String`

A string with a value of `'mark'`.

### `type`

`String`

The custom type of the mark (eg. `bold` or `italic`).

## Static Methods

### `Mark.create`

`Mark.create(properties: Object) => Mark`

Create a mark from a plain JavaScript object of `properties`.

### `Mark.createSet`

`Mark.createSet(array: Array) => Set`

Create a set of marks from a plain JavaScript `array`.

### `Mark.fromJSON`

`Mark.fromJSON(object: Object) => Mark`

Create a mark from a JSON `object`.

### `Mark.isMark`

`Mark.isMark(maybeMark: Any) => Boolean`

Returns a boolean if the passed in argument is a `Mark`.

## Instance Methods

### `toJSON`

`toJSON() => Object`

Returns a JSON representation of the mark.


# Node

`Node` is not a publicly accessible module, but instead an interface that [`Document`](https://docs.slatejs.org/slate-core/document), [`Block`](https://docs.slatejs.org/slate-core/block) and [`Inline`](https://docs.slatejs.org/slate-core/inline) all implement.

## Properties

### `key`

`String`

A short-lived, unique identifier for the node.

By default, keys are **not** meant to be long-lived unique identifiers for nodes that you might store in a database, or elsewhere. They are meant purely to identify a node inside of a single Slate instance. For that reason, they are simply auto-incrementing strings. (eg. `'0'`, `'1'`, `'2'`, ...)

If you want to make your keys uniqueness long-lived, you'll need to supply your own key generating function via the [`setKeyGenerator`](https://docs.slatejs.org/utils#setkeygenerator) util.

### `nodes`

`Immutable.List`

A list of child nodes. Defaults to a list with a single text node child.

### `object`

`String`

An immutable string value of `'document'`, `'block'`, `'inline'` or `'text'` for easily separating this node from [`Inline`](https://docs.slatejs.org/slate-core/inline) or [`Text`](https://docs.slatejs.org/slate-core/text) nodes.

## Computed Properties

### `text`

`String`

A concatenated string of all of the descendant [`Text`](https://docs.slatejs.org/slate-core/text) nodes of this node.

## Methods

### `filterDescendants`

`filterDescendants(iterator: Function) => List`

Deeply filter the descendant nodes of a node by `iterator`.

### `findDescendant`

`findDescendant(iterator: Function) => Node|Void`

Deeply find a descendant node by `iterator`.

### `getAncestors`

`getAncestors(path: List|Array) => List|Void` `getAncestors(key: String) => List|Void`

Get the ancestors of a descendant by `path` or `key`.

### `getBlocks`

`getBlocks() => List`

Get all of the bottom-most [`Block`](https://docs.slatejs.org/slate-core/block) node descendants.

### `getLeafBlocksAtRange`

`getLeafBlocksAtRange(range: Range) => List`

Get all of the bottom-most [`Block`](https://docs.slatejs.org/slate-core/block) nodes in a `range`.

### `getBlocksByType`

`getBlocksByType(type: String) => List`

Get all of the bottom-most [`Block`](https://docs.slatejs.org/slate-core/block) nodes by `type`.

### `getChild`

`getChild(path: List|Array) => Node|Void` `getChild(key: String) => Node|Void`

Get a child by `path` or `key`.

### `getClosest`

`getClosest(path: List|Array, match: Function) => Node|Void` `getClosest(key: String, match: Function) => Node|Void`

Get the closest parent node of a descendant node by `path` or `key` that matches a `match` function.

### `getClosestBlock`

`getClosestBlock(path: List|Array) => Node|Void` `getClosestBlock(key: String) => Node|Void`

Get the closest [`Block`](https://docs.slatejs.org/slate-core/block) node to a descendant node by `path` or `key`.

### `getClosestInline`

`getClosestInline(path: List|Array) => Node|Void` `getClosestInline(key: String) => Node|Void`

Get the closest [`Inline`](https://docs.slatejs.org/slate-core/inline) node to a descendant node by `path` or `key`.

### `getClosestVoid`

`getClosestVoid(path: List|Array) => Node|Void` `getClosestVoid(key: String) => Node|Void`

Get the closest void parent of a descendant node by `path` or `key`.

### `getCommonAncestor`

`getCommonAncestor(path: List|Array) => Number` `getCommonAncestor(key: String) => Number`

Get the lowest common ancestor of a descendant node by `path` or `key`.

### `getDepth`

`getDepth(path: List|Array) => Number` `getDepth(key: String) => Number`

Get the depth of a descendant node by `path` or `key`.

### `getDescendant`

`getDescendant(path: List|Array) => Node|Void` `getDescendant(key: String) => Node|Void`

Get a descendant node by `path` or `key`.

### `getFirstText`

`getFirstText() => Text|Void`

Get the first child text node inside a node.

### `getFragmentAtRange`

`getFragmentAtRange(range: Range) => Document`

Get a document fragment of the nodes in a `range`.

### `getFurthest`

`getFurthest(path: List|Array, iterator: Function) => Node|Null` `getFurthest(key: String, iterator: Function) => Node|Null`

Get the furthest parent of a node by `path` or `key` that matches an `iterator`.

### `getFurthestAncestor`

`getFurthestAncestor(path: List|Array) => Node|Null` `getFurthestAncestor(key: String) => Node|Null`

Get the furthest ancestor of a node by `path` or `key`.

### `getFurthestBlock`

`getFurthestBlock(path: List|Array) => Node|Null` `getFurthestBlock(key: String) => Node|Null`

Get the furthest block parent of a node by `path` or `key`.

### `getFurthestInline`

`getFurthestInline(path: List|Array) => Node|Null` `getFurthestInline(key: String) => Node|Null`

Get the furthest inline parent of a node by `path` or `key`.

### `getFurthestOnlyChildAncestor`

`getFurthestOnlyChildAncestor(path: List|Array) => Node|Null` `getFurthestOnlyChildAncestor(key: String) => Node|Null`

Get the furthest ancestor of a node by `path` or `key` that has only one child.

### `getInlines`

`getInlines() => List`

Get all of the top-most [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in a node.

### `getLeafInlinesAtRange`

`getLeafInlinesAtRange(range: Range) => List`

Get all of the bottom-most [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in a `range`.

### `getInlinesByType`

`getInlinesByType(type: string) => List`

Get all of the top-most [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes by `type`.

### `getLastText`

`getLastText() => Node|Void`

Get the last child text node inside a node.

### `getMarks`

`getMarks(range: Range) => Set`

Get a set of all of the marks in a node.

### `getMarksAtRange`

`getMarksAtRange(range: Range) => Set`

Get a set of all of the marks in a `range`.

### `getMarksByType`

`getMarksByType(type: String) => Set`

Get a set of all of the marks by `type`.

### `getNextBlock`

`getNextBlock(path: List|Array) => Node|Void` `getNextBlock(key: String) => Node|Void`

Get the next, bottom-most [`Block`](https://docs.slatejs.org/slate-core/block) node after a descendant by `path` or `key`.

### `getNextNode`

`getNextNode(path: List|Array) => Node|Void` `getNextNode(key: String) => Node|Void`

Get the next node in the tree of a descendant by `path` or `key`. This will not only check for siblings but instead move up the tree returning the next ancestor if no sibling is found.

### `getNextSibling`

`getNextSibling(path: List|Array) => Node|Void` `getNextSibling(key: String) => Node|Void`

Get the next sibling of a descendant by `path` or `key`.

### `getNextText`

`getNextText(path: List|Array) => Node|Void` `getNextText(key: String) => Node|Void`

Get the next [`Text`](https://docs.slatejs.org/slate-core/text) node after a descendant by `path` or `key`.

### `getNode`

`getNode(path: List|Array) => Node|Void` `getNode(key: String) => Node|Void`

Get a node in the tree by `path` or `key`.

### `getNodesAtRange`

`getNodesAtRange(range: Range) => List`

Get all of the nodes in a `range`. This includes all of the [`Text`](https://docs.slatejs.org/slate-core/text) nodes inside the range and all ancestors of those [`Text`](https://docs.slatejs.org/slate-core/text) nodes up to this node.

### `getOffset`

`getOffset(path: List|Array) => Number` `getOffset(key: String) => Number`

Get the text offset of a descendant in the tree by `path` or `key`.

### `getParent`

`getParent(path: List|Array) => Node|Void` `getParent(key: String) => Node|Void`

Get the parent node of a descendant by `path` or `key`.

### `getPath`

`getPath(path: List|Array) => Node|Void` `getPath(key: String) => Node|Void`

Get the path to a descendant by `path` or `key`.

### `getPreviousBlock`

`getPreviousBlock(path: List|Array) => Node|Void` `getPreviousBlock(key: String) => Node|Void`

Get the previous, bottom-most [`Block`](https://docs.slatejs.org/slate-core/block) node before a descendant by `path` or `key`.

### `getPreviousNode`

`getPreviousNode(path: List|Array) => Node|Void` `getPreviousNode(key: String) => Node|Void`

Get the previous node in the tree of a descendant by `path` or `key`. This will not only check for siblings but instead move up the tree returning the previous ancestor if no sibling is found.

### `getPreviousSibling`

`getPreviousSibling(path: List|Array) => Node|Void` `getPreviousSibling(key: String) => Node|Void`

Get the previous sibling of a descendant by `path` or `key`.

### `getPreviousText`

`getPreviousText(path: List|Array) => Node|Void` `getPreviousText(key: String) => Node|Void`

Get the previous [`Text`](https://docs.slatejs.org/slate-core/text) node before a descendant by `path` or `key`.

### `getRootBlocksAtRange`

`getRootBlocksAtRange(range: Range) => List`

Get all of the top-most [`Block`](https://docs.slatejs.org/slate-core/block) nodes in a `range`.

### `getRootInlinesAtRange`

`getRootInlinesAtRange(range: Range) => List`

Get all of the top-most [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in a `range`.

### `getTextAtOffset`

`getTextAtOffset(offset: Number) => Text || Void`

Get the [`Text`](https://docs.slatejs.org/slate-core/text) node at an `offset`.

### `getTextDirection`

`getTextDirection() => String`

Get the direction of the text content in the node.

### `getTexts`

`getTexts() => List`

Get all of the [`Text`](https://docs.slatejs.org/slate-core/text) nodes in a node.

### `getTextsAtRange`

`getTextsAtRange(range: Range) => List`

Get all of the [`Text`](https://docs.slatejs.org/slate-core/text) nodes in a `range`.

### `hasChild`

`hasChild(path: List|Array) => Boolean` `hasChild(key: String) => Boolean`

Check whether the node has a child node by `path` or `key`.

### `hasDescendant`

`hasDescendant(path: List|Array) => Boolean` `hasDescendant(key: String) => Boolean`

Check whether the node has a descendant node by `path` or `key`.

### `hasNode`

`hasNode(path: List|Array) => Boolean` `hasNode(key: String) => Boolean`

Check whether a node exists in the tree by `path` or `key`.

### `isNodeInRange`

`isNodeInRange(path: List|Array, range: Range) => Boolean` `isNodeInRange(key: String, range: Range) => Boolean`

Check whether a node is inside a `range`. This will return true for all [`Text`](https://docs.slatejs.org/slate-core/text) nodes inside the range and all ancestors of those [`Text`](https://docs.slatejs.org/slate-core/text) nodes up to this node.


# Operation

An operation is the lowest-level description of a specific change to a part of Slate's value. They are designed to be collaborative-editing friendly.

All of the [`Commands`](https://docs.slatejs.org/slate-core/commands) methods result in operations being created and applied to a [`Value`](https://docs.slatejs.org/slate-core/value) They're accessible via the `editor.operations` property.

There are a handful of Slate operation types. The goal is to have the fewest possible types, while still maintaining the necessary semantics for collaborative editing to work.

## Properties

See each operation separately below to see what they consist of.

Note that all operations have a `data` property which can be used to attach arbitrary data to the operation, just like the [`Node`](https://docs.slatejs.org/slate-core/node) models ([`Block`](https://docs.slatejs.org/slate-core/block), [`Inline`](https://docs.slatejs.org/slate-core/inline), etc).

## Text Operations

### `insert_text`

```javascript
{
  type: 'insert_text',
  path: List,
  offset: Number,
  text: String,
  marks: List,
  data: Map,
}
```

Inserts a `text` string at `offset` into a text node at `path`, with optional `marks` to be applied to the inserted characters.

### `remove_text`

```javascript
{
  type: 'remove_text',
  path: List,
  offset: Number,
  text: String,
  data: Map,
}
```

Removes a string of `text` at `offset` into a text node at `path`.

## Mark Operations

### `add_mark`

```javascript
{
  type: 'add_mark',
  path: List,
  offset: Number,
  length: Number,
  mark: Mark,
  data: Map,
}
```

Adds a `mark` to the text node at `path` starting at an `offset` and spanning `length` characters.

### `remove_mark`

```javascript
{
  type: 'remove_mark',
  path: List,
  offset: Number,
  length: Number,
  mark: Mark,
  data: Map,
}
```

Removes a `mark` from a text node at `path` starting at an `offset` and spanning `length` characters.

### `set_mark`

```javascript
{
  type: 'set_mark',
  path: List,
  offset: Number,
  length: Number,
  properties: Object,
  newProperties: Object,
  data: Map,
}
```

Set new `newProperties` on any marks that match an existing `properties` mark in a text node at `path`, starting at an `offset` and spanning `length` characters.

## Node Operations

### `insert_node`

```javascript
{
  type: 'insert_node',
  path: List,
  node: Node,
  data: Map,
}
```

Insert a new `node` at `path`.

### `merge_node`

```javascript
{
  type: 'merge_node',
  path: List,
  position: Number,
  properties: Object,
  data: Map,
}
```

Merge the node at `path` with its previous sibling. The `position` refers to either the index in the child nodes of the previous sibling in the case of [`Block`](https://docs.slatejs.org/slate-core/block) or [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes, and the index in the characters of the previous sibling in the case of [`Text`](https://docs.slatejs.org/slate-core/text) nodes. The `properties` object contains properties of the merged node in the event that the change is undone.

### `move_node`

```javascript
{
  type: 'move_node',
  path: List,
  newPath: Array,
  data: Map,
}
```

Move the node at `path` to a `newPath`.

### `remove_node`

```javascript
{
  type: 'remove_node',
  path: List,
  node: Node,
  data: Map,
}
```

Remove the node at `path`.

### `set_node`

```javascript
{
  type: 'set_node',
  path: List,
  properties: Object,
  newProperties: Object,
  data: Map,
}
```

Set new `properties` on the node at `path`.

### `split_node`

```javascript
{
  type: 'split_node',
  path: List,
  position: Number,
  target: Number,
  properties: Object,
  data: Map,
}
```

Split the node at `path` at `position`. The `position` refers to either the index in the child nodes in the case of [`Block`](https://docs.slatejs.org/slate-core/block) or [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes, and the index in the characters in the case of [`Text`](https://docs.slatejs.org/slate-core/text) nodes. In the case of nested splits, `target` refers to the target path of the child split operation. The `properties` object contains properties that should be assigned to the new node created after the split operation is complete.

## Value Operations

### `set_selection`

```javascript
{
  type: 'set_selection',
  properties: Object,
  newProperties: Object,
  data: Map,
}
```

Set new `properties` on the selection.

### `set_value`

```javascript
{
  type: 'set_value',
  properties: Object,
  newProperties: Object,
  data: Map,
}
```

Set new `properties` on a value. Properties can contain `data` and `decorations`.

## Helpers

### `apply`

`apply(value: Value, operation: Object) => Value`

Applies an `operation` to a `value` object.

### `invert`

`invert(operation: Object) => Object`

Create an inverse operation that will undo the changes made by the original.


# Plugins

Plugins can be attached to an editor to alter its behavior in different ways. Each editor has a "stack" of plugins, which has a specific order, which it runs through when certain hooks are triggered.

> 🤖 The core `slate` editor is designed for use across all environments, and defines a limited set of plugin hooks. But when using `slate-react` there are more hooks defined, for managing in rendering, DOM events, etc. Check out the [React Plugins](https://docs.slatejs.org/slate-react/plugins) reference for more information.

## Hooks

Plugins are plain JavaScript objects, containing a set of middleware functions that run for each hook they choose to implement.

```javascript
{
  normalizeNode: Function,
  onChange: Function,
  onCommand: Function,
  onConstruct: Function,
  onQuery: Function,
  validateNode: Function,
}
```

When a hook is triggered, the middleware function is passed a set of arguments, with the last argument being a `next` function. Choosing whether to call `next` or not determines whether the editor will continue traversing the stack.

### `normalizeNode`

`Function normalizeNode(node: Node, editor: Editor, next: Function) => Function(editor: Editor)|Void`

The `normalizeNode` hook takes a `node` and either returns `undefined` if the node is valid, or a change function that normalizes the node into a valid state if not.

### `onChange`

`onChange(editor: Editor, next: Function) => Void`

```javascript
{
  onChange(editor, next) {
    ...
    return next()
  }
}
```

The `onChange` hook is called whenever a new change is about to be applied to an editor. This is useful if you'd like to apply some behavior to every change, or even abort certain changes.

### `onCommand`

`onCommand(command: Object, editor: Editor, next: Function) => Void`

```javascript
{
  onCommand(command, editor, next) {
    const { type, args } = command

    if (type === 'wrapQuote') {
      editor.wrapBlock('quote')
    } else {
      return next()
    }
  }
}
```

```javascript
{
  type: String,
  args: Array,
}
```

The `onCommand` hook is called with a `command` object resulting from an `editor.command(type, ...args)` or a `change[command](...args)` call:

The `onCommand` hook is a low-level way to have access to all of the commands passing through the editor. Most of the time you should use the `commands` shorthand instead.

### `onConstruct`

`onConstruct(editor: Editor, next: Function) => Void`

```javascript
{
  onConstruct(editor, next) {
    editor.registerCommand('wrapList')
    return next()
  }
}
```

The `onConstruct` hook is called when a new instance of `Editor` is created. This is where you can call `editor.registerCommand` or `editor.registerQuery`.

> 🤖 This is always called with the low-level `Editor` instance, and not the React `<Editor>` component. And it is called before the React editor has its `value` set based on its props. It is purely used for editor-related configuration setup, and not for any schema-related or value-related purposes.

### `onQuery`

`onQuery(query: Object, editor: Editor, next: Function) => Void`

```javascript
{
  onQuery(query, editor, next) {
    const { type, args } = query

    if (type === 'getActiveList') {
      return ...
    } else {
      return next()
    }
  }
}
```

```javascript
{
  type: String,
  args: Array,
}
```

The `onQuery` hook is called with a `query` object resulting from an `editor.query(type, ...args)` or a `change[query](...args)` call:

The `onQuery` hook is a low-level way to have access to all of the queries passing through the editor. Most of the time you should use the `queries` shorthand instead.

### `validateNode`

`Function validateNode(node: Node, editor: Editor, next: Function) => SlateError|Void`

The `validateNode` hook takes a `node` and either returns `undefined` if the node is valid, or a `SlateError` object if it is invalid.

## Shorthands

In addition to the middleware functions, Slate also provides three shorthands which implement common behaviors in `commands`, `queries` and `schema`.

```javascript
{
  commands: Object,
  queries: Object,
  schema: Object,
}
```

### `commands`

`commands: Object`

```javascript
{
  commands: {
    setHeader(editor, level) {
      editor.setBlocks({ type: 'header', data: { level }})
    }
  }
}
```

The `commands` shorthand defines a set of custom commands that are made available in the editor, and as first-class methods on the `editor`.

Each command has a signature of `(editor, ...args)`.

### `queries`

`queries: Object`

```javascript
{
  queries: {
    getActiveList(editor) {
      ...
    }
  }
}
```

The `queries` shorthand defines a set of custom queries that are made available in the editor, and as first-class methods on the `editor`.

Each query has a signature of `(editor, ...args)`.

### `schema`

`schema: Object`

```javascript
{
  schema: {
    blocks: {
      image: {
        isVoid: true,
        parent: { type: 'figure' },
      },
      ...
    }
  }
}
```

```javascript
{
  document: Object,
  blocks: Object,
  inlines: Object,
  rules: Array,
}
```

The `schema` shorthand defines your custom requires for the data in your editor. It allows you to enforce rules about what "valid" content is in the editor, and how nodes behave.

Check out the [Schema](https://docs.slatejs.org/slate-core/schema) reference for more information.


# Point

```javascript
import { Point } from 'slate'
```

A point in a Slate [`Document`](https://docs.slatejs.org/slate-core/document). Points in Slate are inspired by the [DOM Range API](https://developer.mozilla.org/en-US/docs/Web/API/Range), with terms like "offset".

## Properties

```javascript
Point({
  key: String,
  path: List,
  offset: Number,
})
```

### `key`

`String`

The key of the text node at the point's point.

### `path`

`List`

The path to the text node at the point's point.

### `object`

`String`

A string with a value of `'point'`.

### `offset`

`Number`

The number of characters from the start of the text node at the point's point.

## Computed Properties

### `isSet`

`Boolean`

Whether the key, path and offset of a point is not `null`.

### `isUnset`

`Boolean`

Whether any of the key, path or offset of a point is `null`.

## Static Methods

### `Point.create`

`Point.create(properties: Object|Point) => Point`

Create a new `Point` with `properties`.

### `Point.createProperties`

`Point.createProperties(object: Object|Point) => Object`

Create a new dictionary of point properties from an `object`.

### `Point.fromJSON`

`Point.fromJSON(object: Object) => Point`

Create a point from a JSON `object`.

### `Point.isPoint`

`Point.isPoint(value: Any) => Boolean`

Check whether a `value` is a `Point`.

## Instance Methods

### `toJSON`

`toJSON() => Object`

Return a JSON representation of the point.

## Checking Methods

### `isAfterRange`

`isAfterRange(range: Range) => Boolean`

Determine whether the point is after a `range`.

### `isAtEndOfRange`

`isAtEndOfRange(range: Range) => Boolean`

Determine whether the point is at the end of a `range`.

### `isAtStartOfRange`

`isAtStartOfRange(range: Range) => Boolean`

Determine whether the point is at the start of a `range`.

### `isBeforeRange`

`isBeforeRange(range: Range) => Boolean`

Determine whether the point is before a `range`.

### `isInRange`

`isInRange(range: Range) => Boolean`

Determine whether the point is inside a `range`.

### `isAtEndOfNode`

`isAtEndOfNode(node: Node) => Boolean`

Determine whether the point is at the end of a `node`.

### `isAtStartOfNode`

`isAtStartOfNode(node: Node) => Boolean`

Determine whether the point is at the start of a `node`.

### `isInNode`

`isInNode(node: Node) => Boolean`

Determine whether a point is inside a `node`.

## Mutating Methods

### `moveBackward`

`moveBackward(n: Number) => Point`

Return a new point with its offset moved backwards by `n` characters.

### `moveForward`

`moveForward(n: Number) => Point`

Return a new point with its offset moved forwards by `n` characters.

### `moveTo`

`moveTo(path: List, offset: Number) => Point` `moveTo(key: String, offset: Number) => Point` `moveTo(offset: Number) => Point`

Return a new point with its `path`, `key` and `offset` set to new values.

> 🤖 When using `point.moveTo`, since the point isn't aware of the document, it's possible it will become "unset" if the path or key changes and need to be re-normalized relative to the document using `point.normalize(document)`.

### `moveToEndOfNode`

`moveToEndOfNode(node: Node) => Point`

Return a new point at the end of a `node`.

> 🤖 This method may need to be followed by `point.normalize(document)`, like [`moveTo`](#moveto).

### `moveToStartOfNode`

`moveToStartOfNode(node: Node) => Point`

Return a new point at the start of a `node`.

> 🤖 This method may need to be followed by `point.normalize(document)`, like [`moveTo`](#moveto).

### `normalize`

`normalize(node: Node) => Point`

Normalize the point relative to a `node`, ensuring that its key and path are in sync, that its offset is valid, and that it references a leaf text node.

### `setKey`

`setKey(key: String|Null) => Point`

Return a new point with a new `key`.

### `setOffset`

`setOffset(offset: Number|Null) => Point`

Return a new point with a new `offset`.

### `setPath`

`setPath(path: List|Array|Null) => Point`

Return a new point with a new `path`.

### `unset`

`unset() => Point`

Return a new point with the key, path, and offset all set to `null`.


# Range

```javascript
import { Range } from 'slate'
```

A range of a Slate [`Document`](https://docs.slatejs.org/slate-core/document). Ranges in Slate are modeled after a combination of the [DOM Selection API](https://developer.mozilla.org/en-US/docs/Web/API/Selection) and the [DOM Range API](https://developer.mozilla.org/en-US/docs/Web/API/Range), using terms like "anchor", "focus" and "collapsed".

The "anchor" is the fixed point in a range, and the "focus" is the non-fixed point, which may move when you move the cursor (eg. when pressing `Shift + Right Arrow`).

Often times, you don't need to specifically know which point is the "anchor" and which is the "focus", and you just need to know which comes first and last in the document. For these cases, there are many convenience equivalent properties and methods referring to the "start" and "end" points.

The `Range` model is also used as an interface and implemented by the [`Decoration`](https://docs.slatejs.org/slate-core/decoration) and [`Selection`](https://docs.slatejs.org/slate-core/selection) models.

## Properties

```javascript
Range({
  anchor: Point,
  focus: Point,
})
```

### `anchor`

`Point`

The range's anchor point.

### `focus`

`Point`

The range's focus point.

### `object`

`String`

A string with a value of `'range'`.

## Computed Properties

These properties aren't supplied when creating a range, but are instead computed based on the real properties.

### `end`

Either the `anchor` or the `focus` point, depending on which comes last in the document order.

### `isBackward`

`Boolean`

Whether the range is backward. A range is considered "backward" when its focus point references a location earlier in the document than its anchor point.

### `isCollapsed`

`Boolean`

Whether the range is collapsed. A range is considered "collapsed" when the anchor point and focus point of the range are the same.

### `isExpanded`

`Boolean`

The opposite of `isCollapsed`, for convenience.

### `isForward`

`Boolean`

The opposite of `isBackward`, for convenience.

### `isSet`

`Boolean`

Whether both the `anchor` and `focus` points are set.

### `isUnset`

`Boolean`

Whether either the `anchor` and `focus` points are unset.

### `start`

Either the `anchor` or the `focus` point, depending on which comes first in the document order.

## Static Methods

### `Range.create`

`Range.create(properties: Object) => Range`

Create a new `Range` instance with `properties`.

### `Range.createProperties`

`Range.createProperties(object: Object|Range) => Object`

Create a new dictionary of range properties from an `object`.

### `Range.fromJSON`

`Range.fromJSON(object: Object) => Range`

Create a range from a JSON `object`.

### `Range.isRange`

`Range.isRange(value: Any) => Boolean`

Check whether a `value` is a `Range`.

## Instance Methods

### `toJSON`

`toJSON() => Object`

Return a JSON representation of the range.

## Mutating Methods

### `move{Point}Backward`

`move{Point}Backward(n: Number) => Range`

Move the `{Point}` of the range backwards by `n` characters. The `{Point}` can be one of: `Anchor`, `Focus`, `Start`, `End`, or ommited to move both the `anchor` and `focus` point at once.

### `move{Point}Forward`

`move{Point}Forward(n: Number) => Range`

Move the `{Point}` of the range forwards by `n` characters. The `{Point}` can be one of: `Anchor`, `Focus`, `Start`, `End`, or ommited to move both the `anchor` and `focus` point at once.

### `move{Point}To`

`move{Point}To(path: List, offset: Number) => Range` `move{Point}To(key: String, offset: Number) => Range` `move{Point}To(offset: Number) => Range`

Move the `{Point}` of the range to a new `key`, `path` and `offset`. The `{Point}` can be one of: `Anchor`, `Focus`, `Start`, `End`, or ommited to move both the `anchor` and `focus` point at once.

> 🤖 When using `range.move{Point}To`, since the range isn't aware of the document, it's possible it will become "unset" if the path or key changes and need to be re-normalized relative to the document using `range.normalize(document)`.

### `move{Point}ToEndOfNode`

`move{Point}ToEndOfNode(node: Node) => Range`

Move the `{Point}` to the end of a `node`. The `{Point}` can be one of: `Anchor`, `Focus`, `Start`, `End`, or ommited to move both the `anchor` and `focus` point at once.

> 🤖 This method may need to be followed by `range.normalize(document)`, like [`move{Point}To`](#movepointto).

### `move{Point}ToStartOfNode`

`move{Point}ToStartOfNode(node: Node) => Range`

Move the `{Point}` to the start of a `node`. The `{Point}` can be one of: `Anchor`, `Focus`, `Start`, `End`, or ommited to move both the `anchor` and `focus` point at once.

> 🤖 This method may need to be followed by `range.normalize(document)`, like [`move{Point}To`](#movepointto).

### `moveTo{Point}`

`moveTo{Point}() => Range`

Move both points of the range to `{Point}`, collapsing it. The `{Point}` can be one of: `Anchor`, `Focus`, `Start` or `End`.

### `moveToRangeOfNode`

`moveToRangeOfNode(node: Node) => Range`

Move the range to be spanning the entirity of a `node`, by placing its `anchor` point at the start of the node and its `focus` point at the end of the node.

> 🤖 This method may need to be followed by `range.normalize(document)`, like [`move{Point}To`](#movepointto).

### `normalize`

`normalize(node: Node) => Range`

Normalize the range relative to a `node`, ensuring that its anchor and focus points exist in the `node`, that their keys and paths are in sync, that their offsets are valid, and that they references leaf text nodes.

### `setAnchor`

`setAnchor(anchor: Point) => Range`

Return a new range with a new `anchor` point.

### `setEnd`

`setEnd(end: Point) => Range`

Return a new range with a new `end` point.

### `setFocus`

`setFocus(focus: Point) => Range`

Return a new range with a new `focus` point.

### `setProperties`

`setProperties(properties: Object|Range) => Range`

Return a new range with new `properties` set.

### `setStart`

`setStart(start: Point) => Range`

Return a new range with a new `start` point.

### `unset`

`unset() => Range`

Return a new range with both of its point unset.


# Schema

Every Slate editor has a "schema" associated with it, which contains information about the structure of its content. For the most basic cases, you'll just rely on Slate's default core schema. But for advanced use cases, you can enforce rules about what the content of a Slate document can contain.

## Properties

```javascript
{
  document: Object,
  blocks: Object,
  inlines: Object,
  rules: Array,
}
```

The top-level properties of a schema give you a way to define validation "rules" that the schema enforces.

### `document`

`Object`

```javascript
{
  document: {
    nodes: [
      {
        match: { type: 'paragraph' },
      },
    ]
  }
}
```

A set of validation rules that apply to the top-level document.

### `blocks`

`Object`

```javascript
{
  blocks: {
    list: {
      nodes: [{
        match: { type: 'item' }
      }]
    },
    item: {
      parent: { type: 'list' }
    },
  }
}
```

A dictionary of blocks by type, each with its own set of validation rules.

### `inlines`

`Object`

```javascript
{
  inlines: {
    emoji: {
      isVoid: true,
      nodes: [{
        match: { object: 'text' }
      }]
    },
  }
}
```

A dictionary of inlines by type, each with its own set of validation rules.

## Rule Properties

```javascript
{
  data: Object,
  first: Object|Array,
  isVoid: Boolean,
  last: Object|Array,
  next: Object|Array,
  marks: Array,
  match: Object|Array,
  nodes: Array,
  normalize: Function,
  parent: Object|Array,
  previous: Object|Array,
  text: RegExp,
}
```

Slate schemas are built using a set of validation rules. Each of the properties will validate certain pieces of the document based on the properties it defines.

### `data`

`Object`

```javascript
{
  data: {
    level: 2,
    href: v => isUrl(v),
  }
}
```

A dictionary of data attributes and their corresponding values or validation functions. The functions should return a boolean indicating whether the data value is valid or not.

### `first`

`Object|Array`

```javascript
{
  first: { type: 'quote' },
}
```

```javascript
{
  first: [{ type: 'quote' }, { type: 'paragraph' }],
}
```

Will validate the first child node against a [`match`](#match).

### `isVoid`

`Boolean`

```javascript
{
  isVoid: true,
}
```

Will determine whether the node is treated as a "void" node or not, making its content a black box that Slate doesn't control editing for.

### `last`

`Object|Array`

```javascript
{
  last: { type: 'quote' },
}
```

```javascript
{
  last: [{ type: 'quote' }, { type: 'paragraph' }],
}
```

Will validate the last child node against a [`match`](#match).

### `next`

`Object|Array`

```javascript
{
  next: { type: 'quote' },
}
```

```javascript
{
  next: [{ type: 'quote' }, { type: 'paragraph' }],
}
```

Will validate the next sibling node against a [`match`](#match).

### `nodes`

`Array`

```javascript
{
  nodes: [
    {
      match: [{ type: 'image' }, { type: 'video' }],
      min: 1,
      max: 3,
    },
    {
      match: { type: 'paragraph' },
      min: 0,
    },
  ],
}
```

Will validate a node's children. The `nodes` definitions can declare a [`match`](#match) as well as `min` and `max` properties.

> 🤖 The `nodes` array is order-sensitive! The example above will require that the first node be either an `image` or `video`, and that it be followed by one or more `paragraph` nodes.

### `marks`

`Array`

```javascript
{
  marks: [{ type: 'bold' }, { type: 'italic' }]
}
```

Will validate a node's marks. The `marks` definitions can declare the `type` property, providing a list of mark types to be allowed. If declared, any marks that are not in the list will be removed.

### `normalize`

`normalize(editor: Editor, error: SlateError) => Void`

```javascript
{
  normalize: (editor, error) => {
    switch (error.code) {
      case 'child_object_invalid':
        editor.wrapBlockByKey(error.child.key, 'paragraph')
        return
      case 'child_type_invalid':
        editor.setNodeByKey(error.child.key, 'paragraph')
        return
    }
  }
}
```

A function that can be provided to override the default behavior in the case of a rule being invalid. By default, Slate will do what it can, but since it doesn't know much about your schema, it will often remove invalid nodes. If you want to override this behavior and "fix" the node instead of removing it, pass a custom `normalize` function.

For more information on the arguments passed to `normalize`, see the [Errors](#errors) section.

### `parent`

`Object|Array`

```javascript
{
  parent: { type: 'list' },
}
```

```javascript
{
  parent: [{ type: 'ordered_list' }, { type: 'unordered_list' }],
}
```

Will validate a node's parent against a [`match`](#match).

### `previous`

`Object|Array`

```javascript
{
  previous: { type: 'quote' },
}
```

```javascript
{
  previous: [{ type: 'quote' }, { type: 'paragraph' }],
}
```

Will validate the previous sibling node against a [`match`](#match).

### `text`

`RegExp|Function`

```javascript
{
  text: /^\w+$/
}
```

```javascript
{
  text: string => string === 'valid'
}
```

Will validate a node's text with a regex or function.

## Errors

When supplying your own `normalize` property for a schema rule, it will be called with `(editor, error)`. The error `code` will be one of a set of potential code strings, and it will contain additional helpful properties depending on the type of error.

### `'child_object_invalid'`

```javascript
{
  child: Node,
  index: Number,
  node: Node,
  rule: Object,
}
```

Raised when the `object` property of a child node is invalid.

### `child_min_invalid`

```javascript
{
  index: Number,
  count: Number,
  limit: Number,
  node: Node,
  rule: Object,
}
```

Raised when a child node repeats less than required by a rule's `min` property.

### `child_max_invalid`

```javascript
{
  index: Number,
  count: Number,
  limit: Number,
  node: Node,
  rule: Object,
}
```

Raised when a child node repeats more than permitted by a rule's `max` property.

### `'child_type_invalid'`

```javascript
{
  child: Node,
  index: Number,
  node: Node,
  rule: Object,
}
```

Raised when the `type` property of a child node is invalid.

### `'child_unknown'`

```javascript
{
  child: Node,
  index: Number,
  node: Node,
  rule: Object,
}
```

Raised when a child was not expected but one was found.

### `'first_child_object_invalid'`

```javascript
{
  child: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `object` property of the first child node is invalid, when a specific `first` rule was defined in a schema.

### `'first_child_type_invalid'`

```javascript
{
  child: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `type` property of the first child node is invalid, when a specific `first` rule was defined in a schema.

### `'last_child_object_invalid'`

```javascript
{
  child: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `object` property of the last child node is invalid, when a specific `last` rule was defined in a schema.

### `'last_child_type_invalid'`

```javascript
{
  child: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `type` property of the last child node is invalid, when a specific `last` rule was defined in a schema.

### `'next_sibling_object_invalid'`

```javascript
{
  next: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `object` property of the next sibling node is invalid, when a specific `next` rule was defined in a schema.

### `'next_sibling_type_invalid'`

```javascript
{
  next: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `type` property of the next sibling node is invalid, when a specific `next` rule was defined in a schema.

### `'node_data_invalid'`

```javascript
{
  key: String,
  node: Node,
  rule: Object,
  value: Mixed,
}
```

Raised when the `data` property of a node contains an invalid entry.

### `'node_is_void_invalid'`

```javascript
{
  node: Node,
  rule: Object,
}
```

Raised when the `isVoid` property of a node is invalid.

### `'node_mark_invalid'`

```javascript
{
  mark: Mark,
  node: Node,
  rule: Object,
}
```

Raised when one of the marks in a node is invalid.

### `'node_text_invalid'`

```javascript
{
  text: String,
  node: Node,
  rule: Object,
}
```

Raised when the text content of a node is invalid.

### `'parent_object_invalid'`

```javascript
{
  node: Node,
  parent: Node,
  rule: Object,
}
```

Raised when the `object` property of the parent of a node is invalid, when a specific `parent` rule was defined in a schema.

### `'parent_type_invalid'`

```javascript
{
  node: Node,
  parent: Node,
  rule: Object,
}
```

Raised when the `type` property of the parent of a node is invalid, when a specific `parent` rule was defined in a schema.

### `'previous_sibling_object_invalid'`

```javascript
{
  previous: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `object` property of the previous sibling node is invalid, when a specific `previous` rule was defined in a schema.

### `'previous_sibling_type_invalid'`

```javascript
{
  previous: Node,
  node: Node,
  rule: Object,
}
```

Raised when the `type` property of the previous sibling node is invalid, when a specific `previous` rule was defined in a schema.


# Selection

```javascript
import { Selection } from 'slate'
```

The user's current selection in a Slate [`Document`](https://docs.slatejs.org/slate-core/document). Selections implement the [`Range`](https://docs.slatejs.org/slate-core/range) interface, but also expose data about the current "focus" and the cursor current marks.

## Properties

```javascript
Selection({
  anchor: Point,
  focus: Point,
  isFocused: Boolean,
  marks: Set,
})
```

### `isFocused`

`Boolean`

Whether the range currently has focus.

### `marks`

`Set`

A set of marks associated with the range.

### `object`

`String`

A string with a value of `'selection'`.

## Computed Properties

### `isBlurred`

`Boolean`

The opposite of `isFocused`, for convenience.

## Static Methods

### `Selection.create`

`Selection.create(properties: Object) => Selection`

Create a new `Selection` instance with `properties`.

### `Selection.createProperties`

`Selection.createProperties(object: Object|Selection) => Object`

Create a new dictionary of range properties from an `object`.

### `Selection.fromJSON`

`Selection.fromJSON(object: Object) => Selection`

Create a range from a JSON `object`.

### `Selection.isSelection`

`Selection.isSelection(value: Any) => Boolean`

Check whether a `value` is a `Selection`.

## Instance Methods

### `toJSON`

`toJSON() => Object`

Return a JSON representation of the range.

## Mutating Methods

### `setIsFocused`

`setIsFocused(isFocused: Boolean) => Selection`

Return a new range with a new `isFocused` value.

### `setMarks`

`setMarks(marks: Set|Null) => Selection`

Return a new range with a new set of `marks`.


# Text

```javascript
import { Text } from 'slate'
```

A text node in a Slate [`Document`](https://docs.slatejs.org/slate-core/document). Text nodes are always the bottom-most leaves in the document, just like in the DOM.

## Properties

```javascript
Text({
  key: String,
  text: String,
  marks: Immutable.List<Mark>,
})
```

### `key`

`String`

A unique identifier for the node.

### `text`

`String`

The text contents of this node.

### `marks`

`Immutable.Set<Mark>,`

A list of marks for this node.

### `object`

`String`

An immutable string value of `'text'` for easily separating this node from [`Inline`](https://docs.slatejs.org/slate-core/inline) or [`Block`](https://docs.slatejs.org/slate-core/block) nodes.

## Static Methods

### `Text.create`

`Text.create(properties: Object) => Text`

Create a text from a plain JavaScript object of `properties`.

### `Text.fromJSON`

`Text.fromJSON(object: Object) => Text`

Create a text from a JSON `object`.

### `Text.isText`

`Text.isText(maybeText: Any) => Boolean`

Returns a boolean if the passed in argument is a `Text`.

## Instance Methods

### `toJSON`

`toJSON() => Object`

Returns a JSON representation of the text.


# Utils

```javascript
import { KeyUtils } from 'slate'
```

Utility functions that ship with Slate that may be useful for certain use cases.

## Key Utils

### `KeyUtils.create`

`create() => String`

Create a new key using the current key generator.

### `KeyUtils.resetGenerator`

`resetGenerator() => Void`

Resets Slate's internal key generating function to its default state. This is useful for server-side rendering, or anywhere you want to ensure fresh, deterministic creation of keys.

### `KeyUtils.setGenerator`

`setGenerator(generator: Function) => Void`

Allows you to specify your own key generating function, instead of using Slate's built-in default generator which simply uses auto-incrementing number strings. (eg. `'0'`, `'1'`, `'2'`, ...)

This will act globally on all uses of the Slate dependency.


# Value

```javascript
import { Value } from 'slate'
```

A `Value` is the top-level representation of data in Slate, containing both a [`Document`](https://docs.slatejs.org/slate-core/document) and a [`Selection`](https://docs.slatejs.org/slate-core/selection). It's what you need to pass into the Slate [`<Editor>`](https://docs.slatejs.org/slate-react/editor) to render something onto the page.

## Properties

```javascript
Value({
  document: Document,
  selection: Selection,
  data: Data,
  decorations: List<Decoration>,
})
```

### `data`

`Data`

An object containing arbitrary data for the value.

### `decorations`

`List<Decoration>`

A list of ranges in the document with marks that aren't part of the content itself—like matches for the current search string.

### `document`

`Document`

The current document of the value.

### `object`

`String`

A string with a value of `'value'`.

### `selection`

`Selection`

The current selection of the value.

## Computed Properties

These properties aren't supplied when creating a `Value`, but are instead computed based on the current `document` and `selection`.

### `{edge}Text`

`Text`

Get the leaf [`Text`](https://docs.slatejs.org/slate-core/text) node at `{edge}`. Where `{edge}` is one of: `anchor`, `focus`, `start` or `end`.

### `{edge}Block`

`Block`

Get the leaf [`Block`](https://docs.slatejs.org/slate-core/block) node at `{edge}`. Where `{edge}` is one of: `anchor`, `focus`, `start` or `end`.

### `marks`

`Set`

Get a set of the [`Marks`](https://docs.slatejs.org/slate-core/mark) in the current selection.

### `activeMarks`

`Set`

Get a subset of the [`Marks`](https://docs.slatejs.org/slate-core/mark) that are present in *all* the characters in the current selection. It can be used to determine the active/inactive state of toolbar buttons corresponding to marks, based on the usual rich text editing conventions.

### `blocks`

`List`

Get a list of the lowest-depth [`Block`](https://docs.slatejs.org/slate-core/block) nodes in the current selection.

### `fragment`

`Document`

Get a [`Document`](https://docs.slatejs.org/slate-core/document) fragment of the current selection.

### `inlines`

`List`

Get a list of the lowest-depth [`Inline`](https://docs.slatejs.org/slate-core/inline) nodes in the current selection.

### `texts`

`List`

Get a list of the [`Text`](https://docs.slatejs.org/slate-core/text) nodes in the current selection.

## Static Methods

### `Value.create`

`Value.create(properties: Object) => Value`

Create a new `Value` instance with `properties`.

### `Value.fromJSON`

`Value.fromJSON(object: Object) => Value`

Create a value from a JSON `object`.

### `Value.isValue`

`Value.isValue(any: Any) => Boolean`

Returns a boolean if the passed in argument is a `Value`.

## Instance Methods

### `toJSON`

`toJSON() => Object`

Returns a JSON representation of the value.


# Editor

```javascript
import { Editor } from 'slate-react'
```

The top-level React component that renders the Slate editor itself.

## Props

```javascript
<Editor
  id={String}
  autoCorrect={Boolean}
  autoFocus={Boolean}
  className={String}
  commands={Object}
  onChange={Function}
  placeholder={String | Element}
  plugins={Array}
  queries={Object}
  readOnly={Boolean}
  role={String}
  schema={Object}
  spellCheck={Boolean}
  value={Value}
  style={Object}
  tabIndex={Number}
/>
```

### `id`

`String`

Id for the top-level rendered HTML element of the editor.

### `autoCorrect`

`Boolean`

Whether or not the editor should attempt to autocorrect spellcheck errors.

### `autoFocus`

`Boolean`

Whether or not the editor should attempt to give the contenteditable element focus when it's loaded onto the page.

### `className`

`String`

An optional class name to apply to the contenteditable element.

### `onChange`

`Function onChange(change: Change)`

A change handler that will be called with the `change` that applied the change. You should usually pass the newly changed `change.value` back into the editor through its `value` property. This hook allows you to add persistence logic to your editor.

### `placeholder`

`String || Element`

A placeholder string (or React element) that will be rendered if the document only contains a single empty block.

### `plugins`

`Array`

An array of [`Plugins`](https://docs.slatejs.org/slate-react/plugins) that define the editor's behavior.

### `readOnly`

`Boolean`

Whether the editor should be in "read-only" mode, where all of the rendering is the same, but the user is prevented from editing the editor's content.

### `role`

`String`

ARIA property to define the role of the editor, it defaults to `textbox` when editable.

### `spellCheck`

`Boolean`

Whether or not spellcheck is turned on for the editor.

### `style`

`Object`

An optional dictionary of styles to apply to the contenteditable element.

### `tabIndex`

`Number`

Indicates if it should participate to [sequential keyboard navigation](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/tabindex).

### `value`

`Value`

A [`Value`](https://docs.slatejs.org/slate-core/value) object representing the current value of the editor.

## Plugin-like Props

In addition to its own properties, the editor allows passing any of the properties that a [plugin](https://docs.slatejs.org/slate-react/plugins) defines as well.

These properties are actually just a convenience—an implicit plugin definition. Internally, they are grouped together and turned into a plugin that is given first priority in the plugin stack.

For example, these two snippets of code are equivalent:

```javascript
const plugins = [
  somePlugin
]

<Editor
  onKeyDown={myKeyHandler}
  plugins={plugins}
  value={value}
/>
```

```javascript
const editorPlugin = {
  onKeyDown: myKeyHandler
}

const plugins = [
  editorPlugin,
  somePlugin
]

<Editor
  plugins={plugins}
  value={value}
/>
```

### `onBeforeInput`

### `onBlur`

### `onFocus`

### `onCopy`

### `onCut`

### `onDrop`

### `onKeyDown`

### `onKeyUp`

### `onPaste`

### `onSelect`

### `schema`

To see how these properties behave, check out the [Plugins reference](https://docs.slatejs.org/slate-react/plugins).


# Plugins

Plugins can be attached to an editor to alter its behavior in different ways. Each editor has a "stack" of plugins, which has a specific order, which it runs through when certain hooks are triggered.

Plugins are plain JavaScript objects, containing a set of middleware functions that run for each hook they choose to implement.

## Hooks

In addition to the [core plugin hooks](https://docs.slatejs.org/slate-core/plugins), when using `slate-react` there are additional browser-specific event handling hooks, and React-specific rendering hooks available to plugins.

```javascript
{
  decorateNode: Function,
  onBeforeInput: Function,
  onBlur: Function,
  onCopy: Function,
  onCut: Function,
  onDrop: Function,
  onFocus: Function,
  onKeyDown: Function,
  onKeyUp: Function,
  onMouseUp: Function,
  onPaste: Function,
  onSelect: Function,
  renderEditor: Function,
  renderMark: Function,
  renderAnnotation: Function,
  renderDecoration: Function,
  renderBlock: Function,
  renderInline: Function,
  shouldNodeComponentUpdate: Function,
}
```

The event hooks have a signature of `(event, editor, next)`—the `event` is a React object that you are used to from React's event handlers.

The rendering hooks are just like render props common to other React API's, and receive `(props, editor, next)`. For more information, see the [Rendering](https://docs.slatejs.org/slate-react/rendering) reference.

### `decorateNode`

`Function decorateNode(node: Node, editor: Editor, next: Function) => Array<Decoration>|Void`

The `decorateNode` hook takes a `node` and returns an array of decorations with marks to be applied to the node when it is rendered.

### `onBeforeInput`

`Function onBeforeInput(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called right before a string of text is inserted into the `contenteditable` element.

Make sure to `event.preventDefault()` if you do not want the default insertion behavior to occur!

### `onBlur`

`Function onBlur(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called when the editor's `contenteditable` element is blurred.

### `onFocus`

`Function onFocus(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called when the editor's `contenteditable` element is focused.

### `onCopy`

`Function onCopy(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called when there is a copy event in the editor's `contenteditable` element.

### `onCut`

`Function onCut(event: Event, editor: Editor, next: Function) => Boolean`

This handler is equivalent to the `onCopy` handler.

### `onDrop`

`Function onDrop(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called when the user drops content into the `contenteditable` element. The event is already prevented by default, so you must define a value change to have any affect occur.

### `onKeyDown`

`Function onKeyDown(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called when any key is pressed in the `contenteditable` element, before any action is taken.

Make sure to `event.preventDefault()` if you do not want the default insertion behavior to occur!

### `onKeyUp`

`Function onKeyUp(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called when any key is released in the `contenteditable` element.

### `onPaste`

`Function onPaste(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called when the user pastes content into the `contenteditable` element. The event is already prevented by default, so you must define a value change to have any affect occur.

### `onSelect`

`Function onSelect(event: Event, editor: Editor, next: Function) => Boolean`

This handler is called whenever the native DOM selection changes.

> 🤖 This is **not** Slate's internal selection representation. If you want to get notified when Slate's `value.selection` changes, use the [`onChange`](https://docs.slatejs.org/editor#onchange) property of the `<Editor>`. This handler is instead meant to give you lower-level access to the DOM selection handling, which **is not always triggered** as you'd expect.

### `renderEditor`

`Function renderEditor(props: Object, editor: Editor, next: Function) => ReactNode|Void`

The `renderEditor` property allows you to define higher-order-component-like behavior. It is passed all of the properties of the editor, including `children`, which you can access as `next()`. You can then choose to wrap the existing `children` in any custom elements or proxy the properties however you choose. Note, that multiple plugins can define `renderEditor` and each one can add a specific behaviour to the editor, as `next()` refers to `children` from another plugin in the stack. This can be useful for rendering toolbars, styling the editor, rendering validation, etc, and each plugin can be responsible for a given functionality only, keeping your code dry and well organized. Just remember that the `renderEditor` function has to render `children` for editor's content to render. For example:

```javascript
renderEditor: (props, editor, next) => {
  const children = next()

  return (
    <div>
      <MyToolbarComponent editor={editor} />
      <MyEditorComponent editor={editor}>{children}</MyEditorComponent>
    </div>
  )
}
```

### `renderMark`

`Function renderMark(props: Object, editor: Editor, next: Function) => ReactNode|Void`

Render a `Mark` with `props`. The `props` object contains:

```javascript
{
  attributes: Object,
  children: ReactNode,
  editor: Editor,
  mark: Mark,
  marks: Set<Mark>,
  node: Node,
  offset: Number,
  text: String,
}
```

You must spread the `props.attributes` onto the top-level DOM node you use to render the mark.

### `renderDecoration`

`Function renderDecoration(props: Object, editor: Editor, next: Function) => ReactNode|Void`

Render a `Decoration` with `props`. The `props` object contains:

```javascript
{
  attributes: Object,
  children: ReactNode,
  editor: Editor,
  decoration: Decoration,
  marks: Set<Mark>,
  node: Node,
  offset: Number,
  text: String,
}
```

You must spread the `props.attributes` onto the top-level DOM node you use to render the annotation.

### `renderAnnotation`

`Function renderAnnotation(props: Object, editor: Editor, next: Function) => ReactNode|Void`

Render an `Annotation` with `props`. The `props` object contains:

```javascript
{
  attributes: Object,
  children: ReactNode,
  editor: Editor,
  annotation: Annotation,
  marks: Set<Mark>,
  node: Node,
  offset: Number,
  text: String,
}
```

You must spread the `props.attributes` onto the top-level DOM node you use to render the annotation.

### `renderBlock`

`Function renderBlock(props: Object, editor: Editor, next: Function) => ReactNode|Void`

Render a Block `Node` with `props`. The `props` object contains:

```javascript
{
  attributes: Object,
  children: ReactNode,
  editor: Editor,
  isFocused: Boolean,
  isSelected: BOolean,
  node: Node,
  parent: Node,
  readOnly: Boolean,
}
```

You must spread the `props.attributes` onto the top-level DOM node you use to render the node. You must also be sure to assign `attributes.ref` to the native DOM component being rendered (using `forwardRef` or `innerRef` if necessary).

### `renderInline`

`Function renderInline(props: Object, editor: Editor, next: Function) => ReactNode|Void`

Render an Inline `Node` with `props`. The `props` object contains:

```javascript
{
  attributes: Object,
  children: ReactNode,
  editor: Editor,
  isFocused: Boolean,
  isSelected: BOolean,
  node: Node,
  parent: Node,
  readOnly: Boolean,
}
```

You must spread the `props.attributes` onto the top-level DOM node you use to render the node. You must also be sure to assign `attributes.ref` to the native DOM component being rendered (using `forwardRef` or `innerRef` if necessary).

### `shouldNodeComponentUpdate`

`Function shouldNodeComponentUpdate(previousProps: Object, props: Object, editor: Editor, next: Function) => Boolean|Void`

If this function returns `true`, it can force updating the node's component where otherwise it wouldn't for performance.


# Rendering

Slate will render custom nodes for [`Block`](https://docs.slatejs.org/slate-core/block) and [`Inline`](https://docs.slatejs.org/slate-core/inline) models, based on what you pass in as your schema. This allows you to completely customize the rendering behavior of your Slate editor.

## Props

```javascript
{
  attributes: Object,
  children: Object,
  editor: Editor,
  isSelected: Boolean,
  isFocused: Boolean,
  node: Node,
  parent: Node,
  readOnly: Boolean,
}
```

### `attributes`

`Object`

A dictionary of DOM attributes that you must attach to the main DOM element of the node you render. For example:

```javascript
return <p {...props.attributes}>{props.children}</p>
```

```javascript
return (
  <figure {...props.attributes}>
    <img src={...} />
  </figure>
)
```

### `children`

`Object`

A set of React children elements that are composed of internal Slate components that handle all of the editing logic of the editor for you. You must render these as the children of your non-void nodes. For example:

```javascript
return <p {...props.attributes}>{props.children}</p>
```

### `editor`

`Editor`

A reference to the Slate [`<Editor>`](https://docs.slatejs.org/slate-react/editor) instance. This allows you to retrieve the current `value` of the editor, or perform a `change` on the value. For example:

```javascript
const value = editor.value
```

```javascript
editor.moveToRangeOfDocument().delete()
```

### `isSelected`

`Boolean`

A boolean representing whether the node you are rendering is currently selected. You can use this to render a visual representation of the selection.

This boolean is true when the node is selected and the editor is blurred.

### `isFocused`

`Boolean`

A boolean representing whether the node you are rendering is currently focused. You can use this to render a visual representation of the focused selection.

### `node`

`Node`

A reference to the [`Node`](https://docs.slatejs.org/slate-core/node) being rendered.

### `parent`

`Node`

A reference to the parent of the current [`Node`](https://docs.slatejs.org/slate-core/node) being rendered.

### `readOnly`

`Boolean`

Whether the editor is in "read-only" mode, where all of the rendering is the same, but the user is prevented from editing the editor's content.


# Utils

```javascript
import {
  cloneFragment,
  findDOMNode,
  findDOMRange,
  findNode,
  findRange,
  getEventRange,
  getEventTransfer,
  setEventTransfer,
} from 'slate-react'
```

React-specific utility functions for Slate that may be useful in certain use cases.

## Functions

### `cloneFragment`

`cloneFragment(event: DOMEvent|ReactEvent, editor: Editor, fragment: Document)`

During a cut or copy event, sets `fragment` as the Slate document fragment to be copied.

```javascript
function onCopy(event, editor, next) {
  const fragment = // ... create a fragment from a set of nodes ...

  if (fragment) {
    cloneFragment(event, editor, fragment)
    return true
  }
}
```

Note that calling `cloneFragment` should be the last thing you do in your event handler. If you change the window selection after calling `cloneFragment`, the browser may copy the wrong content. If you need to perform an action after calling `cloneFragment`, wrap it in `requestAnimationFrame`:

```javascript
function onCut(event, editor, next) {
  const fragment = // ... create a fragment from a set of nodes ...

  if (fragment) {
    cloneFragment(event, editor, fragment)
    window.requestAnimationFrame(() => {
      editor.delete()
    })
    return true
  }
}
```

### `findDOMNode`

`findDOMNode(node: Node) => DOMElement`

Find the DOM node from a Slate [`Node`](https://docs.slatejs.org/slate-core/node). Modelled after React's built-in `findDOMNode` helper.

```javascript
function componentDidUpdate() {
  const { node } = this.props
  const element = findDOMNode(node)
  // Do something with the DOM `element`...
}
```

### `findDOMRange`

`findDOMRange(range: Range) => DOMRange`

Find the DOM range from a Slate [`Range`](https://docs.slatejs.org/slate-core/range).

```javascript
function onChange(editor) {
  const { value } = editor
  const range = findDOMRange(value.selection)
  // Do something with the DOM `range`...
}
```

### `findNode`

`findNode(element: DOMElement, editor: Editor) => Node`

Find the Slate node from a DOM `element` and Slate `editor`.

```javascript
function onSomeNativeEvent(event) {
  const node = findNode(event.target, editor)
  // Do something with `node`...
}
```

### `findRange`

`findRange(selection: DOMSelection, editor: Editor) => Range` `findRange(range: DOMRange, editor: Editor) => Range`

Find the Slate range from a DOM `range` or `selection` and a Slate `editor`.

```javascript
function onSomeNativeEvent() {
  // You can find a range from a native DOM selection...
  const nativeSelection = window.getSelection()
  const range = findRange(nativeSelection, editor)

  // ...or from a native DOM range...
  const nativeRange = nativeSelection.getRangeAt(0)
  const range = findRange(nativeRange, editor)
}
```

### `getEventRange`

`getEventRange(event: DOMEvent|ReactEvent, editor: Editor) => Range`

Get the affected Slate range from a DOM `event` and Slate `editor`.

```javascript
function onDrop(event, editor, next) {
  const targetRange = getEventRange(event, editor)
  // Do something at the drop `targetRange`...
}
```

### `getEventTransfer`

`getEventTransfer(event: DOMEvent|ReactEvent) => Object`

Get the Slate-related data from a DOM `event` and Slate `value`.

```javascript
function onDrop(event, editor, next) {
  const transfer = getEventTransfer(event)
  const { type, node } = transfer

  if (type == 'node') {
    // Do something with `node`...
  }
}
```

### `setEventTransfer`

`setEventTransfer(event: DOMEvent|ReactEvent, type: String, data: Any)`

Sets the Slate-related `data` with `type` on an `event`. The `type` must be one of the types Slate recognizes: `'fragment'`, `'html'`, `'node'`, `'rich'`, or `'text'`.

```javascript
function onDragStart(event, editor, next) {
  const { value } = editor
  const { startNode } = value
  setEventTransfer(event, 'node', startNode)
}
```


# slate-html-serializer

```javascript
import Html from 'slate-html-serializer'
```

The HTML serializer lets you parse and stringify arbitrary HTML content, based on your specific schema's use case. You must pass a series of `rules` to define how your Slate schema should be serialized to and from HTML.

For an example of the HTML serializer in action, check out the [`paste-html` example](https://github.com/ianstormtaylor/slate/tree/a0b7976cb9a2812d8d96361e9993fe8853a2cc64/examples/paste-html/README.md).

## Example

```
<p>The Slate editor gives you <em>complete</em> control over the logic you can add.</p>
<p>In its simplest form, when representing plain text, Slate is a glorified <code>&laquo;textarea&raquo;</code>. But you can augment it to be much more than that.</p>
<p>Check out <a href="http://slatejs.org">http://slatejs.org</a> for examples!</p>
```

## Properties

```javascript
new Html({
  rules: Array,
  defaultBlock: String | Object | Block,
  parseHtml: Function,
})
```

### `rules`

`Array`

An array of rules to initialize the HTML serializer with, defining your schema.

### `defaultBlock`

`String|Object|Block`

A set of properties to use for blocks which do not match any rule. Can be a string such as `'paragraph'` or an object with a `type` attribute such as `{ type: 'paragraph' }`, or even a [`Block`](https://docs.slatejs.org/slate-core/block).

### `parseHtml`

`Function`

A function to parse an HTML string and return a DOM object. Defaults to using the native `DOMParser` in browser environments that support it. For older browsers or server-side rendering, you can include the [jsdom](https://www.npmjs.com/package/jsdom) package and pass `JSDOM.fragment` as the `parseHtml` option.

This parse function should return the `<body>` node of the DOM.

## Methods

### `Html.deserialize`

`Html.deserialize(html: String, [options: Object]) => Value`

Deserialize an HTML `string` into a [`Value`](https://docs.slatejs.org/slate-core/value). How the string is deserialized will be determined by the rules that the HTML serializer was constructed with.

If you pass `toJSON: true` as an option, the return value will be a JSON object instead of a [`Value`](https://docs.slatejs.org/slate-core/value) object.

### `Html.serialize`

`Html.serialize(value: Value, [options: Object]) => String || Array`

Serialize a `value` into an HTML string. How the string is serialized will be determined by the rules that the HTML serializer was constructed with.

If you pass `render: false` as an option, the return value will instead be an iterable list of the top-level React elements, to be rendered as children in your own React component.

## Rules

To initialize an HTML serializer, you must pass it an array of rules, defining your schema. Each rule defines how to deserialize and serialize a node or mark, by implementing two functions.

Each rule must define two properties:

```javascript
{
  deserialize: Function,
  serialize: Function
}
```

### `rule.deserialize`

`rule.deserialize(el: Element, next: Function) => Object || Void`

The `deserialize` function receives a DOM element and should return a plain JavaScript object representing the deserialized value, or nothing if the rule in question doesn't know how to deserialize the object, in which case the next rule in the stack will be attempted. Returning `null` will halt the rule chain and add nothing. To delegate to the next rule, the return value must be `undefined`.

The object should be one of:

```javascript
{
  object: 'block',
  type: String,
  data: Object,
  nodes: next(...)
}

{
  object: 'inline',
  type: String,
  data: Object,
  nodes: next(...)
}

{
  object: 'mark',
  type: String,
  data: Object,
  nodes: next(...)
}

{
  object: 'text',
  leaves: Array
}
```

### `rule.serialize`

`rule.serialize(object: Node || Mark || String, children: String || Element || Array) => Element || Void`

The `serialize` function should return a React element representing the serialized HTML, or nothing if the rule in question doesn't know how to serialize the object, in which case the next rule in the stack will be attempted.

The function will be called with either a `Node`, a `Mark`, or a special `String` immutable object, with a `object: 'string'` property and a `text` property containing the text string.

### Default Text Rule

The HTML serializer includes a default rule to handle "normal text". That is, a final rule exists to serialize `object: 'string'` text (replacing line feed characters with `<br>`), and to deserialize text inversely. To avoid this default handling simply provide your own `deserialize` and `serialize` rules for text.


# slate-hyperscript

```javascript
import h from 'slate-hyperscript'
import { createHyperscript } from 'slate-hyperscript'
```

A hyperscript helper for writing Slate documents with JSX!

## Example

```javascript
/** @jsx h */

import h from 'slate-hyperscript'

const value = (
  <value>
    <document>
      <block type="paragraph">
        A string of <mark type="bold">bold</mark> in a{' '}
        <inline type="link" data={{ src: 'http://slatejs.org' }}>
          Slate
        </inline>{' '}
        editor!
      </block>
      <block type="image" data={{ src: 'https://...' }} />
    </document>
  </value>
)
```

```javascript
/** @jsx h */

import { createHyperscript } from 'slate-hyperscript'

const h = createHyperscript({
  blocks: {
    paragraph: 'paragraph',
    image: 'image',
  },
  inlines: {
    link: 'link',
  },
  marks: {
    b: 'bold',
  },
})

const value = (
  <value>
    <document>
      <paragraph>
        A string of <b>bold</b> in a <link src="http://slatejs.org">Slate</link>{' '}
        editor!
      </paragraph>
      <image src="https://..." />
    </document>
  </value>
)
```

## Exports

### `h`

`Function`

The default export of `slate-hyperscript` is a barebones hyperscript helper that you can immediately start using to create Slate objects.

### `createHyperscript`

`createHyperscript(options: Object) => Function`

The other export is a `createHyperscript` helper that you can use to create your own, smarter, schema-aware hyperscript helper. You can pass it `options` that tell it about your schema to make creating objects much terser.

```javascript
{
  blocks: Object,
  inlines: Object,
  marks: Object,
  decorations: Object,
  creators: Object,
}
```


# slate-plain-serializer

```javascript
import Plain from 'slate-plain-serializer'
```

A serializer that converts a Slate [`Value`](https://docs.slatejs.org/slate-core/value) to and from a plain text string.

## Example

```
The Slate editor gives you full control over the logic you can add.\n
In its simplest form, when representing plain text, Slate is a glorified <textarea>. But you can augment it to be much more than that.\n
Check out http://slatejs.org for examples!
```

## Methods

### `Plain.deserialize`

`Plain.deserialize(string: String, [options: Object]) => Value`

Deserialize a plain text `string` into a [`Value`](https://docs.slatejs.org/slate-core/value). A series of blocks will be created by splitting the input string on `\n` characters. Each block is given a type of `'line'`.

If you pass `toJSON: true` as an option, the return value will be a JSON object instead of a [`Value`](https://docs.slatejs.org/slate-core/value) object.

### `Plain.serialize`

`Plain.serialize(value: Value) => String`

Serialize a `value` into a plain text string. Each direct child block of the document will be separated by a `\n` character.


# slate-prop-types

```javascript
import Types from 'slate-prop-types'
```

A set of React prop types for Slate editors and plugins.

## Example

```javascript
import React from 'react'
import Types from 'slate-prop-types'

class Toolbar extends React.Component {

  propTypes = {
    block: Types.block,
    value: Types.value.isRequired,
  }

  ...

}
```

## Exports

### `block`

Ensure that a value is a Slate `Block`.

### `blocks`

Ensure that a value is an immutable `List` of Slate [`Block`](https://docs.slatejs.org/slate-core/block) objects.

### `change`

Ensure that a value is a Slate `Change`.

### `data`

Ensure that a value is a Slate `Data`.

### `document`

Ensure that a value is a Slate `Document`.

### `inline`

Ensure that a value is a Slate `Inline`.

### `inlines`

Ensure that a value is an immutable `List` of Slate [`Inline`](https://docs.slatejs.org/slate-core/inline) objects.

### `leaf`

Ensure that a value is a Slate `Leaf`.

### `leaves`

Ensure that a value is an immutable `List` of Slate [`Leaf`](https://github.com/ianstormtaylor/slate/tree/a0b7976cb9a2812d8d96361e9993fe8853a2cc64/docs/reference/slate/leaf.md) objects.

### `mark`

Ensure that a value is a Slate `Mark`.

### `marks`

Ensure that a value is an immutable `Set` of Slate [`Mark`](https://docs.slatejs.org/slate-core/mark) objects.

### `node`

Ensure that a value is a Slate `Node`.

### `nodes`

Ensure that a value is an immutable `List` of Slate [`Node`](https://docs.slatejs.org/slate-core/mark) objects.

### `range`

Ensure that a value is a Slate `Range`.

### `ranges`

Ensure that a value is an immutable `List` of Slate [`Range`](https://docs.slatejs.org/slate-core/range) objects.

### `text`

Ensure that a value is a Slate [`Text`](https://docs.slatejs.org/slate-core/text).

### `texts`

Ensure that a value is an immutable `List` of Slate [`Text`](https://docs.slatejs.org/slate-core/text) objects.

### `value`

Ensure that a value is a Slate `Value`.


# Introduction

[Slate](http://slatejs.org) is a *completely* customizable framework for building rich text editors.

Slate lets you build rich, intuitive editors like those in [Medium](https://medium.com/), [Dropbox Paper](https://www.dropbox.com/paper) or [Google Docs](https://www.google.com/docs/about/)—which are becoming table stakes for applications on the web—without your codebase getting mired in complexity.

It can do this because all of its logic is implemented with a series of plugins, so you aren't ever constrained by what *is* or *isn't* in "core". You can think of it like a pluggable implementation of `contenteditable` built on top of [React](https://facebook.github.io/react/). It was inspired by libraries like [Draft.js](https://facebook.github.io/draft-js/), [Prosemirror](http://prosemirror.net/) and [Quill](http://quilljs.com/).

> 🤖 **Slate is currently in beta**. Its core API is usable now, but you might need to pull request fixes for advanced use cases. Some of its APIs are not "finalized" and will (breaking) change over time as we find better solutions.

## Why?

Why create Slate? Well... *(Beware: this section has a few of* [*my*](https://github.com/ianstormtaylor) *opinions!)*

Before creating Slate, I tried a lot of the other rich text libraries out there—[**Draft.js**](https://facebook.github.io/draft-js/), [**Prosemirror**](http://prosemirror.net/), [**Quill**](http://quilljs.com/), etc. What I found was that while getting simple examples to work was easy enough, once you started trying to build something like [Medium](https://medium.com/), [Dropbox Paper](https://www.dropbox.com/paper) or [Google Docs](https://www.google.com/docs/about/), you ran into deeper issues...

* **The editor's "schema" was hardcoded and hard to customize.** Things like bold and italic were supported out of the box, but what about comments, or embeds, or even more domain-specific needs?
* **Transforming the documents programmatically was very convoluted.** Writing as a user may have worked, but making programmatic changes, which is critical for building advanced behaviors, was needlessly complex.
* **Serializing to HTML, Markdown, etc. seemed like an afterthought.** Simple things like transforming a document to HTML or Markdown involved writing lots of boilerplate code, for what seemed like very common use cases.
* **Re-inventing the view layer seemed inefficient and limiting.** Most editors rolled their own views, instead of using existing technologies like React, so you had to learn a whole new system with new "gotchas".
* **Collaborative editing wasn't designed for in advance.** Often the editor's internal representation of data made it impossible to use for a realtime, collaborative editing use case without basically rewriting the editor.
* **The repositories were monolithic, not small and reusable.** The code bases for many of the editors often didn't expose the internal tooling that could have been re-used by developers, leading to having to reinvent the wheel.
* **Building complex, nested documents was impossible.** Many editors were designed around simplistic "flat" documents, making things like tables, embeds and captions difficult to reason about and sometimes impossible.

Of course not every editor exhibits all of these issues, but if you've tried using another editor you might have run into similar problems. To get around the limitations of their APIs and achieve the user experience you're after, you have to resort to very hacky things. And some experiences are just plain impossible to achieve.

If that sounds familiar, you might like Slate.

Which brings me to how Slate solves all of that...

## Principles

Slate tries to solve the question of "[Why?](#why)" with a few principles:

1. **First-class plugins.** The most important part of Slate is that plugins are first-class entities. That means you can *completely* customize the editing experience, to build complex editors like Medium's or Dropbox's, without having to fight against the library's assumptions.
2. **Schema-less core.** Slate's core logic assumes very little about the schema of the data you'll be editing, which means that there are no assumptions baked into the library that'll trip you up when you need to go beyond the most basic use cases.
3. **Nested document model.** The document model used for Slate is a nested, recursive tree, just like the DOM itself. This means that creating complex components like tables or nested block quotes are possible for advanced use cases. But it's also easy to keep it simple by only using a single level of hierarchy.
4. **Parallel to the DOM.** Slate's data model is based on the DOM—the document is a nested tree, it uses selections and ranges, and it exposes all the standard event handlers. This means that advanced behaviors like tables or nested block quotes are possible. Pretty much anything you can do in the DOM, you can do in Slate.
5. **Intuitive commands.** Slate documents are edited using "commands", that are designed to be high-level and extremely intuitive to write and read, so that custom functionality is as expressive as possible. This greatly increases your ability to reason about your code.
6. **Collaboration-ready data model.** The data model Slate uses—specifically how operations are applied to the document—has been designed to allow for collaborative editing to be layered on top, so you won't need to rethink everything if you decide to make your editor collaborative.
7. **Clear "core" boundaries.** With a plugin-first architecture, and a schema-less core, it becomes a lot clearer where the boundary is between "core" and "custom", which means that the core experience doesn't get bogged down in edge cases.

## Demo

Check out the [**live demo**](http://slatejs.org) of all of the examples!

## Examples

To get a sense for how you might use Slate, check out a few of the examples:

* [**Plain text**](https://www.slatejs.org/examples/plaintext) — showing the most basic case: a glorified `<textarea>`.
* [**Rich text**](https://www.slatejs.org/examples/richtext) — showing the features you'd expect from a basic editor.
* [**Markdown preview**](https://www.slatejs.org/examples/markdown-preview) — showing how to add key handlers for Markdown-like shortcuts.
* [**Inlines**](https://www.slatejs.org/examples/inlines) — showing how to wrap text in inline nodes with associated data.
* [**Images**](https://www.slatejs.org/examples/images) — showing how to use void (text-less) nodes to add images.
* [**Hovering toolbar**](https://www.slatejs.org/examples/hovering-toolbar) — showing how a contextual hovering menu can be implemented.
* [**Tables**](https://www.slatejs.org/examples/tables) — showing how to nest blocks to render more advanced components.
* [**Paste HTML**](https://www.slatejs.org/examples/paste-html) — showing how to use an HTML serializer to handle pasted HTML.
* [**Mentions**](https://www.slatejs.org/examples/mentions) — showing how to use inline void nodes for simple @-mentions.

Each example includes a **View Source** link to the code that implements it. And we have [other examples](https://github.com/ianstormtaylor/slate/tree/master/site/examples) too.

If you have an idea for an example that shows a common use case, pull request it!

## Documentation

If you're using Slate for the first time, check out the [Getting Started](http://docs.slatejs.org/walkthroughs/01-installing-slate) walkthroughs and the [Concepts](http://docs.slatejs.org/concepts) to familiarize yourself with Slate's architecture and mental models.

* [**Walkthroughs**](http://docs.slatejs.org/walkthroughs)
* [**Concepts**](http://docs.slatejs.org/concepts)
* [**FAQ**](http://docs.slatejs.org/general/faq)
* [**Resources**](http://docs.slatejs.org/general/resources)

If even that's not enough, you can always [read the source itself](https://github.com/ianstormtaylor/slate/tree/master/packages), which is heavily commented.

There are also translations of the documentation into other languages:

* [中文](https://doodlewind.github.io/slate-doc-cn/)

If you're maintaining a translation, feel free to pull request it here!

## Contributing!

All contributions are super welcome! Check out the [Contributing instructions](https://docs.slatejs.org/general/contributing) for more info!

Slate is [MIT-licensed](https://github.com/ianstormtaylor/slate/tree/f6bfe034d707693488c38da77537fd36cb8856cf/License.md).


# Installing Slate

Slate is a monorepo divided up into multiple npm packages, so to install it you do:

```
yarn add slate slate-react
```

You'll also need to be sure to install Slate's peer dependencies:

```
yarn add react react-dom
```

*Note, if you'd rather use a pre-bundled version of Slate, you can `yarn add slate` and retrieve the bundled `dist/slate.js` file! Check out the* [*Using the Bundled Source*](https://github.com/ianstormtaylor/slate/blob/main/docs/walkthroughs/xx-using-the-bundled-source.md) *guide for more information.*

Once you've installed Slate, you'll need to import it.

```jsx
// Import React dependencies.
import React, { useState } from 'react'
// Import the Slate editor factory.
import { createEditor } from 'slate'

// Import the Slate components and React plugin.
import { Slate, Editable, withReact } from 'slate-react'
```

Before we use those imports, let's start with an empty `<App>` component:

```jsx
// Define our app...
const App = () => {
  return null
}
```

The next step is to create a new `Editor` object. We want the editor to be stable across renders, so we use the `useState` hook [without a setter](https://github.com/ianstormtaylor/slate/pull/3925#issuecomment-781179930):

```jsx
const App = () => {
  // Create a Slate editor object that won't change across renders.
  const [editor] = useState(() => withReact(createEditor()))
  return null
}
```

Of course we haven't rendered anything, so you won't see any changes.

> If you are using TypeScript, you will also need to extend the `Editor` with `ReactEditor` and add annotations as per the documentation on [TypeScript](https://docs.slatejs.org/concepts/12-typescript). The example below also includes the custom types required for the rest of this example.

```typescript
// TypeScript users only add this code
import { BaseEditor, Descendant } from 'slate'
import { ReactEditor } from 'slate-react'

type CustomElement = { type: 'paragraph'; children: CustomText[] }
type CustomText = { text: string }

declare module 'slate' {
  interface CustomTypes {
    Editor: BaseEditor & ReactEditor
    Element: CustomElement
    Text: CustomText
  }
}
```

Next up is to render a `<Slate>` context provider.

The provider component keeps track of your Slate editor, its plugins, its value, its selection, and any changes that occur. It **must** be rendered above any `<Editable>` components. But it can also provide the editor state to other components like toolbars, menus, etc. using the `useSlate` hook.

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))
  // Render the Slate context.
  return <Slate editor={editor} initialValue={initialValue} />
}
```

You can think of the `<Slate>` component as providing a context to every component underneath it.

> Slate Provider's "value" prop is only used as initial state for editor.children. If your code relies on replacing editor.children you should do so by replacing it directly instead of relying on the "value" prop to do this for you. See [Slate PR 4540](https://github.com/ianstormtaylor/slate/pull/4540) for a more in-depth discussion.

This is a slightly different mental model than things like `<input>` or `<textarea>`, because richtext documents are more complex. You'll often want to include toolbars, or live previews, or other complex components next to your editable content.

By having a shared context, those other components can execute commands, query the editor's state, etc.

The next step is to render the `<Editable>` component itself. The component acts like `contenteditable`; anywhere you render it will render an editable richtext document for the nearest editor context.

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))
  return (
    // Add the editable component inside the context.
    <Slate editor={editor} initialValue={initialValue}>
      <Editable />
    </Slate>
  )
}
```

There you have it!

That's the most basic example of Slate. If you render that onto the page, you should see a paragraph with the text `A line of text in a paragraph.` And when you type, you should see the text change!


# Adding Event Handlers

Okay, so you've got Slate installed and rendered on the page, and when you type in it, you can see the changes reflected. But you want to do more than just type a plaintext string.

What makes Slate great is how easy it is to customize. Just like other React components you're used to, Slate allows you to pass in handlers that are triggered on certain events.

Let's use the `onKeyDown` handler to change the editor's content when we press a key.

Here's our app from earlier:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable />
    </Slate>
  )
}
```

Now we add an `onKeyDown` handler:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        // Define a new handler which prints the key that was pressed.
        onKeyDown={event => {
          console.log(event.key)
        }}
      />
    </Slate>
  )
}
```

Cool, now when a key is pressed in the editor, its corresponding keycode is logged in the console.

Now we want to make it actually change the content. For the purposes of our example, let's implement turning all ampersand, `&`, keystrokes into the word `and` upon being typed.

Our `onKeyDown` handler might look like this:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        onKeyDown={event => {
          if (event.key === '&') {
            // Prevent the ampersand character from being inserted.
            event.preventDefault()
            // Execute the `insertText` method when the event occurs.
            editor.insertText('and')
          }
        }}
      />
    </Slate>
  )
}
```

With that added, try typing `&`, and you should see it suddenly become `and` instead!

This offers a sense of what can be done with Slate's event handlers. Each one will be called with the `event` object, and you can use your `editor` to perform commands in response. Simple!


# Defining Custom Elements

In our previous example, we started with a paragraph, but we never actually told Slate anything about the `paragraph` block type. We just let it use its internal default renderer, which uses a plain old `<div>`.

But that's not all you can do. Slate lets you define any type of custom blocks you want, like block quotes, code blocks, list items, etc.

We'll show you how. Let's start with our app from earlier:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        onKeyDown={event => {
          if (event.key === '&') {
            event.preventDefault()
            editor.insertText('and')
          }
        }}
      />
    </Slate>
  )
}
```

Now let's add "code blocks" to our editor.

The problem is, code blocks won't just be rendered as a plain paragraph, they'll need to be rendered differently. To make that happen, we need to define a "renderer" for `code` element nodes.

Element renderers are just simple React components, like so:

```jsx
// Define a React component renderer for our code blocks.
const CodeElement = props => {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}
```

Easy enough.

See the `props.attributes` reference? Slate passes attributes that should be rendered on the top-most element of your blocks, so that you don't have to build them up yourself. You **must** mix the attributes into your component.

And see that `props.children` reference? Slate will automatically render all of the children of a block for you, and then pass them to you just like any other React component would, via `props.children`. That way you don't have to muck around with rendering the proper text nodes or anything like that. You **must** render the children as the lowest leaf in your component.

And here's a component for the "default" elements:

```jsx
const DefaultElement = props => {
  return <p {...props.attributes}>{props.children}</p>
}
```

Now, let's add that renderer to our `Editor`:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  // Define a rendering function based on the element passed to `props`. We use
  // `useCallback` here to memoize the function for subsequent renders.
  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        // Pass in the `renderElement` function.
        renderElement={renderElement}
        onKeyDown={event => {
          if (event.key === '&') {
            event.preventDefault()
            editor.insertText('and')
          }
        }}
      />
    </Slate>
  )
}

const CodeElement = props => {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}

const DefaultElement = props => {
  return <p {...props.attributes}>{props.children}</p>
}
```

Okay, but now we'll need a way for the user to actually turn a block into a code block. So let's change our `onKeyDown` function to add a `` Ctrl-` `` shortcut that does just that:

```jsx
// Import the `Editor` and `Transforms` helpers from Slate.
import { Editor, Transforms, Element } from 'slate'

const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        renderElement={renderElement}
        onKeyDown={event => {
          if (event.key === '`' && event.ctrlKey) {
            // Prevent the "`" from being inserted by default.
            event.preventDefault()
            // Otherwise, set the currently selected blocks type to "code".
            Transforms.setNodes(
              editor,
              { type: 'code' },
              { match: n => Element.isElement(n) && Editor.isBlock(editor, n) }
            )
          }
        }}
      />
    </Slate>
  )
}

const CodeElement = props => {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}

const DefaultElement = props => {
  return <p {...props.attributes}>{props.children}</p>
}
```

Now, if you press `` Ctrl-` `` the block your cursor is in should turn into a code block! Magic!

But we forgot one thing. When you hit `` Ctrl-` `` again, it should change the code block back into a paragraph. To do that, we'll need to add a bit of logic to change the type we set based on whether any of the currently selected blocks are already a code block:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        renderElement={renderElement}
        onKeyDown={event => {
          if (event.key === '`' && event.ctrlKey) {
            event.preventDefault()
            // Determine whether any of the currently selected blocks are code blocks.
            const [match] = Editor.nodes(editor, {
              match: n => n.type === 'code',
            })
            // Toggle the block type depending on whether there's already a match.
            Transforms.setNodes(
              editor,
              { type: match ? 'paragraph' : 'code' },
              { match: n => Element.isElement(n) && Editor.isBlock(editor, n) }
            )
          }
        }}
      />
    </Slate>
  )
}
```

And there you have it! If you press `` Ctrl-` `` while inside a code block, it should turn back into a paragraph!


# Applying Custom Formatting

In the previous guide we learned how to create custom block types that render chunks of text inside different containers. But Slate allows for more than just "blocks".

In this guide, we'll show you how to add custom formatting options, like **bold**, *italic*, `code` or ~~strikethrough~~.

So we start with our app from earlier:

```jsx
const renderElement = props => {
  switch (props.element.type) {
    case 'code':
      return <CodeElement {...props} />
    default:
      return <DefaultElement {...props} />
  }
}

const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        renderElement={renderElement}
        onKeyDown={event => {
          if (event.key === '`' && event.ctrlKey) {
            event.preventDefault()
            const [match] = Editor.nodes(editor, {
              match: n => n.type === 'code',
            })
            Transforms.setNodes(
              editor,
              { type: match ? 'paragraph' : 'code' },
              { match: n => Element.isElement(n) && Editor.isBlock(editor, n) }
            )
          }
        }}
      />
    </Slate>
  )
}
```

And now, we'll edit the `onKeyDown` handler to make it so that when you press `control-B`, it will add a `bold` format to the currently selected text:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        renderElement={renderElement}
        onKeyDown={event => {
          if (!event.ctrlKey) {
            return
          }

          switch (event.key) {
            // When "`" is pressed, keep our existing code block logic.
            case '`': {
              event.preventDefault()
              const [match] = Editor.nodes(editor, {
                match: n => n.type === 'code',
              })
              Transforms.setNodes(
                editor,
                { type: match ? 'paragraph' : 'code' },
                {
                  match: n => Element.isElement(n) && Editor.isBlock(editor, n),
                }
              )
              break
            }

            // When "B" is pressed, bold the text in the selection.
            case 'b': {
              event.preventDefault()
              Editor.addMark(editor, 'bold', true)
              break
            }
          }
        }}
      />
    </Slate>
  )
}
```

Unlike the code format from the previous step, which is a block-level format, bold is a character-level format. Slate manages text contained within blocks (or any other element) using "leaves". Slate's character-level formats/styles are called "marks". Adjacent text with the same marks (styles) applied will be grouped within the same "leaf". When we use `addMark` to add our bold mark to the selected text, Slate will automatically break up the "leaves" using the selection boundaries and produce a new "leaf" with the bold mark added.

Okay, so we've got the hotkey handler setup... but! If you happen to now try selecting text and hitting `Ctrl-B`, you won't notice any change. That's because we haven't told Slate how to render a "bold" mark.

For every format you add, you need to tell Slate how to render it, just like for elements. So let's define a `Leaf` component:

```jsx
// Define a React component to render leaves with bold text.
const Leaf = props => {
  return (
    <span
      {...props.attributes}
      style={{ fontWeight: props.leaf.bold ? 'bold' : 'normal' }}
    >
      {props.children}
    </span>
  )
}
```

Pretty familiar, right? Note that it is described with a `span` - This is because all leaves must be an [inline element](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements). You can learn more about leaves in the [Rendering section](https://docs.slatejs.org/concepts/09-rendering#leaves).

And now, let's tell Slate about that leaf. To do that, we'll pass in the `renderLeaf` prop to our editor.

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  // Define a leaf rendering function that is memoized with `useCallback`.
  const renderLeaf = useCallback(props => {
    return <Leaf {...props} />
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        renderElement={renderElement}
        // Pass in the `renderLeaf` function.
        renderLeaf={renderLeaf}
        onKeyDown={event => {
          if (!event.ctrlKey) {
            return
          }

          switch (event.key) {
            case '`': {
              event.preventDefault()
              const [match] = Editor.nodes(editor, {
                match: n => n.type === 'code',
              })
              Transforms.setNodes(
                editor,
                { type: match ? null : 'code' },
                {
                  match: n => Element.isElement(n) && Editor.isBlock(editor, n),
                }
              )
              break
            }

            case 'b': {
              event.preventDefault()
              Editor.addMark(editor, 'bold', true)
              break
            }
          }
        }}
      />
    </Slate>
  )
}

const Leaf = props => {
  return (
    <span
      {...props.attributes}
      style={{ fontWeight: props.leaf.bold ? 'bold' : 'normal' }}
    >
      {props.children}
    </span>
  )
}
```

Now, if you try selecting a piece of text and hitting `Ctrl-B` you should see it turn bold! Magic!


# Executing Commands

Up until now, everything we've learned has been about how to write one-off logic for your specific Slate editor. But one of the most powerful things about Slate is that it lets you model your specific rich text "domain" however you'd like, and write less one-off code.

In the previous guides we've written some useful code to handle formatting code blocks and bold marks. And we've hooked up the `onKeyDown` handler to invoke that code. But we've always done it using the built-in `Editor` helpers directly, instead of using "commands".

Slate lets you augment the built-in `editor` object to handle your own custom rich text commands. And you can even use pre-packaged "plugins" which add a given set of functionality.

Let's see how this works.

We'll start with our app from earlier:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  const renderLeaf = useCallback(props => {
    return <Leaf {...props} />
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        renderElement={renderElement}
        renderLeaf={renderLeaf}
        onKeyDown={event => {
          if (!event.ctrlKey) {
            return
          }

          switch (event.key) {
            case '`': {
              event.preventDefault()
              const [match] = Editor.nodes(editor, {
                match: n => n.type === 'code',
              })
              Transforms.setNodes(
                editor,
                { type: match ? null : 'code' },
                {
                  match: n => Element.isElement(n) && Editor.isBlock(editor, n),
                }
              )
              break
            }

            case 'b': {
              event.preventDefault()
              Editor.addMark(editor, 'bold', true)
              break
            }
          }
        }}
      />
    </Slate>
  )
}
```

It has the concept of "code blocks" and "bold formatting". But these things are all defined in one-off cases inside the `onKeyDown` handler. If you wanted to reuse that logic elsewhere you'd need to extract it.

We can instead implement these domain-specific concepts by creating custom helper functions:

```jsx
// Define our own custom set of helpers.
const CustomEditor = {
  isBoldMarkActive(editor) {
    const marks = Editor.marks(editor)
    return marks ? marks.bold === true : false
  },

  isCodeBlockActive(editor) {
    const [match] = Editor.nodes(editor, {
      match: n => n.type === 'code',
    })

    return !!match
  },

  toggleBoldMark(editor) {
    const isActive = CustomEditor.isBoldMarkActive(editor)
    if (isActive) {
      Editor.removeMark(editor, 'bold')
    } else {
      Editor.addMark(editor, 'bold', true)
    }
  },

  toggleCodeBlock(editor) {
    const isActive = CustomEditor.isCodeBlockActive(editor)
    Transforms.setNodes(
      editor,
      { type: isActive ? null : 'code' },
      { match: n => Element.isElement(n) && Editor.isBlock(editor, n) }
    )
  },
}

const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  const renderLeaf = useCallback(props => {
    return <Leaf {...props} />
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        renderElement={renderElement}
        renderLeaf={renderLeaf}
        onKeyDown={event => {
          if (!event.ctrlKey) {
            return
          }

          // Replace the `onKeyDown` logic with our new commands.
          switch (event.key) {
            case '`': {
              event.preventDefault()
              CustomEditor.toggleCodeBlock(editor)
              break
            }

            case 'b': {
              event.preventDefault()
              CustomEditor.toggleBoldMark(editor)
              break
            }
          }
        }}
      />
    </Slate>
  )
}
```

Now our commands are clearly defined and you can invoke them from anywhere we have access to our `editor` object. For example, from hypothetical toolbar buttons:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  const renderLeaf = useCallback(props => {
    return <Leaf {...props} />
  }, [])

  return (
    // Add a toolbar with buttons that call the same methods.
    <Slate editor={editor} initialValue={initialValue}>
      <div>
        <button
          onMouseDown={event => {
            event.preventDefault()
            CustomEditor.toggleBoldMark(editor)
          }}
        >
          Bold
        </button>
        <button
          onMouseDown={event => {
            event.preventDefault()
            CustomEditor.toggleCodeBlock(editor)
          }}
        >
          Code Block
        </button>
      </div>
      <Editable
        editor={editor}
        renderElement={renderElement}
        renderLeaf={renderLeaf}
        onKeyDown={event => {
          if (!event.ctrlKey) {
            return
          }

          switch (event.key) {
            case '`': {
              event.preventDefault()
              CustomEditor.toggleCodeBlock(editor)
              break
            }

            case 'b': {
              event.preventDefault()
              CustomEditor.toggleBoldMark(editor)
              break
            }
          }
        }}
      />
    </Slate>
  )
}
```

That's the benefit of extracting the logic.

And there you have it! We just added a ton of functionality to the editor with very little work. And we can keep all of our command logic tested and isolated in a single place, making the code easier to maintain.


# Saving to a Database

Now that you've learned the basics of how to add functionality to the Slate editor, you might be wondering how you'd go about saving the content you've been editing, such that you can come back to your app later and have it load.

In this guide, we'll show you how to add logic to save your Slate content to a database for storage and retrieval later.

Let's start with a basic editor:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable />
    </Slate>
  )
}
```

That will render a basic Slate editor on your page, and when you type things will change. But if you refresh the page, everything will be reverted back to its original value—nothing saves!

What we need to do is save the changes you make somewhere. For this example, we'll just be using [Local Storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), but it will give you an idea for where you'd need to add your own database hooks.

So, in our `onChange` handler, we need to save the `value` if anything besides the selection was changed:

```jsx
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate
      editor={editor}
      initialValue={initialValue}
      onChange={value => {
        const isAstChange = editor.operations.some(
          op => 'set_selection' !== op.type
        )
        if (isAstChange) {
          // Save the value to Local Storage.
          const content = JSON.stringify(value)
          localStorage.setItem('content', content)
        }
      }}
    >
      <Editable />
    </Slate>
  )
}
```

Now whenever you edit the page, if you look in Local Storage, you should see the `content` value changing.

But... if you refresh the page, everything is still reset. That's because we need to make sure the initial value is pulled from that same Local Storage location, like so:

```jsx
const App = () => {
  const [editor] = useState(() => withReact(createEditor()))
  // Update the initial content to be pulled from Local Storage if it exists.
  const initialValue = useMemo(
    () =>
      JSON.parse(localStorage.getItem('content')) || [
        {
          type: 'paragraph',
          children: [{ text: 'A line of text in a paragraph.' }],
        },
      ],
    []
  )

  return (
    <Slate
      editor={editor}
      initialValue={initialValue}
      onChange={value => {
        const isAstChange = editor.operations.some(
          op => 'set_selection' !== op.type
        )
        if (isAstChange) {
          // Save the value to Local Storage.
          const content = JSON.stringify(value)
          localStorage.setItem('content', content)
        }
      }}
    >
      <Editable />
    </Slate>
  )
}
```

Now you should be able to save changes across refreshes!

Success—you've got JSON in your database.

But what if you want something other than JSON? Well, you'd need to serialize your value differently. For example, if you want to save your content as plain text instead of JSON, we can write some logic to serialize and deserialize plain text values:

```jsx
// Import the `Node` helper interface from Slate.
import { Node } from 'slate'

// Define a serializing function that takes a value and returns a string.
const serialize = value => {
  return (
    value
      // Return the string content of each paragraph in the value's children.
      .map(n => Node.string(n))
      // Join them all with line breaks denoting paragraphs.
      .join('\n')
  )
}

// Define a deserializing function that takes a string and returns a value.
const deserialize = string => {
  // Return a value array of children derived by splitting the string.
  return string.split('\n').map(line => {
    return {
      children: [{ text: line }],
    }
  })
}

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))
  // Use our deserializing function to read the data from Local Storage.
  const initialValue = useMemo(
    deserialize(localStorage.getItem('content')) || '',
    []
  )

  return (
    <Slate
      editor={editor}
      initialValue={initialValue}
      onChange={value => {
        const isAstChange = editor.operations.some(
          op => 'set_selection' !== op.type
        )
        if (isAstChange) {
          // Serialize the value and save the string value to Local Storage.
          localStorage.setItem('content', serialize(value))
        }
      }}
    >
      <Editable />
    </Slate>
  )
}
```

That works! Now you're working with plain text.

You can emulate this strategy for any format you like. You can serialize to HTML, to Markdown, or even to your own custom JSON format that is tailored to your use case.

> 🤖 Note that even though you *can* serialize your content however you like, there are tradeoffs. The serialization process has a cost itself, and certain formats may be harder to work with than others. In general we recommend writing your own format only if your use case has a specific need for it. Otherwise, you're often better leaving the data in the format Slate uses.

If you want to update the editor's content in response to events from outside of Slate, you need to change the children property directly. The simplest way is to replace the value of editor.children `editor.children = newValue` and trigger a re-rendering (e.g. by calling `editor.onChange()` in the example above). Alternatively, you can use Slate's internal operations to transform the value, for example:

```javascript
  /**
  * resetNodes resets the value of the editor.
  * It should be noted that passing the `at` parameter may cause a "Cannot resolve a DOM point from Slate point" error.
  */
  resetNodes<T extends Node>(
    editor: Editor,
    options: {
      nodes?: Node | Node[],
      at?: Location
    } = {}
  ): void {
    const children = [...editor.children]

    children.forEach((node) => editor.apply({ type: 'remove_node', path: [0], node }))

    if (options.nodes) {
      const nodes = Node.isNode(options.nodes) ? [options.nodes] : options.nodes

      nodes.forEach((node, i) => editor.apply({ type: 'insert_node', path: [i], node: node }))
    }

    const point = options.at && Point.isPoint(options.at)
      ? options.at
      : Editor.end(editor, [])

    if (point) {
      Transforms.select(editor, point)
    }
  }
```


# Enabling Collaborative Editing

A common use case for text editors is collaborative editing, and the Slate editor was designed with this in mind. You can enable multiplayer editing with [Yjs](https://github.com/yjs/yjs), a network-agnostic CRDT implementation that allows you to share data among connected users. Because Yjs is network-agnostic, each project requires a [communication provider](https://github.com/yjs/yjs#providers) set up on the back end to link users together.

In this guide, we'll show you how to set up a collaborative Slate editor using a Yjs provider. We'll also be adding [slate-yjs](https://github.com/BitPhinix/slate-yjs) which allows you to add multiplayer features to Slate, such as live cursors.

Let's start with a basic editor:

```jsx
import { Slate } from 'slate-react'

const initialValue = {
  children: [{ text: '' }],
}

export const CollaborativeEditor = () => {
  return <SlateEditor />
}

const SlateEditor = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable />
    </Slate>
  )
}
```

Yjs is network-agnostic, which means each Yjs provider is set up in a slightly different way. For example [@liveblocks/yjs](https://liveblocks.io/docs/api-reference/liveblocks-yjs) is fully-hosted, whereas others such as [y-websocket](https://github.com/yjs/y-websocket) require you to host your own WebSocket server. Because of this, we'll use code snippets that work for each provider, without going into too much detail about setting up the provider itself.

This is how to connect to a collaborative Yjs document, ready to be used in your Slate editor.

```jsx
import { useEffect, useMemo, useState } from 'react'
import { createEditor, Editor, Transforms } from 'slate'
import { Editable, Slate, withReact } from 'slate-react'
import * as Y from 'yjs'

const initialValue = {
  children: [{ text: '' }],
}

export const CollaborativeEditor = () => {
  const [connected, setConnected] = useState(false)
  const [sharedType, setSharedType] = useState()
  const [provider, setProvider] = useState()

  // Set up your Yjs provider and document
  useEffect(() => {
    const yDoc = new Y.Doc()
    const sharedDoc = yDoc.get('slate', Y.XmlText)

    // Set up your Yjs provider. This line of code is different for each provider.
    const yProvider = new YjsProvider(/* ... */)

    yProvider.on('sync', setConnected)
    setSharedType(sharedDoc)
    setProvider(yProvider)

    return () => {
      yDoc?.destroy()
      yProvider?.off('sync', setConnected)
      yProvider?.destroy()
    }
  }, [])

  if (!connected || !sharedType || !provider) {
    return <div>Loading…</div>
  }

  return <SlateEditor />
}

const SlateEditor = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable />
    </Slate>
  )
}
```

After setting up your Yjs document like this, you can then link it your editor by passing down `sharedType`, which contains the multiplayer text, and by using functions from `slate-yjs`. We're also passing down `provider` which will be helpful later.

```jsx
import { useEffect, useMemo, useState } from 'react'
import { createEditor, Editor, Transforms } from 'slate'
import { Editable, Slate, withReact } from 'slate-react'
import { withYjs, YjsEditor } from '@slate-yjs/core'
import * as Y from 'yjs'

const initialValue = {
  children: [{ text: '' }],
}

export const CollaborativeEditor = () => {
  const [connected, setConnected] = useState(false)
  const [sharedType, setSharedType] = useState()
  const [provider, setProvider] = useState()

  // Connect to your Yjs provider and document
  useEffect(() => {
    const yDoc = new Y.Doc()
    const sharedDoc = yDoc.get('slate', Y.XmlText)

    // Set up your Yjs provider. This line of code is different for each provider.
    const yProvider = new YjsProvider(/* ... */)

    yProvider.on('sync', setConnected)
    setSharedType(sharedDoc)
    setProvider(yProvider)

    return () => {
      yDoc?.destroy()
      yProvider?.off('sync', setConnected)
      yProvider?.destroy()
    }
  }, [])

  if (!connected || !sharedType || !provider) {
    return <div>Loading…</div>
  }

  return <SlateEditor sharedType={sharedType} provider={provider} />
}

const SlateEditor = ({ sharedType, provider }) => {
  const editor = useMemo(() => {
    const e = withReact(withYjs(createEditor(), sharedType))

    // Ensure editor always has at least 1 valid child
    const { normalizeNode } = e
    e.normalizeNode = (entry, options) => {
      const [node] = entry

      if (!Editor.isEditor(node) || node.children.length > 0) {
        return normalizeNode(entry, options)
      }

      Transforms.insertNodes(editor, initialValue, { at: [0] })
    }

    return e
  }, [])

  useEffect(() => {
    YjsEditor.connect(editor)
    return () => YjsEditor.disconnect(editor)
  }, [editor])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable />
    </Slate>
  )
}
```

That's all you need to attach Yjs to Slate!

Let's look at a real-world example of setting up Yjs—here's a code snippet for setting up a [Liveblocks provider](https://liveblocks.io/docs/get-started/yjs-slate-react). Liveblocks uses the concept of rooms, spaces where users can collaborative. To use a Liveblocks provider, you join a multiplayer room with `RoomProvider`, then pass the room to `new LiveblocksProvider`, along with the Yjs document.

```jsx
import LiveblocksProvider from '@liveblocks/yjs'
import { RoomProvider, useRoom } from '../liveblocks.config'

// Join a Liveblocks room and show the editor after connecting
export const App = () => {
  return (
    <RoomProvider id="my-room-name" initialPresence={{}}>
      <ClientSideSuspense fallback={<div>Loading…</div>}>
        {() => <CollaborativeEditor />}
      </ClientSideSuspense>
    </RoomProvider>
  )
}

export const CollaborativeEditor = () => {
  const room = useRoom()
  const [connected, setConnected] = useState(false)
  const [sharedType, setSharedType] = useState()
  const [provider, setProvider] = useState()

  // Connect to your Yjs provider and document
  useEffect(() => {
    const yDoc = new Y.Doc()
    const sharedDoc = yDoc.get('slate', Y.XmlText)

    // Set up your Liveblocks provider with the current room and document
    const yProvider = new LiveblocksProvider(room, yDoc)

    yProvider.on('sync', setConnected)
    setSharedType(sharedDoc)
    setProvider(yProvider)

    return () => {
      yDoc?.destroy()
      yProvider?.off('sync', setConnected)
      yProvider?.destroy()
    }
  }, [room])

  if (!connected || !sharedType || !provider) {
    return <div>Loading…</div>
  }

  return <SlateEditor sharedType={sharedType} provider={provider} />
}

const SlateEditor = ({ sharedType, provider }) => {
  // ...
}
```

Unlike other providers, Liveblocks hosts your Yjs back end for you, which means you don't need to run your own server to get this working. For more information on setting up Liveblocks providers, make sure to read their [Slate getting started](https://liveblocks.io/docs/get-started/yjs-slate-react) guide.

> Note that Liveblocks is independent of the Slate project, and isn't required for collaboration, but it may be convenient depending on your needs. [Other providers](https://github.com/yjs/yjs#providers) are available should you wish to set up and host a Yjs back end yourself.

After setting up Yjs, it's possible to add multiplayer cursors to your app. You can do this with hooks supplied by [slate-yjs](https://docs.slatejs.org/walkthroughs/07-enabling-collaborative-editing), which allow you to find the cursor positions of other users. Here's an example of setting up a cursor component.

```jsx
import {
  CursorOverlayData,
  useRemoteCursorOverlayPositions,
} from '@slate-yjs/react'
import { useRef } from 'react'

export function Cursors({ children }) {
  const containerRef = useRef(null)
  const [cursors] = useRemoteCursorOverlayPositions({ containerRef })

  return (
    <div className="cursors" ref={containerRef}>
      {children}
      {cursors.map(cursor => (
        <Selection key={cursor.clientId} {...cursor} />
      ))}
    </div>
  )
}

function Selection({ data, selectionRects, caretPosition }) {
  if (!data) {
    return null
  }

  const selectionStyle = {
    backgroundColor: data.color,
  }

  return (
    <>
      {selectionRects.map((position, i) => (
        <div
          style={{ ...selectionStyle, ...position }}
          className="selection"
          key={i}
        />
      ))}
      {caretPosition && <Caret caretPosition={caretPosition} data={data} />}
    </>
  )
}

function Caret({ caretPosition, data }) {
  const caretStyle = {
    ...caretPosition,
    background: data?.color,
  }

  const labelStyle = {
    transform: 'translateY(-100%)',
    background: data?.color,
  }

  return (
    <div style={caretStyle} className="caretMarker">
      <div className="caret" style={labelStyle}>
        {data?.name}
      </div>
    </div>
  )
}
```

With some matching styles to set up the positioning:

```css
.cursors {
  position: relative;
}

.caretMarker {
  position: absolute;
  width: 2px;
}

.caret {
  position: absolute;
  font-size: 14px;
  color: #fff;
  white-space: nowrap;
  top: 0;
  border-radius: 6px;
  border-bottom-left-radius: 0;
  padding: 2px 6px;
  pointer-events: none;
}

.selection {
  position: absolute;
  pointer-events: none;
  opacity: 0.2;
}
```

You can then import this into your `SlateEditor` component. Notice that we're using `withCursors` from `slate-yjs`, adding `provider.awareness` and the current user's name to it. We're then wrapping `<Editable>` in the new `<Cursors>` component we've just created.

```jsx
import { useEffect, useMemo, useState } from 'react'
import { createEditor, Editor, Transforms } from 'slate'
import { Editable, Slate, withReact } from 'slate-react'
import { withCursors, withYjs, YjsEditor } from '@slate-yjs/core'
import { Cursors } from './Cursors'
import * as Y from 'yjs'

export const CollaborativeEditor = () => {
  // ...
}

const SlateEditor = ({ sharedType, provider }) => {
  const editor = useMemo(() => {
    const e = withReact(
      withCursors(withYjs(createEditor(), sharedType), provider.awareness, {
        // The current user's name and color
        data: {
          name: 'Chris',
          color: '#00ff00',
        },
      })
    )

    // Ensure editor always has at least 1 valid child
    const { normalizeNode } = e
    e.normalizeNode = (entry, options) => {
      const [node] = entry

      if (!Editor.isEditor(node) || node.children.length > 0) {
        return normalizeNode(entry, options)
      }

      Transforms.insertNodes(editor, initialValue, { at: [0] })
    }

    return e
  }, [])

  useEffect(() => {
    YjsEditor.connect(editor)
    return () => YjsEditor.disconnect(editor)
  }, [editor])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Cursors>
        <Editable />
      </Cursors>
    </Slate>
  )
}
```

You should now be seeing multiplayer cursors! To learn more, make sure to read the [slate-yjs documentation](https://docs.slate-yjs.dev/).


# Using the Bundled Source

For most folks, you'll want to install Slate via `npm`, in which case you can follow the regular [Installing Slate](https://docs.slatejs.org/walkthroughs/01-installing-slate) guide.

But, if you'd rather install Slate by simply adding a `<script>` tag to your application, this guide will help you. To make the "bundled" use case simpler, each version of Slate ships with a bundled source file called `slate.js`.

To get a copy of `slate.js`, download the version of Slate you want from npm:

```
npm install slate@latest
```

And then look in the `node_modules` folder for the bundled `slate.js` file:

```
node_modules/
  slate/
    dist/
      slate.js
      slate.min.js
```

A minified version called `slate.min.js` is also included for convenience.

Before you can add `slate.js` to your page, you need to bring your own copy of `react`, `react-dom` and `react-dom-server`, like so:

```markup
<script src="./vendor/react.js"></script>
<script src="./vendor/react-dom.js"></script>
<script src="./vendor/react-dom-server.js"></script>
```

This ensures that Slate isn't bundling its own copy of React, which would greatly increase the file size of your application.

Then you can add `slate.js` after those includes:

```markup
<script src="./vendor/slate.js"></script>
```

To make things easier, for quick prototyping, you can also use the [`unpkg.com`](https://unpkg.com/#/) delivery network that makes working with bundled npm modules easier. In that case, your includes would look like:

```markup
<script src="https://unpkg.com/react/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/react-dom/umd/react-dom-server.browser.production.min.js"></script>
<script src="https://unpkg.com/slate/dist/slate.js"></script>
<script src="https://unpkg.com/slate-react/dist/slate-react.js"></script>
```

That's it, you're ready to go!


# Improving Performance

When building a text editor, it's important for user interactions to take place without any noticeable delay. For small and moderately sized documents (less than 1000 blocks), you probably don't need to worry about performance. If your editor needs to support very large documents (10,000+ or 100,000+ blocks), follow this guide to ensure the editor stays responsive.

The [Huge Document](https://slatejs.org/examples/huge-document) example contains an interactive playground where you can explore the effect of various factors on the performance of a very simple Slate editor.

The type of performance this guide is mostly concerned with is the **Interaction to Next Paint** (INP) while typing. If the INP is below roughly 100ms, typing should feel very responsive. The editor will still be usable when the INP duration is longer, but it will feel increasingly sluggish and unpleasant to use.

Other performance metrics to be aware of (but which are not currently covered in this guide) are **time to first paint** and the INP when performing non-typing operations (such as selecting all content or pasting).

INP is easiest to measure in Chrome using the [Performance panel](https://developer.chrome.com/docs/devtools/performance) in DevTools, but there are ways to determine it in Firefox and Safari too. For example, in Firefox, you can use the [Firefox Profiler](https://profiler.firefox.com/) to see a timeline of events.

![Screenshot of the Stack Chart tab of the Firefox Profiler, annotated to show a breakdown of time spent in core Slate, React, and painting the DOM.](https://807786356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Kuki-R9UbW5PP_Bubk1-2910905616%2Fuploads%2Fgit-blob-9dcbc031e966334f921c487d487681c8b7ac2ad9%2Ffirefox-inp.png?alt=media)

There are three main areas that can be optimized:

* [Slate core](#optimizing-slate-core)
* [React](#optimizing-react)
* [DOM painting](#optimizing-dom-painting)

Before you start optimizing, make sure you know which of these areas is most responsible for any slowness you're seeing. The best way of doing this is to use your browser's profiler (see the example for Firefox above), but you can also use these heuristics to guess which area is most at fault:

1. If performance is much better in Firefox than in Chrome or Safari, DOM painting is usually the problem (tested May 2025).
2. If disabling any custom normalization logic improves performance, the normalization logic is the problem.
3. Otherwise, it's likely to be React.

## Optimizing Slate Core

Usually, if the core Slate logic is causing a noticeable delay, it's because of [normalizing](https://docs.slatejs.org/concepts/11-normalizing). If custom normalization logic is causing slowness in your app, consider whether the logic can be made more efficient.

Understand that `normalizeNode` is called once for every modified node and every ancestor of a modified node. As a result, `normalizeNode` is called for the editor node whenever anything changes in the editor, but for other nodes it is called much less frequently.

Make sure you only normalize the node passed into `normalizeNode` and (occasionally) its direct children, not its children's descendants. Normalization logic should only be applied directly to the editor node when absolutely necessary, such when enforcing that the last block in the document is a paragraph.

## Optimizing React

### Reduce Renders

The `renderElement` prop and any React component it returns will re-render every time the element or any of its descendants changes. This is unavoidable. However, sometimes custom logic can cause React components to re-render more often than this, which can have a detrimental effect on performance.

Ensure that function props such as `renderElement`, `renderLeaf`, `renderChunk` and `decorate` do not change on every render. Either they should be defined at the top level of the file (not inside a component or hook), or they should be wrapped inside a `useCallback` and all dependencies should be properly memoized.

If unmodified elements are being re-rendered, check to see if they are subscribing to any contexts or hooks that are causing unnecessary re-renders. You can also apply these techniques to any toolbars or other non-element React components that may be re-rendering in response to changes in the editor.

The `useSlate`, `useSlateSelection`, `useSlateSelector`, `useSelected` and `useFocused` hooks cause React components to re-render in various circumstances. If you're using `useSlate`, consider if you can use `useSlateStatic` (which does not cause re-renders) instead. If you're using `useSlateSelection`, consider using `editor.selection`. If you only care about some value derived from the editor (such as whether a given mark is active), use `useSlateSelector` to only re-render when this value changes.

If your components depend on custom React contexts containing non-primitive values (such as objects or arrays), ensure that these values are properly memoized so that components only re-render when these values change. In some circumstances, you may instead want to consider passing a ref object or an unchanging getter function to retrieve the latest value.

```tsx
// Provider
const myDataRef = useRef(myData)
myDataRef.current = myData
return <MyContext.Provider value={myDataRef}>{children}</MyContext.Provider>

// Consumer
// Does not re-render when `myData` changes
const myDataRef = useContext(MyContext)

const onClick = () => {
  console.log(myDataRef.current)
}
```

### Enable Chunking (experimental)

Chunking is an internal optimization used by `slate-react`, and must be explicitly enabled. It works by splitting a node's children into nested "chunks", each of which is a separately memoized React component. This reduces the amount of work React needs to do when processing changes to the JSX, resulting in a 10x speed-up in ideal circumstances.

To enable chunking, you need to implement `editor.getChunkSize(node: Ancestor) => number | null`, which controls the number of nodes per lowest-level chunk for a given parent node. In most circumstances, setting the chunk size to 1000 for the editor and `null` for all other ancestors works well.

```typescript
editor.getChunkSize = node => (Editor.isEditor(node) ? 1000 : null)
```

Note that chunking can only be enabled for nodes whose children are all block elements. Attempting to enable chunking for leaf blocks (blocks containing inline nodes) will have no effect.

By default, chunking has no effect on the DOM. You can override this by passing a `renderChunk` prop to `Editable`.

## Optimizing DOM Painting

In Chrome and Safari, painting large numbers of DOM nodes can be extremely slow, over 100x slower than the core Slate logic and React rendering combined in some cases. In Firefox, the impact of painting on performance is much less significant.

The best way of speeding up painting large documents is to use the [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/content-visibility) CSS property. When set to `auto`, this property instructs browsers not to paint content that is off-screen. However, it also comes with a performance overhead proportional to the number of DOM nodes it is applied to, which is especially bad in Safari. When rendering large documents in Safari, applying `content-visibility: auto` to each Slate element individually is often slower than not using it at all.

The recommended solution is to enable [chunking](#enable-chunking-experimental) and apply `content-visibility: auto` on each lowest-level chunk by passing a `renderChunk` prop to `Editable`.

```tsx
const renderChunk = ({ attributes, lowest, children }: RenderChunkProps) => (
  <div
    {...attributes}
    style={lowest ? { contentVisibility: 'auto' } : undefined}
  >
    {children}
  </div>
)
```

Note that this will modify the DOM structure of your editor, which may have adverse effects on its appearance. During development, it is recommended to set the chunk size to a small number such as 3 so that styling issues caused by nested chunks are easier to detect.

If you previously had a CSS rule such as this to apply spacing between top-level blocks:

```css
[data-slate-editor] > * + * {
  margin-top: 1em;
}
```

It should be changed to this:

```css
[data-slate-editor] > * + *,
[data-slate-chunk] > * + * {
  margin-top: 1em;
}
```

Also bear in mind this warning about `content-visibility: auto` from MDN:

> Since styles for off-screen content are not rendered, elements intentionally hidden with `display: none` or `visibility: hidden` *will still appear in the accessibility tree*. If you don't want an element to appear in the accessibility tree, use `aria-hidden="true"`.


# Interfaces

Slate works with pure JSON objects. All it requires is that those JSON objects conform to certain interfaces. For example, a text node in Slate must obey the `Text` interface:

```typescript
interface Text {
  text: string
}
```

Which means it must have a `text` property with a string of content.

But **any** other custom properties are also allowed, and completely up to you. This lets you tailor your data to your specific domain and use case, adding whatever formatting logic you'd like, without Slate getting in the way.

This interface-based approach separates Slate from most other rich text editors which require you to work with their hand-rolled "model" classes and makes it much easier to reason about. It also means that it avoids startup time penalties related to "initializing" the data model.

## Custom Properties

To take another example, the `Element` node interface in Slate is:

```typescript
interface Element {
  children: Node[]
}
```

This is a very permissive interface. All it requires is that the `children` property gets defined containing the element's child nodes.

But you can extend elements (or any other interface) with your custom properties that are specific to your domain. For example, you might have "paragraph" and "link" elements:

```javascript
const paragraph = {
  type: 'paragraph',
  children: [...],
}

const link = {
  type: 'link',
  url: 'https://example.com',
  children: [...]
}
```

The `type` and `url` properties are your custom API. Slate sees that they exist, but doesn't use them. However, when Slate renders a link element, you'll receive an object with the custom properties attached so that you can render it as:

```jsx
<a href={element.url}>{element.children}</a>
```

When getting started with Slate, it's important to understand all of the interfaces it defines. There are a handful of interfaces that are discussed in each of the guides.

## Helper Functions

In addition to the typing information, each interface in Slate also exposes a series of helper functions that make them easier to work with.

For example, when working with nodes:

```javascript
import { Node } from 'slate'

// Get the string content of an element node.
const string = Node.string(element)

// Get the node at a specific path inside a root node.
const descendant = Node.get(value, path)
```

Or, when working with ranges:

```javascript
import { Range } from 'slate'

// Get the start and end points of a range in order.
const [start, end] = Range.edges(range)

// Check if a range is collapsed to a single point.
if (Range.isCollapsed(range)) {
  // ...
}
```

There are many helper functions available for all common use cases when working with different interfaces. When getting started it helps to read through all of them so you can often simplify complex logic into just a handful of lines of code.

## Custom Helpers

In addition to the built-in helper functions, you might want to define your custom helper functions and expose them on your custom namespaces.

For example, if your editor supports images, you might want a helper that determines if an element is an image element:

```javascript
const isImageElement = element => {
  return element.type === 'image' && typeof element.url === 'string'
}
```

You can define these as one-off functions easily. But you might also bundle them up into namespaces, just like the core interfaces do, and use them instead.

For example:

```javascript
import { Element } from 'slate'

// You can use `MyElement` everywhere to have access to your extensions.
export const MyElement = {
  ...Element,
  isImageElement,
  isParagraphElement,
  isQuoteElement,
}
```

This makes it easy to reuse domain-specific logic alongside the built-in Slate helpers.


# Nodes

The most important types are the `Node` objects:

* A root-level `Editor` node that contains the entire document's content.
* Container `Element` nodes that have semantic meaning in your domain.
* And leaf-level `Text` nodes which contain the document's text.

These three interfaces are combined to form a tree—just like the DOM. For example, here's a simple plaintext value:

```javascript
const editor = {
  children: [
    {
      type: 'paragraph',
      children: [
        {
          text: 'A line of text!',
        },
      ],
    },
  ],
  // ...the editor has other properties too.
}
```

Mirroring the DOM as much as possible is one of Slate's principles. People use the DOM to represent documents with rich text-like structures all the time. Mirroring the DOM helps make the library familiar for new users, and it lets us reuse battle-tested patterns without having to reinvent them ourselves.

> 🤖 The following content on Mozilla's Developer Network may help you learn more about the corresponding DOM concepts:
>
> * [Document](https://developer.mozilla.org/en-US/docs/Web/API/Document)
> * [Block Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements)
> * [Inline elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements)
> * [Text elements](https://developer.mozilla.org/en-US/docs/Web/API/Text)

A Slate document is a nested and recursive structure. In a document, elements can have children nodes—all of which may have children nodes without limit. The nested and recursive structure enables you to model simple behaviors such as user mentions and hashtags or complex behaviors such as tables and figures with captions.

## `Editor`

The top-level node in a Slate document is the `Editor` itself. It encapsulates all of the rich text "content" of the document. Its interface is:

```typescript
interface Editor {
  children: Node[]
  ...
}
```

We'll cover its functionality later, but the important part as far as nodes are concerned is its `children` property which contains a tree of `Node` objects.

## `Element`

Elements make up the middle layers of a rich text document. They are the nodes that are custom to your domain. Their interface is:

```typescript
interface Element {
  children: Node[]
}
```

You can define custom elements for any type of content you want. For example, you might have paragraphs and quotes in your data model which are differentiated by a `type` property:

```javascript
const paragraph = {
  type: 'paragraph',
  children: [...],
}

const quote = {
  type: 'quote',
  children: [...],
}
```

It's important to note that you can use *any* custom properties you want. The `type` property in that example isn't something Slate knows or cares about. If you were defining your own "link" nodes, you might have a `url` property:

```javascript
const link = {
  type: 'link',
  url: 'https://example.com',
  children: [...],
}
```

Or maybe you want to give all of your nodes an ID property:

```javascript
const paragraph = {
  id: 1,
  type: 'paragraph',
  children: [...],
}
```

All that matters is that elements always have a `children` property.

## Blocks vs. Inlines

Depending on your use case, you might want to define another behavior for `Element` nodes which determines their editing "flow".

All elements default to being "block" elements. They each appear separated by vertical space, and they never run into each other.

But in certain cases, like for links, you might want to make them "inline" flowing elements instead. That way they live at the same level as text nodes, and flow.

> 🤖 This is a concept borrowed from the DOM's behavior, see [Block Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) and [Inline Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements).

You can define which nodes are treated as inline nodes by overriding the `editor.isInline` function. (By default it always returns `false`.) Note that inline nodes cannot be the first or last child of a parent block, nor can they be next to another inline node in the `children` array. Slate will automatically space these with `{ text: '' }` children by default with [`normalizeNode`](https://docs.slatejs.org/11-normalizing#built-in-constraints).

Elements can either contain block elements or inline elements intermingled with text nodes as children. But elements **cannot** contain some children that are blocks and some that are inlined.

## Voids

Similar to blocks and inlines, there is another element-specific behavior you can define depending on your use case: their "void"-ness.

Elements default to being non-void, meaning that their children are fully editable as text. But in some cases, like for images, you want to ensure that Slate doesn't treat their content as editable text, but instead as a black box.

> 🤖 This is a concept borrowed from the HTML spec, see [Void Elements](https://www.w3.org/TR/2011/WD-html-markup-20110405/syntax.html#void-element).

You can define which elements are treated as void by overriding the `editor.isVoid` function. (By default it always returns `false`.) See [Rendering Void Elements](https://docs.slatejs.org/api/nodes/element#rendering-void-elements) for implementation details.

## `Text`

Text nodes are the lowest-level nodes in the tree, containing the text content of the document, along with any formatting. Their interface is:

```typescript
interface Text {
  text: string
}
```

For example, a string of bold text:

```javascript
const text = {
  text: 'A string of bold text',
  bold: true,
}
```

Text nodes too can contain any custom properties you want, and that's how you implement custom formatting like **bold**, *italic*, `code`, etc. These custom properties are sometimes called [marks](https://docs.slatejs.org/api/nodes/editor#mark-methods).


# Locations

Locations are how you refer to specific places in the document when inserting, deleting, or doing anything else with a Slate editor. There are a few different kinds of location interfaces, each for different use cases.

## `Path`

Paths are the lowest-level way to refer to a location. Each path is a simple array of numbers that refers to a node in the document tree by its indexes in each of its ancestor nodes down the tree:

```typescript
type Path = number[]
```

For example, in this document:

```javascript
const editor = {
  children: [
    {
      type: 'paragraph',
      children: [
        {
          text: 'A line of text!',
        },
      ],
    },
  ],
}
```

The leaf text node would have a path of: `[0, 0]`.

The Editor itself has a path of `[]`. For example, to select the whole contents of the editor, call `Transforms.select(editor, [])`

## `Point`

Points are slightly more specific than paths, and contain an `offset` into a specific text node. Their interface is:

```typescript
interface Point {
  path: Path
  offset: number
}
```

For example, with that same document, if you wanted to refer to the very first place you could put your cursor it would be:

```javascript
const start = {
  path: [0, 0],
  offset: 0,
}
```

Or, if you wanted to refer to the end of the sentence:

```javascript
const end = {
  path: [0, 0],
  offset: 15,
}
```

It can be helpful to think of points as being "cursors" (or "carets") of a selection.

> 🤖 Points *always* refer to text nodes! Since they are the only ones with strings that can have cursors.

## `Range`

Ranges are a way to refer not just to a single point in the document, but to a wider span of content between two points. (An example of a range is when you make a selection.) Their interface is:

```typescript
interface Range {
  anchor: Point
  focus: Point
}
```

> 🤖 The terms "anchor" and "focus" are borrowed from the DOM, see [Anchor](https://developer.mozilla.org/en-US/docs/Web/API/Selection/anchorNode) and [Focus](https://developer.mozilla.org/en-US/docs/Web/API/Selection/focusNode).

An anchor and focus are established by a user interaction. The anchor point isn't always *before* the focus point in the document. Just like in the DOM, the ordering of an anchor and selection point depend on whether the range is backwards or forwards.

Here's how Mozilla Developer Network explains it:

> A user may make a selection from left to right (in document order) or right to left (reverse of document order). The anchor is where the user began the selection and the focus is where the user ends the selection. If you make a selection with a desktop mouse, the anchor is placed where you pressed the mouse button and the focus is placed where you released the mouse button. Anchor and focus should not be confused with the start and end positions of a selection, since anchor can be placed before the focus or vice versa, depending on the direction you made your selection. — [`Selection`, MDN](https://developer.mozilla.org/en-US/docs/Web/API/Selection)

One important distinction is that the anchor and focus points of ranges **always reference the leaf-level text nodes** in a document and never reference elements. This behavior is different than the DOM, but it simplifies working with ranges as there are fewer edge cases for you to handle.

> 🤖 For more info, check out the [Range API reference](https://docs.slatejs.org/api/locations/range).

## Selection

Ranges are used in many places in Slate's API when you need to refer to a span of content between two points. One of the most common, though, is the user's current "selection".

The selection is a special range that is a property of the top-level `Editor`. For example, say someone has the whole sentence currently selected:

```javascript
const editor = {
  selection: {
    anchor: { path: [0, 0], offset: 0 },
    focus: { path: [0, 0], offset: 15 },
  },
  children: [
    {
      type: 'paragraph',
      children: [
        {
          text: 'A line of text!',
        },
      ],
    },
  ],
}
```

> 🤖 The selection concept is also borrowed from the DOM, see [`Selection`, MDN](https://developer.mozilla.org/en-US/docs/Web/API/Selection), although in a greatly-simplified form because Slate doesn't allow for multiple ranges inside a single selection, which makes things a lot easier to work with.

There isn't a special `Selection` interface. It's just an object that happens to respect the more general-purpose `Range` interface instead.

For example, to find the lowest block that contains all of the current selection:

```javascript
function getCommonBlock(editor) {
  const range = Editor.unhangRange(editor, editor.selection, { voids: true })

  let [common, path] = SlateNode.common(
    editor,
    range.anchor.path,
    range.focus.path
  )

  if (Editor.isBlock(editor, common) || Editor.isEditor(common)) {
    return [common, path]
  } else {
    return Editor.above(editor, {
      at: path,
      match: n => Editor.isBlock(editor, n) || Editor.isEditor(n),
    })
  }
}
```


# Transforms

Slate's data structure is immutable, so you can't modify or delete nodes directly. Instead, Slate comes with a collection of "transform" functions that let you change your editor's value.

Slate's transform functions are designed to be very flexible, to make it possible to represent all kinds of changes you might need to make to your editor. However, that flexibility can be hard to understand at first.

Typically, you'll apply a single operation to zero or more Nodes. For example, here's how you flatten the syntax tree, by applying `unwrapNodes` to every parent of block Elements:

```javascript
Transforms.unwrapNodes(editor, {
  at: [], // Path of Editor
  match: node =>
    !Editor.isEditor(node) &&
    node.children?.every(child => Editor.isBlock(editor, child)),
  mode: 'all', // also the Editor's children
})
```

Non-standard operations (or debugging/tracing which Nodes will be affected by a set of NodeOptions) may require using `Editor.nodes` to create a JavaScript Iterator of NodeEntries and a for..of loop to act. For example, to replace all image elements with their alt text:

```javascript
const imageElements = Editor.nodes(editor, {
  at: [], // Path of Editor
  match: (node, path) => 'image' === node.type,
  // mode defaults to "all", so this also searches the Editor's children
})
for (const nodeEntry of imageElements) {
  const altText =
    nodeEntry[0].alt ||
    nodeEntry[0].title ||
    /\/([^/]+)$/.exec(nodeEntry[0].url)?.[1] ||
    '☹︎'
  Transforms.select(editor, nodeEntry[1])
  Editor.insertFragment(editor, [{ text: altText }])
}
```

> 🤖 Check out the [Transforms](https://docs.slatejs.org/api/transforms) reference for a full list of Slate's transforms.

## Selection Transforms

Selection-related transforms are some of the simpler ones. For example, here's how you set the selection to a new range:

```javascript
Transforms.select(editor, {
  anchor: { path: [0, 0], offset: 0 },
  focus: { path: [1, 0], offset: 2 },
})
```

But they can be more complex too.

For example, it's common to need to move a cursor forwards or backwards by varying distances—by character, by word, by line. Here's how you'd move the cursor backwards by three words:

```javascript
Transforms.move(editor, {
  distance: 3,
  unit: 'word',
  reverse: true,
})
```

> 🤖 For more info, check out the [Selection Transforms API Reference](https://docs.slatejs.org/api/transforms#selection-transforms)

## Text Transforms

Text transforms act on the text content of the editor. For example, here's how you'd insert a string of text as a specific point:

```javascript
Transforms.insertText(editor, 'some words', {
  at: { path: [0, 0], offset: 3 },
})
```

Or you could delete all of the content in an entire range from the editor:

```javascript
Transforms.delete(editor, {
  at: {
    anchor: { path: [0, 0], offset: 0 },
    focus: { path: [1, 0], offset: 2 },
  },
})
```

> 🤖 For more info, check out the [Text Transforms API Reference](https://docs.slatejs.org/api/transforms#text-transforms)

## Node Transforms

Node transforms act on the individual element and text nodes that make up the editor's value. For example you could insert a new text node at a specific path:

```javascript
Transforms.insertNodes(
  editor,
  {
    text: 'A new string of text.',
  },
  {
    at: [0, 1],
  }
)
```

Or you could move nodes from one path to another:

```javascript
Transforms.moveNodes(editor, {
  at: [0, 0],
  to: [0, 1],
})
```

> 🤖 For more info, check out the [Node Transforms API Reference](https://docs.slatejs.org/api/transforms#node-transforms)

## The `at` Option

Many transforms act on a specific location in the document. By default, they will use the user's current selection. But this can be overridden with the `at` option.

For example when inserting text, this would insert the string at the user's current cursor:

```javascript
Transforms.insertText(editor, 'some words')
```

Whereas this would insert it at a specific point:

```javascript
Transforms.insertText(editor, 'some words', {
  at: { path: [0, 0], offset: 3 },
})
```

The `at` option is very versatile, and can be used to implement more complex transforms very easily. Since it is a `Location` it can always be either a `Path`, `Point`, or `Range`. And each of those types of locations will result in slightly different transformations.

For example, in the case of inserting text, if you specify a `Range` location, the range will first be deleted, collapsing to a single point where your text is then inserted.

So to replace a range of text with a new string you can do:

```javascript
Transforms.insertText(editor, 'some words', {
  at: {
    anchor: { path: [0, 0], offset: 0 },
    focus: { path: [0, 0], offset: 3 },
  },
})
```

Or, if you specify a `Path` location, it will expand to a range that covers the entire node at that path. Then, using the range-based behavior it will delete all of the content of the node, and replace it with your text.

So to replace the text of an entire node with a new string you can do:

```javascript
Transforms.insertText(editor, 'some words', {
  at: [0, 0],
})
```

These location-based behaviors work for all the transforms that take an `at` option. It can be hard to wrap your head around at first, but it makes the API very powerful and capable of expressing many subtly different transforms.

## The `match` Option

Many of the node-based transforms take a `match` function option, which restricts the transform to only apply to nodes for which the function returns `true`. When combined with `at`, `match` can also be very powerful.

For example, consider a basic transform that moves a node from one path to another:

```javascript
Transforms.moveNodes(editor, {
  at: [2],
  to: [5],
})
```

Although it looks like it simply takes a path and moves it to another place. Under the hood two things are happening…

First, the `at` option is expanded to be a range representing all of the content inside the node at `[2]`. Which might look something like:

```javascript
at: {
  anchor: { path: [2, 0], offset: 0 },
  focus: { path: [2, 2], offset: 19 }
}
```

Second, the `match` option is defaulted to a function that only matches the specific path, in this case `[2]`:

```javascript
match: (node, path) => Path.equals(path, [2])
```

Then Slate iterates over the range and moves any nodes that pass the matcher function to the new location. In this case, since `match` is defaulted to only match the exact `[2]` path, that node is moved.

But what if you wanted to move the children of the node at `[2]` instead?

You might consider looping over the node's children and moving them one at a time, but this gets very complex to manage because as you move the nodes the paths you're referring to become outdated.

Instead, you can take advantage of the `at` and `match` options to match all of the children:

```javascript
Transforms.moveNodes(editor, {
  // This will again be expanded to a range of the entire node at `[2]`.
  at: [2],
  // Matches nodes with a longer path, which are the children.
  match: (node, path) => path.length === 2,
  to: [5],
})
```

Here we're using the same `at` path (which is expanded to a range), but instead of letting it match just that path by default, we're supplying our own `match` function which happens to match only the children of the node.

Using `match` can make representing complex logic a lot simpler.

For example, consider wanting to add a bold mark to any text nodes that aren't already italic:

```javascript
Transforms.setNodes(
  editor,
  { bold: true },
  {
    // This path references the editor, and is expanded to a range that
    // will encompass all the content of the editor.
    at: [],
    // This only matches text nodes that are not already italic.
    match: (node, path) => Text.isText(node) && node.italic !== true,
  }
)
```

When performing transforms, if you're ever looping over nodes and transforming them one at a time, consider seeing if `match` can solve your use case, and offload the complexity of managing loops to Slate instead. The `match` function can examine the children of a node, in `node.children`, or use `Node.parent` to examine its parent.

## Transforms and Normalization

Sequences of Transforms may need to be wrapped in [`Editor.withoutNormalizing`](https://docs.slatejs.org/api/nodes/editor#editorwithoutnormalizingeditor-editor-fn---void--void) if the node tree should *not* be normalized between Transforms. See [Normalization - Implications for Other Code](https://docs.slatejs.org/11-normalizing#implications-for-other-code);


# Operations

Operations are the granular, low-level actions that occur while invoking transforms. A single transform could result in many low-level operations being applied to the editor.

Slate's core defines all of the possible operations that can occur on a richtext document. For example:

```javascript
editor.apply({
  type: 'insert_text',
  path: [0, 0],
  offset: 15,
  text: 'A new string of text to be inserted.',
})

editor.apply({
  type: 'remove_node',
  path: [0, 0],
  node: {
    text: 'A line of text!',
  },
})

editor.apply({
  type: 'set_selection',
  properties: {
    anchor: { path: [0, 0], offset: 0 },
  },
  newProperties: {
    anchor: { path: [0, 0], offset: 15 },
  },
})
```

Under the covers Slate converts complex transforms into the low-level operations and applies them to the editor automatically. So you rarely have to think about operations unless you're implementing collaborative editing.

> 🤖 Slate's editing behaviors being defined as operations is what makes things like collaborative editing possible, because each change is easily define-able, apply-able, compose-able and even undo-able!


# Commands

While editing richtext content, your users will be doing things like inserting text, deleting text, splitting paragraphs, adding formatting, etc. Under the cover these edits are expressed using transforms and operations. But at a high level we talk about them as "commands".

Commands are the high-level actions that represent a specific intent of the user. They are represented as helper functions on the `Editor` interface. A handful of helpers are included in core for common richtext behaviors, but you are encouraged to write your own that model your specific domain.

For example, here are some of the built-in commands:

```javascript
Editor.insertText(editor, 'A new string of text to be inserted.')

Editor.deleteBackward(editor, { unit: 'word' })

Editor.insertBreak(editor)
```

But you can (and will!) also define your own custom commands that model your domain. For example, you might want to define a `formatQuote` command, or an `insertImage` command, or a `toggleBold` command depending on what types of content you allow.

Commands always describe an action to be taken as if the **user** was performing the action. For that reason, they never need to define a location to perform the command, because they always act on the user's current selection.

> 🤖 The concept of commands is loosely based on the DOM's built-in [`execCommand`](https://developer.mozilla.org/en-US/docs/Web/API/Document/execCommand) APIs. However Slate defines its own simpler (and extendable!) version of the API, because the DOM's version is too opinionated and inconsistent.

Under the covers, Slate takes care of converting each command into a set of low-level "operations" that are applied to produce a new value. This is what makes collaborative editing implementations possible. But you don't have to worry about that, because it happens automatically.

## Custom Commands

When defining custom commands, you can create your own namespace:

```javascript
const MyEditor = {
  ...Editor,

  insertParagraph(editor) {
    // ...
  },
}
```

When writing your own commands, you'll often make use of the `Transforms` helpers that ship with Slate.

## Transforms

Transforms are a specific set of helpers that allow you to perform a wide variety of specific changes to the document, for example:

```javascript
// Set a "bold" format on all of the text nodes in a range.
// Normally you would apply a style like bold using the Editor.addMark() command.
// The addMark() command performs a similar setNodes transform, but it uses a more
// complicated match function in order to apply marks within markableVoid elements.
Transforms.setNodes(
  editor,
  { bold: true },
  {
    at: range,
    match: node => Text.isText(node),
    split: true,
  }
)

// Wrap the lowest block at a point in the document in a quote block.
Transforms.wrapNodes(
  editor,
  { type: 'quote', children: [] },
  {
    at: point,
    match: node => Editor.isBlock(editor, node),
    mode: 'lowest',
  }
)

// Insert new text to replace the text in a node at a specific path.
Transforms.insertText(editor, 'A new string of text.', { at: path })

// ...there are many more transforms!
```

The transform helpers are designed to be composed together. So you might use a handful of them for each command.


# Editor

All of the behaviors, content and state of a Slate editor is rolled up into a single, top-level `Editor` object. It has an interface of:

```typescript
interface Editor {
  // Current editor state
  children: Node[]
  selection: Range | null
  operations: Operation[]
  marks: Omit<Text, 'text'> | null
  // Schema-specific node behaviors.
  isInline: (element: Element) => boolean
  isVoid: (element: Element) => boolean
  markableVoid: (element: Element) => boolean
  normalizeNode: (entry: NodeEntry) => void
  onChange: (options?: { operation?: Operation }) => void
  // Overrideable core actions.
  addMark: (key: string, value: any) => void
  apply: (operation: Operation) => void
  deleteBackward: (unit: 'character' | 'word' | 'line' | 'block') => void
  deleteForward: (unit: 'character' | 'word' | 'line' | 'block') => void
  deleteFragment: () => void
  insertBreak: () => void
  insertSoftBreak: () => void
  insertFragment: (fragment: Node[]) => void
  insertNode: (node: Node) => void
  insertText: (text: string) => void
  removeMark: (key: string) => void
}
```

It is slightly more complex than the others, because it contains all of the top-level functions that define your custom, domain-specific behaviors.

The `children` property contains the document tree of nodes that make up the editor's content.

The `selection` property contains the user's current selection, if any. Don't set it directly; use [Transforms.select](https://docs.slatejs.org/04-transforms#selection-transforms)

The `operations` property contains all of the operations that have been applied since the last "change" was flushed. (Since Slate batches operations up into ticks of the event loop.)

The `marks` property stores formatting to be applied when the editor inserts text. If `marks` is `null`, the formatting will be taken from the current selection. Don't set it directly; use `Editor.addMark` and `Editor.removeMark`.

## Overriding Behaviors

In previous guides we've already hinted at this, but you can override any of the behaviors of an editor by overriding its function properties.

For example, if you want to define link elements that are inline nodes:

```javascript
const { isInline } = editor

editor.isInline = element => {
  return element.type === 'link' ? true : isInline(element)
}
```

Or maybe you want to override the `insertText` behavior to "linkify" URLs:

```javascript
const { insertText } = editor

editor.insertText = text => {
  if (isUrl(text)) {
    // ...
    return
  }

  insertText(text)
}
```

If you have void "mention" elements that can accept marks like bold or italic:

```javascript
const { isVoid, markableVoid } = editor

editor.isVoid = element => {
  return element.type === 'mention' ? true : isVoid(element)
}

editor.markableVoid = element => {
  return element.type === 'mention' || markableVoid(element)
}
```

Or you can even define custom "normalizations" that take place to ensure that links obey certain constraints:

```javascript
const { normalizeNode } = editor

editor.normalizeNode = (entry, options) => {
  const [node, path] = entry

  if (Element.isElement(node) && node.type === 'link') {
    // ...
    return
  }

  normalizeNode(entry, options)
}
```

Whenever you override behaviors, be sure to call the existing functions as a fallback mechanism for the default behavior. Unless you really do want to completely remove the default behaviors (which is rarely a good idea).

> 🤖 For more info, check out the [Editor Instance Methods to Override API Reference](https://docs.slatejs.org/api/nodes/editor#schema-specific-instance-methods-to-override)

## Helper Functions

The `Editor` interface, like all Slate interfaces, exposes helper functions that are useful when implementing certain behaviors. There are many, many editor-related helpers. For example:

```javascript
// Get the start point of a specific node at path.
const point = Editor.start(editor, [0, 0])

// Get the fragment (a slice of the document) at a range.
const fragment = Editor.fragment(editor, range)
```

There are also many iterator-based helpers, for example:

```javascript
// Iterate over every node in a range.
for (const [node, path] of Editor.nodes(editor, { at: range })) {
  // ...
}

// Iterate over every point in every text node in the current selection.
for (const point of Editor.positions(editor)) {
  // ...
}
```

> 🤖 For more info, check out the [Editor Static Methods API Reference](https://docs.slatejs.org/api/nodes/editor#static-methods)


# Plugins

You've already seen how the behaviors of Slate editors can be overridden. These overrides can also be packaged up into "plugins" to be reused, tested and shared. This is one of the most powerful aspects of Slate's architecture.

A plugin is simply a function that takes an `Editor` object and returns it after it has augmented it in some way.

For example, a plugin that marks image nodes as "void":

```javascript
const withImages = editor => {
  const { isVoid } = editor

  editor.isVoid = element => {
    return element.type === 'image' ? true : isVoid(element)
  }

  return editor
}
```

And then to use the plugin, simply:

```javascript
import { createEditor } from 'slate'

const editor = withImages(createEditor())
```

This plugin composition model makes Slate extremely easy to extend!

## Helper Functions

In addition to the plugin functions, you might want to expose helper functions that are used alongside your plugins. For example:

```javascript
import { Editor, Element } from 'slate'

const MyEditor = {
  ...Editor,
  insertImage(editor, url) {
    const element = { type: 'image', url, children: [{ text: '' }] }
    Transforms.insertNodes(editor, element)
  },
}

const MyElement = {
  ...Element,
  isImageElement(value) {
    return Element.isElement(element) && element.type === 'image'
  },
}
```

Then you can use `MyEditor` and `MyElement` everywhere and have access to all your helpers in one place.


# Rendering

One of the best parts of Slate is that it's built with React, so it fits right into your existing application. It doesn't re-invent its own view layer that you have to learn. It tries to keep everything as React-y as possible.

To that end, Slate gives you control over the rendering behavior of your custom nodes and properties in your richtext domain.

You can define these behaviors by passing "render props" to the top-level `<Editable>` component.

For example if you wanted to render custom element components, you'd pass in the `renderElement` prop:

```jsx
import { createEditor } from 'slate'
import { Slate, Editable, withReact } from 'slate-react'

const MyEditor = () => {
  const [editor] = useState(() => withReact(createEditor()))
  const renderElement = useCallback(({ attributes, children, element }) => {
    switch (element.type) {
      case 'quote':
        return <blockquote {...attributes}>{children}</blockquote>
      case 'link':
        return (
          <a {...attributes} href={element.url}>
            {children}
          </a>
        )
      default:
        return <p {...attributes}>{children}</p>
    }
  }, [])

  return (
    <Slate editor={editor}>
      <Editable renderElement={renderElement} />
    </Slate>
  )
}
```

> 🤖 Be sure to mix in `props.attributes` and render `props.children` in your custom components! The attributes must be added to the top-level DOM element inside the component, as they are required for Slate's DOM helper functions to work. And the children are the "leaves" holding text content and inline elements.

You don't have to use simple HTML elements, you can use your own custom React components too:

```javascript
const renderElement = useCallback(props => {
  switch (props.element.type) {
    case 'quote':
      return <QuoteElement {...props} />
    case 'link':
      return <LinkElement {...props} />
    default:
      return <DefaultElement {...props} />
  }
}, [])
```

## Leaves

When text-level formatting is rendered, the characters are grouped into "leaves" of text that each contain the same formatting (marks) applied to them.

To customize the rendering of each leaf, you use a custom `renderLeaf` prop:

```jsx
const renderLeaf = useCallback(({ attributes, children, leaf }) => {
  return (
    <span
      {...attributes}
      style={{
        fontWeight: leaf.bold ? 'bold' : 'normal',
        fontStyle: leaf.italic ? 'italic' : 'normal',
      }}
    >
      {children}
    </span>
  )
}, [])
```

Notice though how we've handled it slightly differently than `renderElement`. Since text formatting tends to be fairly simple, we've opted to ditch the `switch` statement and just toggle on/off a few styles instead. (But there's nothing preventing you from using custom components if you'd like!)

> 🤖 As with the Element renderer, be sure to mix in `props.attributes` and render `props.children` in your leaf renderer! The attributes must be added to the top-level DOM element inside the component, as they are required for Slate's DOM helper functions to work. And the children are the actual text content of your document which Slate manages for you automatically.

When decorations split a single text node, the `renderLeaf` function will receive an additional `leafPosition` property. This object contains the `start` and `end` offsets of the leaf within the original text node, along with optional `isFirst` and `isLast` booleans. This `leafPosition` property is only added when a text node is actually split by decorations.

One disadvantage of text-level formatting is that you cannot guarantee that any given format is "contiguous"—meaning that it stays as a single leaf. This limitation with respect to leaves is similar to the DOM, where this is invalid:

```markup
<em>t<strong>e</em>x</strong>t
```

Because the elements in the above example do not properly close themselves they are invalid. Instead, you would write the above HTML as follows:

```markup
<em>t</em><strong><em>e</em>x</strong>t
```

If you happened to add another overlapping section of `<strike>` to that text, you might have to rearrange the closing tags yet again. Rendering leaves in Slate is similar—you can't guarantee that even though a word has one type of formatting applied to it that that leaf will be contiguous, because it depends on how it overlaps with other formatting.

Of course, this leaf stuff sounds pretty complex. But, you do not have to think about it much, as long as you use text-level formatting and element-level formatting for their intended purposes:

* Text properties are for **non-contiguous**, character-level formatting.
* Element properties are for **contiguous**, semantic elements in the document.

## Texts

While `renderLeaf` allows you to customize the rendering of individual leaves based on their formatting (marks and decorations), sometimes you need to customize the rendering for an entire text node, regardless of how decorations might split it into multiple leaves.

This is where the `renderText` prop comes in. It allows you to render a component that wraps all the leaves generated for a single `Text` node.

```jsx
const renderText = useCallback(({ attributes, children, text }) => {
  return (
    <span {...attributes} className="custom-text">
      {children}
      {/* Render anything you want here */}
    </span>
  )
}, [])

// In your editor component:
<Editable
  renderText={renderText}
  renderLeaf={renderLeaf}
/>
```

**When to use `renderLeaf` vs `renderText`:**

* **`renderLeaf`**: Use this when you need to apply styles or rendering logic based on the specific properties of each individual leaf (e.g., applying bold style if `leaf.bold` is true, or highlighting based on a decoration). This function might be called multiple times for a single text node if decorations split it. You can use the optional `leafPosition` prop (available when a text node is split) to conditionally render something based on the position of the leaf within the text node.
* **`renderText`**: Use this when you need to render something exactly once for a given text node, regardless of how many leaves it's split into. It's ideal for wrapping the entire text node's content or adding elements associated with the text node as a whole without worrying about duplication caused by decorations.

You can use both `renderText` and `renderLeaf` together. `renderLeaf` renders the individual marks and decorations within a text node (leaves), and `renderText` renders the container of those leaves.

## Decorations

Decorations are another type of text-level formatting. They are similar to regular old custom properties, except each one applies to a `Range` of the document instead of being associated with a given text node.

However, decorations are computed at **render-time** based on the content itself. This is helpful for dynamic formatting like syntax highlighting or search keywords, where changes to the content (or some external data) has the potential to change the formatting.

Decorations are different from Marks in that they are not stored on editor state.

## Toolbars, Menus, Overlays, and more!

In addition to controlling the rendering of nodes inside Slate, you can also retrieve the current editor context from inside other components using the `useSlate` hook.

That way other components can execute commands, query the editor state, or anything else.

A common use case for this is rendering a toolbar with formatting buttons that are highlighted based on the current selection:

```jsx
const MyEditor = () => {
  const [editor] = useState(() => withReact(createEditor()))
  return (
    <Slate editor={editor}>
      <Toolbar />
      <Editable />
    </Slate>
  )
}

const Toolbar = () => {
  const editor = useSlate()
  return (
    <div>
      <Button active={isBoldActive(editor)}>B</Button>
      <Button active={isItalicActive(editor)}>I</Button>
    </div>
  )
}
```

Because the `<Toolbar>` uses the `useSlate` hook to retrieve the context, it will re-render whenever the editor changes, so that the active state of the buttons stays in sync.

## Editor Styling

Custom styles can be applied to the editor itself by using the `style` prop on the `<Editable>` component.

```jsx
const MyEditor = () => {
  const [editor] = useState(() => withReact(createEditor()))
  return (
    <Slate editor={editor}>
      <Editable style={{ minHeight: '200px', backgroundColor: 'lime' }} />
    </Slate>
  )
}
```

It is also possible to apply custom styles with a stylesheet and `className`. However, Slate uses inline styles to provide some default styles for the editor. Because inline styles take precedence over stylesheets, styles you provide using stylesheets will not override the default styles. If you are trying to use a stylesheet and your rules are not taking effect, do one of the following:

* Provide your styles using the `style` prop instead of a stylesheet, which overrides the default inline styles.
* Pass the `disableDefaultStyles` prop to the `<Editable>` component.
* Use `!important` in your stylesheet declarations to make them override the inline styles.

## Performance

See [Improving Performance](https://docs.slatejs.org/walkthroughs/09-performance) for ways to improve the rendering performance of the editor.


# Serializing

Slate's data model has been built with serialization in mind. Specifically, its text nodes are defined in a way that makes them easier to read at a glance, but also easy to serialize to common formats like HTML and Markdown.

And, because Slate uses plain JSON for its data, you can write serialization logic very easily.

## Plaintext

For example, taking the value of an editor and returning plaintext:

```javascript
import { Node } from 'slate'

const serialize = nodes => {
  return nodes.map(n => Node.string(n)).join('\n')
}
```

Here we're taking the children nodes of an `Editor` as a `nodes` argument, and returning a plaintext representation where each top-level node is separated by a single `\n` new line character.

For an input of:

```javascript
const nodes = [
  {
    type: 'paragraph',
    children: [{ text: 'An opening paragraph...' }],
  },
  {
    type: 'quote',
    children: [{ text: 'A wise quote.' }],
  },
  {
    type: 'paragraph',
    children: [{ text: 'A closing paragraph!' }],
  },
]
```

You'd end up with:

```
An opening paragraph...
A wise quote.
A closing paragraph!
```

Notice how the quote block isn't distinguishable in any way, that's because we're talking about plaintext. But you can serialize the data to anything you want—it's just JSON after all.

## HTML

For example, here's a similar `serialize` function for HTML:

```javascript
import escapeHtml from 'escape-html'
import { Text } from 'slate'

const serialize = node => {
  if (Text.isText(node)) {
    let string = escapeHtml(node.text)
    if (node.bold) {
      string = `<strong>${string}</strong>`
    }
    return string
  }

  const children = node.children.map(n => serialize(n)).join('')

  switch (node.type) {
    case 'quote':
      return `<blockquote><p>${children}</p></blockquote>`
    case 'paragraph':
      return `<p>${children}</p>`
    case 'link':
      return `<a href="${escapeHtml(node.url)}">${children}</a>`
    default:
      return children
  }
}
```

This one is a bit more aware than the plaintext serializer above. It's actually *recursive* so that it can keep iterating deeper through a node's children until it gets to the leaf text nodes. And for each node it receives, it converts it to an HTML string.

It also takes a single node as input instead of an array, so if you passed in an editor like:

```javascript
const editor = {
  children: [
    {
      type: 'paragraph',
      children: [
        { text: 'An opening paragraph with a ' },
        {
          type: 'link',
          url: 'https://example.com',
          children: [{ text: 'link' }],
        },
        { text: ' in it.' },
      ],
    },
    {
      type: 'quote',
      children: [{ text: 'A wise quote.' }],
    },
    {
      type: 'paragraph',
      children: [{ text: 'A closing paragraph!' }],
    },
  ],
  // `Editor` objects also have other properties that are omitted here...
}
```

You'd receive back (line breaks added for legibility):

```markup
<p>An opening paragraph with a <a href="https://example.com">link</a> in it.</p>
<blockquote><p>A wise quote.</p></blockquote>
<p>A closing paragraph!</p>
```

It's really that easy!

## Deserializing

Another common use case in Slate is doing the reverse—deserializing. This is when you have some arbitrary input and want to convert it into a Slate-compatible JSON structure. For example, when someone pastes HTML into your editor and you want to ensure it gets parsed with the proper formatting for your editor.

Slate has a built-in helper for this: the `slate-hyperscript` package.

The most common way to use `slate-hyperscript` is for writing JSX documents, for example when writing tests. You might use it like so:

```jsx
/** @jsx jsx */
import { jsx } from 'slate-hyperscript'

const input = (
  <fragment>
    <element type="paragraph">A line of text.</element>
  </fragment>
)
```

And the JSX feature of your compiler (Babel, TypeScript, etc.) would turn that `input` variable into:

```javascript
const input = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text.' }],
  },
]
```

This is great for test cases, or places where you want to be able to write a lot of Slate objects in a very readable form.

However! This doesn't help with deserialization.

But `slate-hyperscript` isn't only for JSX. It's just a way to build *trees of Slate content*. Which happens to be exactly what you want to do when you're deserializing something like HTML.

For example, here's a `deserialize` function for HTML:

```javascript
import { jsx } from 'slate-hyperscript'

const deserialize = (el, markAttributes = {}) => {
  if (el.nodeType === Node.TEXT_NODE) {
    return jsx('text', markAttributes, el.textContent)
  } else if (el.nodeType !== Node.ELEMENT_NODE) {
    return null
  }

  const nodeAttributes = { ...markAttributes }

  // define attributes for text nodes
  switch (el.nodeName) {
    case 'STRONG':
      nodeAttributes.bold = true
  }

  const children = Array.from(el.childNodes)
    .map(node => deserialize(node, nodeAttributes))
    .flat()

  if (children.length === 0) {
    children.push(jsx('text', nodeAttributes, ''))
  }

  switch (el.nodeName) {
    case 'BODY':
      return jsx('fragment', {}, children)
    case 'BR':
      return '\n'
    case 'BLOCKQUOTE':
      return jsx('element', { type: 'quote' }, children)
    case 'P':
      return jsx('element', { type: 'paragraph' }, children)
    case 'A':
      return jsx(
        'element',
        { type: 'link', url: el.getAttribute('href') },
        children
      )
    default:
      return children
  }
}
```

It takes in an `el` HTML element object and returns a Slate fragment. So if you have an HTML string, you can parse and deserialize it like so:

```javascript
const html = '...'
const document = new DOMParser().parseFromString(html, 'text/html')
deserialize(document.body)
```

With this input:

```markup
<p>An opening paragraph with a <a href="https://example.com">link</a> in it.</p>
<blockquote><p>A wise quote.</p></blockquote>
<p>A closing paragraph!</p>
```

You'd end up with this output:

```javascript
const fragment = [
  {
    type: 'paragraph',
    children: [
      { text: 'An opening paragraph with a ' },
      {
        type: 'link',
        url: 'https://example.com',
        children: [{ text: 'link' }],
      },
      { text: ' in it.' },
    ],
  },
  {
    type: 'quote',
    children: [
      {
        type: 'paragraph',
        children: [{ text: 'A wise quote.' }],
      },
    ],
  },
  {
    type: 'paragraph',
    children: [{ text: 'A closing paragraph!' }],
  },
]
```

And just like the serializing function, you can extend it to fit your exact domain model's needs.


# Normalizing

Slate editors can edit complex, nested data structures. And for the most part this is great. But in certain cases inconsistencies in the data structure can be introduced—most often when allowing a user to paste arbitrary richtext content.

"Normalizing" is how you can ensure that your editor's content is always of a certain shape. It's similar to "validating", except instead of just determining whether the content is valid or invalid, its job is to fix the content to make it valid again.

## Built-in Constraints

Slate editors come with a few built-in constraints out of the box. These constraints are there to make working with content *much* more predictable than standard `contenteditable`. All of the built-in logic in Slate depends on these constraints, so unfortunately you cannot omit them. They are...

1. **All `Element` nodes must contain at least one `Text` descendant** — even [Void Elements](https://docs.slatejs.org/02-nodes#voids). If an element node does not contain any children, an empty text node will be added as its only child. This constraint exists to ensure that the selection's anchor and focus points (which rely on referencing text nodes) can always be placed inside any node. Without this, empty elements (or void elements) wouldn't be selectable.
2. **Two adjacent texts with the same custom properties will be merged.** If two adjacent text nodes have the same formatting, they're merged into a single text node with a combined text string of the two. This exists to prevent the text nodes from only ever expanding in count in the document, since both adding and removing formatting results in splitting text nodes.
3. **Block nodes can only contain other blocks, or inline and text nodes.** For example, a `paragraph` block cannot have another `paragraph` block element *and* a `link` inline element as children at the same time. The type of children allowed is determined by the first child. Any other non-conforming children are tried to be converted (if possible) or removed. This ensures that common richtext behaviors like "splitting a block in two" function consistently. Conversion of block nodes is done by unwrapping the block node; conversion of inline/text nodes is performed by wrapping such nodes into a `fallbackElement` if specified in the `normalizeNode` options. The `fallbackElement` can be specified by editors overriding the `normalizeNode` function.
4. **Inline nodes cannot be the first or last child of a parent block, nor can it be next to another inline node in the children array.** If this is the case, an empty text node will be added to correct this to be in compliance with the constraint.
5. **The top-level editor node can only contain block nodes.** If any of the top-level children are inline or text nodes they will be removed. This ensures that there are always block nodes in the editor so that behaviors like "splitting a block in two" work as expected.
6. **Nodes must be JSON-serializable.** For example, avoid using `undefined` in your data model. This ensures that [operations](https://docs.slatejs.org/concepts/05-operations) are also JSON-serializable, a property which is assumed by collaboration libraries.
7. **Property values must not be `null`.** Instead, you should use an optional property, e.g. `foo?: string` instead of `foo: string | null`. This limitation is due to `null` being used in [operations](https://docs.slatejs.org/concepts/05-operations) to represent the absence of a property.

These default constraints are all mandated because they make working with Slate documents *much* more predictable.

> 🤖 Although these constraints are the best we've come up with now, we're always looking for ways to have Slate's built-in constraints be less constraining if possible—as long as it keeps standard behaviors easy to reason about. If you come up with a way to reduce or remove a built-in constraint with a different approach, we're all ears!

## Adding Constraints

The built-in constraints are fairly generic. But you can also add your own constraints on top of the built-in ones that are specific to your domain.

To do this, you extend the `normalizeNode` function on the editor. The `normalizeNode` function gets called every time an operation is applied that inserts or updates a node (or its descendants), giving you the opportunity to ensure that the changes didn't leave it in an invalid state, and correcting the node if so.

For example here's a plugin that ensures `paragraph` blocks only have text or inline elements as children:

```javascript
import { Transforms, Element, Node } from 'slate'

const withParagraphs = editor => {
  const { normalizeNode } = editor

  editor.normalizeNode = (entry, options) => {
    const [node, path] = entry

    // If the element is a paragraph, ensure its children are valid.
    if (Element.isElement(node) && node.type === 'paragraph') {
      for (const [child, childPath] of Node.children(editor, path)) {
        if (Element.isElement(child) && !editor.isInline(child)) {
          Transforms.unwrapNodes(editor, { at: childPath })
          return
        }
      }
    }

    // Fall back to the original `normalizeNode` to enforce other constraints.
    normalizeNode(entry, options)
  }

  return editor
}
```

This example is fairly simple. Whenever `normalizeNode` gets called on a paragraph element, it loops through each of its children ensuring that none of them are block elements. And if one is a block element, it gets unwrapped, so that the block is removed and its children take its place. The node is "fixed".

But what if the child has nested blocks?

## Multi-pass Normalizing

One thing to understand about `normalizeNode` constraints is that they are **multi-pass**.

If you check the example above again, you'll notice the `return` statement:

```javascript
if (Element.isElement(child) && !editor.isInline(child)) {
  Transforms.unwrapNodes(editor, { at: childPath })
  return
}
```

You might at first think this is odd, because with the `return` there, the original `normalizeNodes` will never be called, and the built-in constraints won't get a chance to run their own normalizations.

But, there's a slight "trick" to normalizing.

When you do call `Transforms.unwrapNodes`, you're actually changing the content of the node that is currently being normalized. So even though you're ending the current normalization pass, by making a change to the node you're kicking off a *new* normalization pass. This results in a sort of *recursive* normalizing.

This multi-pass characteristic makes it *much* easier to write normalizations, because you only ever have to worry about fixing a single issue at once, and not fixing *every* possible issue that could be putting a node in an invalid state.

To see how this works in practice, let's start with this invalid document:

```jsx
<editor>
  <paragraph a>
    <paragraph b>
      <paragraph c>word</paragraph>
    </paragraph>
  </paragraph>
</editor>
```

The editor starts by running `normalizeNode` on `<paragraph c>`. And it is valid, because it contains only text nodes as children.

But then, it moves up the tree, and runs `normalizeNode` on `<paragraph b>`. This paragraph is invalid, since it contains a block element (`<paragraph c>`). So that child block gets unwrapped, resulting in a new document of:

```jsx
<editor>
  <paragraph a>
    <paragraph b>word</paragraph>
  </paragraph>
</editor>
```

And in performing that fix, the top-level `<paragraph a>` changed. It gets normalized, and it is invalid, so `<paragraph b>` gets unwrapped, resulting in:

```jsx
<editor>
  <paragraph a>word</paragraph>
</editor>
```

And now when `normalizeNode` runs, no changes are made, so the document is valid!

> 🤖 For the most part you don't need to think about these internals. You can just know that anytime `normalizeNode` is called and you spot an invalid state, you can fix that single invalid state and trust that `normalizeNode` will be called again until the node becomes valid.

## Empty Children Early Constraint Execution

One special normalization executes before all other normalizations and this can be important to keep in mind when writing your normalizers.

Before any of the other normalizations can execute, Slate iterates through all `Element` nodes and makes sure they have at least one child. If it does not, an empty `Text` descendant is created.

This can trip you up when you have custom handling when an `Element` has no children. For example, if a table element has no rows, you may wish to remove the table; however, this will never happen because a `Text` node would automatically be created before that normalization could run.

## Incorrect Fixes

One pitfall to avoid is creating an infinite normalization loop. This can happen if you check for a specific invalid structure, but then **don't** actually fix that structure with the change you make to the node. This results in an infinite loop because the node continues to be flagged as invalid, but it is never fixed properly.

For example, consider a normalization that ensured `link` elements have a valid `url` property:

```javascript
// WARNING: this is an example of incorrect behavior!
const withLinks = editor => {
  const { normalizeNode } = editor

  editor.normalizeNode = (entry, options) => {
    const [node, path] = entry

    if (
      Element.isElement(node) &&
      node.type === 'link' &&
      typeof node.url !== 'string'
    ) {
      // ERROR: null is not a valid value for a url
      Transforms.setNodes(editor, { url: null }, { at: path })
      return
    }

    normalizeNode(entry, options)
  }

  return editor
}
```

This fix is incorrectly written. It wants to ensure that all `link` elements have a `url` property string. But to fix invalid links it sets the `url` to `null`, which is still not a string!

In this case you'd either want to unwrap the link, removing it entirely. *Or* expand your validation to accept an "empty" `url == null` as well.

## Implications for Other Code

Sequences of Transforms may need to be wrapped in [`Editor.withoutNormalizing`](https://docs.slatejs.org/api/nodes/editor#editorwithoutnormalizingeditor-editor-fn---void--void) if the node tree should *not* be normalized between Transforms. This is frequently the case when you `unwrapNodes` followed by `wrapNodes`. For example, you might write a function to change the type of a block as follows:

```javascript
const LIST_TYPES = ['numbered-list', 'bulleted-list']

function changeBlockType(editor, type) {
  Editor.withoutNormalizing(editor, () => {
    const isActive = isBlockActive(editor, type)
    const isList = LIST_TYPES.includes(type)

    Transforms.unwrapNodes(editor, {
      match: n =>
        LIST_TYPES.includes(
          !Editor.isEditor(n) && SlateElement.isElement(n) && n.type
        ),
      split: true,
    })
    const newProperties = {
      type: isActive ? 'paragraph' : isList ? 'list-item' : type,
    }
    Transforms.setNodes(editor, newProperties)

    if (!isActive && isList) {
      const block = { type: type, children: [] }
      Transforms.wrapNodes(editor, block)
    }
  })
}
```


# TypeScript

Slate supports typing of one Slate document model (ie. one set of custom `Editor`, `Element` and `Text` types). If you need to support more than one document model, see the section Multiple Document Models.

**Warning:** You must define `CustomTypes`, annotate `useState`, and annotate the editor's initial state when using TypeScript or Slate will display typing errors.

## Migrating from 0.47.x

When migrating from 0.47.x, read the guide below first. Also keep in mind these common migration issues:

* When referring to `node.type`, you may see the error `Property 'type' does not exist on type 'Node'`. To fix this, you need to add code like `Element.isElement(node) && node.type === 'paragraph'`. This is necessary because a `Node` can be an `Element` or `Text` and `Text` does not have a `type` property.
* Be careful when you define the CustomType for `Editor`. Make sure to define the CustomType for `Editor` as `BaseEditor & ...`. It should not be `Editor & ...`

## Defining `Editor`, `Element` and `Text` Types

To define a custom `Element` or `Text` type, extend the `CustomTypes` interface in the `slate` module like this.

```typescript
// This example is for an Editor with `ReactEditor` and `HistoryEditor`
import { BaseEditor } from 'slate'
import { ReactEditor } from 'slate-react'
import { HistoryEditor } from 'slate-history'

type CustomElement = { type: 'paragraph'; children: CustomText[] }
type CustomText = { text: string; bold?: true }

declare module 'slate' {
  interface CustomTypes {
    Editor: BaseEditor & ReactEditor & HistoryEditor
    Element: CustomElement
    Text: CustomText
  }
}
```

## Annotations in the Editor

Annotate the editor's initial value w/ `Descendant[]`.

```tsx
import React, { useState } from 'react'
import { createEditor, Descendant } from 'slate'
import { Slate, Editable, withReact } from 'slate-react'

const initialValue: Descendant[] = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable />
    </Slate>
  )
}
```

## Best Practices for `Element` and `Text` Types

While you can define types directly in the `CustomTypes` interface, best practice is to define and export each type separately so that you can reference individual types like a `ParagraphElement`.

Using best practices, the custom types might look something like:

```typescript
// This example is for an Editor with `ReactEditor` and `HistoryEditor`
import { BaseEditor } from 'slate'
import { ReactEditor } from 'slate-react'
import { HistoryEditor } from 'slate-history'

export type CustomEditor = BaseEditor & ReactEditor & HistoryEditor

export type ParagraphElement = {
  type: 'paragraph'
  children: CustomText[]
}

export type HeadingElement = {
  type: 'heading'
  level: number
  children: CustomText[]
}

export type CustomElement = ParagraphElement | HeadingElement

export type FormattedText = { text: string; bold?: true }

export type CustomText = FormattedText

declare module 'slate' {
  interface CustomTypes {
    Editor: CustomEditor
    Element: CustomElement
    Text: CustomText
  }
}
```

In this example, `CustomText` is equal to `FormattedText` but in a real editor, there can be more types of text like text in a code block which may not allow formatting for example.

## Why Is The Type Definition Unusual

Because it gets asked often, this section explains why Slate's type definition is atypical.

Slate needs to support a feature called type discrimination which is available when using union types (e.g. `ParagraphElement | HeadingElement`). This allows a user to narrow a type. If presented with code like `if (node.type === 'paragraph') { ... }` the inside of the block, will narrow the type of node to `ParagraphElement`.

Slate also needs a way to allow developers to get their custom types into Slate. This is done through declaration merging which is a feature of an `interface`.

Slate combines a union type and an interface in order to use both features.

For more information see [Proposal: Add Custom TypeScript Types to Slate](https://github.com/ianstormtaylor/slate/issues/3725)

## Multiple Document Models

At the moment, Slate supports types for a single document model at a time. For example, it cannot support two different Rich Text Editor with different document schemas.

Slate's TypeScript support was designed this way because typing for one document schema was better than none. The goal is to eventually support typing for multiple editor definitions and there is currently an in progress PR built by the creator of Slate.

One workaround for supporting multiple document models is to create each editor in a separate package and then import them. This hasn't been tested but should work.

## Extending Other Types

Currently there is also support for extending other types but these haven't been tested as thoroughly as the ones documented above:

* `Selection`
* `Range`
* `Point`

Feel free to extend these types but extending these types should be considered experimental. Please report bugs on GitHub issues.

## TypeScript Examples

For some examples of how to use types, see `packages/slate-react/src/custom-types.ts` in the slate repository.


# Migrating

Migrating from earlier versions of Slate to the `0.50.x` versions is not a simple task. The entire framework was re-considered from the ground up. This has resulted in a **much** better set of abstractions, which will result in you writing less code. But the migration process is not simple.

It's highly recommended that after reading this guide you read through the original [Walkthroughs](https://docs.slatejs.org/walkthroughs/01-installing-slate) and the other [Concepts](https://docs.slatejs.org/concepts/01-interfaces) to see how all of the new concepts get applied.

## Major Differences

Here's an overview of the *major* differences in the `0.50.x` version of Slate from an architectural point of view.

### JSON!

The data model is now comprised of simple JSON objects. Previously, it used [Immutable.js](https://immutable-js.github.io/immutable-js/) data structures. This is a huge change, and one that unlocks many other things. Hopefully it will also increase the average performance when using Slate. It also makes it much easier to get started for newcomers. This will be a large change to migrate from, but it will be worth it.

### Interfaces

The data model is interface-based. Previously each model was an instance of a class. Now, not only is the data plain objects, but Slate only expects that the objects implement an interface. So custom properties that used to live in `node.data` can now live at the top-level of the nodes.

### Namespaces

A lot of helper functions are exposed as a collection of helper functions on a namespace. For example, `Node.get(root, path)` or `Range.isCollapsed(range)`. This ends up making code much clearer because you can always quickly see what interface you're working with.

### TypeScript

The codebase now uses TypeScript. Working with pure JSON as a data model, and using an interface-based API are two things that have been made easier by migrating to TypeScript. You don't need to use it yourself, but if you do you'll get a lot more security when using the APIs. (And if you use VS Code you'll get nice autocompletion regardless!)

### Fewer Concepts

The number of interfaces and commands has been reduced. Previously `Selection`, `Annotation`, and `Decoration` used to all be separate classes. Now they are simply objects that implement the `Range` interface. Previously `Block` and `Inline` were separate; now they are objects that implement the `Element` interface. Previously there was a `Document` and `Value`, but now the top-level `Editor` contains the children nodes of the document itself.

The number of commands has been reduced too. Previously we had commands for every type of input, like `insertText`, `insertTextAtRange`, `insertTextAtPath`. These have been merged into a smaller set of more customizable commands, eg. `insertText` which can take `at: Path | Range | Point`.

### Fewer Packages

In an attempt to decrease the maintenance burden, and because the new abstraction and APIs in Slate's core packages make things much easier, the total number of packages has been reduced. Things like `slate-plain-serializer`, `slate-base64-serializer`, etc. have been removed and can be implemented in userland easily if needed. Even the `slate-html-deserializer` can now be implemented in userland (in \~10 LOC leveraging `slate-hyperscript`). And internal packages like `slate-dev-environment`, `slate-dev-test-utils`, etc. are no longer exposed because they are implementation details.

### Commands

A new "command" concept has been introduced. (The old "commands" are now called "transforms".) This new concept expresses the semantic intent of a user editing the document. And they allow for the right abstraction to tap into user behaviors—for example to change what happens when a user presses enter, or backspace, etc. Instead of using `keydown` events you should likely override command behaviors instead.

Commands are triggered by calling the `editor.*` core functions. And they travel through a middleware-like stack, but built from composed functions. Any plugin can override the behaviors to augment an editor.

### Plugins

Plugins are now plain functions that augment the `Editor` object they receive and return it again. For example, they can augment the command execution by composing the `editor.exec` function or listen to operations by composing `editor.apply`. Previously they relied on a custom middleware stack, and they were just bags of handlers that got merged onto an editor. Now we're using plain old function composition (aka wrapping) instead.

### Elements

Block-ness and inline-ness is now a runtime choice. Previously it was baked into the data model with the `object: 'block'` or `object: 'inline'` attributes. Now, it checks whether an "element" is inline or not at runtime. For example, you might check to see that `element.type === 'link'` and treat it as inline.

### More React-ish

Rendering and event-handling are no longer a plugin's concern. Previously plugins had full control over the rendering and event-handling logic in the editor. This creates a bad incentive to start putting **all** rendering logic in plugins, which puts Slate in a position of being a wrapper around all of React, which is very hard to do well. Instead, the new architecture has plugins focused purely on the richtext aspects, and leaves the rendering and event handling aspects to React.

### Context

Previously the `<Editor>` component was doing double duty as a sort of "controller" object and also the `contenteditable` DOM element. This led to a lot of awkwardness in how other components worked with Slate. In the new version, there is a new `<Slate>` context provider and a simpler `<Editable>` `contenteditable`-like component. By putting the `<Slate>` provider higher up in your component tree, you can share the editor directly with toolbars, buttons, etc. using the `useSlate` hook.

### Hooks

In addition to the `useSlate` hook, there are a handful of other hooks. For example the `useSelected` and `useFocused` hooks help with knowing when to render selected states (often for void nodes). And since they use React's Context API they will automatically re-render when their state changes.

### `beforeinput`

We now use the `beforeinput` event almost exclusively. Instead of relying on a series of shims and the quirks of React synthetic events, we're now using the standardized `beforeinput` event as our baseline. It is fully supported in Safari and Chrome, will soon be supported in the new Chromium-based Edge, and is currently being worked on in Firefox. In the meantime there are a few patches to make Firefox work. Internet Explorer is no longer supported in core out of the box.

### History-less

The core history logic has now finally been extracted into a standalone plugin. This makes it much easier for people to implement their own custom history behaviors. And it ensures that plugins have enough control to augment the editor in complex ways, because the history requires it.

### Mark-less

Marks have been removed from the Slate data model. Now that we have the ability to define custom properties right on the nodes themselves, you can model marks as custom properties of text nodes. For example bold can be modelled simply as a `bold: true` property.

### Annotation-less

Similarly, annotations have been removed from Slate's core. They can be fully implemented now in userland by defining custom operations and rendering annotated ranges using decorations. But most cases should be using custom text node properties or decorations anyways. There were not that many use cases that benefited from annotations.

## Reductions

One of the goals was to dramatically simplify a lot of the logic in Slate to make it easier to maintain and iterate on. This was done by refactoring to better base abstractions that can be built on, by leveraging modern DOM APIs, and by migrating to simpler React patterns.

To give you a sense for the change in total lines of code:

```
slate                       8,436  ->  3,958  (47%)
slate-react                 3,905  ->  1,954  (50%)

slate-base64-serializer        38  ->      0
slate-dev-benchmark           340  ->      0
slate-dev-environment         102  ->      0
slate-dev-test-utils           44  ->      0
slate-history                   0  ->    211
slate-hotkeys                  62  ->      0
slate-html-serializer         253  ->      0
slate-hyperscript             447  ->    345
slate-plain-serializer         56  ->      0
slate-prop-types               62  ->      0
slate-react-placeholder        62  ->      0

total                      13,807  ->  6,468  (47%)
```

It's quite a big difference! And that doesn't even include the dependencies that were shed in the process too.


# Transforms

Transforms are helper functions operating on the document. They can be used in defining your own commands.

* [Node options](#node-options)
* [Static methods](#static-methods)
  * [Node transforms](#node-transforms)
  * [Selection transforms](#selection-transforms)
  * [Text transforms](#text-transforms)
  * [Editor transforms](#editor-transforms)

## Node options

All transforms support a parameter `options`. This includes options specific to the transform and general `NodeOptions` to specify which Nodes in the document the transform is applied to.

```typescript
interface NodeOptions {
  at?: Location
  match?: (node: Node, path: Location) => boolean
  mode?: 'highest' | 'lowest'
  voids?: boolean
}
```

* The `at` option selects a [Location](https://docs.slatejs.org/concepts/03-locations) in the editor. It defaults to the user's current selection. [Learn more about the `at` option](https://docs.slatejs.org/concepts/04-transforms#the-at-option)
* The `match` option filters the set of Nodes with a custom function. [Learn more about the `match` option](https://docs.slatejs.org/concepts/04-transforms#the-match-option)
* The `mode` option also filters the set of nodes.
* When `voids` is false, [void Elements](https://docs.slatejs.org/nodes/editor#schema-specific-instance-methods-to-override) are filtered out.

## Static methods

### Node transforms

These transforms operate on nodes.

#### `Transforms.insertFragment(editor: Editor, fragment: Node[], options?)`

Insert a fragment of nodes at the specified location or (if not defined) the current selection or (if not defined) the end of the document.

Options: `{at?: Location, hanging?: boolean, voids?: boolean}`

#### `Transforms.insertNodes(editor: Editor, nodes: Node | Node[], options?)`

Atomically inserts `nodes` at the specified location or (if not defined) the current selection or (if not defined) the end of the document.

Options supported: `NodeOptions & {hanging?: boolean, select?: boolean}`.

For example, to insert at the very end, without replacing the current selection and regardless of block nesting, use

```javascript
Transforms.insertNodes(
  editor,
  { type: targetType, children: [{ text: '' }] },
  { at: [editor.children.length] }
)
```

#### `Transforms.removeNodes(editor: Editor, options?)`

Remove nodes at the specified location in the document. If no location is specified, remove the nodes in the selection.

Options supported: `NodeOptions & {hanging?: boolean}`

#### `Transforms.mergeNodes(editor: Editor, options?)`

Merge a node at the specified location with the previous node at the same depth. If no location is specified, use the selection. Resulting empty container nodes are removed.

Options supported: `NodeOptions & {hanging?: boolean}`

#### `Transforms.splitNodes(editor: Editor, options?)`

Split nodes at the specified location. If no location is specified, split the selection.

Options supported: `NodeOptions & {height?: number, always?: boolean}`

#### `Transforms.wrapNodes(editor: Editor, element: Element, options?)`

Wrap nodes at the specified location in the `element` container. If no location is specified, wrap the selection.

Options supported: `NodeOptions & {split?: boolean}`.

* `options.mode`: `'all'` is also supported.
* `options.split` indicates that it's okay to split a node in order to wrap the location. For example, if `ipsum` was selected in a `Text` node with `lorem ipsum dolar`, `split: true` would wrap the word `ipsum` only, resulting in splitting the `Text` node. If `split: false`, the entire `Text` node `lorem ipsum dolar` would be wrapped.

#### `Transforms.unwrapNodes(editor: Editor, options?)`

Unwrap nodes at the specified location. If necessary, the parent node is split. If no location is specified, use the selection.

Options supported: `NodeOptions & {split?: boolean}`. For `options.mode`, `'all'` is also supported.

#### `Transforms.setNodes(editor: Editor, props: Partial<Node>, options?)`

Set properties of nodes at the specified location. If no location is specified, use the selection.

If `props` contains `undefined` values, the node's corresponding property will also be set to `undefined` as opposed to ignored.

Options supported: `NodeOptions & {hanging?: boolean, split?: boolean}`. For `options.mode`, `'all'` is also supported.

#### `Transforms.unsetNodes(editor: Editor, props: string | string[], options?)`

Unset properties of nodes at the specified location. If no location is specified, use the selection.

Options supported: `NodeOptions & {hanging?: boolean, split?: boolean}`. For `options.mode`, `'all'` is also supported.

#### `Transforms.liftNodes(editor: Editor, options?)`

Lift nodes at the specified location upwards in the document tree. If necessary, the parent node is split. If no location is specified, use the selection.

Options supported: `NodeOptions`. For `options.mode`, `'all'` is also supported.

#### `Transforms.moveNodes(editor: Editor, options)`

Move the nodes from an origin to a destination. A destination must be specified in the `options`. If no origin is specified, move the selection.

Options supported: `NodeOptions & {to: Path}`. For `options.mode`, `'all'` is also supported.

### Selection transforms

Transforms that operate on the document's selection.

#### `Transforms.collapse(editor: Editor, options?)`

Collapse the selection to a single point.

Options: `{edge?: 'anchor' | 'focus' | 'start' | 'end'}`

#### `Transforms.select(editor: Editor, target: Location)`

Set the selection to a new value specified by `target`. When a selection already exists, this method is just a proxy for `setSelection` and will update the existing value.

For example, to set the selection to the entire contents of the editor:

```javascript
Transforms.select(editor, {
  anchor: Editor.start(editor, []),
  focus: Editor.end(editor, []),
})
```

#### `Transforms.deselect(editor: Editor)`

Unset the selection.

#### `Transforms.move(editor: Editor, options?)`

Move the selection's point forward or backward.

Options: `{distance?: number, unit?: 'offset' | 'character' | 'word' | 'line', reverse?: boolean, edge?: 'anchor' | 'focus' | 'start' | 'end'}`

#### `Transforms.setPoint(editor: Editor, props: Partial<Point>, options?)`

Set new properties on one of the selection's points.

Options: `{edge?: 'anchor' | 'focus' | 'start' | 'end'}`

#### `Transforms.setSelection(editor: Editor, props: Partial<Range>)`

Set new properties on an active selection. Since the value is a `Partial<Range>`, this method can only handle updates to an existing selection. If there is no active selection the operation will be void. Use `select` if you'd like to create a selection when there is none.

### Text transforms

Transforms that operate on text.

#### `Transforms.delete(editor: Editor, options?)`

Delete text in the document.

Options: `{at?: Location, distance?: number, unit?: 'character' | 'word' | 'line' | 'block', reverse?: boolean, hanging?: boolean, voids?: boolean}`

#### `Transforms.insertText(editor: Editor, text: string, options?)`

Insert a string of text at the specified location or (if not defined) the current selection or (if not defined) the end of the document.

Options: `{at?: Location, voids?: boolean}`

### Editor transforms

#### `Transforms.transform(editor: Editor, transform: Transform)`

Transform the `editor` by an `operation`.


# Node Types

The `Node` union type represents all of the different types of nodes that occur in a Slate document tree.

```typescript
type Node = Editor | Element | Text

type Descendant = Element | Text
type Ancestor = Editor | Element
```

* [Node](https://docs.slatejs.org/api/nodes/node)
* [NodeEntry](https://docs.slatejs.org/api/nodes/node-entry)
* [Editor](https://docs.slatejs.org/api/nodes/editor)
* [Element](https://docs.slatejs.org/api/nodes/element)
* [Text](https://docs.slatejs.org/api/nodes/text)


# Editor

The `Editor` object stores all the state of a Slate editor. It can be extended by [plugins](https://docs.slatejs.org/concepts/08-plugins) to add helpers and implement new behaviors. It's a type of `Node` and its path is `[]`.

```typescript
interface Editor {
  children: Node[]
  selection: Range | null
  operations: Operation[]
  marks: Omit<Text, 'text'> | null

  // Schema-specific node behaviors.
  isInline: (element: Element) => boolean
  isVoid: (element: Element) => boolean
  markableVoid: (element: Element) => boolean
  normalizeNode: (entry: NodeEntry) => void
  onChange: (options?: { operation?: Operation }) => void

  // Overrideable core actions.
  addMark: (key: string, value: any) => void
  apply: (operation: Operation) => void
  deleteBackward: (unit: 'character' | 'word' | 'line' | 'block') => void
  deleteForward: (unit: 'character' | 'word' | 'line' | 'block') => void
  deleteFragment: () => void
  insertBreak: () => void
  insertFragment: (fragment: Node[]) => void
  insertNode: (node: Node) => void
  insertText: (text: string) => void
  removeMark: (key: string) => void
}
```

* [Instantiation methods](#instantiation-methods)
* [Static methods](#static-methods)
  * [Retrieval methods](#retrieval-methods)
  * [Manipulation methods](#manipulation-methods)
  * [Check methods](#check-methods)
  * [Normalization methods](#normalization-methods)
  * [Ref methods](#ref-methods)
* [Instance methods](#instance-methods)
  * [Schema-specific methods to override](#schema-specific-instance-methods-to-override)
  * [Element Type Methods](#element-type-methods)
  * [Normalize Methods](#normalize-methods)
  * [Callback Method](#callback-method)
  * [Mark Methods](#mark-methods)
  * [getFragment Method](#getfragment-method)
  * [Delete Methods](#delete-methods)
  * [Insert Methods](#insert-methods)
  * [Operation Handling Method](#operation-handling-method)

## Instantiation methods

#### `createEditor() => Editor`

Note: This method is imported directly from Slate and is not part of the Editor object.

Creates a new, empty `Editor` object.

## Static methods

### Retrieval methods

#### `Editor.above<T extends Ancestor>(editor: Editor, options?) => NodeEntry<T> | undefined`

Get the matching ancestor above a location in the document.

Options:

* `at?: Location = editor.selection`: Where to start at which is `editor.selection` by default.
* `match?: NodeMatch = () => true`: Narrow the match
* `mode?: 'highest' | 'lowest' = 'lowest'`: If `lowest` (default), returns the lowest matching ancestor. If `highest`, returns the highest matching ancestor.
* `voids?: boolean = false`: When `false` ignore void objects.

#### `Editor.after(editor: Editor, at: Location, options?) => Point | undefined`

Get the point after a location.

If there is no point after the location (e.g. we are at the bottom of the document) returns `undefined`.

Options: `{distance?: number, unit?: 'offset' | 'character' | 'word' | 'line' | 'block', voids?: boolean}`

#### `Editor.before(editor: Editor, at: Location, options?) => Point | undefined`

Get the point before a location.

If there is no point before the location (e.g. we are at the top of the document) returns `undefined`.

Options: `{distance?: number, unit?: 'offset' | 'character' | 'word' | 'line' | 'block', voids?: boolean}`

#### `Editor.edges(editor: Editor, at: Location) => [Point, Point]`

Get the start and end points of a location.

#### `Editor.end(editor: Editor, at: Location) => Point`

Get the end point of a location.

#### `Editor.first(editor: Editor, at: Location) => NodeEntry`

Get the first node at a location.

#### `Editor.fragment(editor: Editor, at: Location) => Descendant[]`

Get the fragment at a location.

#### `Editor.last(editor: Editor, at: Location) => NodeEntry`

Get the last node at a location.

#### `Editor.leaf(editor: Editor, at: Location, options?) => NodeEntry`

Get the leaf text node at a location.

Options: `{depth?: number, edge?: 'start' | 'end'}`

#### `Editor.levels<T extends Node>(editor: Editor, options?) => Generator<NodeEntry<T>, void, undefined>`

Iterate through all of the levels at a location.

Options: `{at?: Location, match?: NodeMatch, reverse?: boolean, voids?: boolean}`

#### `Editor.marks(editor: Editor) => Omit<Text, 'text'> | null`

Get the marks that would be added to text at the current selection.

#### `Editor.next<T extends Descendant>(editor: Editor, options?) => NodeEntry<T> | undefined`

Get the matching node in the branch of the document after a location.

Note: To find the next Point, and not the next Node, use the `Editor.after` method

Options: `{at?: Location, match?: NodeMatch, mode?: 'all' | 'highest' | 'lowest', voids?: boolean}`

#### `Editor.node(editor: Editor, at: Location, options?) => NodeEntry`

Get the node at a location.

Options: `depth?: number, edge?: 'start' | 'end'`

#### `Editor.nodes<T extends Node>(editor: Editor, options?) => Generator<NodeEntry<T>, void, undefined>`

At any given `Location` or `Span` in the editor provided by `at` (default is the current selection), the method returns a Generator of `NodeEntry` objects that represent the nodes that include `at`. At the top of the hierarchy is the `Editor` object itself.

Options: `{at?: Location | Span, match?: NodeMatch, mode?: 'all' | 'highest' | 'lowest', universal?: boolean, reverse?: boolean, voids?: boolean, pass?: (node: NodeEntry => boolean)}`

`options.match`: Provide a value to the `match?` option to limit the `NodeEntry` objects that are returned.

`options.mode`:

* `'all'` (default): Return all matching nodes
* `'highest'`: in a hierarchy of nodes, only return the highest level matching nodes
* `'lowest'`: in a hierarchy of nodes, only return the lowest level matching nodes

`options.pass`: Skip the descendants of certain nodes (but not the nodes themselves).

#### `Editor.parent(editor: Editor, at: Location, options?) => NodeEntry<Ancestor>`

Get the parent node of a location.

Options: `{depth?: number, edge?: 'start' | 'end'}`

#### `Editor.path(editor: Editor, at: Location, options?) => Path`

Get the path of a location.

Options: `{depth?: number, edge?: 'start' | 'end'}`

#### `Editor.point(editor: Editor, at: Location, options?) => Point`

Get the `start` or `end` (default is `start`) point of a location.

Options: `{edge?: 'start' | 'end'}`

#### `Editor.positions(editor: Editor, options?) => Generator<Point, void, undefined>`

Iterate through all of the positions in the document where a `Point` can be placed. The first `Point` returns is always the starting point followed by the next `Point` as determined by the `unit` option.

Read `options.unit` to see how this method iterates through positions.

Note: By default void nodes are treated as a single point and iteration will not happen inside their content unless the voids option is set, then iteration will occur.

Options:

* `at?: Location = editor.selection`: The `Location` in which to iterate the positions of.
* `unit?: 'offset' | 'character' | 'word' | 'line' | 'block' = 'offset'`:
  * `offset`: Moves to the next offset `Point`. It will include the `Point` at the end of a `Text` object and then move onto the first `Point` (at the 0th offset) of the next `Text` object. This may be counter-intuitive because the end of a `Text` and the beginning of the next `Text` might be thought of as the same position.
  * `character`: Moves to the next `character` but is not always the next `index` in the string. This is because Unicode encodings may require multiple bytes to create one character. Unlike `offset`, `character` will not count the end of a `Text` and the beginning of the next `Text` as separate positions to return. Warning: The character offsets for Unicode characters does not appear to be reliable in some cases like a Smiley Emoji will be identified as 2 characters.
  * `word`: Moves to the position immediately after the next `word`. In `reverse` mode, moves to the position immediately before the previous `word`.
  * `line` | `block`: Starts at the beginning position and then the position at the end of the block. Then starts at the beginning of the next block and then the end of the next block.
* `reverse?: boolean = false`: When `true` returns the positions in reverse order. In the case of the `unit` being `word`, the actual returned positions are different (i.e. we will get the start of a word in reverse instead of the end).
* `voids?: boolean = false`: When `true` include void Nodes.

#### `Editor.previous<T extends Node>(editor: Editor, options?) => NodeEntry<T> | undefined`

Get the matching node in the branch of the document before a location.

Note: To find the previous Point, and not the previous Node, use the `Editor.before` method

Options: `{at?: Location, match?: NodeMatch, mode?: 'all' | 'highest' | 'lowest', voids?: boolean}`

#### `Editor.range(editor: Editor, at: Location, to?: Location) => Range`

Get a range of a location.

#### `Editor.start(editor: Editor, at: Location) => Point`

Get the start point of a location.

#### `Editor.string(editor: Editor, at: Location, options?) => string`

Get the text string content of a location.

Note: by default the text of void nodes is considered to be an empty string, regardless of content, unless the voids option is set.

Options: : `{voids?: boolean}`

#### `Editor.void(editor: Editor, options?) => NodeEntry<Element> | undefined`

Match a void node in the current branch of the editor.

Options: `{at?: Location, mode?: 'highest' | 'lowest', voids?: boolean}`

### Manipulation methods

#### `Editor.addMark(editor: Editor, key: string, value: any) => void`

Add a custom property to the leaf text nodes and any nodes that `editor.markableVoid()` allows in the current selection.

If the selection is currently collapsed, the marks will be added to the `editor.marks` property instead, and applied when text is inserted next.

#### `Editor.deleteBackward(editor: Editor, options?) => void`

Delete content in the editor backward from the current selection.

Options: `{unit?: 'character' | 'word' | 'line' | 'block'}`

#### `Editor.deleteForward(editor: Editor, options?) => void`

Delete content in the editor forward from the current selection.

Options: `{unit?: 'character' | 'word' | 'line' | 'block'}`

#### `Editor.deleteFragment(editor: Editor) => void`

Delete the content in the current selection.

#### `Editor.insertBreak(editor: Editor) => void`

Insert a block break at the current selection.

#### `Editor.insertSoftBreak(editor: Editor) => void`

Insert a soft break at the current selection.

#### `Editor.insertFragment(editor: Editor, fragment: Node[], options?) => void`

Inserts a fragment at the specified location or (if not defined) the current selection or (if not defined) the end of the document.

Options: `{at?: Location, hanging?: boolean, voids?: boolean}`

#### `Editor.insertNode(editor: Editor, node: Node, options?) => void`

Atomically insert `node` at the specified location or (if not defined) the current selection or (if not defined) the end of the document.

Options supported: `NodeOptions & {hanging?: boolean, select?: boolean}`.

#### `Editor.insertText(editor: Editor, text: string, options?) => void`

Insert a string of text at the specified location or (if not defined) the current selection or (if not defined) the end of the document.

Options: `{at?: Location, voids?: boolean}`

#### `Editor.removeMark(editor: Editor, key: string) => void`

Remove a custom property from all of the leaf text nodes within non-void nodes or void nodes that `editor.markableVoid()` allows in the current selection.

If the selection is currently collapsed, the removal will be stored on `editor.marks` and applied to the text inserted next.

#### `Editor.unhangRange(editor: Editor, range: Range, options?) => Range`

Convert a range into a non-hanging one.

A "hanging" range is one created by the browser's "triple-click" selection behavior. When triple-clicking a block, the browser selects from the start of that block to the start of the *next* block. The range thus "hangs over" into the next block. If `unhangRange` is given such a range, it moves the end backwards until it's in a non-empty text node that precedes the hanging block.

Note that `unhangRange` is designed for the specific purpose of fixing triple-clicked blocks, and therefore currently has a number of caveats:

* It does not modify the start of the range; only the end. For example, it does not "unhang" a selection that starts at the end of a previous block.
* It only does anything if the start block is fully selected. For example, it does not handle ranges created by double-clicking the end of a paragraph (which browsers treat by selecting from the end of that paragraph to the start of the next).

Options:

* `voids?: boolean = false`: Allow placing the end of the selection in a void node.

### Check methods

#### `Editor.hasBlocks(editor: Editor, element: Element) => boolean`

Check if a node has block children.

#### `Editor.hasInlines(editor: Editor, element: Element) => boolean`

Check if a node has inline and text children.

#### `Editor.hasTexts(editor: Editor, element: Element) => boolean`

Check if a node has text children.

#### `Editor.isBlock(editor: Editor, value: any) => value is Element`

Check if a value is a block `Element` object.

#### `Editor.isEditor(value: any) => value is Editor`

Check if a value is an `Editor` object.

#### `Editor.isEnd(editor: Editor, point: Point, at: Location) => boolean`

Check if a point is the end point of a location.

#### `Editor.isEdge(editor: Editor, point: Point, at: Location) => boolean`

Check if a point is an edge of a location.

#### `Editor.isEmpty(editor: Editor, element: Element) => boolean`

Check if an element is empty, accounting for void nodes.

#### `Editor.isInline(editor: Editor, value: any) => value is Element`

Check if a value is an inline `Element` object.

#### `Editor.isNormalizing(editor: Editor) => boolean`

Check if the editor is currently normalizing after each operation.

#### `Editor.isStart(editor: Editor, point: Point, at: Location) => boolean`

Check if a point is the start point of a location.

#### `Editor.isVoid(editor: Editor, value: any) => value is Element`

Check if a value is a void `Element` object.

### Normalization methods

#### `Editor.normalize(editor: Editor, options?) => void`

Normalize any dirty objects in the editor.

Options: `{force?: boolean; operation?: Operation}`

#### `Editor.withoutNormalizing(editor: Editor, fn: () => void) => void`

Call a function, deferring normalization until after it completes. See [Normalization - Implications for Other Code](https://docs.slatejs.org/concepts/11-normalizing#implications-for-other-code);

### Ref Methods

#### `Editor.pathRef(editor: Editor, path: Path, options?) => PathRef`

Create a mutable ref for a `Path` object, which will stay in sync as new operations are applied to the editor.

Options: `{affinity?: 'backward' | 'forward' | null}`

#### `Editor.pathRefs(editor: Editor) => Set<PathRef>`

Get the set of currently tracked path refs of the editor.

#### `Editor.pointRef(editor: Editor, point: Point, options?) => PointRef`

Create a mutable ref for a `Point` object, which will stay in sync as new operations are applied to the editor.

Options: `{affinity?: 'backward' | 'forward' | null}`

#### `Editor.pointRefs(editor: Editor) => Set<PointRef>`

Get the set of currently tracked point refs of the editor.

#### `Editor.rangeRef(editor: Editor, range: Range, options?) => RangeRef`

Create a mutable ref for a `Range` object, which will stay in sync as new operations are applied to the editor.

Options: `{affinity?: 'backward' | 'forward' | 'outward' | 'inward' | null}`

#### `Editor.rangeRefs(editor: Editor) => Set<RangeRef>`

Get the set of currently tracked range refs of the editor.

## Instance Methods

### Schema-specific instance methods to override

Replace these methods to modify the original behavior of the editor when building [Plugins](https://docs.slatejs.org/concepts/08-plugins). When modifying behavior, call the original method when appropriate. For example, a plugin that marks image nodes as "void":

```javascript
const withImages = editor => {
  const { isVoid } = editor

  editor.isVoid = element => {
    return element.type === 'image' ? true : isVoid(element)
  }

  return editor
}
```

### Element type methods

Use these methods so that Slate can identify certain elements as [inlines](https://docs.slatejs.org/concepts/02-nodes#blocks-vs-inlines) or [voids](https://docs.slatejs.org/concepts/02-nodes#voids).

#### `isInline(element: Element) => boolean`

Check if a value is an inline `Element` object.

#### `isVoid(element: Element) => boolean`

Check if a value is a void `Element` object.

### Normalize methods

#### `normalizeNode(entry: NodeEntry, { operation, fallbackElement }) => void`

[Normalize](https://docs.slatejs.org/concepts/11-normalizing) a Node according to the schema.

#### `shouldNormalize: (options) => boolean`

Override this method to prevent normalizing the editor.

Options: `{ dirtyPaths: Path[]; initialDirtyPathsLength: number; iteration: number; operation?: Operation }`

### Callback method

#### `onChange(options?: { operation?: Operation }) => void`

Called when there is a change in the editor.

### Mark methods

#### `markableVoid: (element: Element) => boolean`

Tells which void nodes accept Marks. Slate's default implementation returns `false`, but if some void elements support formatting, override this function to include them.

#### `addMark(key: string, value: any) => void`

Add a custom property to the leaf text nodes within non-void nodes or void nodes that `editor.markableVoid()` allows in the current selection. If the selection is currently collapsed, the marks will be added to the `editor.marks` property instead, and applied when text is inserted next.

#### `removeMark(key: string) => void`

Remove a custom property from the leaf text nodes within non-void nodes or void nodes that `editor.markableVoid()` allows in the current selection.

### getFragment method

#### `getFragment() => Descendant[]`

Returns the fragment at the current selection. Used when cutting or copying, as an example, to get the fragment at the current selection.

### Delete methods

When a user presses backspace or delete, it invokes the method based on the selection. For example, if the selection is expanded over some text and the user presses the backspace key, `deleteFragment` will be called, but if the selection is collapsed, `deleteBackward` will be called.

#### `deleteBackward(options?: {unit?: 'character' | 'word' | 'line' | 'block'}) => void`

Delete content in the editor backward from the current selection.

#### `deleteForward(options?: {unit?: 'character' | 'word' | 'line' | 'block'}) => void`

Delete content in the editor forward from the current selection.

#### `deleteFragment() => void`

Delete the content of the current selection.

### Insert methods

#### `insertFragment(fragment: Node[]) => void`

Insert a fragment at the current selection. If the selection is currently expanded, delete it first.

#### `insertBreak() => void`

Insert a block break at the current selection. If the selection is currently expanded, delete it first.

#### `insertSoftBreak() => void`

Insert a soft break at the current selection. If the selection is currently expanded, delete it first.

#### `insertNode(node: Node) => void`

Insert a node at the current selection. If the selection is currently expanded, delete it first.

#### `insertText(text: string) => void`

Insert text at the current selection. If the selection is currently expanded, delete it first.

### Operation handling method

#### `apply(operation: Operation) => void`

Apply an operation in the editor.


# Element

`Element` objects are a type of `Node` in a Slate document that contain other `Element` nodes or `Text` nodes.

```typescript
interface Element {
  children: Node[]
}
```

* [Behavior Types](#element-behavior-types)
  * [Block vs. Inline](#block-vs-inline)
  * [Void vs Not Void](#void-vs-not-void)
    * [Rendering Void Elements](#rendering-void-elements)
* [Static methods](#static-methods)
  * [Retrieval methods](#retrieval-methods)
  * [Check methods](#check-methods)

## Element Behavior Types

Element nodes behave differently depending on the [Slate editor's configuration](https://docs.slatejs.org/api/editor#schema-specific-instance-methods-to-override). An element can be:

* "block" or "inline" as defined by `editor.isInline`
* either "void" or "not void" as defined by `editor.isVoid`

### Block vs. Inline

A "block" element can only be siblings with other "block" elements. An "inline" node can be siblings with `Text` nodes or other "inline" elements.

### Void vs Not Void

In a not "void" element, Slate handles the rendering of its `children` (e.g. in a paragraph where the `Text` and `Inline` children are rendered by Slate). In a "void" element, the `children` are rendered by the `Element`'s render code.

#### Voids That Support Marks

Some void elements are effectively stand-ins for text, such as with the [Mentions](https://www.slatejs.org/examples/mentions) example, where the mention element renders the character's name. Users might want to format Void elements like this with bold, or set their font and size, so `editor.markableVoid` tells Slate whether or not to apply Marks to the text children of void elements.

#### Rendering Void Elements

Void Elements must

* always have one empty child text node (for selection)
* render using `attributes` and `children` (so, their outermost HTML element **can't** be an HTML void element)
* set `contentEditable={false}` (for Firefox)

Typical rendering code will resemble this `thematic-break` (horizontal rule) element:

```javascript
return (
  <div {...attributes} contentEditable={false}>
    {children}
    <hr />
  </div>
)
```

For a "markable" void such as a `mention` element, marks on the empty child element can be used to determine how the void element is rendered (Slate Marks are applied only to Text leaves):

```javascript
const Mention = ({ attributes, children, element }) => {
  const selected = useSelected()
  const focused = useFocused()
  const style: React.CSSProperties = {
    padding: '3px 3px 2px',
    margin: '0 1px',
    verticalAlign: 'baseline',
    display: 'inline-block',
    borderRadius: '4px',
    backgroundColor: '#eee',
    fontSize: '0.9em',
    boxShadow: selected && focused ? '0 0 0 2px #B4D5FF' : 'none',
  }
  // See if our empty text child has any styling marks applied and apply those
  if (element.children[0].bold) {
    style.fontWeight = 'bold'
  }
  if (element.children[0].italic) {
    style.fontStyle = 'italic'
  }
  return (
    <span
      {...attributes}
      contentEditable={false}
      data-cy={`mention-${element.character.replace(' ', '-')}`}
      style={style}
    >
      {children}@{element.character}
    </span>
  )
}
```

## Static methods

### Retrieval methods

#### `Element.matches(element: Element, props: Partial<Element>) => boolean`

Check if an element matches a set of `props`. Note: This checks custom properties, but it does not ensure that any children are equivalent.

### Check methods

#### `Element.isAncestor(value: any) => value is Ancestor`

Check if a value implements the 'Ancestor' interface.

#### `Element.isElement(value: any) => value is Element`

Check if a `value` implements the `Element` interface.

#### `Element.isElementList(value: any) => value is Element[]`

Check if a `value` is an array of `Element` objects.

#### `Element.isElementType<T Extends Element>(value: any, elementVal: string, ElementKey: string = 'type'): value is T`

Check if a value implements the `Element` interface and has elementKey with selected value. Default it check to `type` key value


# Node

* [Static methods](#static-methods)
  * [Retrieval methods](#retrieval-methods)
  * [Text methods](#text-methods)
  * [Check methods](#check-methods)

## Static methods

### Retrieval methods

#### `Node.ancestor(root: Node, path: Path) => Ancestor`

Get the node at a specific `path`, asserting that it is an ancestor node. If the specified node is not an ancestor node, throw an error.

#### `Node.ancestors(root: Node, path: Path, options?) => Generator<NodeEntry<Ancestor>>`

Return a generator of all the ancestor nodes above a specific path. By default, the order is top-down, from highest to lowest ancestor in the tree, but you can pass the `reverse: true` option to go bottom-up.

Options: `{reverse?: boolean}`

#### `Node.child(root: Node, index: number) => Descendant`

Get the child of a node at the specified `index`.

#### `Node.children(root: Node, path: Path, options?) => Generator<NodeEntry<Descendant>>`

Iterate over the children of a node at a specific path.

Options: `{reverse?: boolean}`

#### `Node.common(root: Node, path: Path, another: Path) => NodeEntry`

Get an entry for the common ancestor node of two paths. It might be a Text node, an Element, or the Editor itself.

For the common block ancestor, see [Editor Selection](https://docs.slatejs.org/concepts/03-locations#selection)

#### `Node.descendant(root: Node, path: Path) => Descendant`

Get the node at a specific path, asserting that it's a descendant node.

#### `Node.descendants(root: Node, options?) => Generator<NodeEntry<Descendant>>`

Return a generator of all the descendant node entries inside a root node. Each iteration will return a `NodeEntry` tuple consisting of `[Node, Path]`.

Options: `{from?: Path, to?: Path, reverse?: boolean, pass?: (node: NodeEntry => boolean)}`

#### `Node.elements(root: Node, options?) => Generator<ElementEntry>`

Return a generator of all the element nodes inside a root node. Each iteration will return an `ElementEntry` tuple consisting of `[Element, Path]`. If the root node is an element, it will be included in the iteration as well.

Options: `{from?: Path, to?: Path, reverse?: boolean, pass?: (node: NodeEntry => boolean)}`

#### `Node.extractProps(node: Node) => NodeProps`

Extract all properties from a Node except for its content-related fields (`children` for Element nodes and `text` for Text nodes).

```typescript
// For an Element node
const element = {
  type: 'paragraph',
  align: 'center',
  children: [{ text: 'Try it out for yourself!' }],
}
const props = Node.extractProps(element)
// Returns: { type: 'paragraph', align: "center" }

// For a Text node
const text = { text: 'Hello', bold: true }
const props = Node.extractProps(text)
// Returns: { bold: true }
```

#### `Node.first(root: Node, path: Path) => NodeEntry`

Get the first node entry in a root node from a `path`.

#### `Node.fragment(root: Node, range: Range) => Descendant[]`

Get the sliced fragment represented by the `range`.

#### `Node.get(root: Node, path: Path) => Node`

Get the descendant node referred to by a specific `path`. If the path is an empty array, get the root node itself.

#### `Node.getIf(root: Node, path: Path) => Node | undefined`

Get a descendant node at a specific path, returning `undefined` if the node does not exist. This is a safer alternative to `Node.get()` as it won't throw an error if the path is invalid.

```typescript
const node = Node.getIf(root, [0, 1])
if (node) {
  // node exists at path [0, 1]
} else {
  // no node exists at path [0, 1]
}
```

#### `Node.last(root: Node, path: Path) => NodeEntry`

Get the last node entry in a root node at a specific `path`.

#### `Node.leaf(root: Node, path: Path) => Text`

Get the node at a specific `path`, ensuring it's a leaf text node. If the node is not a leaf text node, throw an error.

#### `Node.levels(root: Node, path: Path, options?) => Generator<NodeEntry>`

Return a generator of the nodes in a branch of the tree, from a specific `path`. By default, the order is top-down, from the highest to the lowest node in the tree, but you can pass the `reverse: true` option to go bottom-up.

Options: `{reverse?: boolean}`

#### `Node.nodes(root: Node, options?) => Generator<NodeEntry>`

Return a generator of all the node entries of a root node. Each entry is returned as a `[Node, Path]` tuple, with the path referring to the node's position inside the root node.

Options: `{from?: Path, to?: Path, reverse?: boolean, pass?: (node: NodeEntry => boolean)}`

#### `Node.parent(root: Node, path: Path) => Ancestor`

Get the parent of a node at a specific `path`.

### Text methods

Methods related to Text.

#### `Node.string(root: Node) => string`

Get the concatenated text string of a node's content. Note that this will not include spaces or line breaks between block nodes. This is not intended as a user-facing string, but as a string for performing offset-related computations for a node.

#### `Node.texts(root: Node, options?) => Generator<NodeEntry<Text>>`

Return a generator of all leaf text nodes in a root node.

Options: `{from?: Path, to?: Path, reverse?: boolean, pass?: (node: NodeEntry => boolean)}`

### Check methods

Methods used to check some attribute of a Node.

#### `Node.has(root: Node, path: Path) => boolean`

Check if a descendant node exists at a specific `path`.

#### `Node.isNode(value: any) => value is Node`

Check if a `value` implements the `Node` interface.

#### `Node.isNodeList(value: any) => value is Node[]`

Check if a `value` is a list of `Node` objects.

#### `Node.matches(root: Node, props: Partial<Node>) => boolean`

Check if a node matches a set of `props`.


# NodeEntry

`NodeEntry` objects are returned when iterating over the nodes in a Slate document tree. They consist of an array with two elements: the `Node` and its `Path` relative to the root node in the document.

They are generics meaning that sometimes they will return a subset of `Node` types like an `Element` or `Text`.

```typescript
type NodeEntry<T extends Node = Node> = [T, Path]
```


# Text

`Text` objects represent the nodes that contain the actual text content of a Slate document along with any formatting properties. They are always leaf nodes in the document tree as they cannot contain any children.

```typescript
interface Text {
  text: string
}
```

* [Static methods](#static-methods)
  * [Retrieval methods](#retrieval-methods)
  * [Check methods](#check-methods)

## Static methods

### Retrieval methods

#### `Text.matches(text: Text, props: Partial<Text>) => boolean`

Check if `text` matches a set of `props`.

The way the check works is that it makes sure that (a) all the `props` exist in the `text`, and (b) if it exists, that it exactly matches the properties in the `text`.

If a `props.text` property is passed in, it will be ignored.

If there are properties in `text` that are not in `props`, those will be ignored when it comes to testing for a match.

#### `Text.decorations(node: Text, decorations: DecoratedRange[]) => { leaf: Text; position?: LeafPosition }[]`

Get the leaves and positions for a text node, given `decorations`.

### Check methods

#### `Text.equals(text: Text, another: Text, options?) => boolean`

Check if two text nodes are equal.

Options: `{loose?: boolean}`

* `loose?`: When `true`, it checks if the properties of the `Text` object are equal except for the `text` property (i.e. the `String` value of the `Text`). When `false` (default), checks all properties including `text`.

#### `Text.isText(value: any) => value is Text`

Check if a `value` implements the `Text` interface.

#### `Text.isTextList(value: any): value is Text[]`

Check if `value` is an `Array` of only `Text` objects.


# Location Types

The `Location` interface is a union of the ways to refer to a specific location in a Slate document: paths, points or ranges. Methods will often accept a `Location` instead of requiring only a `Path`, `Point` or `Range`.

```typescript
type Location = Path | Point | Range
```

* [Location](https://docs.slatejs.org/api/locations/location)
* [Path](https://docs.slatejs.org/api/locations/path)
* [PathRef](https://docs.slatejs.org/api/locations/path-ref)
* [Point](https://docs.slatejs.org/api/locations/point)
* [PointEntry](https://docs.slatejs.org/api/locations/point-entry)
* [PointRef](https://docs.slatejs.org/api/locations/point-ref)
* [Range](https://docs.slatejs.org/api/locations/range)
* [RangeRef](https://docs.slatejs.org/api/locations/range-ref)
* [Span](https://docs.slatejs.org/api/locations/span)


# Location

The Location interface is a union of the ways to refer to a specific location in a Slate document: paths, points or ranges. Methods will often accept a Location instead of requiring only a Path, Point or Range.

```typescript
type Location = Path | Point | Range
```

* [Static methods](#static-methods)
  * [Check methods](#check-methods)

## Static methods

### Check methods

#### `Location.isLocation(value: any) => value is Location`

Check if a value implements the `Location` interface.


# Path

`Path` arrays are a list of indexes that describe a node's exact position in a Slate node tree. Although they are usually relative to the root `Editor` object, they can be relative to any `Node` object.

```typescript
type Path = number[]
```

* [Static methods](#static-methods)
  * [Retrieval methods](#retrieval-methods)
  * [Check methods](#check-methods)
  * [Transform method](#transform-method)

## Static methods

### Retrieval methods

#### `Path.ancestors(path: Path, options: { reverse?: boolean } = {}) => Path[]`

Get a list of ancestor paths for a given path.

The paths are sorted from shallowest to deepest ancestor. However, if the `reverse: true` option is passed, they are reversed.

#### `Path.common(path: Path, another: Path) => Path`

Get the common ancestor path of two paths.

#### `Path.compare(path: Path, another: Path) => -1 | 0 | 1`

Compare a path to another, returning an integer indicating whether the path was before, at, or after the other.

Note: Two paths of unequal length can still receive a `0` result if one is directly above or below the other. If you want exact matching, use \[\[Path.equals]] instead.

#### `Path.levels(path: Path, options?) => Path[]`

Get a list of paths at every level down to a path. Note: this is the same as `Path.ancestors`, but includes the path itself.

The paths are sorted from shallowest to deepest. However, if the `reverse: true` option is passed, they are reversed.

Options: `{reverse?: boolean}`

#### `Path.next(path: Path) => Path`

Given a path, gets the path to the next sibling node. The method does not ensure that the returned `Path` is valid in the document.

#### `Path.parent(path: Path) => Path`

Given a path, return a new path referring to the parent node above it. If the `path` argument is equal to `[]`, throws an error.

#### `Path.previous(path: Path) => Path`

Given a path, get the path to the previous sibling node. The method will throw an error if there are no previous siblings (e.g. if the Path is currently `[1, 0]`, the previous path would be `[1, -1]` which is illegal and will throw an error).

#### `Path.relative(path: Path, ancestor: Path) => Path`

Given two paths, one that is an ancestor to the other, returns the relative path from the `ancestor` argument to the `path` argument. If the `ancestor` path is not actually an ancestor or equal to the `path` argument, throws an error.

### Check methods

Check some attribute of a path. Always returns a boolean.

#### `Path.endsAfter(path: Path, another: Path) => boolean`

Check if a path ends after one of the indexes in another.

#### `Path.endsAt(path: Path, another: Path) => boolean`

Check if a path ends at one of the indexes in another.

#### `Path.endsBefore(path: Path, another: Path) => boolean`

Check if a path ends before one of the indexes in another.

#### `Path.equals(path: Path, another: Path) => boolean`

Check if a path is exactly equal to another.

#### `Path.hasPrevious(path: Path) => boolean`

Check if the path of previous sibling node exists

#### `Path.isAfter(path: Path, another: Path) => boolean`

Check if a path is after another.

#### `Path.isAncestor(path: Path, another: Path) => boolean`

Check if a path is an ancestor of another.

#### `Path.isBefore(path: Path, another: Path) => boolean`

Check if a path is before another.

#### `Path.isChild(path: Path, another: Path) => boolean`

Check if a path is a child of another.

#### `Path.isCommon(path: Path, another: Path) => boolean`

Check if a path is equal to or an ancestor of another.

#### `Path.isDescendant(path: Path, another: Path) => boolean`

Check if a path is a descendant of another.

#### `Path.isParent(path: Path, another: Path) => boolean`

Check if a path is the parent of another.

#### `Path.isPath(value: any) => value is Path`

Check is a value implements the `Path` interface.

#### `Path.isSibling(path: Path, another: Path) => boolean`

Check if a path is a sibling of another.

#### `Path.operationCanTransformPath(operation: Operation) => operation is InsertNodeOperation | RemoveNodeOperation | MergeNodeOperation | SplitNodeOperation | MoveNodeOperation`

Returns whether this operation can affect paths or not.

### Transform method

#### `Path.transform(path: Path, operation: Operation, options?) => Path | null`

Transform a path by an operation.

Options: `{ affinity?: 'forward' | 'backward' | null }`


# PathRef

`PathRef` objects keep a specific path in a document synced over time as new operations are applied to the editor. It is created using the `Editor.pathRef` method. You can access their property `current` at any time for the up-to-date `Path` value. When you no longer need to track this location, call `unref()` to free the resources. The `affinity` refers to the direction the `PathRef` will go when a user inserts content at the current position of the `Path`.

```typescript
interface PathRef {
  current: Path | null
  affinity: 'forward' | 'backward' | null
  unref(): Path | null
}
```

* [Instance methods](#instance-methods)
* [Static methods](#static-methods)
  * [Transform methods](#trasnform-methods)

## Instance methods

#### `unref() => Path | null`

Free the resources used by the PathRef. This should be called when you no longer need to track the path. Returns the final path value before being unrefed, or null if the path was already invalid.

## Static methods

### Transform methods

#### `PathRef.transform(ref: PathRef, op: Operation)`

Transform the path refs current value by an `op`. The editor calls this as needed, so normally you won't need to.


# Point

`Point` objects refer to a specific location in a text node in a Slate document. Its `path` refers to the location of the node in the tree, and its `offset` refers to distance into the node's string of text. Points may only refer to `Text` nodes.

```typescript
interface Point {
  path: Path
  offset: number
}
```

* [Static methods](#static-methods)
  * [Retrieval methods](#retrieval-methods)
  * [Check methods](#check-methods)
  * [Transform methods](#transform-methods)

## Static methods

### Retrieval methods

#### `Point.compare(point: Point, another: Point) => -1 | 0 | 1`

Compare a `point` to `another`, returning an integer indicating whether the point was before, at or after the other.

### Check methods

#### `Point.isAfter(point: Point, another: Point) => boolean`

Check if a `point` is after `another`.

#### `Point.isBefore(point: Point, another: Point) => boolean`

Check if a `point` is before `another`.

#### `Point.equals(point: Point, another: Point) => boolean`

Check if a `point` is exactly equal to `another`.

#### `Point.isPoint(value: any) => value is Point`

Check if a `value` implements the `Point` interface.

### Transform methods

#### `Point.transform(point: Point, op: Operation, options?) => Point | null`

Transform a `point` by an `op`.

Options: `{affinity?: 'forward' | 'backward' | null}`


# PointEntry

`PointEntry` objects are returned when iterating over `Point` objects that belong to a range.

```typescript
type PointEntry = [Point, 'anchor' | 'focus']
```


# PointRef

`PointRef` objects keep a specific point in a document synced over time as new operations are applied to the editor. It is created using the `Editor.pointRef` method. You can access their property `current` at any time for the up-to-date `Point` value. When you no longer need to track this location, call `unref()` to free the resources. The `affinity` refers to the direction the `PointRef` will go when a user inserts content at the current position of the `Point`.

```typescript
interface PointRef {
  current: Point | null
  affinity: 'forward' | 'backward' | null
  unref(): Point | null
}
```

* [Instance methods](#instance-methods)
* [Static methods](#static-methods)
  * [Transform methods](#trasnform-methods)

## Instance methods

#### `unref() => Point | null`

Call this when you no longer need to sync this point. It also returns the current value.

## Static methods

### Transform methods

#### `PointRef.transform(ref: PointRef, op: Operation)`

Transform the point refs current value by an `op`. The editor calls this as needed, so normally you won't need to.


# Range

`Range` objects are a set of points that refer to a specific span of a Slate document. They can define a span inside a single node or they can span across multiple nodes. The editor's `selection` is stored as a range.

```typescript
interface Range {
  anchor: Point
  focus: Point
}
```

* [Static methods](#static-methods)
  * [Retrieval methods](#retrieval-methods)
  * [Check methods](#check-methods)
  * [Transform methods](#transform-methods)

## Static methods

### Retrieval methods

#### `Range.edges(range: Range, options?) => [Point, Point]`

Get the start and end points of a `range`, in the order in which they appear in the document.

Options: `{reverse?: boolean}`

#### `Range.end(range: Range) => Point`

Get the end point of a `range` according to the order in which it appears in the document.

#### `Range.intersection(range: Range, another: Range) => Range | null`

Get the intersection of one `range` with `another`. If the two ranges do not overlap, return `null`.

#### `Range.points(range: Range) => Generator<PointEntry>`

Iterate through the two point entries in a `Range`. First it will yield a `PointEntry` representing the `anchor`, then it will yield a `PointEntry` representing the `focus`.

#### `Range.start(range: Range) => Point`

Get the start point of a `range` according to the order in which it appears in the document.

### Check methods

Check some attribute of a Range. Always returns a boolean.

#### `Range.equals(range: Range, another: Range) => boolean`

Check if a `range` is exactly equal to `another`.

#### `Range.includes(range: Range, target: Path | Point | Range) => boolean`

Check if a `range` includes a path, a point, or part of another range.

For clarity the definition of `includes` can mean partially includes. Another way to describe this is if one Range intersects the other Range.

#### `Range.surrounds(range: Range, target: Range) => boolean`

Check if a `range` includes another range.

#### `Range.isBackward(range: Range) => boolean`

Check if a `range` is backward, meaning that its anchor point appears *after* its focus point in the document.

#### `Range.isCollapsed(range: Range) => boolean`

Check if a `range` is collapsed, meaning that both its anchor and focus points refer to the exact same position in the document.

#### `Range.isExpanded(range: Range) => boolean`

Check if a `range` is expanded. This is the opposite of `Range.isCollapsed` and is provided for legibility.

#### `Range.isForward(range: Range) => boolean`

Check if a `range` is forward. This is the opposite of `Range.isBackward` and is provided for legibility.

#### `Range.isRange(value: any) => value is Range`

Check if a `value` implements the `Range` interface.

### Transform methods

#### `Range.transform(range: Range, op: Operation, options) => Range | null`

Transform a `range` by an `op`.

Options: `{affinity: 'forward' | 'backward' | 'outward' | 'inward' | null}`


# RangeRef

`RangeRef` objects keep a specific range in a document synced over time as new operations are applied to the editor. It is created using the `Editor.rangeRef` method. You can access their property `current` at any time for the up-to-date `Range` value. When you no longer need to track this location, call `unref()` to free the resources. The `affinity` refers to the direction the `RangeRef` will go when a user inserts content at the edges of the `Range`. `inward` means that the `Range` tends to stay the same size when content is inserted at its edges, and `outward` means that the `Range` tends to grow when content is inserted at its edges.

```typescript
interface RangeRef {
  current: Range | null
  affinity: 'forward' | 'backward' | 'outward' | 'inward' | null
  unref(): Range | null
}
```

For example:

```typescript
const selectionRef = Editor.rangeRef(editor, editor.selection, {
  affinity: 'inward',
})
// Allow the user to do stuff which might change the selection
Transforms.unwrapNodes(editor)
Transforms.select(editor, selectionRef.unref())
```

* [Instance methods](#instance-methods)
* [Static methods](#static-methods)
  * [Transform methods](#transform-methods)

## Instance methods

#### `unref() => Range | null`

Call this when you no longer need to sync this range. It also returns the current value.

## Static methods

### Transform methods

#### `RangeRef.transform(ref: RangeRef, op: Operation)`

Transform the range refs current value by an `op`. The editor calls this as needed, so normally you won't need to.


# Span

A `Span` is a low-level way to refer to a `Range` using `Element` as the end points instead of a `Point` which requires the use of leaf text nodes.

```typescript
type Span = [Path, Path]
```

* [Static methods](#static-methods)
  * [Check methods](#check-methods)

## Static Methods

### Check Methods

#### `Span.isSpan(value: any) => value is Span`

Check if a `value` implements the `Span` interface.


# Operation Types

`Operation` objects define the low-level instructions that Slate editors use to apply changes to their internal state. Representing all changes as operations is what allows Slate editors to easily implement history, collaboration, and other features.

* Operation object
  * [Operation](https://docs.slatejs.org/api/operations/operation)
* Operation subtypes
  * [Node Operations](#node-operations)
  * [Text Operations](#text-operations)
  * [Selection Operation](#selection-operation)
  * [Base Operation](#base-operation)

### Node Operations

Node operations operate on `Node` objects.

```typescript
// insert a new `Node`
type InsertNodeOperation = {
  type: 'insert_node'
  path: Path
  node: Node
}

// merge two `Node` objects
type MergeNodeOperation = {
  type: 'merge_node'
  path: Path
  position: number
  properties: Partial<Node>
}

// move `Node` from one path to another
type MoveNodeOperation = {
  type: 'move_node'
  path: Path
  newPath: Path
}

// Remove a `Node`
type RemoveNodeOperation = {
  type: 'remove_node'
  path: Path
  node: Node
}

// Set properties of a `Node`
type SetNodeOperation = {
  type: 'set_node'
  path: Path
  properties: Partial<Node>
  newProperties: Partial<Node>
}

// Split a node into two separate `Node` objects
type SplitNodeOperation = {
  type: 'split_node'
  path: Path
  position: number
  properties: Partial<Node>
}

export type NodeOperation =
  | InsertNodeOperation
  | MergeNodeOperation
  | MoveNodeOperation
  | RemoveNodeOperation
  | SetNodeOperation
  | SplitNodeOperation
```

### Text Operations

Text operations operate on `Text` objects only.

Note: `Text` objects are `Node` objects so you can use `Node` operations on `Text` objects.

```typescript
// insert text into an existing `Text` node
type InsertTextOperation = {
  type: 'insert_text'
  path: Path
  offset: number
  text: string
}

// remove text from an existing `Text` node
type RemoveTextOperation = {
  type: 'remove_text'
  path: Path
  offset: number
  text: string
}

export type TextOperation = InsertTextOperation | RemoveTextOperation
```

### Selection Operation

Operation to set or unset a selection `Range`.

```typescript
type SetSelectionOperation =
  | {
      type: 'set_selection'
      properties: null
      newProperties: Range
    }
  | {
      type: 'set_selection'
      properties: Partial<Range>
      newProperties: Partial<Range>
    }
  | {
      type: 'set_selection'
      properties: Range
      newProperties: null
    }

export type SelectionOperation = SetSelectionOperation
```

### Base Operation

The combination of all operation types.

```typescript
export type BaseOperation = NodeOperation | SelectionOperation | TextOperation
```


# Operation

`Operation` objects define the low-level instructions that Slate editors use to apply changes to their internal state. Representing all changes as operations is what allows Slate editors to easily implement history, collaboration, and other features.

* [Static methods](#static-methods)
  * [Manipulation methods](#manipulation-methods)
  * [Check methods](#check-methods)

## Static methods

### Manipulation methods

#### `Operation.inverse(op: Operation) => Operation`

Invert an operation, returning a new operation that will exactly undo the original when applied.

### Check methods

#### `Operation.isNodeOperation(value: any) => boolean`

Check if a value is a `NodeOperation` object. Returns the value as a `NodeOperation` if it is one.

#### `Operation.isOperation(value: any) => boolean`

Check if a value is an `Operation` object. Returns the value as an `Operation` if it is one.

#### `Operation.isOperationList(value: any) => boolean`

Check if a value is a list of `Operation` objects. Returns the value as an `Operation[]` if it is one.

#### `Operation.isSelectionOperation(value: any) => boolean`

Check if a value is a `SelectionOperation` object. Returns the value as a `SelectionOperation` if it is one.

#### `Operation.isTextOperation(value: any) => boolean`

Check if a value is a `TextOperation` object. Returns the value as a `TextOperation` if it is one.


# Scrubber

When Slate throws an exception, it includes a stringified representation of the relevant data. For example, if your application makes an API call to access the child of a text Node (an impossible operation), Slate will throw an exception like this:

```
Cannot get the child of a text node: {"text": "This is my text node."}
```

If your rich text editor can include sensitive customer data, you may want to scrub or obfuscate that text. To help with that, you can use the Scrubber API. Here's an example of recursively scrubbing the `'text'` fields of any entity that gets logged.

```typescript
import { Scrubber } from 'slate'

Scrubber.setScrubber((key, value) => {
  if (key === 'text') return '... scrubbed ...'
  return value
})
```

By setting the scrubber in this way, the error example given above will be printed as:

```
Cannot get the child of a text node: {"text": "... scrubbed ..."}
```

## Text Randomizer Example

Here's an example "textRandomizer" scrubber, which randomizes particular fields of Nodes, preserving their length, but replacing their contents with randomly chosen alphanumeric characters.

```typescript
import { Scrubber } from 'slate'

const textRandomizer = (fieldNames: string[]) => (key, value) => {
  if (fieldNames.includes(key)) {
    if (typeof value === 'string') {
      return value.split('').map(generateRandomCharacter).join('')
    } else {
      return '... scrubbed ...'
    }
  }

  return value
}

const generateRandomCharacter = (): string => {
  const chars =
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLKMNOPQRSTUVWXYZ1234567890'
  return chars.charAt(Math.floor(Math.random() * chars.length))
}

// randomize the 'text' and 'src' fields of any Node that is included in an
// exception thrown by Slate
Scrubber.setScrubber(Scrubber.textRandomizer(['text', 'src']))
```

In this example, a Node that looked like:

```json
{ "text": "My test input string", "count": 5 }
```

will be logged by Slate in an exception as (the random string will differ):

```json
{ "text": "rSIvEzKe39l6rqQSCfyv", "count": 5 }
```


# Slate React

This sub-library contains the React-specific logic for Slate.

* [withReact](https://docs.slatejs.org/libraries/slate-react/with-react)
* [ReactEditor](https://docs.slatejs.org/libraries/slate-react/react-editor)
* [Hooks](https://docs.slatejs.org/libraries/slate-react/hooks)
* [Slate Component](https://docs.slatejs.org/libraries/slate-react/slate)
* [Editable Component](https://docs.slatejs.org/libraries/slate-react/editable)
* [Event Handling](https://docs.slatejs.org/libraries/slate-react/event-handling)


# withReact

Adds React and DOM specific behaviors to the editor.

### `withReact<T extends Editor>(editor: T, clipboardFormatKey = 'x-slate-fragment'): T & ReactEditor`

When used with withHistory, withReact should be applied outside. For example:

```typescript
const [editor] = useState(() => withReact(withHistory(createEditor())))
```

**`clipboardFormatKey` option**

The `clipboardFormatKey` option allows you to customize the `DataTransfer` type when Slate data is copied to the clipboard. By default, it is `application/x-slate-fragment` but it can be customized using this option.

This can be useful when a user copies from one Slate editor to a differently configured Slate editor. This could cause nodes to be inserted which are not correctly typed for the receiving editor, corrupting the document. By customizing the `clipboardFormatKey` one can ensure that the raw JSON data isn't copied between editors with different schemas.


# ReactEditor

`ReactEditor` is added to `Editor` when it is instantiated using the `withReact` method.

```typescript
const [editor] = useState(() => withReact(withHistory(createEditor())))
```

* [Static methods](#static-methods)
  * [Check methods](#check-methods)
  * [Focus and selection methods](#focus-and-selection-methods)
  * [DOM translation methods](#dom-translation-methods)
  * [DataTransfer methods](#datatransfer-methods)

## Static methods

### Check methods

#### `ReactEditor.isComposing(editor: ReactEditor): boolean`

Check if the user is currently composing inside the editor.

#### `ReactEditor.isFocused(editor: ReactEditor): boolean`

Check if the editor is focused.

#### `ReactEditor.isReadOnly(editor: ReactEditor): boolean`

Check if the editor is in read-only mode.

### Focus and selection methods

#### `ReactEditor.blur(editor: ReactEditor): void`

Blur the editor.

#### `ReactEditor.focus(editor: ReactEditor): void`

Focus the editor.

#### `ReactEditor.deselect(editor: ReactEditor): void`

Deselect the editor.

### DOM translation methods

#### `ReactEditor.findKey(editor: ReactEditor, node: Node): Key`

Find a key for a Slate node.

Returns an instance of `Key` which looks like `{ id: string }`

#### `ReactEditor.findPath(editor: ReactEditor, node: Node): Path`

Find the path of Slate node.

#### `ReactEditor.hasDOMNode(editor: ReactEditor, target: DOMNode, options: { editable?: boolean } = {}): boolean`

Check if a DOM node is within the editor.

#### `ReactEditor.toDOMNode(editor: ReactEditor, node: Node): HTMLElement`

Find the native DOM element from a Slate node.

#### `ReactEditor.toDOMPoint(editor: ReactEditor, point: Point): DOMPoint`

Find a native DOM selection point from a Slate point.

#### `ReactEditor.toDOMRange(editor: ReactEditor, range: Range): DOMRange`

Find a native DOM range from a Slate `range`.

#### `ReactEditor.toSlateNode(editor: ReactEditor, domNode: DOMNode): Node`

Find a Slate node from a native DOM `element`.

#### `ReactEditor.findEventRange(editor: ReactEditor, event: any): Range`

Get the target range from a DOM `event`.

#### `ReactEditor.toSlatePoint(editor: ReactEditor, domPoint: DOMPoint): Point | null`

Find a Slate point from a DOM selection's `domNode` and `domOffset`.

#### `ReactEditor.toSlateRange(editor: ReactEditor, domRange: DOMRange | DOMStaticRange | DOMSelection, options?: { exactMatch?: boolean } = {}): Range | null`

Find a Slate range from a DOM range or selection.

### DataTransfer methods

#### `ReactEditor.insertData(editor: ReactEditor, data: DataTransfer): void`

Insert data from a `DataTransfer` into the editor. This is a proxy method to call in this order `insertFragmentData(editor: ReactEditor, data: DataTransfer)` and then `insertTextData(editor: ReactEditor, data: DataTransfer)`.

#### `ReactEditor.insertFragmentData(editor: ReactEditor, data: DataTransfer): true`

Insert fragment data from a `DataTransfer` into the editor. Returns true if some content has been effectively inserted.

#### `ReactEditor.insertTextData(editor: ReactEditor, data: DataTransfer): true`

Insert text data from a `DataTransfer` into the editor. Returns true if some content has been effectively inserted.

#### `ReactEditor.setFragmentData(editor: ReactEditor, data: DataTransfer, originEvent?: 'drag' | 'copy' | 'cut'): void`

Sets data from the currently selected fragment on a `DataTransfer`.


# Hooks

#### `useComposing(): boolean`

Get the current `composing` state of the editor. It deals with `compositionstart`, `compositionupdate`, `compositionend` events.

Composition events are triggered by typing (composing) with a language that uses a composition character (e.g. Chinese, Japanese, Korean, etc.) [example](https://en.wikipedia.org/wiki/Input_method#/media/File:Typing_%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4_in_Dubeolsik_keyboard_layout.gif).

#### `useElement(): Element`

Get the current element object. Re-renders whenever the element or any of its descendants changes.

#### `useElementIf(): Element | null`

The same as `useElement()` but returns `null` instead of throwing an error when not inside an element.

#### `useFocused(): boolean`

Get the current `focused` state of the editor.

#### `useReadOnly(): boolean`

Get the current `readOnly` state of the editor.

#### `useSelected(): boolean`

Get the current `selected` state of an element. An element is selected if `editor.selection` exists and overlaps any part of the element.

#### `useSlate(): Editor`

Get the current editor object. Re-renders whenever changes occur in the editor.

#### `useSlateStatic(): Editor`

Get the current editor object from the React context. A version of useSlate that does not re-render the context. Previously called `useEditor`.

#### `useSlateSelection(): (BaseRange & { placeholder?: string | undefined; onPlaceholderResize?: ((node: HTMLElement | null) => void) | undefined }) | null`

Get the current editor selection. Only re-renders when the selection changes.

#### `useSlateSelector<T>(selector: (editor: Editor) => T, equalityFn?: (a: T, b: T) => boolean): T`

Use redux style selectors to prevent re-rendering on every keystroke.

Bear in mind re-rendering can only prevented if the returned value is a value type or for reference types (e.g. objects and arrays) add a custom equality function.

If `selector` is memoized using `useCallback`, then it will only be called when it or the editor state changes. Otherwise, `selector` will be called every time the component renders.

Example:

```typescript
const isSelectionActive = useSlateSelector(editor => Boolean(editor.selection))
```


# Slate Component

## `Slate(props: SlateProps): React.JSX.Element`

The `Slate` component must include somewhere in its `children` the `Editable` component.

### Props

```typescript
type SlateProps = {
  editor: ReactEditor
  value: Descendant[]
  children: React.ReactNode
  onChange?: (value: Descendant[]) => void
  onSelectionChange?: (selection: Selection) => void
  onValueChange?: (value: Descendant[]) => void
}
```

#### `props.editor: ReactEditor`

An instance of `ReactEditor`

#### `props.value: Descendant[]`

The initial value of the Editor.

This prop is deceptively named.

Slate once was a controlled component (i.e. it's contents were strictly controlled by the `value` prop) but due to features like its edit history which would be corrupted by direct editing of the `value` it is no longer a controlled component.

#### `props.children: React.ReactNode`

The `children` which must contain an `Editable` component.

#### `props.onChange: (value: Descendant[]) => void`

An optional callback function which you can use to be notified of changes in the editor's value.

#### `props.onValueChange?: (value: Descendant[]) => void`

`props.onChange` alias.

#### `props.onSelectionChange?: (selection: Selection) => void`

An optional callback function which you can use to be notified of changes of the editor's selection.


# Editable Component

## `Editable(props: EditableProps): React.JSX.Element`

The `Editable` component is the main editing component. Note that it must be inside a `Slate` component.

### Props

It takes as its props, any props accepted by a Textarea element plus the following props.

```typescript
type EditableProps = {
  decorate?: (entry: NodeEntry) => Range[]
  onDOMBeforeInput?: (event: InputEvent) => void
  placeholder?: string
  readOnly?: boolean
  role?: string
  style?: React.CSSProperties
  renderElement?: (props: RenderElementProps) => React.JSX.Element
  renderLeaf?: (props: RenderLeafProps) => React.JSX.Element
  renderPlaceholder?: (props: RenderPlaceholderProps) => React.JSX.Element
  scrollSelectionIntoView?: (editor: ReactEditor, domRange: DOMRange) => void
  as?: React.ElementType
  disableDefaultStyles?: boolean
} & React.TextareaHTMLAttributes<HTMLDivElement>
```

*NOTE: Detailed breakdown of Props not completed. Refer to the* [*source code*](https://github.com/ianstormtaylor/slate/blob/main/packages/slate-react/src/components/editable.tsx) *at the moment. Under construction.*

#### `placeholder?: string = ""`

The text to display as a placeholder when the Editor is empty. A typical value for `placeholder` would be "Enter text here..." or "Start typing...". The placeholder text will not be treated as an actual value and will disappear when the user starts typing in the Editor.

#### `readOnly?: boolean = false`

When set to true, renders the editor in a "read-only" state. In this state, user input and interactions will not modify the editor's content.

If this prop is omitted or set to false, the editor remains in the default "editable" state, allowing users to interact with and modify the content.

This prop is particularly useful when you want to display text or rich media content without allowing users to edit it, such as when displaying published content or a preview of the user's input.

#### `renderElement?: (props: RenderElementProps) => React.JSX.Element`

The `renderElement` prop is a function used to render a custom component for a specific type of Element node in the Slate.js document model.

Here is the type of the `RenderElementProps` passed into the function.

```typescript
export interface RenderElementProps {
  children: any
  element: Element
  attributes: {
    'data-slate-node': 'element'
    'data-slate-inline'?: true
    'data-slate-void'?: true
    dir?: 'rtl'
    ref: any
  }
}
```

The `attributes` must be added to the props of the top level HTML element returned from the function and the `children` must be rendered somewhere inside the returned JSX.

Here is a typical usage of `renderElement` with two types of elements.

```javascript
const initialValue = [
  {
    type: 'paragraph',
    children: [{ text: 'A line of text in a paragraph.' }],
  },
]

const App = () => {
  const [editor] = useState(() => withReact(createEditor()))

  // Define a rendering function based on the element passed to `props`. We use
  // `useCallback` here to memoize the function for subsequent renders.
  const renderElement = useCallback(props => {
    switch (props.element.type) {
      case 'code':
        return <CodeElement {...props} />
      default:
        return <DefaultElement {...props} />
    }
  }, [])

  return (
    <Slate editor={editor} initialValue={initialValue}>
      <Editable
        // Pass in the `renderElement` function.
        renderElement={renderElement}
      />
    </Slate>
  )
}

const CodeElement = props => {
  return (
    <pre {...props.attributes}>
      <code>{props.children}</code>
    </pre>
  )
}

const DefaultElement = props => {
  return <p {...props.attributes}>{props.children}</p>
}
```

#### `renderLeaf?: (props: RenderLeafProps) => React.JSX.Element`

The `renderLeaf` prop allows you to customize the rendering of leaf nodes in the document tree of your Slate editor. A "leaf" in Slate is the smallest chunk of text and its associated formatting attributes.

The `renderLeaf` function receives an object of type `RenderLeafProps` as its argument:

```typescript
export interface RenderLeafProps {
  children: any
  leaf: Text
  text: Text
  attributes: {
    'data-slate-leaf': true
  }
  /**
   * The position of the leaf within the Text node, only present when the text node is split by decorations.
   */
  leafPosition?: {
    start: number
    end: number
    isFirst?: true
    isLast?: true
  }
}
```

Example usage:

```typescript
<Editor
  renderLeaf={({ attributes, children, leaf }) => {
    return (
      <span
        {...attributes}
        style={{ fontWeight: leaf.bold ? 'bold' : 'normal' }}
      >
        {children}
      </span>
    )
  }}
/>
```

#### `renderText?: (props: RenderTextProps) => React.JSX.Element`

The `renderText` prop allows you to customize the rendering of the container element for a Text node in the Slate editor. This is useful when you need to wrap the entire text node content or add elements associated with the text node as a whole, regardless of how decorations might split the text into multiple leaves.

The `renderText` function receives an object of type `RenderTextProps` as its argument:

```typescript
export interface RenderTextProps {
  text: Text
  children: any
  attributes: {
    'data-slate-node': 'text'
    ref: any
  }
}
```

Example usage:

```jsx
<Editable
  renderText={({ attributes, children, text }) => {
    return (
      <span {...attributes} className="custom-text">
        {children}
        {text.tooltipContent && <Tooltip content={text.tooltipContent} />}
      </span>
    )
  }}
/>
```

#### `renderPlaceholder?: (props: RenderPlaceholderProps) => React.JSX.Element`

The `renderPlaceholder` prop allows you to customize how the placeholder of the Slate.js `Editable` component is rendered when the editor is empty. The placeholder will only be shown when the editor's content is empty.

The `RenderPlaceholderProps` interface looks like this:

```typescript
export type RenderPlaceholderProps = {
  children: any
  attributes: {
    'data-slate-placeholder': boolean
    dir?: 'rtl'
    contentEditable: boolean
    ref: React.RefCallback<any>
    style: React.CSSProperties
  }
}
```

An example usage might look like:

```jsx
<Editable
  renderPlaceholder={({ attributes, children }) => (
    <div {...attributes} style={{ fontStyle: 'italic', color: 'gray' }}>
      {children}
    </div>
  )}
/>
```

#### `scrollSelectionIntoView?: (editor: ReactEditor, domRange: DOMRange) => void`

Slate has its own default method to scroll a DOM selection into view that works for most cases; however, if the default behavior isn't working for you, possible due to some complex styling, you may need to override the default behavior by providing a different function here.

#### `as?: React.ElementType = "div"`

The as prop specifies the type of element that will be used to render the Editable component in your React application. By default, this is a `div`.

#### `disableDefaultStyles?: boolean = false`

The `disableDefaultStyles` prop determines whether the default styles of the Slate.js `Editable` component are applied or not.

Please note that with this prop set to `true`, you will need to ensure that your styles cater to all the functionalities of the editor that rely on specific styles to work properly.

Here are the default styles:

```typescript
const defaultStyles = {
  // Allow positioning relative to the editable element.
  position: 'relative',
  // Preserve adjacent whitespace and new lines.
  whiteSpace: 'pre-wrap',
  // Allow words to break if they are too long.
  wordWrap: 'break-word',
  // Make the minimum height that of the placeholder.
  ...(placeholderHeight ? { minHeight: placeholderHeight } : {}),
}
```


# Event Handling

By default, the `Editable` component comes with a set of event handlers that handle typical rich-text editing behaviors (for example, it implements its own `onCopy`, `onPaste`, `onDrop`, and `onKeyDown` handlers).

In some cases you may want to extend or override Slate's default behavior, which can be done by passing your own event handler(s) to the `Editable` component.

Your custom event handler can control whether or not Slate should execute its own event handling for a given event after your handler runs depending on the return value of your event handler as described below.

```jsx
import {Editable} from 'slate-react';

function MyEditor() {
  const onClick = event => {
    // Implement custom event logic...

    // When no value is returned, Slate will execute its own event handler when
    // neither isDefaultPrevented nor isPropagationStopped was set on the event
  };

  const onDrop = event => {
    // Implement custom event logic...

    // No matter the state of the event, treat it as being handled by returning
    // true here, Slate will skip its own event handler
    return true;
  };

  const onDragStart = event => {
    // Implement custom event logic...

    // No matter the status of the event, treat event as *not* being handled by
    // returning false, Slate will execute its own event handler afterward
    return false;
  };

  return (
    <Editable
      onClick={onClick}
      onDrop={onDrop}
      onDragStart={onDragStart}
      {/*...*/}
    />
  )
}
```


# Slate History

This sub-library tracks changes to the Slate value state over time, and enables undo and redo functionality.

* [withHistory](https://docs.slatejs.org/libraries/slate-history/with-history)
* [HistoryEditor](https://docs.slatejs.org/libraries/slate-history/history-editor)
* [History](https://docs.slatejs.org/libraries/slate-history/history)


# withHistory

The `withHistory` plugin adds the `HistoryEditor` to an `Editor` instance and keeps track of the operation history of a Slate editor as operations are applied to it, using undo and redo stacks.

#### `withHistory<T extends Editor>(editor: T): T & HistoryEditor`

Add `HistoryEditor` interface to an instance of any `Editor`.

When used with `withReact`, `withHistory` should be applied inside. For example:

```javascript
const [editor] = useState(() => withReact(withHistory(createEditor())))
```


# HistoryEditor

The `HistoryEditor` interface is added to the `Editor` when it is instantiated using the `withHistory` method.

```typescript
const [editor] = useState(() => withReact(withHistory(createEditor())))
```

This adds properties to `editor` that enables undo and redo in Slate.

There are also static methods for working with the Editor's undo/redo history.

```typescript
export interface HistoryEditor extends BaseEditor {
  history: History
  undo: () => void
  redo: () => void
  writeHistory: (stack: 'undos' | 'redos', batch: any) => void
}
```

* [Static methods](#static-methods)
  * [Undo and Redo](#undo-and-redo)
  * [Merging and Saving](#merging-and-saving)
  * [Check methods](#check-methods)
* [Instance methods](#instance-methods)

## Static methods

### Undo and Redo

#### `HistoryEditor.redo(editor: HistoryEditor): void`

Redo to the next saved state.

#### `HistoryEditor.undo(editor: HistoryEditor): void`

Undo to the previous saved state.

### Merging and Saving

#### `HistoryEditor.withMerging(editor: HistoryEditor, fn: () => void): void`

Apply a series of changes inside a synchronous `fn`, These operations will be merged into the previous history.

#### `HistoryEditor.withNewBatch(editor: HistoryEditor, fn: () => void): void`

Apply a series of changes inside a synchronous `fn`, ensuring that the first operation starts a new batch in the history. Subsequent operations will be merged as usual.

#### `HistoryEditor.withoutMerging(editor: HistoryEditor, fn: () => void): void`

Apply a series of changes inside a synchronous `fn`, without merging any of the new operations into previous save point in the history.

#### `HistoryEditor.withoutSaving(editor: HistoryEditor, fn: () => void): void`

Apply a series of changes inside a synchronous `fn`, without saving any of their operations into the history.

### Check methods

#### `HistoryEditor.isHistoryEditor(value: any): value is HistoryEditor`

Check if a value is a `HistoryEditor` (i.e. it has the `HistoryEditor` interface).

#### `HistoryEditor.isMerging(editor: HistoryEditor): boolean | undefined`

Get the merge flag's current value.

#### `HistoryEditor.isSaving(editor: HistoryEditor): boolean | undefined`

Get the saving flag's current value.

## Instance methods

#### `undo(): void`

Undo the last batch of operations

#### `redo(): void`

Redo the last undone batch of operations

#### `writeHistory(stack: 'undos'| 'redos', batch: any) => void`

Push a batch of operations as either `undos` or `redos` onto `editor.undos` or `editor.redos`


# History

The `History` object contains the undo and redo history for the editor.

It can be accessed from an `Editor` instance as the property `history`.

This property is only available on the `Editor` if the editor was instantiated using the `withHistory` method which adds undo/redo functionality to the Slate editor.

```typescript
export interface History {
  redos: Batch[]
  undos: Batch[]
}

interface Batch {
  operations: Operation[]
  selectionBefore: Range | null
}
```

* [Static Methods](#static-methods)

## Static Methods

#### `History.isHistory(value: any): value is History`

Returns `true` if the passed in `value` is a `History` object and also acts as a type guard for `History`.


# Slate Hyperscript

This package contains a hyperscript helper for creating Slate documents with JSX!




---

[Next Page](/llms-full.txt/1)


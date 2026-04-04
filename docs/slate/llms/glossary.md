# Source: https://docs.slatejs.org/v0.47/general/glossary.md

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

A `match`, is an object with possible fields of `type` and `object` that are used to *match* `Nodes` when defining rules in a [Schema](https://docs.slatejs.org/v0.47/slate-core/schema). An example of `match` could be `{type: 'paragraph'}`, `{objet: 'inline', type: '@-tag'}`, etc.

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

A Slate *"schema"* is a JavaScript object with properties that describe the document, block nodes, and inline nodes in your editor. Every Slate editor has a "schema" associated with it, which contains information about the structure of its content. For the most basic cases, you'll just rely on Slate's default core schema. But for advanced use cases, you can enforce rules about what the content of a Slate document can contain. Read [Schema reference](https://docs.slatejs.org/v0.47/slate-core/schema) to learn more.

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

A Slate *"value"* is the top-level object in Slate and is an object encapsulating the entire value of a Slate editor. Read the [Data Model guide](https://docs.slatejs.org/v0.47/guides/data-model#the-value) to learn more.

## Wrap

To *"wrap"* is to surround a piece of text or a node in another node. For example, if you select the text `Google` and want to turn it into a link, you'd "wrap" it with an inline link node.

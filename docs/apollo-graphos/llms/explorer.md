# Source: https://www.apollographql.com/docs/graphos/platform/explorer.md

# GraphOS Studio Explorer

The GraphOS Studio Explorer is a powerful web IDE for creating, running, and managing GraphQL operations.

The Explorer is free for all GraphOS organizations. It supports all GraphQL operation types (`Query`, `Mutation`, and [`Subscription`](https://www.apollographql.com/docs/graphos/platform/explorer/subscription-support/)).

The Explorer is also available in a [sandbox mode](https://www.apollographql.com/docs/apollo-sandbox/) that doesn't require an Apollo account.

## Setup

To get started with the Explorer, [create a graph](https://www.apollographql.com/docs/graphos/get-started/guides/graphql#create-supergraph) in GraphOS Studio and then navigate to that graph's **Explorer** page from the left navigation.

## Building a query

Here's an example [embedded Explorer](https://www.apollographql.com/docs/graphos/platform/explorer/embed/) you can use to try out the query-building features described below!

### The operation editor

The Explorer's operation editor is built on [Monaco](https://microsoft.github.io/monaco-editor/). It provides common features of query-building tools, including:

* Panels for specifying headers, variables, and environment variables
* Persistence across sessions
* Keyboard shortcuts (click the keyboard icon in the bottom-right corner of the operation editor to view all available shortcuts)

The editor also provides full IntelliSense support for GraphQL, including:

* Query linting
* Autocomplete
* Peek definitions on mouse hover
* Jump-to-definition with command-click

The editor can manage multiple operations and reason about those operations individually. As you work, the editor shifts focus to whichever operation you click into. Each operation has its own context menu (`•••`) that enables you to format it, copy a link to share, or generate a `curl` command.

### The Documentation tab

The Explorer's Documentation tab enables you to step into your schema, beginning at one of its entry points. As you step into a field and its subfields, the Explorer keeps track of your current path within the schema.

You can click the **⊕** button next to any field in the Documentation tab to add that field to the operation editor, at your current path. By default, the Explorer automatically generates variables for that field's arguments.

## Searching your schema

The Explorer provides a two-step schema search (shortcut `⌘+K`):

1. Find the schema field you're looking for
2. Find the ideal path to that field from your schema's entry points

### 1. Find a field

First, you search for a field by its name, for example, `email`. The interface helps you differentiate between fields with the same name, for example, `User.email` versus `Organization.email`. The search is "fuzzy," so it works even if you don't know a field's exact spelling.

If you know exactly which type and which field you're looking for, you can separate those values with a period, for example, `User.email`.

### 2. Find a path to the field

After you identify a type-field pair, the Explorer lists all the paths to that field that start at your schema's entry points (`Query`, `Mutation` and `Subscription`). These paths are ordered by depth.

Finding the path to a field is particularly important with GraphQL, because you can only query a field if that field's position within your query is valid.

After you select which path you want, the Explorer opens that path in its Documentation tab. You can then click the **⊕** button to add that path to your query.

## Additional features

The Explorer also provides:

* [Sandbox support](https://www.apollographql.com/docs/apollo-sandbox/) that doesn't require an Apollo account
* Multiple methods for [authenticating](https://www.apollographql.com/docs/graphos/platform/explorer/connect) with your GraphQL server
* [Operation collections](https://www.apollographql.com/docs/graphos/platform/explorer/operation-collections) for sharing common operations with other team members
* The ability to [embed the Explorer](https://www.apollographql.com/docs/graphos/platform/explorer/embed) on your own website
* [Display options, federation support, and more](https://www.apollographql.com/docs/graphos/platform/explorer/additional-features)

## What data does GraphOS log about operations executed in the Explorer?

Only frontend usage metrics for improving the product. Explorer enables you to build and execute operations against your graph, and these operations are sent directly from your browser and do not pass through Apollo's systems.

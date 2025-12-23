# Source: https://reactflow.dev/api-reference

# API Reference 

This reference attempts to document every function, hook, component, and type exported by React Flow. If you are looking for guides and tutorials, please refer to our [learn section](/learn).

## How to use this reference[](#how-to-use-this-reference) 

We think that documentation should answer two broad questions: "what is this thing?" and "how do I use it?"

To that end, our API reference aims to **concisely** answer that first question and learn section goes into more detail on the second. If you find yourself clicking around the reference wondering what the heck any of this means, maybe we have a guide that can help you out!

[](/learn/customization/custom-nodes)

Custom nodes

A powerful feature of React Flow is the ability to add custom nodes. Within your custom nodes you can render everything you want. You can define multiple source and target handles and render form inputs or charts for example. In this guide we will implement a node with an input field that updates some text in another part of the application.

Read more ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0iaW5saW5lIHctNCBoLTQiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTEyIDIuMjVjLTUuMzg1IDAtOS43NSA0LjM2NS05Ljc1IDkuNzVzNC4zNjUgOS43NSA5Ljc1IDkuNzUgOS43NS00LjM2NSA5Ljc1LTkuNzVTMTcuMzg1IDIuMjUgMTIgMi4yNVptNC4yOCAxMC4yOGEuNzUuNzUgMCAwIDAgMC0xLjA2bC0zLTNhLjc1Ljc1IDAgMSAwLTEuMDYgMS4wNmwxLjcyIDEuNzJIOC4yNWEuNzUuNzUgMCAwIDAgMCAxLjVoNS42OWwtMS43MiAxLjcyYS43NS43NSAwIDEgMCAxLjA2IDEuMDZsMy0zWiIgY2xpcC1ydWxlPSJldmVub2RkIiAvPjwvc3ZnPg==)

[](/learn/layouting/layouting)

Layouting

We regularly get asked how to handle layouting in React Flow. While we could build some basic layouting into React Flow, we believe that you know your app\'s requirements best and with so many options out there we think it\'s better you choose the best right tool for the job. In this guide we\'ll look at four layouting libraries and how to use them.

Read more ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBhcmlhLWhpZGRlbj0idHJ1ZSIgZGF0YS1zbG90PSJpY29uIiBjbGFzcz0iaW5saW5lIHctNCBoLTQiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTEyIDIuMjVjLTUuMzg1IDAtOS43NSA0LjM2NS05Ljc1IDkuNzVzNC4zNjUgOS43NSA5Ljc1IDkuNzUgOS43NS00LjM2NSA5Ljc1LTkuNzVTMTcuMzg1IDIuMjUgMTIgMi4yNVptNC4yOCAxMC4yOGEuNzUuNzUgMCAwIDAgMC0xLjA2bC0zLTNhLjc1Ljc1IDAgMSAwLTEuMDYgMS4wNmwxLjcyIDEuNzJIOC4yNWEuNzUuNzUgMCAwIDAgMCAxLjVoNS42OWwtMS43MiAxLjcyYS43NS43NSAwIDEgMCAxLjA2IDEuMDZsMy0zWiIgY2xpcC1ydWxlPSJldmVub2RkIiAvPjwvc3ZnPg==)

## A note for our long-term users[](#a-note-for-our-long-term-users) 

If you're coming here from our old API pages things might look a bit different! We've reorganized our documentation to make it easier to look things up if you know what you're looking for. All our types, components, hooks, and util functions get their own page now to help you find exactly what you need.

If you're new to React Flow or you're not sure where to look for something, take a look at the section below.

## A note for JavaScript users[](#a-note-for-javascript-users) 

React Flow is written in TypeScript, but we know that not everyone uses it. We encourage developers to use the technology that works best for them, and throughout our documentation there is a blend of TypeScript and JavaScript examples.

For our API reference, however, we use TypeScript's syntax to document the types of props and functions. Here's a quick crash course on how to read it:

• `?` means that the field or argument is optional.

• `<T>` in a type definition represents a generic type parameter. Like a function argument but for types! The definition `type Array<T> = ...` means a type called `Array` that takes a generic type parameter `T`.

• `<T>` when referring to a type is like "filling in" a generic type parameter. It's like calling a function but for types! The type `Array<number>` is the type `Array` with the generic type parameter `T` filled in with the type `number`.

• `T | U` means that the type is either `T` or `U`: this is often called a *union*.

• `T & U` means that the type is both `T` and `U`: this is often called an *intersection*.

The TypeScript folks have their own [handy guide for reading types ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html) that you might find useful. If you're still stuck on something, feel free to drop by our [Discord ![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBzdHJva2Utd2lkdGg9IjEuNyIgdmlld2JveD0iMCAwIDI0IDI0IiBoZWlnaHQ9IjFlbSIgY2xhc3M9Ing6aW5saW5lIHg6YWxpZ24tYmFzZWxpbmUgeDpzaHJpbmstMCI+PHBhdGggZD0iTTcgMTdMMTcgNyIgLz48cGF0aCBkPSJNNyA3aDEwdjEwIiAvPjwvc3ZnPg==)](https://discord.com/invite/RVmnytFmGW) and ask for help!
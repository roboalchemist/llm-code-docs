# Rescript React Documentation

Source: https://rescript-lang.org/docs/react/latest/llms-full.txt

---

# The ReScript Programming Language

```markdown
# The ReScript Programming Language

## Fast, Simple, Fully Typed JavaScript from the Future

ReScript is a robustly typed language that compiles to efficient and human-readable JavaScript. It comes with a lightning fast compiler toolchain that scales to any codebase size.

[Get started](/docs/manual/installation)

## Write in ReScript

```rescript
module Button = {
  @react.component
  let make = (~count) => {
    let times = switch count {
    | 1 => "once"
    | 2 => "twice"
    | n => n->Int.toString ++ " times"
    }
    let text = `Click me ${times}`
    
    <button> {text->React.string} </button>
  }
}
```

## Compile to JavaScript

```js
import * as JsxRuntime from "react/jsx-runtime";

function Playground$Button(props) {
  var count = props.count;
  var times = count !== 1 ? (
    count !== 2 ? count.toString() + " times" : "twice"
  ) : "once";
  var text = "Click me " + times;
  return JsxRuntime.jsx("button", {
    children: text
  });
}

var Button = {
  make: Playground$Button
};

export {
  Button,
}
```

[Edit this example in Playground](/try?code=module%20Button%20%3D%20%7B%0A%20%20%40react.component%0A%20%20let%20make%20%3D%20(~count)%20%3D%3E%20%7B%0A%20%20%20%20let%20times%20%3D%20switch%20count%20%7B%0A%20%20%20%20%7C%201%20%3D%3E%20%22once%22%0A%20%20%20%20%7C%202%20%3D%3E%20%22twice%22%0A%20%20%20%20%7C%20n%20%3D%3E%20n-%3EInt.toString%20%2B%2B%20%22%20times%22%0A%20%20%20%20%7D%0A%20%20%20%20let%20text%20%3D%20%60Click%20me%20%24%7Btimes%7D%60%0A%0A%20%20%20%20%3Cbutton%3E%20%7Btext-%3EReact.string%7D%20%3C%2Fbutton%3E%0A%20%20%7D%0A%7D)

## Leverage the full power of JavaScript in a robustly typed language without the fear of `any` types.

### ReScript is used to ship and maintain mission-critical products with good UI and UX.

## Quick Install

You can quickly add ReScript to your existing JavaScript codebase via npm / yarn:

```bash
npm install rescript
```

Or generate a new project from the official template with npx:

```bash
npx create-rescript-app
```

## Fast and simple

### The fastest build system on the web

ReScript cares about a consistent and fast feedback loop for any codebase size. Refactor code, pull complex changes, or switch to feature branches as you please. No sluggish CI builds, stale caches, wrong type hints, or memory hungry language servers that slow you down.

## A robust type system

### Type Better

Every ReScript app is fully typed and provides reliable type information for any given value in your program. We prioritize simpler types over complex types for the sake of clarity and easy debugability. No `any`, no magic types, no surprise `undefined`.

## Seamless Integration

### The familiar JS ecosystem at your fingertips

Use any library from JavaScript, export ReScript libraries to JavaScript, automatically generate TypeScript types. It's like you've never left the good parts of JavaScript at all.

## A community of programmers who value getting things done

No language can be popular without a solid community. A great type system isn't useful if library authors abuse it. Performance doesn't show if all the libraries are slow. Join the ReScript community — A group of companies and individuals who deeply care about simplicity, speed and practicality.

[Join our Forum](https://forum.rescript-lang.org)

## Tooling that just works out of the box

A builtin pretty printer, memory friendly VSCode & Vim plugins, a stable type system and compiler that doesn't require lots of extra configuration. ReScript brings all the tools you need to build reliable JavaScript, Node and ReactJS applications.

## Easy to adopt — without any lock-in

ReScript was made with gradual adopt
```
```
```
# Source: https://docs.flux.ai/reference/typescript.md

# TypeScript

The models can always be written in JavaScript. After all, models run in the browser, and browsers only support JavaScript.

You're free to use plain JavaScript, or any of the languages that can be translated into JavaScript. However, to build a quality model that won't crash in unexpected situations, we **strongly** recommend the use of TypeScript.

## What is TypeScript?

TypeScript is **not a new language**. It is an extension of the JavaScript language. You can write JavaScript code, paste it into a TypeScript file. Congratulations, you've just written TypeScript!

TypeScript allows you to add _type annotations_ to your code. These don't change how your code runs, they are just notes for yourself and for the compiler

```typescript
// The ': string[]' is an annotation 
let list: string[] = [] 
for (const node of flux.properties) { 
  list.push(node.type)``
}

// The ': number' are also annotations 
function doThing(x: number, str: string) { 
  // ... 
}
```



Paired with our built in IDE, the editor is smart about knowing what variable has which properties, _while you are typing_!

These type annotations are more than just comments with a new syntax. The TypeScript compiler can use them to detect accidental errors.

```typescript
let list: string[] = []
for (const node of flux.properties) { 
  // Error! Type SceneNode is not assignable to type 'string' list.push(node) 
}
```



Having the compiler tell you about errors generally allows you to develop faster. It's much easier to catch and fix errors when the compiler tells you exactly what line is wrong, whereas having to test the plugin to find bugs (or worse, having your _users_ test the plugin) is much more expensive. TypeScript doesn't prevent all bugs from happening of course, but it does eliminate a large class of them.
# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/type-aliases/opdecorator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# OpDecorator

> TypeScript SDK reference

# OpDecorator

Ƭ **OpDecorator**\<`T`>: (`value`: `T`, `context`: `ClassMethodDecoratorContext`) => `T` | `void` & (`target`: `Object`, `propertyKey`: `string` | `symbol`, `descriptor`: `TypedPropertyDescriptor`\<`T`>) => `TypedPropertyDescriptor`\<`T`> | `void`

Helper type for decorators
This represents a decorator function that can be used with both legacy and Stage 3 decorators.

For Stage 3 decorators:
target: The function being decorated (T)
context: MethodDecoratorContext

For legacy decorators:
target: The prototype (instance methods) or constructor (static methods)
propertyKey: The method name
descriptor: The property descriptor containing the method

#### Type parameters

| Name | Type                                   |
| :--- | :------------------------------------- |
| `T`  | extends (...`args`: `any`\[]) => `any` |

#### Defined in

[opType.ts:41](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/opType.ts#L41)

## Functions

# Source: https://rolldown.rs/reference/Class.Visitor.md

---
url: /reference/Class.Visitor.md
---
# Class: Visitor

Visitor class for traversing AST.

## Example

```ts
import { Visitor } from 'rolldown/utils';
import { parseSync } from 'rolldown/utils';

const result = parseSync(...);
const visitor = new Visitor({
  VariableDeclaration(path) {
    // Do something with the variable declaration
  },
  "VariableDeclaration:exit"(path) {
    // Do something after visiting the variable declaration
  }
});
visitor.visit(result.program);
```

## Constructors

### Constructor

* **Type**: (`visitor`: `VisitorObject`) => `Visitor`
* **Experimental**

#### Parameters

##### visitor

`VisitorObject`

#### Returns

`Visitor`

## Methods

### visit()

* **Type**: (`program`: `Program`) => `void`
* **Experimental**

#### Parameters

##### program

`Program`

#### Returns

`void`

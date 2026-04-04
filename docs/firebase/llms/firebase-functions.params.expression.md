# Source: https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.params.expression.md.txt

# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md.txt

# params.Expression class

**Signature:**  

    export declare abstract class Expression<T extends string | number | boolean | string[]> 

## Methods

|                                                             Method                                                              | Modifiers |                                     Description                                      |
|---------------------------------------------------------------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------|
| [toCEL()](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpressiontocel)   |           | Returns the expression's representation as a braced CEL expression.                  |
| [toJSON()](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpressiontojson) |           | Returns the expression's representation as JSON.                                     |
| [value()](https://firebase.google.com/docs/reference/functions/firebase-functions.params.expression.md#paramsexpressionvalue)   |           | Returns the expression's runtime value, based on the CLI's resolution of parameters. |

## params.Expression.toCEL()

Returns the expression's representation as a braced CEL expression.

**Signature:**  

    toCEL(): string;

**Returns:**

string

## params.Expression.toJSON()

Returns the expression's representation as JSON.

**Signature:**  

    toJSON(): string;

**Returns:**

string

## params.Expression.value()

Returns the expression's runtime value, based on the CLI's resolution of parameters.

**Signature:**  

    value(): T;

**Returns:**

T
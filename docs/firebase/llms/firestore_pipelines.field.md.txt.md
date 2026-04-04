# Source: https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md.txt

# Field class

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

Represents a reference to a field in a Firestore document, or outputs of a [Pipeline](https://firebase.google.com/docs/reference/js/firestore_pipelines.pipeline.md#pipeline_class) stage.

<br />

Field references are used to access document field values in expressions and to specify fields for sorting, filtering, and projecting data in Firestore pipelines.

<br />

You can create a `Field` instance using the static method:

**Signature:**

    export declare class Field extends Expression implements Selectable 

**Extends:** [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class)

**Implements:** [Selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.selectable.md#selectable_interface)

## Properties

| Property | Modifiers | Type | Description |
|---|---|---|---|
| [alias](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#fieldalias) |   | string | ***(Public Preview)*** |
| [expr](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#fieldexpr) |   | [Expression](https://firebase.google.com/docs/reference/js/firestore_pipelines.expression.md#expression_class) | ***(Public Preview)*** |
| [expressionType](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#fieldexpressiontype) |   | [ExpressionType](https://firebase.google.com/docs/reference/js/firestore_pipelines.md#expressiontype) | ***(Public Preview)*** |
| [fieldName](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#fieldfieldname) |   | string | ***(Public Preview)*** |
| [selectable](https://firebase.google.com/docs/reference/js/firestore_pipelines.field.md#fieldselectable) |   | true | ***(Public Preview)*** |

## Field.alias

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    get alias(): string;

## Field.expr

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    get expr(): Expression;

## Field.expressionType

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    readonly expressionType: ExpressionType;

## Field.fieldName

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    get fieldName(): string;

## Field.selectable

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.

**Signature:**

    selectable: true;

### Example

    // Create a Field instance for the 'name' field
    const nameField = field("name");

    // Create a Field instance for a nested field 'address.city'
    const cityField = field("address.city");
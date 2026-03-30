# Source: https://docs.flux.ai/reference/api-errors.md

# API errors

Like any software, Flux enforces that anything you create is _valid_. For example, we make sure that there's no way for a user to make "Node A" the parent of "Node B" _and_ make "Node B" the parent of "Node A" at the same time. After all, what would that even mean?

Inside the tool, we enforce these restrictions by limiting the actions that you can take. Similarly, we make sure that models can't create invalid documents by throwing **exceptions** if an operation is invalid.

A key part of building a quality model is to get familiar with these restrictions. This way, your model is robust and won't crash if the user runs it on a document configured differently than your test files.

These restrictions are documented here as well as in the details page of various properties and functions.

## Invalid writes

#### **Error: in &lt;property/method&gt;: Expected to have type but got instead**

Functions that take arguments and property setters always have restrictions on what kind of values you can give them. For example, `resistance` can only be set to a number. It must also be a number between 0 and X. So if you write:

```typescript
flux.elements[0].properties[0].resistance = "test"
```



the above would throw 

```typescript
Error: in set_resistance: Expected "resistance" to have type number but got string instead.
```



There are too many variations of this error to list out for every property, but hopefully the error message should be self-explanatory. Please refer to the signature of the methods or properties you're using to know what kind of values are accepted.

#### **Cannot write to internal and read-only node**

Some nodes are read-only. Therefore, attempts to edit them will throw this error.
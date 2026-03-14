# Source: https://docs.flux.ai/reference/pcb-layout-rules-cascade-and-inheritance.md

# Layout Rules Inheritance and Precedence

## Inheritance

Besides the rules that are manually set by the user, there is an important concept to understand: inheritance.

**A rule is inheritable when the value for that rule is automatically passed down to that object's children(s).** For example, if you set a "Pad shape" rule on an object, every pad inside it will be styled with that pad shape unless you've applied different pad shape values directly to them. On the contrary, if you set a "Size" rule of 3mm on an object, all of its descendants do not get a size of 3mm of their parent's width.

![](https://uploads.developerhub.io/prod/86Yw/yr72u0urxyy555z0el4766mrtkstywm0z2b21bbq2xm26jy16bkd5kcxg1k7jh6z.png)

To check if a specific rule is inheritable or not, open the "Add rule" dialog and search for the "Inheritable" field.

## Precedence

When more than one rule applies to the same object, the rule that will end up being applied is dictated by two concepts: specificity and cascading.

### Specificity

**Specificity is a weight that is applied to a given PCB layout rule set when the same element is targeted by multiple rules**. 

These are the rules that govern specificity.

- Rules directly targeting objects will always take precedence over [inherited rules](https://docs.flux.ai/flux/reference/pcb-rules#inheritance)
- [Object-specific rules](https://docs.flux.ai/flux/reference/object-specific-pcb-rules) (e.g., `size="12mm"`) always take precedence over [selector-based rules](https://docs.flux.ai/flux/reference/pcb-layout-rule-selectors).
- More specific rules take precedence over less specific rules
    - An attribute selector is more specific — it will select only the objects on a page that match that specific attribute value — so will get a higher score.
    - An object selector is less specific — it will select all objects of that type that appear on a page — so will get a lower score.

#### Example

The following list of selector types increases by specificity:

1. Type selectors (e.g., `pad`)
2. Attributes selectors (e.g., `["Part Type"="ground"]`).
3. ID selectors (e.g., `#R2` or `#<object id>`).

Universal selector (*), combinators (+, &gt;, ~, " ", ||) and negation pseudo-class (:not()) have no effect on specificity.

### Cascading

**Cascading means that the order of rules matters; when two rules apply that have equal specificity, the one that comes last is lower in the list of selector rules will be used.**

![In this case, R2 will take priority over R1 since it's the one that comes last.](https://uploads.developerhub.io/prod/86Yw/qd4kqj3qeo7005e1vtxjgcoo4h3lyc9ty9mqk7bqj8bujz9dd91vv2kuxrqriaxk.png)
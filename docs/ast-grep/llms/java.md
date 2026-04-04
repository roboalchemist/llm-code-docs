# Source: https://ast-grep.github.io/catalog/java.md

---
url: /catalog/java.md
---
# Java

This page curates a list of example ast-grep rules to check and to rewrite Java code.

## No Unused Vars in Java&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmEiLCJxdWVyeSI6ImlmKHRydWUpeyQkJEJPRFl9IiwicmV3cml0ZSI6IiRDOiBMaXN0WyRUXSA9IHJlbGF0aW9uc2hpcCgkJCRBLCB1c2VsaXN0PVRydWUsICQkJEIpIiwic3RyaWN0bmVzcyI6InNtYXJ0Iiwic2VsZWN0b3IiOiIiLCJjb25maWciOiJpZDogbm8tdW51c2VkLXZhcnNcbnJ1bGU6XG4gICAga2luZDogbG9jYWxfdmFyaWFibGVfZGVjbGFyYXRpb25cbiAgICBhbGw6XG4gICAgICAgIC0gaGFzOlxuICAgICAgICAgICAgaGFzOlxuICAgICAgICAgICAgICAgIGtpbmQ6IGlkZW50aWZpZXJcbiAgICAgICAgICAgICAgICBwYXR0ZXJuOiAkSURFTlRcbiAgICAgICAgLSBub3Q6XG4gICAgICAgICAgICBwcmVjZWRlczpcbiAgICAgICAgICAgICAgICBzdG9wQnk6IGVuZFxuICAgICAgICAgICAgICAgIGhhczpcbiAgICAgICAgICAgICAgICAgICAgc3RvcEJ5OiBlbmRcbiAgICAgICAgICAgICAgICAgICAgYW55OlxuICAgICAgICAgICAgICAgICAgICAgICAgLSB7IGtpbmQ6IGlkZW50aWZpZXIsIHBhdHRlcm46ICRJREVOVCB9XG4gICAgICAgICAgICAgICAgICAgICAgICAtIHsgaGFzOiB7a2luZDogaWRlbnRpZmllciwgcGF0dGVybjogJElERU5ULCBzdG9wQnk6IGVuZH19XG5maXg6ICcnXG4iLCJzb3VyY2UiOiJTdHJpbmcgdW51c2VkID0gXCJ1bnVzZWRcIjtcbk1hcDxTdHJpbmcsIFN0cmluZz4gZGVjbGFyZWRCdXROb3RJbnN0YW50aWF0ZWQ7XG5cblN0cmluZyB1c2VkMSA9IFwidXNlZFwiO1xuaW50IHVzZWQyID0gMztcbmJvb2xlYW4gdXNlZDMgPSBmYWxzZTtcbmludCB1c2VkNCA9IDQ7XG5TdHJpbmcgdXNlZDUgPSBcIjVcIjtcblxuXG5cbnVzZWQxO1xuU3lzdGVtLm91dC5wcmludGxuKHVzZWQyKTtcbmlmKHVzZWQzKXtcbiAgICBTeXN0ZW0ub3V0LnByaW50bG4oXCJzb21lIHZhcnMgYXJlIHVudXNlZFwiKTtcbiAgICBNYXA8U3RyaW5nLCBTdHJpbmc+IHVudXNlZE1hcCA9IG5ldyBIYXNoTWFwPD4oKSB7e1xuICAgICAgICBwdXQodXNlZDUsIFwidXNlZDVcIik7XG4gICAgfX07XG5cbiAgICAvLyBFdmVuIHRob3VnaCB3ZSBkb24ndCByZWFsbHkgZG8gYW55dGhpbmcgd2l0aCB0aGlzIG1hcCwgc2VwYXJhdGluZyB0aGUgZGVjbGFyYXRpb24gYW5kIGluc3RhbnRpYXRpb24gbWFrZXMgaXQgY291bnQgYXMgYmVpbmcgdXNlZFxuICAgIGRlY2xhcmVkQnV0Tm90SW5zdGFudGlhdGVkID0gbmV3IEhhc2hNYXA8PigpO1xuXG4gICAgcmV0dXJuIHVzZWQ0O1xufSJ9)

### Description

Identifying unused variables is a common task in code refactoring. You should rely on a Java linter or IDE for this task rather than writing a custom rule in ast-grep, but for educational purposes, this rule demonstrates how to find unused variables in Java.

This approach makes some simplifying assumptions. We only consider local variable declarations and ignore the other many ways variables can be declared: Method Parameters, Fields, Class Variables, Constructor Parameters, Loop Variables, Exception Handler Parameters, Lambda Parameters, Annotation Parameters, Enum Constants, and Record Components. Now you may see why it is recommended to use a rule from an established linter or IDE rather than writing your own.

### YAML

```yaml
id: no-unused-vars
rule:
    kind: local_variable_declaration
    all:
        - has:
            has:
                kind: identifier
                pattern: $IDENT
        - not:
            precedes:
                stopBy: end
                has:
                    stopBy: end
                    any:
                        - { kind: identifier, pattern: $IDENT }
                        - { has: {kind: identifier, pattern: $IDENT, stopBy: end}}
fix: ''
```

First, we identify the local variable declaration and capture the pattern of the identifier inside of it. Then we use `not` and `precedes` to only match the local variable declaration if the identifier we captured does not appear later in the code.

It is important to note that we use `all` here to force the ordering of the `has` rule to be before the `not` rule. This guarantees that the meta-variable `$IDENT` is captured by looking inside of the local variable declaration.

Additionally, when looking ahead in the code, we can't just look for the identifier directly, but for any node that may contain the identifier.

### Example

```java
String unused = "unused"; // [!code --]
String used = "used";
System.out.println(used);
```

## Find Java field declarations of type String

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmEiLCJxdWVyeSI6ImAkVEFHYCIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoic21hcnQiLCJzZWxlY3RvciI6IiIsImNvbmZpZyI6InJ1bGU6XG4gIGtpbmQ6IGZpZWxkX2RlY2xhcmF0aW9uXG4gIGhhczpcbiAgICBmaWVsZDogdHlwZVxuICAgIHJlZ2V4OiBeU3RyaW5nJCIsInNvdXJjZSI6IkBDb21wb25lbnRcbmNsYXNzIEFCQyBleHRlbmRzIE9iamVjdHtcbiAgICBAUmVzb3VyY2VcbiAgICBwcml2YXRlIGZpbmFsIFN0cmluZyB3aXRoX2Fubm87XG5cbiAgICBwcml2YXRlIGZpbmFsIFN0cmluZyB3aXRoX211bHRpX21vZDtcblxuICAgIHB1YmxpYyBTdHJpbmcgc2ltcGxlO1xufSJ9)

### Description

To extract all Java field names of type `String` is not as straightforward as one might think. A simple pattern like `String $F;` would only match fields declared without any modifiers or annotations. However, a pattern like `$MOD String $F;` cannot be correctly parsed by tree-sitter.

:::details Use playground pattern debugger to explore the AST

You can use the [playground](https://ast-grep.github.io/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoiamF2YSIsInF1ZXJ5IjoiY2xhc3MgQUJDe1xuICAgJE1PRCBTdHJpbmcgdGVzdDtcbn0iLCJyZXdyaXRlIjoiIiwic3RyaWN0bmVzcyI6ImFzdCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoicnVsZTpcbiAga2luZDogZmllbGRfZGVjbGFyYXRpb25cbiAgaGFzOlxuICAgIGZpZWxkOiB0eXBlXG4gICAgcmVnZXg6IF5TdHJpbmckIiwic291cmNlIjoiQENvbXBvbmVudFxuY2xhc3MgQUJDIGV4dGVuZHMgT2JqZWN0e1xuICAgIEBSZXNvdXJjZVxuICAgIHByaXZhdGUgZmluYWwgU3RyaW5nIHdpdGhfYW5ubztcblxuICAgIHByaXZhdGUgZmluYWwgU3RyaW5nIHdpdGhfbXVsdGlfbW9kO1xuXG4gICAgcHVibGljIFN0cmluZyBzaW1wbGU7XG59In0=)'s pattern tab to visualize the AST of `class A { $MOD String $F; }`.

```
field_declaration
  $MOD
  variable_declarator
    identifier: String
  ERROR
    identifier: $F
```

Tree-sitter does not think `$MOD` is a valid modifier, so it produces an `ERROR`.

While the valid AST for code like `private String field;` produces different AST structures:

```
field_declaration
  modifiers
  type_identifier
  variable_declarator
    identifier: field
```

:::

A more robust approach is to use a structural rule that targets `field_declaration` nodes and applies a `has` constraint on the `type` child node to match the type `String`. This method effectively captures fields regardless of their modifiers or annotations.

### YAML

```yaml
id: find-field-with-type
language: java
rule:
  kind: field_declaration
  has:
    field: type
    regex: ^String$
```

### Example

```java {3-4,6,8}
@Component
class ABC extends Object{
    @Resource
    private final String with_anno;

    private final String with_multi_mod;

    public String simple;
}
```

### Contributed by

Inspired by the post [discussion](https://github.com/ast-grep/ast-grep/discussions/2195)

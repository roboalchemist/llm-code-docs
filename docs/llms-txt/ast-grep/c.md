# Source: https://ast-grep.github.io/catalog/c.md

---
url: /catalog/c.md
---
# C

This page curates a list of example ast-grep rules to check and to rewrite C code.

:::tip C files can be parsed as Cpp
You can parse C code as Cpp to avoid rewriting similar rules. The [`languageGlobs`](/reference/sgconfig.html#languageglobs) option can force ast-grep to parse `.c` files as Cpp.
:::

## Match Function Call in C

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImMiLCJxdWVyeSI6InRlc3QoJCQkKSIsInJld3JpdGUiOiIiLCJjb25maWciOiJydWxlOlxuICBwYXR0ZXJuOiBcbiAgICBjb250ZXh0OiAkTSgkJCQpO1xuICAgIHNlbGVjdG9yOiBjYWxsX2V4cHJlc3Npb24iLCJzb3VyY2UiOiIjZGVmaW5lIHRlc3QoeCkgKDIqeClcbmludCBhID0gdGVzdCgyKTtcbmludCBtYWluKCl7XG4gICAgaW50IGIgPSB0ZXN0KDIpO1xufSJ9)

### Description

One of the common questions of ast-grep is to match function calls in C.

A plain pattern like `test($A)` will not work. This is because [tree-sitter-c](https://github.com/tree-sitter/tree-sitter-c)
parse the code snippet into `macro_type_specifier`, see the [pattern output](https://ast-grep.github.io/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoiYyIsInF1ZXJ5IjoidGVzdCgkJCQpIiwicmV3cml0ZSI6IiIsImNvbmZpZyI6InJ1bGU6XG4gIHBhdHRlcm46IFxuICAgIGNvbnRleHQ6ICRNKCQkJCk7XG4gICAgc2VsZWN0b3I6IGNhbGxfZXhwcmVzc2lvbiIsInNvdXJjZSI6IiNkZWZpbmUgdGVzdCh4KSAoMip4KVxuaW50IGEgPSB0ZXN0KDIpO1xuaW50IG1haW4oKXtcbiAgICBpbnQgYiA9IHRlc3QoMik7XG59In0=).

To avoid this ambiguity, ast-grep lets us write a [contextual pattern](/guide/rule-config/atomic-rule.html#pattern), which is a pattern inside a larger code snippet.
We can use `context` to write a pattern like this: `test($A);`. Then, we can use the selector `call_expression` to match only function calls.

### YAML

```yaml
id: match-function-call
language: c
rule:
  pattern:
    context: $M($$$);
    selector: call_expression
```

### Example

```c{2,4}
#define test(x) (2*x)
int a = test(2);
int main(){
    int b = test(2);
}
```

### Caveat

Note, tree-sitter-c parses code differently when it receives code fragment. For example,

* `test(a)` is parsed as `macro_type_specifier`
* `test(a);` is parsed as `expression_statement -> call_expression`
* `int b = test(a)` is parsed as `declaration -> init_declarator -> call_expression`

The behavior is controlled by how the tree-sitter parser is written. And tree-sitter-c behaves differently from [tree-sitter-cpp](https://github.com/tree-sitter/tree-sitter-cpp).

Please file issues on tree-sitter-c repo if you want to change the behavior. ast-grep will respect changes and decision from upstream authors.

## Rewrite Method to Function Call&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImMiLCJxdWVyeSI6IiRDT1VOVCA9ICRcbiIsInJld3JpdGUiOiIiLCJjb25maWciOiJpZDogbWV0aG9kX3JlY2VpdmVyXG5ydWxlOlxuICBwYXR0ZXJuOiAkUi4kTUVUSE9EKCQkJEFSR1MpXG50cmFuc2Zvcm06XG4gIE1BWUJFX0NPTU1BOlxuICAgIHJlcGxhY2U6XG4gICAgICBzb3VyY2U6ICQkJEFSR1NcbiAgICAgIHJlcGxhY2U6ICdeLisnXG4gICAgICBieTogJywgJ1xuZml4OlxuICAkTUVUSE9EKCYkUiRNQVlCRV9DT01NQSQkJEFSR1MpXG4iLCJzb3VyY2UiOiJ2b2lkIHRlc3RfZnVuYygpIHtcbiAgICBzb21lX3N0cnVjdC0+ZmllbGQubWV0aG9kKCk7XG4gICAgc29tZV9zdHJ1Y3QtPmZpZWxkLm90aGVyX21ldGhvZCgxLCAyLCAzKTtcbn0ifQ==)

### Description

In C, there is no built-in support for object-oriented programming, but some programmers use structs and function pointers to simulate classes and methods. However, this style can have some drawbacks, such as:

* extra memory allocation and deallocation for the struct and the function pointer.
* indirection overhead when calling the function pointer.

A possible alternative is to use a plain function call with the struct pointer as the first argument.

### YAML

```yaml
id: method_receiver
language: c
rule:
  pattern: $R.$METHOD($$$ARGS)
transform:
  MAYBE_COMMA:
    replace:
      source: $$$ARGS
      replace: '^.+'
      by: ', '
fix:
  $METHOD(&$R$MAYBE_COMMA$$$ARGS)
```

### Example

```c {2-3}
void test_func() {
    some_struct->field.method();
    some_struct->field.other_method(1, 2, 3);
}
```

### Diff

```c
void test_func() {
    some_struct->field.method(); // [!code --]
    method(&some_struct->field); // [!code ++]
    some_struct->field.other_method(1, 2, 3); // [!code --]
    other_method(&some_struct->field, 1, 2, 3); // [!code ++]
}
```

### Contributed by

[Surma](https://twitter.com/DasSurma), adapted from the [original tweet](https://twitter.com/DasSurma/status/1706086320051794217)

## Rewrite Check to Yoda Condition&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImMiLCJxdWVyeSI6IiRDOiAkVCA9IHJlbGF0aW9uc2hpcCgkJCRBLCB1c2VsaXN0PVRydWUsICQkJEIpIiwicmV3cml0ZSI6IiRDOiBMaXN0WyRUXSA9IHJlbGF0aW9uc2hpcCgkJCRBLCB1c2VsaXN0PVRydWUsICQkJEIpIiwiY29uZmlnIjoiaWQ6IG1heS10aGUtZm9yY2UtYmUtd2l0aC15b3Vcbmxhbmd1YWdlOiBjXG5ydWxlOlxuICBwYXR0ZXJuOiAkQSA9PSAkQiBcbiAgaW5zaWRlOlxuICAgIGtpbmQ6IHBhcmVudGhlc2l6ZWRfZXhwcmVzc2lvblxuICAgIGluc2lkZToge2tpbmQ6IGlmX3N0YXRlbWVudH1cbmNvbnN0cmFpbnRzOlxuICBCOiB7IGtpbmQ6IG51bWJlcl9saXRlcmFsIH1cbmZpeDogJEIgPT0gJEEiLCJzb3VyY2UiOiJpZiAobXlOdW1iZXIgPT0gNDIpIHsgLyogLi4uICovfVxuaWYgKG5vdE1hdGNoID09IGFub3RoZXIpIHt9XG5pZiAobm90TWF0Y2gpIHt9In0=)

### Description

In programming jargon, a [Yoda condition](https://en.wikipedia.org/wiki/Yoda_conditions) is a style that places the constant portion of the expression on the left side of the conditional statement. It is used to prevent assignment errors that may occur in languages like C.

### YAML

```yaml
id: may-the-force-be-with-you
language: c
rule:
  pattern: $A == $B                 # Find equality comparison
  inside:                           # inside an if_statement
    kind: parenthesized_expression
    inside: {kind: if_statement}
constraints:                        # with the constraint that
  B: { kind: number_literal }       # right side is a number
fix: $B == $A
```

The rule targets an equality comparison, denoted by the [pattern](/guide/pattern-syntax.html) `$A == $B`. This comparison must occur [inside](/reference/rule.html#inside) an `if_statement`. Additionally, there’s a [constraint](/reference/yaml.html#constraints) that the right side of the comparison, `$B`, must be a number\_literal like `42`.

### Example

```c {1}
if (myNumber == 42) { /* ... */}
if (notMatch == another) { /* ... */}
if (notMatch) { /* ... */}
```

### Diff

```c
if (myNumber == 42) { /* ... */} // [!code --]
if (42 == myNumber) { /* ... */} // [!code ++]
if (notMatch == another) { /* ... */}
if (notMatch) { /* ... */}
```

### Contributed by

Inspired by this [thread](https://x.com/cocoa1han/status/1763020689303581141)

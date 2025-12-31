# Source: https://ast-grep.github.io/catalog/python/optional-to-none-union.md

---
url: /catalog/python/optional-to-none-union.md
---
## Rewrite `Optional[Type]` to `Type | None`&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InB5dGhvbiIsInF1ZXJ5IjoiIiwicmV3cml0ZSI6IiIsInN0cmljdG5lc3MiOiJzaWduYXR1cmUiLCJzZWxlY3RvciI6IiIsImNvbmZpZyI6InJ1bGU6XG4gIHBhdHRlcm46IFxuICAgIGNvbnRleHQ6ICdhOiBPcHRpb25hbFskVF0nXG4gICAgc2VsZWN0b3I6IGdlbmVyaWNfdHlwZVxuZml4OiAkVCB8IE5vbmUiLCJzb3VyY2UiOiJkZWYgYShhcmc6IE9wdGlvbmFsW0ludF0pOiBwYXNzIn0=)

### Description

[PEP 604](https://peps.python.org/pep-0604/) recommends that `Type | None` is preferred over `Optional[Type]` for Python 3.10+.

This rule performs such rewriting. Note `Optional[$T]` alone is interpreted as subscripting expression instead of generic type, we need to use [pattern object](/guide/rule-config/atomic-rule.html#pattern-object) to disambiguate it with more context code.

### YAML

```yaml
id: optional-to-none-union
language: python
rule:
  pattern:
    context: 'a: Optional[$T]'
    selector: generic_type
fix: $T | None
```

### Example

```py {1}
def a(arg: Optional[int]): pass
```

### Diff

```py
def a(arg: Optional[int]): pass # [!code --]
def a(arg: int | None): pass # [!code ++]
```

### Contributed by

[Bede Carroll](https://github.com/ast-grep/ast-grep/discussions/1492)

# Source: https://ast-grep.github.io/catalog/rule-template.md

---
url: /catalog/rule-template.md
---
## Your Rule Name&#x20;

* [Playground Link](/playground.html#)

### Description

Some Description for your rule!

### Pattern

```shell
ast-grep -p pattern -r rewrite -l js
# or without fixer
ast-grep -p pattern -l js
```

### YAML

```yaml
```

### Example

```js {1}
var a = 123
```

### Diff

```js
var a = 123 // [!code --]
let a = 123 // [!code ++]
```

### Contributed by

[Author Name](https://your-social.link)

# Source: https://docs.vale.sh/fixes/remove.md

# remove

## remove

Learn how to remove matches from your content.

```go
func remove(match string)
```

`remove` will remove the matched text of any rule.

```yaml
extends: existence
message: "Don't use an ellipsis in documentation."
nonword: true
action:
  name: remove
tokens:
  - '...'
```

[replace](https://docs.vale.sh/fixes/replace) [edit](https://docs.vale.sh/fixes/edit)

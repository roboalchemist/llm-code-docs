# Source: https://docs.vale.sh/keys/basedonstyles.md

# BasedOnStyles

Learn how to enable a style for a specific file type.

```ini
StylesPath = styles

[*.md]
BasedOnStyles = Vale, MyStyle
```

`BasedOnStyles` specifies styles that should have all of their rules enabled.

If you only want to enable certain rules within a style, you can do so on an individual basis:

```ini
[*.md]

# Enables only this rule:
Style1.Rule = YES
```

You can also selectively disable rules from a style:

```ini
[*.md]
BasedOnStyles = Vale, MyStyle

Vale.Spelling = NO
```

[SkippedScopes](https://docs.vale.sh/keys/skippedscopes) [BlockIgnores](https://docs.vale.sh/keys/blockignores)

# Source: https://docs.vale.sh/keys/ignoredclasses.md

# IgnoredClasses

Learn about how to ignore HTML classes.

```ini
Copy

StylesPath = styles

IgnoredClasses = my-class, another-class

[*.md]
BasedOnStyles = Vale
```

`IgnoredClasses` specifies classes to ignore. These classes may appear on both inline- and block-level HTML elements.

[IgnoredScopes](https://docs.vale.sh/keys/ignoredscopes) [SkippedScopes](https://docs.vale.sh/keys/skippedscopes)

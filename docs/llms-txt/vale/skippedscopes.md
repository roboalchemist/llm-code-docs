# Source: https://docs.vale.sh/keys/skippedscopes.md

# SkippedScopes

Learn about how to ignore block-level HTML tags.

```ini
StylesPath = styles

SkippedScopes = script, style, pre

[*.md]
BasedOnStyles = Vale
```

`SkippedScopes` specifies block-level HTML tags to ignore. Any content in these scopes will be ignored.

By default, Vale ignores `script`, `style`, and `pre` tags. For example, considering the following Markdown file:

````markdown
This is a sentence that contains normal text.

```python
# This is a code block.
print("Hello, world!")
```

Another normal sentence.
````

Vale will not raise any alerts for the content within the code block.

See [Markup](https://docs.vale.sh/topics/scopes) for more information.

[IgnoredClasses](https://docs.vale.sh/keys/ignoredclasses) [BasedOnStyles](https://docs.vale.sh/keys/basedonstyles)

# Source: https://docs.vale.sh/keys/tokenignores.md

# TokenIgnores

Learn define custom inline-level ignores in your Vale configuration.

{% hint style="warning" %}
`TokenIgnores` are only supported in Markdown, reStructuredText, AsciiDoc, and Org Mode.
{% endhint %}

```ini
StylesPath = styles

[*.md]
BasedOnStyles = Vale

TokenIgnores = ($+[^\n$]+$+), (:math:`.*`)
```

`TokenIgnores` allow you to exclude certain inline-level sections of text that don’t have an associated HTML tag that could be used with [`IgnoredScopes`](https://docs.vale.sh/keys/ignoredscopes).

The idea is to write a regular expression that captures the entire token in the first grouping. See this [regex101 session](https://regex101.com/r/3Raecd/1) for a more thorough explanation.

Related:

* [BlockIgnores](https://docs.vale.sh/keys/blockignores)
* [CommentDelimiters](https://docs.vale.sh/keys/commentdelimiters)

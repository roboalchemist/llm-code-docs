lightningcss::stylesheet

# Struct StyleSheet

Source

```
pub struct StyleSheet<'i, 'o, T = DefaultAtRule> {
    pub rules: CssRuleList<'i, T>,
    pub sources: Vec<String>,
    pub license_comments: Vec<CowArcStr<'i>>,
    /* private fields */
}
```

## Fields§

§`rules: CssRuleList<'i, T>`

A list of top-level rules within the style sheet.
§`sources: Vec<String>`

A list of file names for all source files included within the style sheet.
Sources are referenced by index in the `loc` property of each rule.
§`license_comments: Vec<CowArcStr<'i>>`

The license comments that appeared at the start of the file.

## Implementations§

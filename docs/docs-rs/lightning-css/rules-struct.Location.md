lightningcss::rules

# Struct Location

Source

```
pub struct Location {
    pub source_index: u32,
    pub line: u32,
    pub column: u32,
}
```

## Fields§

§`source_index: u32`

The index of the source file within the source map.
§`line: u32`

The line number, starting at 0.
§`column: u32`

The column number within a line, starting at 1 for first the character of the line.
Column numbers are counted in UTF-16 code units.

## Trait Implementations§

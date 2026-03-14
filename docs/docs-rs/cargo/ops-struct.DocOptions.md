cargo::ops

# Struct DocOptions

Source

```
pub struct DocOptions {
    pub open_result: bool,
    pub output_format: OutputFormat,
    pub compile_opts: CompileOptions,
}
```

## Fields§

§`open_result: bool`

Whether to attempt to open the browser after compiling the docs
§`output_format: OutputFormat`

Same as `rustdoc --output-format`
§`compile_opts: CompileOptions`

Options to pass through to the compiler

## Trait Implementations§

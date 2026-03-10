# Source: https://transloadit.com/docs/robots/file-filter.md

Think of this Robot as an `if/else` condition for building advanced file conversion workflows. With it, you can filter and direct certain uploaded files depending on their metadata.

The Robot has two modes of operation:

* Constructing conditions out of arrays with 3 members each. For example, `["${file.size}", "<=", "720"]`
* Writing conditions in JavaScript. For example, `${file.size <= 720}`. See also [Dynamic Evaluation](/docs/topics/dynamic-evaluation.md).

Passing JavaScript allows you to implement logic as complex as you wish, however it’s slower than combining arrays of conditions, and will be charged for per invocation via [🤖/script/run](/docs/robots/script-run.md).

### Conditions as arrays

The `accepts` and `declines` parameters can each be set to an array of arrays with three members:

1. A value or job variable, such as `${file.mime}`
2. One of the following operators: `==`, `===`, `<`, `>`, `<=`, `>=`, `!=`, `!==`, `regex`, `!regex`, `includes`, `!includes`
3. A value or job variable, such as `50` or `"foo"`

Examples:

* `[["${file.meta.width}", ">", "${file.meta.height}"]]`
* `[["${file.size}", "<=", "720"]]`
* `[["${file.size}", ">", "20mb"]]`
* `[["720", ">=", "${file.size}"]]`
* `[["${file.mime}", "regex", "image"]]`

For numeric comparisons (`<`, `>`, `<=`, `>=`), you can use human-readable byte values such as `"20mb"`, `"1gb"`, or `"512kb"`. These use binary (1024-based) multipliers. Supported units: `b`, `kb`, `mb`, `gb`, `tb`, `pb` (and their IEC equivalents `kib`, `mib`, `gib`, `tib`, `pib`).

The `includes` and `!includes` operators work with arrays or strings (strings use substring checks).

###### Warning

If you would like to match against a `null` value or a value that is not present (like an audio file does not have a `video_codec` property in its metadata), match against `""` (an empty string) instead. We’ll support proper matching against `null` in the future, but we cannot easily do so right now without breaking backwards compatibility.

### Conditions as JavaScript

The `accepts` and `declines` parameters can each be set to strings of JavaScript, which return a boolean value.

Examples:

* `${file.meta.width > file.meta.height}`
* `${file.size <= 720}`
* `${/image/.test(file.mime)}`
* `${Math.max(file.meta.width, file.meta.height) > 100}`

As indicated, we charge for this via [🤖/script/run](/docs/robots/script-run.md). See also [Dynamic Evaluation](/docs/topics/dynamic-evaluation.md) for more details on allowed syntax and behavior.

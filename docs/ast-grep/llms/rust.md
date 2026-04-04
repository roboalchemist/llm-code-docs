# Source: https://ast-grep.github.io/catalog/rust.md

---
url: /catalog/rust.md
---
# Rust

This page curates a list of example ast-grep rules to check and to rewrite Rust applications.

## Avoid Duplicated Exports

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InJ1c3QiLCJxdWVyeSI6IiIsImNvbmZpZyI6InJ1bGU6XG4gIGFsbDpcbiAgICAgLSBwYXR0ZXJuOiBwdWIgdXNlICRCOjokQztcbiAgICAgLSBpbnNpZGU6XG4gICAgICAgIGtpbmQ6IHNvdXJjZV9maWxlXG4gICAgICAgIGhhczpcbiAgICAgICAgICBwYXR0ZXJuOiBwdWIgbW9kICRBO1xuICAgICAtIGhhczpcbiAgICAgICAgcGF0dGVybjogJEFcbiAgICAgICAgc3RvcEJ5OiBlbmQiLCJzb3VyY2UiOiJwdWIgbW9kIGZvbztcbnB1YiB1c2UgZm9vOjpGb287XG5wdWIgdXNlIGZvbzo6QTo6QjtcblxuXG5wdWIgdXNlIGFhYTo6QTtcbnB1YiB1c2Ugd29vOjpXb287In0=)

### Description

Generally, we don't encourage the use of re-exports.

However, sometimes, to keep the interface exposed by a lib crate tidy, we use re-exports to shorten the path to specific items.
When doing so, a pitfall is to export a single item under two different names.

Consider:

```rs
pub mod foo;
pub use foo::Foo;
```

The issue with this code, is that `Foo` is now exposed under two different paths: `Foo`, `foo::Foo`.

This unnecessarily increases the surface of your API.
It can also cause issues on the client side. For example, it makes the usage of auto-complete in the IDE more involved.

Instead, ensure you export only once with `pub`.

### YAML

```yaml
id: avoid-duplicate-export
language: rust
rule:
  all:
     - pattern: pub use $B::$C;
     - inside:
        kind: source_file
        has:
          pattern: pub mod $A;
     - has:
        pattern: $A
        stopBy: end
```

### Example

```rs {2,3}
pub mod foo;
pub use foo::Foo;
pub use foo::A::B;


pub use aaa::A;
pub use woo::Woo;
```

### Contributed by

Julius Lungys([voidpumpkin](https://github.com/voidpumpkin))

## Beware of char offset when iterate over a string&#x20;

* [Playground Link](https://ast-grep.github.io/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoicnVzdCIsInF1ZXJ5IjoiJEEuY2hhcnMoKS5lbnVtZXJhdGUoKSIsInJld3JpdGUiOiIkQS5jaGFyX2luZGljZXMoKSIsImNvbmZpZyI6IiIsInNvdXJjZSI6ImZvciAoaSwgY2hhcikgaW4gc291cmNlLmNoYXJzKCkuZW51bWVyYXRlKCkge1xuICAgIHByaW50bG4hKFwiQm9zaGVuIGlzIGFuZ3J5IDopXCIpO1xufSJ9)

### Description

It's a common pitfall in Rust that counting *character offset* is not the same as counting *byte offset* when iterating through a string. Rust string is represented by utf-8 byte array, which is a variable-length encoding scheme.

`chars().enumerate()` will yield the character offset, while [`char_indices()`](https://doc.rust-lang.org/std/primitive.str.html#method.char_indices) will yield the byte offset.

```rs
let yes = "y̆es";
let mut char_indices = yes.char_indices();
assert_eq!(Some((0, 'y')), char_indices.next()); // not (0, 'y̆')
assert_eq!(Some((1, '\u{0306}')), char_indices.next());
// note the 3 here - the last character took up two bytes
assert_eq!(Some((3, 'e')), char_indices.next());
assert_eq!(Some((4, 's')), char_indices.next());
```

Depending on your use case, you may want to use `char_indices()` instead of `chars().enumerate()`.

### Pattern

```shell
ast-grep -p '$A.chars().enumerate()' \
   -r '$A.char_indices()' \
   -l rs
```

### Example

```rs {1}
for (i, char) in source.chars().enumerate() {
    println!("Boshen is angry :)");
}
```

### Diff

```rs
for (i, char) in source.chars().enumerate() { // [!code --]
for (i, char) in source.char_indices() { // [!code ++]
    println!("Boshen is angry :)");
}
```

### Contributed by

Inspired by [Boshen's Tweet](https://x.com/boshen_c/status/1719033308682870891)

![Boshen's footgun](https://pbs.twimg.com/media/F9s7mJHaYAEndnY?format=jpg\&name=medium)

## Get number of digits in a `usize`&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoicnVzdCIsInF1ZXJ5IjoiJE5VTS50b19zdHJpbmcoKS5jaGFycygpLmNvdW50KCkiLCJyZXdyaXRlIjoiJE5VTS5jaGVja2VkX2lsb2cxMCgpLnVud3JhcF9vcigwKSArIDEiLCJjb25maWciOiIjIFlBTUwgUnVsZSBpcyBtb3JlIHBvd2VyZnVsIVxuIyBodHRwczovL2FzdC1ncmVwLmdpdGh1Yi5pby9ndWlkZS9ydWxlLWNvbmZpZy5odG1sI3J1bGVcbnJ1bGU6XG4gIGFueTpcbiAgICAtIHBhdHRlcm46IGNvbnNvbGUubG9nKCRBKVxuICAgIC0gcGF0dGVybjogY29uc29sZS5kZWJ1ZygkQSlcbmZpeDpcbiAgbG9nZ2VyLmxvZygkQSkiLCJzb3VyY2UiOiJsZXQgd2lkdGggPSAobGluZXMgKyBudW0pLnRvX3N0cmluZygpLmNoYXJzKCkuY291bnQoKTsifQ==)

### Description

Getting the number of digits in a usize number can be useful for various purposes, such as counting the column width of line numbers in a text editor or formatting the output of a number with commas or spaces.

A common but inefficient way of getting the number of digits in a `usize` number is to use `num.to_string().chars().count()`. This method converts the number to a string, iterates over its characters, and counts them. However, this method involves allocating a new string, which can be costly in terms of memory and time.

A better alternative is to use [`checked_ilog10`](https://doc.rust-lang.org/std/primitive.usize.html#method.checked_ilog10).

```rs
num.checked_ilog10().unwrap_or(0) + 1
```

The snippet above computes the integer logarithm base 10 of the number and adds one. This snippet does not allocate any memory and is faster than the string conversion approach. The [efficient](https://doc.rust-lang.org/src/core/num/int_log10.rs.html) `checked_ilog10` function returns an `Option<usize>` that is `Some(log)` if the number is positive and `None` if the number is zero. The `unwrap_or(0)` function returns the value inside the option or `0` if the option is `None`.

### Pattern

```shell
ast-grep -p '$NUM.to_string().chars().count()' \
   -r '$NUM.checked_ilog10().unwrap_or(0) + 1' \
   -l rs
```

### Example

```rs {1}
let width = (lines + num).to_string().chars().count();
```

### Diff

```rs
let width = (lines + num).to_string().chars().count(); // [!code --]
let width = (lines + num).checked_ilog10().unwrap_or(0) + 1; // [!code ++]
```

### Contributed by

[Herrington Darkholme](https://twitter.com/hd_nvim), inspired by [dogfooding ast-grep](https://github.com/ast-grep/ast-grep/issues/550)

## Unsafe Function Without Unsafe Block

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InJ1c3QiLCJxdWVyeSI6IntcbiAgZGVzY3JpcHRpb24gPSAkQVxufSIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoic21hcnQiLCJzZWxlY3RvciI6ImJpbmRpbmciLCJjb25maWciOiIgIGlkOiByZWR1bmRhbnQtdW5zYWZlLWZ1bmN0aW9uXG4gIGxhbmd1YWdlOiBydXN0XG4gIHNldmVyaXR5OiBlcnJvclxuICBtZXNzYWdlOiBVbnNhZmUgZnVuY3Rpb24gd2l0aG91dCB1bnNhZmUgYmxvY2sgaW5zaWRlXG4gIG5vdGU6IHxcbiAgICBDb25zaWRlciB3aGV0aGVyIHRoaXMgZnVuY3Rpb24gbmVlZHMgdG8gYmUgbWFya2VkIHVuc2FmZSBcbiAgICBvciBpZiB1bnNhZmUgb3BlcmF0aW9ucyBzaG91bGQgYmUgd3JhcHBlZCBpbiBhbiB1bnNhZmUgYmxvY2tcbiAgcnVsZTpcbiAgICBhbGw6XG4gICAgICAtIGtpbmQ6IGZ1bmN0aW9uX2l0ZW1cbiAgICAgIC0gaGFzOlxuICAgICAgICAgIGtpbmQ6IGZ1bmN0aW9uX21vZGlmaWVyc1xuICAgICAgICAgIHJlZ2V4OiBcIl51bnNhZmVcIlxuICAgICAgLSBub3Q6XG4gICAgICAgICAgaGFzOlxuICAgICAgICAgICAga2luZDogdW5zYWZlX2Jsb2NrXG4gICAgICAgICAgICBzdG9wQnk6IGVuZCIsInNvdXJjZSI6IiAgLy8gU2hvdWxkIG1hdGNoIC0gdW5zYWZlIGZ1bmN0aW9uIHdpdGhvdXQgdW5zYWZlIGJsb2NrIChubyByZXR1cm4gdHlwZSlcbiAgdW5zYWZlIGZuIHJlZHVuZGFudF91bnNhZmUoKSB7XG4gICAgICBwcmludGxuIShcIk5vIHVuc2FmZSBvcGVyYXRpb25zIGhlcmVcIik7XG4gIH1cblxuICAvLyBTaG91bGQgbWF0Y2ggLSB1bnNhZmUgZnVuY3Rpb24gd2l0aCByZXR1cm4gdHlwZSwgbm8gdW5zYWZlIGJsb2NrXG4gIHVuc2FmZSBmbiByZWR1bmRhbnRfd2l0aF9yZXR1cm4oKSAtPiBpMzIge1xuICAgICAgbGV0IHggPSA1O1xuICAgICAgeCArIDEwXG4gIH1cblxuICAvLyBTaG91bGQgbWF0Y2ggLSB1bnNhZmUgZnVuY3Rpb24gd2l0aCBjb21wbGV4IHJldHVybiB0eXBlXG4gIHVuc2FmZSBmbiByZWR1bmRhbnRfY29tcGxleF9yZXR1cm4oKSAtPiBSZXN1bHQ8U3RyaW5nLCBzdGQ6OmlvOjpFcnJvcj4ge1xuICAgICAgT2soU3RyaW5nOjpmcm9tKFwic2FmZSBvcGVyYXRpb25cIikpXG4gIH1cblxuICAvLyBTaG91bGQgTk9UIG1hdGNoIC0gdW5zYWZlIGZ1bmN0aW9uIHdpdGggdW5zYWZlIGJsb2NrXG4gIHVuc2FmZSBmbiBwcm9wZXJfdW5zYWZlKCkgLT4gKmNvbnN0IGkzMiB7XG4gICAgICB1bnNhZmUge1xuICAgICAgICAgIGxldCBwdHIgPSAweDEyMzQgYXMgKmNvbnN0IGkzMjtcbiAgICAgICAgICBwdHJcbiAgICAgIH1cbiAgfVxuXG4gIC8vIFNob3VsZCBtYXRjaCAtIHVuc2FmZSBhc3luYyBmdW5jdGlvbiB3aXRob3V0IHVuc2FmZSBibG9ja1xuICB1bnNhZmUgYXN5bmMgZm4gYXN5bmNfcmVkdW5kYW50KCkgLT4gaTMyIHtcbiAgICAgIDQyXG4gIH1cblxuICAvLyBTaG91bGQgbWF0Y2ggLSB1bnNhZmUgY29uc3QgZnVuY3Rpb25cbiAgdW5zYWZlIGNvbnN0IGZuIGNvbnN0X3JlZHVuZGFudCgpIC0+IGkzMiB7XG4gICAgICAxMDBcbiAgfVxuXG4gIC8vIFNob3VsZCBOT1QgbWF0Y2ggLSByZWd1bGFyIGZ1bmN0aW9uXG4gIGZuIHJlZ3VsYXJfZnVuY3Rpb24oKSAtPiBpMzIge1xuICAgICAgNDJcbiAgfSJ9)

### Description

This rule detects functions marked with the `unsafe` keyword that do not contain any `unsafe` blocks in their body.

When a function is marked `unsafe`, it indicates that the function contains operations that the compiler cannot verify as safe. However, if the function body doesn't contain any `unsafe` blocks, it may be unnecessarily marked as `unsafe`. This could be a sign that:

1. The function should not be marked `unsafe` if it doesn't perform any unsafe operations
2. Or if there are unsafe operations, they should be explicitly wrapped in `unsafe` blocks for clarity

This rule helps identify such cases so developers can review whether the `unsafe` marker is truly necessary or if the code needs to be refactored.

### YAML

```yaml
id: redundant-unsafe-function
language: rust
severity: error
message: Unsafe function without unsafe block inside
note: |
  Consider whether this function needs to be marked unsafe 
  or if unsafe operations should be wrapped in an unsafe block
rule:
  all:
    - kind: function_item
    - has:
        kind: function_modifiers
        regex: "^unsafe"
    - not:
        has:
          kind: unsafe_block
          stopBy: end
```

### Example

```rs {2,7,12,24,29}
// Should match - unsafe function without unsafe block (no return type)
unsafe fn redundant_unsafe() {
    println!("No unsafe operations here");
}

// Should match - unsafe function with return type, no unsafe block
unsafe fn redundant_with_return() -> i32 {
    let x = 5;
    x + 10
}

// Should match - unsafe function with complex return type
unsafe fn redundant_complex_return() -> Result<String, std::io::Error> {
    Ok(String::from("safe operation"))
}

// Should NOT match - unsafe function with unsafe block
unsafe fn proper_unsafe() -> *const i32 {
    unsafe {
        let ptr = 0x1234 as *const i32;
        ptr
    }
}

// Should match - unsafe async function without unsafe block
unsafe async fn async_redundant() -> i32 {
    42
}

// Should match - unsafe const function
unsafe const fn const_redundant() -> i32 {
    100
}

// Should NOT match - regular function
fn regular_function() -> i32 {
    42
}
```

### Contributed by

Inspired by [@hd\_nvim's Tweet](https://x.com/hd_nvim/status/1992810384072585397?s=20)

## Rewrite `indoc!` macro&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoicnVzdCIsInF1ZXJ5IjoiaW5kb2MhIHsgciNcIiQkJEFcIiMgfSIsInJld3JpdGUiOiJgJCQkQWAiLCJzdHJpY3RuZXNzIjoicmVsYXhlZCIsInNlbGVjdG9yIjoiIiwiY29uZmlnIjoicnVsZTogXG4gYW55OlxuIC0gcGF0dGVybjogJFYgPT09ICRTRU5TRVRJVkVXT1JEXG4gLSBwYXR0ZXJuOiAkU0VOU0VUSVZFV09SRCA9PT0gJFZcbmNvbnN0cmFpbnRzOlxuICBTRU5TRVRJVkVXT1JEOlxuICAgIHJlZ2V4OiBwYXNzd29yZCIsInNvdXJjZSI6ImZuIG1haW4oKSB7XG4gICAgaW5kb2MhIHtyI1wiXG4gICAgICAgIC5mb28ge1xuICAgICAgICAgICAgb3JkZXI6IDE7XG4gICAgICAgIH1cbiAgICBcIiN9O1xufSJ9)

### Description

This example, created from [a Tweet](https://x.com/zack_overflow/status/1885065128590401551), shows a refactoring operation being performed on Rust source code. The changes involve removing `indoc!` macro declarations while preserving the CSS-like content within them.

Previously, the same refactor is implemented by a *unreadable monster regex* in vim syntax.

:::details Click to see the original regex (neovim, btw)

```vimscript
:%s/\v(indoc!|)(| )([|\{)r#"(([^#]+|\n+)+)"#/`\4`
```

I have to confess that I don't understand this regex even if I use neovim, btw.

Let Claude break it down piece by piece:

* `:%s/` - Vim substitution command for all lines
* `\v` - Very magic mode in vim for simpler regex syntax
* `(indoc!|)` - First capture group: matches either "indoc!" or nothing
* `(| )` - Second capture group: matches either empty string or a space
* `([|\{)` - Third capture group: matches either `[` or `{`
* `r#"` - Matches literal `r#"` (Rust raw string delimiter)
* `(([^#]+|\n+)+)` - Fourth capture group (nested):
  * `[^#]+` - One or more non-# characters
  * `|\n+` - OR one or more newlines
  * Outer `()+` makes this repeat one or more times
* `"#` - Matches the closing raw string delimiter
* \`\4\` - Replaces with the fourth capture group wrapped in backticks

This regex is designed to find Rust raw string literals (possibly wrapped in `indoc!` macro), capture their content, and replace the entire match with just the content wrapped in backticks. It's more precise than my previous explanation and matches the pattern you're showing.

:::

### Pattern

```shell
ast-grep --pattern 'indoc! { r#"$$$A"# }' --rewrite '`$$$A`' sgtest.rs
```

### Example

```rs {2-6}
fn main() {
    indoc! {r#"
        .foo {
            order: 1;
        }
    "#};
}
```

### Diff

```rs
fn main() {
    indoc! {r#" // [!code --]
    `.foo {    // [!code ++]
        order: 1;
    }
    "#}; // [!code --]
        `; // [!code ++]
}
```

### Contributed by

[Zack in SF](https://x.com/zack_overflow)

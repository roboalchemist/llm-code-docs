# Source: https://docs.grit.io

# Authoring custom patterns

We recommend authoring Grit patterns in `.md` files, as this format allows you to combine documentation, GritQL, and source code examples in a single file.
[
## VS Code
](https://docs.grit.io/guides/authoring#vs-code)We recommend installing the [Grit extension](/guides/vscode) to get syntax highlighting and authoring assistance for Grit patterns.
You can watch [this video](https://www.youtube.com/embed/WICqSP-w2IU?si=KAtvT12uWXaroS_z%22) to see the extension in action.

[
## Tips
](https://docs.grit.io/guides/authoring#tips)- Use the `grit patterns test` command to test all defined patterns in your repo.
- As you are iterating on a pattern, you can use `--watch` to automatically re-run tests when you save a file.
- You can use `--filter` to run a subset of patterns: this speeds up the test cycle when you are working on a specific pattern.
[
## Markdown Format
](https://docs.grit.io/guides/authoring#markdown-format)Patterns can be stored in `*.md` files within a `.grit/patterns` folder at the root of your repo.
- The `name` of the file is used as the name of the pattern (without the `.md` extension).
- The `title` of the pattern is retrieved from the first heading in the file. This can be overridden by adding a `title` field in the front matter.
- The `description` of the pattern is retrieved from the first non-heading paragraph in the file.
- The GritQL `body` is retrieved from the first fenced code block in the file.
- Additional pattern metadata can be configured as YAML in the frontmatter of the markdown file, delineated between `---` lines at the start of the document.- `level`: (Optional, one of `none`, `info`, `warn`, `error`) The enforcement level of the pattern for running diagnostics via `grit check`. Defaults to `info`.
- `tags`: (Optional, `string[]`) A list of tags which can be used to filter patterns.

- Subheadings are used for each test case, following these conventions:- If a subheading has a single code block, it represents a test case that should be matched by the pattern. You don&#x27;t need to provide a transformed example.
- If a subheading has two code blocks, the first represents the input and the second represents the expected output.
- A negative test case should have two identical code blocks.
- Within the sample patterns, you can use `// @filename: example.js` to represent multiple input/output files that should be tested as a group - like [this example](https://github.com/getgrit/stdlib/blob/main/.grit/patterns/js/split_trpc_router.md?plain=1#L129).

[
## Example
](https://docs.grit.io/guides/authoring#example)Here is an example of a markdown pattern file:
markdown .grit/patterns/remove_console_log.md---
tags: [optional, tags, here]
---
# Remove console.log

Remove console.log in production code.

```grit
`console.log($_)` => .
```

## Test case one

This is the first test case. You can include an explanation of the case here.

```typescript
console.error("keep this");
console.log(&#x27;remove this!&#x27;);
```

It is fine to include additional descriptive text around the test cases.
This is often used to explain the context of the test case, or to explain a convention.

```typescript
console.error("keep this");

```You can find many more examples in the [Grit standard library](https://github.com/getgrit/stdlib/tree/main/.grit/patterns).
# Source: https://docs.grit.io

# Common Idioms

This page covers some common techniques for writing GritQL patterns.
[
## List and string accumulation
](https://docs.grit.io/language/idioms#list-and-string-accumulation)Within `where` clauses, you can assign a value to a metavariable using the `=` operator and then use `+=` to accumulate values. This is particularly common when combined with [`some`](/language/modifiers#some-clause) to iterate over a list of values, such as in [this pattern](https://github.com/getgrit/stdlib/blob/main/.grit/patterns/js/es6_imports.md).
Strings and lists can both be accumulated, as shown in this example:
pattern `namedColors = { $colors }` where {
    $keys = "",
    $values = [],
    $colors <: some bubble($keys, $values) `$name: $color` where {
        // Push the name onto the string
        $keys += $name,
        // Push the values onto the list
        $values += `$color`
    },
    // Join the values together to make a string
    $new_colors = join(list=$values, separator=", ")
} => `$keys = [ $new_colors ]`Before const namedColors = {
  red: &#x27;#ff0000&#x27;,
  green: &#x27;#00ff00&#x27;,
  blue: &#x27;#0000ff&#x27;,
};After const redgreenblue = [
  &#x27;#ff0000&#x27;,
  &#x27;#00ff00&#x27;,
  &#x27;#0000ff&#x27;
];[
## Creating new files
](https://docs.grit.io/language/idioms#creating-new-files)The `$new_files` metavariable allows creating a new file as a side-effect of a pattern.
For example, for following pattern moves all functions which start with `test` to a separate file (`stuff.test.js`):
pattern `function $functionName($_) {$_}` as $f where {
  $functionName <: r"test.*",
  $f => .,
  $new_file_name = `$functionName.test.js`,
  $new_files += file(name = $new_file_name, body = $f)
}Before function doStuff() {}
function testStuff() {}After // stuff.js
function doStuff() {}

// testStuff.test.js
function testStuff() {} - - **Warning:** `$new_files` does not consider the existing files, so it is possible to overwrite existing files.
[
## Accessing the current file name
](https://docs.grit.io/language/idioms#accessing-the-current-file-name)The `$filename` metavariable always contains the name of the current file the query is processing.
For example, the following pattern we move the matching function to a new file that uses the same name as the original file, but with a `.test.js` extension:
pattern `function $functionName($_) {$_}` as $f where {
  $functionName <: r"test.*",
  $f => .,
  $filename <: r"(.*)\.js$"($base_name),
  $new_file_name = `$base_name.test.js`,
  $new_files += file(name = $new_file_name, body = $f)
}Before function doStuff() {}
function testStuff() {}After // stuff.js
function doStuff() {}

// stuff.test.js
function testStuff() {}[
## Comments
](https://docs.grit.io/language/idioms#comments)Comments are supported in GritQL. Any line starting with `//` is considered a comment and ignored by the parser.
grit `console.log($message)` => . where {
  // This is a comment
  $message <: js"&#x27;Hello, world!&#x27;"
}[
## Specific rewrites
](https://docs.grit.io/language/idioms#specific-rewrites)Since GritQL supports nested patterns, it is usually preferable to match a larger pattern and then only *rewrite* the specific metavariables you want to change inside a `where` clause.
This helps in several ways:
- It avoids duplication, as often the right-hand side of the rewrite repeats the left-hand side.
- It helps preserve syntactic and semantic details of the original code.
For example, the following rewrite is not specific and therefore loses the `async` keyword and the comment about arguments:
pattern `function foo($args) { $body }` => `function bar($args) {$body} `Before async function foo(/* no args */) {
  console.log(&#x27;Hello, world!&#x27;);
}After function bar() {
  console.log(&#x27;Hello, world!&#x27;);
}The following rewrite is specific and preserves the `async` keyword and the comment about arguments:
pattern `function $name($args) { $body }` where {
  $name <: `foo` => `bar`
}Before async function foo(/* no args */) {
  console.log(&#x27;Hello, world!&#x27;);
}After async function bar(/* no args */) {
  console.log(&#x27;Hello, world!&#x27;);
}[
## Making small pull requests
](https://docs.grit.io/language/idioms#making-small-pull-requests)In general, huge pull requests are harder to review and more likely to have merge conflicts. You can use the [limit clause](/language/modifiers#limit-clause) to limit the number of files a pattern is applied to.
[
## Targeting specific code blocks
](https://docs.grit.io/language/idioms#targeting-specific-code-blocks)You can use `range` patterns together with the [`$filename` metavariable](#accessing-the-current-file-name) to target specific code blocks that are known ahead of time.
This is often helpful for integrating Grit with other static analysis tools.
For example, to target the `console.log` on the 2nd line of a file called `stuff.js`:
grit `console.log($message)` where {
  $message <: within range(start_line=2, end_line=2),
  $filename <: includes "stuff.js"
}typescript // @filename: stuff.js
console.log("hello");
console.log("goodbye");
console.log("wow");
console.log("multiline");
# Source: https://biomejs.dev/formatter/differences-with-prettier/

# Differences with Prettier 

In some cases, Biome has intentionally decided to format code in a way that doesn't match Prettier's output. These divergences are explained below.

## Prettier doesn't unquote some object properties that are valid JavaScript identifiers. 

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Prettier doesn't unquote some object properties that are valid JavaScript identifiers."]](#prettier-doesnt-unquote-some-object-properties-that-are-valid-javascript-identifiers)

Prettier and Biome unquote object and class properties that are valid JavaScript identifiers. Prettier [unquotes only valid ES5 identifiers](https://github.com/prettier/prettier/blob/a5d502513e5de4819a41fd90b9be7247146effc7/src/language-js/utils/index.js#L646).

This is a legacy restriction in an ecosystem where ES2015 is now widespread. Thus, we decided to diverge here by un-quoting all valid JavaScript identifiers in ES2015+.

A possible workaround would be to introduce a configuration to set the ECMAScript version a project uses. We could then adjust the un-quoting behaviour based on that version. Setting the ECMAScript version to `ES5` could match Prettier's behaviour.

<figure class="frame has-title not-content">
<pre data-language="js"><code>1const obj = </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="js"><code>1const obj = ;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

## Prettier has an inconsistent behavior for assignment in computed keys. 

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Prettier has an inconsistent behavior for assignment in computed keys."]](#prettier-has-an-inconsistent-behavior-for-assignment-in-computed-keys)

Prettier and Biome enclose some assignment expressions between parentheses, particularly in conditionals. This allows Biome to identify an expression that should be a comparison.

Prettier has inconsistent behaviour because it adds parentheses for an assignment in a computed key of an object property and doesn't for a computed key of a class property, as demonstrated by the following example:

Input

<figure class="frame has-title not-content">
<pre data-language="js"><code>1a = 4
5class C </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="js"><code>1a = ;5
6class C </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

[Playground link](/playground?enabledLinting=false&code=YQAgAD0AIAB7AAoAIAAgAFsAeAAgAD0AIAAwAF0AOgAgADEALAAKAH0ACgAKAGMAbABhAHMAcwAgAEMAIAB7AAoAIAAgACAAIABbAHgAIAA9ACAAMABdACAAPQAgADEACgB9AAoA)

To be consistent, we decided to diverge and omit the parentheses. Alternatively, we could enclose any assignment in a computed key of an object or of a class.

## Prettier adds a trailing comma to type parameters of arrow functions even when it is not required. 

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Prettier adds a trailing comma to type parameters of arrow functions even when it is not required."]](#prettier-adds-a-trailing-comma-to-type-parameters-of-arrow-functions-even-when-it-is-not-required)

In some specific cases, a type parameter list of an arrow function requires a trailing comma to distinguish it from a JSX element. When a default type is provided, this trailing comma is not required. Here, we diverge from Prettier because we think it better respects the original intent of Prettier, which was to add a trailing comma only when required.

Input

<figure class="frame has-title not-content">
<pre data-language="tsx"><code>1&lt;T = unknown&gt;() =&gt; ;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.tsx</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="tsx"><code>1&lt;T = unknown,&gt;() =&gt; ;2&lt;T = unknown&gt;() =&gt; ;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.tsx</span></figcaption>
</figure>

## Prettier has an inconsistent behavior for parenthesized non-null-asserted optional chains

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Prettier has an inconsistent behavior for parenthesized non-null-asserted optional chains"]](#prettier-has-an-inconsistent-behavior-for-parenthesized-non-null-asserted-optional-chains)

In *TypeScript*, the non-null assertion operator `!` allows asserting that a value is non-null. When applied on an optional chain, the assertion applies to the entire chain regardless of the presence of parentheses, making equivalent `(a.?.b)!` and `a.?.b!`.

The previous code examples are already well-formatted, according to Prettier. Prettier is used to enforce the presence or the absence of parentheses. This looks like a missed opportunity to normalize the code.

Moreover, Prettier doesn't remove the parentheses even when they enclose the non-null assertion. Instead, it moves the operator outside the parentheses.

Input:

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1a.?.b!2(a.?.b)!3(a.?.b!)</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.ts</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1a.?.b!2(a.?.b)!3a.?.b!4(a.?.b!)5a.?.b!</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.ts</span></figcaption>
</figure>

## Prettier formats invalid syntaxes

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Prettier formats invalid syntaxes"]](#prettier-formats-invalid-syntaxes)

Prettier's Babel-based parsing for JavaScript and TypeScript is very loose and [allows multiple errors](https://github.com/prettier/prettier/blob/e4a74c05f4502dd4ec70495c3130ff08ab088e05/src/language-js/parse/babel.js#L177-L218) to be ignored. Biome's parser is intentionally stricter than the Prettier parser. It correctly identifies the following syntax errors:

-   A function cannot have duplicate modifiers
-   invalid order of properties' modifiers
-   Function declarations are not allowed to have bodies
-   non-abstract classes cannot have abstract properties
-   An optional chain cannot be assigned
-   The `const` modifier cannot be set on a type parameter of an interface
-   top-level return
-   etc.

In Prettier, these errors aren't considered parse errors, and the AST is still built "correctly" with the appropriate nodes. When formatting, Prettier treats these nodes as normal and formats them accordingly.

In Biome, the parsing errors result in `Bogus` nodes, which may contain any number of valid nodes, invalid nodes, and/or raw characters. When formatting, Biome treats bogus nodes as effectively plain text, printing them out verbatim into the resulting code without any formatting since attempting to format them could be incorrect and cause semantic changes.

For class properties, Prettier's current parsing strategy also uses boolean fields for modifiers, meaning only one of each kind of modifier can ever be present (accessibility modifiers are stored as a single string). When printing, Prettier looks at the list of booleans and decides which modifiers to print out again. Biome instead keeps a list of modifiers, meaning duplicates are kept around and can be analyzed (hence the parsing error messages about duplicate modifiers and ordering). When printing out the bogus nodes, this list is kept intact, and printing out the unformatted text results in those modifiers continuing to exist.

There are ways that Biome can address this. One possibility is to try to interpret the Bogus nodes when formatting and construct valid nodes out of them. If a valid node can be built, then it would just format that node like normal, otherwise, it prints the bogus text verbatim as it does currently. However, this is messy and introduces a form of parsing logic into the formatter that is not meaningful.

Another option is to introduce some form of "syntactically-valid bogus node" into the parser, which accepts these kinds of purely semantic errors (duplicate modifiers, abstract properties in non-abstract classes).

It would continue to build the nodes like normal (effectively matching the behavior in Prettier) but store them inside of a new kind of bogus node, including the diagnostics along with it. When formatting, these particular bogus nodes would just attempt to format the inner node and then fallback if there's an error (the existing `format_or_verbatim` utility would do this already). This keeps the parsing and formatting logic separate from each other but introduces more complexity to the parser, allowing invalid states to be considered semi-valid.

### Duplicate modifiers on class properties

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Duplicate modifiers on class properties"]](#duplicate-modifiers-on-class-properties)

Input

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1// Multiple accessibility modifiers2class Foo 5
6// Declare function with body7declare function foo ( ) 8
9// Invalid use of abstract10class Bar 13
14// Duplicate Readonly15class Read </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.ts</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1// Multiple accessibility modifiers2class Foo 6
7// Declare function with body8declare function foo ( ) 9declare function foo() ;10
11// Invalid use of abstract12class Bar 16
17// Duplicate Readonly18class Read </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.ts</span></figcaption>
</figure>

### Assignment to an optional chain

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Assignment to an optional chain"]](#assignment-to-an-optional-chain)

Input

<figure class="frame has-title not-content">
<pre data-language="js"><code>1(a?.b) = c;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="js"><code>1a?.b = c;2(a?.b) = c;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

### Incorrect modifier for the type parameters of an interface

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Incorrect modifier for the type parameters of an interface"]](#incorrect-modifier-for-the-type-parameters-of-an-interface)

Input

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1interface L&lt;in const T&gt; </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1interface L&lt;const in T&gt; 2interface L&lt;in const T&gt; </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

### Top-level return

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Top-level return"]](#top-level-return)

<figure class="frame has-title not-content">
<pre data-language="js"><code>1return someVeryLongStringA &amp;&amp; someVeryLongStringB &amp;&amp; someVeryLongStringC &amp;&amp; someVeryLongStringD</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

<figure class="frame has-title not-content">
<pre data-language="js"><code>1return someVeryLongStringA &amp;&amp; someVeryLongStringB &amp;&amp; someVeryLongStringC &amp;&amp; someVeryLongStringD2return (3  someVeryLongStringA &amp;&amp;4  someVeryLongStringB &amp;&amp;5  someVeryLongStringC &amp;&amp;6  someVeryLongStringD7);</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

### Erroneous self-increment and self-decrement

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Erroneous self-increment and self-decrement"]](#erroneous-self-increment-and-self-decrement)

Input

<figure class="frame has-title not-content">
<pre data-language="js"><code>1(1)++;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

<figure class="frame has-title not-content">
<pre data-language="js"><code>11++;2(1)++;</code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

### Use of `abstract` modifier in non-abstract classes

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Use of abstract modifier in non-abstract classes"]](#use-of-abstract-modifier-in-non-abstract-classes)

Input

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1class C </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1class C </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

## Prettier has inconsistencies between TypeScript and Babel parsing

[[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iY3VycmVudGNvbG9yIiBkPSJtMTIuMTEgMTUuMzktMy44OCAzLjg4YTIuNTIgMi41MiAwIDAgMS0zLjUgMCAyLjQ3IDIuNDcgMCAwIDEgMC0zLjVsMy44OC0zLjg4YTEgMSAwIDAgMC0xLjQyLTEuNDJsLTMuODggMy44OWE0LjQ4IDQuNDggMCAwIDAgNi4zMyA2LjMzbDMuODktMy44OGExIDEgMCAxIDAtMS40Mi0xLjQyWm04LjU4LTEyLjA4YTQuNDkgNC40OSAwIDAgMC02LjMzIDBsLTMuODkgMy44OGExIDEgMCAwIDAgMS40MiAxLjQybDMuODgtMy44OGEyLjUyIDIuNTIgMCAwIDEgMy41IDAgMi40NyAyLjQ3IDAgMCAxIDAgMy41bC0zLjg4IDMuODhhMSAxIDAgMSAwIDEuNDIgMS40MmwzLjg4LTMuODlhNC40OSA0LjQ5IDAgMCAwIDAtNi4zM1pNOC44MyAxNS4xN2ExIDEgMCAwIDAgMS4xLjIyIDEgMSAwIDAgMCAuMzItLjIybDQuOTItNC45MmExIDEgMCAwIDAtMS40Mi0xLjQybC00LjkyIDQuOTJhMSAxIDAgMCAwIDAgMS40MloiPjwvcGF0aD48L3N2Zz4=)][Section titled "Prettier has inconsistencies between TypeScript and Babel parsing"]](#prettier-has-inconsistencies-between-typescript-and-babel-parsing)

Prettier supports a number of different parsers for JavaScript and TypeScript code, all of which are meant to be compatible with the [`estree` spec](https://github.com/estree/estree). Most of the time, Prettier uses Babel as the default parser for JavaScript code, but when parsing TypeScript, it will try to use TypeScript's own parser first and only fall back to Babel with TypeScript enabled afterward. While the TypeScript parser is generally compatible with `estree`, it's not exact, and [this can lead to some inconsistencies](https://github.com/prettier/prettier/issues/15785) that affect the output that Prettier creates. In general, these are considered bugs in Prettier itself, since the output should be the same regardless of which parser is used.

Biome implements its own parsing that handles all forms of JavaScript and TypeScript code, meaning there should not be any inconsistencies between the two. However, when migrating a TypeScript codebase from Prettier to Biome, it's possible that some formatting will appear to have changed because of those discrepancies between parsers from Prettier.

These cases are not considered bugs or incompatibilities in Biome. If formatted code only appears different using the `typescript` parser setting in Prettier, but matches when using `babel` and/or `babel-ts`, then Biome considers the output to be compatible.

As an example, consider this case, formatted using Biome and Prettier 3.1.0 with the `typescript` parser:

Input

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1function someFunctionName(2  someLongBreakingParameterName,3  anotherLongParameterName,4) </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

Diff

<figure class="frame has-title not-content">
<pre data-language="ts"><code>1function someFunctionName(2  someLongBreakingParameterName,3  anotherLongParameterName,4) </code></pre>
<div class="copy">
<div>

</div>
</div>
<figcaption><span class="title">example.js</span></figcaption>
</figure>

Prettier with the TypeScript parser chooses to write the `isEqual` call on a single line, while Biome matches the output of Prettier with the `babel` and `babel-ts` parsers. As such, this is *not* considered an incompatibility with Biome and is instead considered a bug in Prettier.

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLTIyY21rdDNwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuMmVtOyI+PHBhdGggZD0iTTIyIDcuMjRhMSAxIDAgMCAwLS4yOS0uNzFsLTQuMjQtNC4yNGExIDEgMCAwIDAtMS4xLS4yMiAxIDEgMCAwIDAtLjMyLjIybC0yLjgzIDIuODNMMi4yOSAxNi4wNWExIDEgMCAwIDAtLjI5LjcxVjIxYTEgMSAwIDAgMCAxIDFoNC4yNGExIDEgMCAwIDAgLjc2LS4yOWwxMC44Ny0xMC45M0wyMS43MSA4Yy4xLS4xLjE3LS4yLjIyLS4zM2ExIDEgMCAwIDAgMC0uMjR2LS4xNGwuMDctLjA1Wk02LjgzIDIwSDR2LTIuODNsOS45My05LjkzIDIuODMgMi44M0w2LjgzIDIwWk0xOC4xNyA4LjY2bC0yLjgzLTIuODMgMS40Mi0xLjQxIDIuODIgMi44Mi0xLjQxIDEuNDJaIj48L3BhdGg+PC9zdmc+)Edit page](https://github.com/biomejs/website/edit/main/src/content/docs/formatter/differences-with-prettier.md)

[![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNyAxMUg5LjQxbDMuMy0zLjI5YTEuMDA0IDEuMDA0IDAgMSAwLTEuNDItMS40MmwtNSA1YTEgMSAwIDAgMC0uMjEuMzMgMSAxIDAgMCAwIDAgLjc2IDEgMSAwIDAgMCAuMjEuMzNsNSA1YTEuMDAyIDEuMDAyIDAgMCAwIDEuNjM5LS4zMjUgMSAxIDAgMCAwLS4yMTktMS4wOTVMOS40MSAxM0gxN2ExIDEgMCAwIDAgMC0yWiI+PC9wYXRoPjwvc3ZnPg==) [ Previous\
[Introduction] ]](/formatter) [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9ImFzdHJvLXVtd3BqempwIGFzdHJvLTQzd2tlZjVlIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIiBzdHlsZT0iLS1zbC1pY29uLXNpemU6IDEuNXJlbTsiPjxwYXRoIGQ9Ik0xNy45MiAxMS42MmExLjAwMSAxLjAwMSAwIDAgMC0uMjEtLjMzbC01LTVhMS4wMDMgMS4wMDMgMCAxIDAtMS40MiAxLjQybDMuMyAzLjI5SDdhMSAxIDAgMCAwIDAgMmg3LjU5bC0zLjMgMy4yOWExLjAwMiAxLjAwMiAwIDAgMCAuMzI1IDEuNjM5IDEgMSAwIDAgMCAxLjA5NS0uMjE5bDUtNWExIDEgMCAwIDAgLjIxLS4zMyAxIDEgMCAwIDAgMC0uNzZaIj48L3BhdGg+PC9zdmc+) [ Next\
[Formatter Option Philosophy] ]](/formatter/option-philosophy)

Sponsored by

![Depot](/_astro/depot-logo-horizontal-on-light@3x.CwT7__a0_Z1k23Gh.webp?dpl=69532f2b69cab10008a149f1) ![Depot](/_astro/depot-logo-horizontal-on-dark@3x.BWjsBfKV_Z29sH19.webp?dpl=69532f2b69cab10008a149f1)

Copyright (c) 2023-present Biome Developers and Contributors.
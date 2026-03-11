# Source: https://rolldown.rs/reference/Interface.ParserOptions.md

---
url: /reference/Interface.ParserOptions.md
---
# Interface: ParserOptions

Options for parsing a code

## Extends

* `ParserOptions`

## Properties

### astType?

* **Type**: `"js"` | `"ts"`
* **Optional**

Return an AST which includes TypeScript-related properties, or excludes them.

`'js'` is default for JS / JSX files.
`'ts'` is default for TS / TSX files.
The type of the file is determined from `lang` option, or extension of provided `filename`.

#### Inherited from

`BindingParserOptions.astType`

***

### lang?

* **Type**: `"js"` | `"jsx"` | `"ts"` | `"tsx"` | `"dts"`
* **Optional**

Treat the source text as `js`, `jsx`, `ts`, `tsx` or `dts`.

#### Inherited from

`BindingParserOptions.lang`

***

### preserveParens?

* **Type**: `boolean`
* **Optional**

Emit `ParenthesizedExpression` and `TSParenthesizedType` in AST.

If this option is true, parenthesized expressions are represented by
(non-standard) `ParenthesizedExpression` and `TSParenthesizedType` nodes that
have a single `expression` property containing the expression inside parentheses.

#### Default

```ts
true
```

#### Inherited from

`BindingParserOptions.preserveParens`

***

### range?

* **Type**: `boolean`
* **Optional**

Controls whether the `range` property is included on AST nodes.
The `range` property is a `[number, number]` which indicates the start/end offsets
of the node in the file contents.

#### Default

```ts
false
```

#### Inherited from

`BindingParserOptions.range`

***

### showSemanticErrors?

* **Type**: `boolean`
* **Optional**

Produce semantic errors with an additional AST pass.
Semantic errors depend on symbols and scopes, where the parser does not construct.
This adds a small performance overhead.

#### Default

```ts
false
```

#### Inherited from

`BindingParserOptions.showSemanticErrors`

***

### sourceType?

* **Type**: `"module"` | `"commonjs"` | `"script"` | `"unambiguous"`
* **Optional**

Treat the source text as `script` or `module` code.

#### Inherited from

`BindingParserOptions.sourceType`

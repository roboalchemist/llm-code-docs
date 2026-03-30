# Source: https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content/text-variables-7ecb50/

---
title: "Text Variables"
description: "Use variables in scene documents to update content automatically."
platform: ios
url: "https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content/text-variables-7ecb50/"
---

> This is one page of the CE.SDK iOS documentation. For a complete overview, see the [iOS Documentation Index](https://img.ly/docs/cesdk/ios.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/ios/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/ios/guides-8d8b00/) > [Create and Use Templates](https://img.ly/docs/cesdk/ios/create-templates-3aef79/) > [Insert Dynamic Content](https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content-53fad7/) > [Text Variables](https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content/text-variables-7ecb50/)

---

Text variables let you design once and personalize infinitely.
Instead of writing “Erika Mustermann” directly into a template, you insert the token `{{fullName}}`. At render time CE.SDK swaps that token for any value you supply in code or via an external data source. This is ideal for certificates, mail-merge, and multichannel campaigns. In this guide, you’ll learn how to set up variables in text areas at design time and populate them with dynamic text at run time.

## What You’ll Learn

- Add a variable to a text block and to a scene.
- Change the value of a variable at runtime.
- Detect whether a block references any variables.
- Discover and list all variables in a scene.

## When to Use It

- You need mass personalization (names, codes, dates) across many exports.
- The layout is fixed but copy changes per audience or locale.
- You’re merging external data (CSV/JSON/API) into a single design.
- You want a locked layout where only specific text is editable.
- You run A/B tests or multi-variant creatives with consistent design.
- You ship reusable templates across campaigns and need quick reset between runs.

### Adding a Token to a Text Block

The most common use case for variables is to create scenes and templates with text blocks where the value of the text is dynamic by:

- Locking at design time:
  - Font
  - Position
  - Other properties
- Updating the text value at runtime.
- Preserving any styling applied to the block.

To place a variable onto the canvas:

1. Add a text block to a scene or template document.
2. Use curly bracket notation with the variable name.

![Document with a dog-name and done-date variable.](assets/variables-ios-160-1.png)

In the preceding image:

- \{\{dog-name}} and \{\{done-date}} are **tokens** acting as placeholders in the text.
- The text references variables with the keys `dog-name` and `done-date`.

Tokens work this way:

- They **don’t create variables**.
- They mark **where a variable’s value appears** if a value exists in the engine’s variable store.

A token can be part of a longer string. For example: "Greetings, \{\{dog-name}}" renders as "Greetings, Ruth" when the `dog-name` variable is set to "Ruth".

Another way to bind a variable to a token is in code:

```swift
let textBlockId = try engine.block.create(.text)
try engine.block.setString(
  textBlockId,
  property: "text/text",
  value: "Hello {{fullName}}!"
)
```

### Adding a Variable to a Scene

A **variable store** is a key/value store you can use for any purpose. Whenever the engine loads a scene or a template:

- It checks for tokens in the template.
- If it finds tokens that match variable names in the store, the engine replaces the tokens with the values of the matching variables.

Your app can manipulate the variables outside the scope of any scene document. Changing the value of a variable that’s associated with a token immediately updates the value in the document.

> **Note:** Tokens in a document **are not** the same as variables. Though the engine automatically replaces tokens with variable values, it **does not** automatically add tokens to the variable store as variables.

Create or update a variable using the `.set` command. Upon creation, the engine automatically checks any open documents for matching tokens.

```swift
try engine.variable.set(key: "fullName", value: "Marie Dupont")
```

Read a variable using `.get`.

```swift
let name = try engine.variable.get(key: "fullName") // "Marie Dupont"
```

Remove a variable using `.remove`

```swift
try engine.variable.remove(key: "city")
```

Removing a variable that’s associated with a token causes the UI to display the name of the token. To hide a token, set its variable value to an empty string.

### Determine if a Block References a Variable

For any given block, your code can determine if it has an associated variable.

```swift
let hasTokens = try engine.block.referencesAnyVariables(textBlockId)
```

To find all the variables set in the engine:

```swift
let allVariables = try engine.variable.findAll()
```

This **won’t** find tokens in a document. To find all tokens, your code needs to:

1. Traverse the block tree.
2. Look for tokens.

A regular expression is a good way to extract them. Here is a possible strategy:

```swift
func extractVariableKeys(from text: String) -> [String] {
  // matches {{foo}}, {{user.name}}, {{A-1}}
  let pattern = #"\{\{\s*([A-Za-z0-9_.\-]+)\s*\}\}"#
  let regex = try! NSRegularExpression(pattern: pattern)
  let nsrange = NSRange(text.startIndex..<text.endIndex, in: text)
  return regex.matches(in: text, range: nsrange).compactMap { match in
    guard match.numberOfRanges >= 2,
      let r = Range(match.range(at: 1), in: text) else { return nil }
    return String(text[r])
  }
}
```

The preceding function:

1. Searches a `String` for text enclosed in double curly brackets.
2. Maps each match to a new array entry.
3. Returns the new array.

**Remember**, a text block might contain more than one token.

An example workflow could be:

1. Your code traverses the block tree.
2. It extracts all of the token names.
3. You create UI to let the user populate them or manipulate them in some other way.

Because the variables in the engine are a key/value store. Once your code has the `String` for a variable name, it can read and set values for the variable.

Here’s a minimal code example for traversing the tree and extracting any tokens:

```swift
for id in try engine.block.find(byType: .text) {
  if let s = try? engine.block.getString(id, property: "text/text") {
    print(extractVariableKeys(from: s))
  }
}
```

## Troubleshooting

**❌ `findAll()` Returns an Empty Array**:

- `findAll()` lists the keys in an engine’s variable store. Tokens like `{{dog-name}}` in text blocks aren’t automatically registered.
- Either seed known keys at load time with `set(key:value:)` or scan text blocks for tokens and call set with empty defaults.

**❌ `referencesAnyVariables(_:)` Always Returns `false`**:

- Make sure you’re checking the correct block id and property. A parent block id doesn’t check it’s children.
- When using `styled/rich text` or another text-bearing property, make sure you are using that property to filter blocks.

**❌ No Visual Change When setting `textVariableHighlightColor`**:

- iOS prebuilt editors don’t show token highlights. Only web editors have that affordance.
- If you need a cue for users, add your own overlay or styling.

**❌ Token Appears Verbatim at Runtime**:

- Variable isn’t registered with the engine.
- Call `set(key:value)` before preview or export. If you want to hide optional token names, set the value to `""` and handle any surrounding punctuation.

**❌ Regex Misses Some Tokens**:

- Look for smart or unicode braces or spaces inside of tokens.
- Normalize the string before processing and ensure your regular expression pattern tolerates whitespace by using `s*` in the pattern.
- Avoid using braces in regular typography.

**❌ Variables Disappear on Relaunch**:

- Variables persist with the scene upon save. If they’re only set in memory and the document isn’t saved, they won’t appear next time.
- Save the scene after seeding variables, or re-seed variables on load.

**❌ Token is Still Visible after `.remove(key:)`**:

- Removing a variable from the store doesn’t remove tokens from a document. When the engine cannot resolve a token to a variable, the token text gets displayed.
- Either re-add the variable with a value or set it to `""` if you want the token location to disappear from the layout.

## Next Steps

Variables provide a lightweight, scene-scoped key–value store that CE.SDK resolves inside text properties at render time. Use tokens (`{{key}}`) to bind content in your text blocks, and manage values programmatically through `engine.variable`. For production flows, choose one of two patterns:

- Store-first: Seed known keys on load, drive a simple form, validate, export.
- Reference-first: Scan for tokens, register keys, populate values, validate, export.

Both patterns keep layout stable while allowing large-scale personalization without duplicating designs.

Now that you can replace text, here are some related topics to explore:

- Swap entire media blocks (images/video/audio) using [placeholders to replace content](https://img.ly/docs/cesdk/ios/create-templates/add-dynamic-content/placeholders-d9ba8a/).



---

## More Resources

- **[iOS Documentation Index](https://img.ly/docs/cesdk/ios.md)** - Browse all iOS documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/ios/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/ios/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support

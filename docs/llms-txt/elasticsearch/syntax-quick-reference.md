# Source: https://www.elastic.co/docs/contribute-docs/syntax-quick-reference

﻿---
title: Syntax quick reference
description: Elastic documentation uses a custom implementation of MyST Markdown with extended syntax for directives, metadata, and tagging. This page offers quick...
url: https://www.elastic.co/docs/contribute-docs/syntax-quick-reference
---

# Syntax quick reference
Elastic documentation uses a custom implementation of [MyST Markdown](https://mystmd.org/) with extended syntax for directives, metadata, and tagging.
This page offers quick guidance on commonly used syntax elements. Elements are in alphabetical order.
For the full syntax reference, go to [elastic.github.io/docs-builder/syntax/](https://elastic.github.io/docs-builder/syntax/).
<tip>
  Contributing to [elastic.co/guide](https://www.elastic.co/guide/index.html)? Refer to [Contribute to `elastic.co/guide` (Asciidoc)](https://www.elastic.co/docs/contribute-docs/asciidoc-guide).
</tip>


## Admonitions

Use admonitions to caution users, or to provide helpful tips or extra information.
<dropdown title="Types">
  These examples show the syntax first, followed by the rendered admonition.**Warning**
  ```markdown
      :::{warning}
      Users could permanently lose data or leak sensitive information.
      :::
  ```

  <warning>
    Users could permanently lose data or leak sensitive information.
  </warning>
  **Important**
  ```markdown
      :::{important}
      Less dire than a warning. Users might encounter issues with performance or stability.
      :::
  ```

  <important>
    Less dire than a warning. Users might encounter issues with performance or stability.
  </important>
  **Note**
  ```markdown
      :::{note}
      Supplemental information that provides context or clarification.
      :::
  ```

  <note>
    Supplemental information that provides context or clarification.
  </note>
  **Tip**
  ```markdown
      :::{tip}
      Advice that helps users work more efficiently or make better choices.
      :::
  ```

  <tip>
    Advice that helps users work more efficiently or make better choices.
  </tip>
  **Custom**
  ```markdown
      :::{admonition} Special note
      Custom admonition with custom label.
      :::
  ```

  <admonition title="Special note">
    Custom admonition with custom label.
  </admonition>
</dropdown>

**DOs**
✅ **Do:** Use custom admonitions as needed
**DON'Ts**
❌ **Don't:** Stack admonitions
❌ **Don't:** Overload a page with too many admonitions
For more details, refer to [Admonitions](https://elastic.github.io/docs-builder/syntax/admonitions).


---


## Anchors

A default anchor is automatically created for each [heading](#headings), in the form `#heading-text` (lowercase, with spaces converted to hyphens and special characters removed). To create a custom anchor, add it in square brackets at the end of a heading: `[my-better-anchor]`
<dropdown title="Default anchor">
  ```markdown
  #### Hello world!
  <!-- Auto-generated default anchor: #hello-world -->
  ```
</dropdown>

<dropdown title="Custom anchor">
  ```markdown
  #### Hello world! [get-started]
  ```
</dropdown>

**DOs**
✅ **Do:** Create custom anchors for repeated structural headings like "Example request"
**DON'Ts**
❌ **Don't:** Include punctuation marks in custom anchors
❌ **Don't:** Define custom anchors in text that is not a heading
For more details, refer to [Links](https://elastic.github.io/docs-builder/syntax/links#same-page-links-anchors).


---


## Applies to

Use `applies_to` metadata to tag content for specific contexts, for example whether a feature is available on certain products, versions, or deployment types.
This metadata enables you to write [cumulative documentation](https://www.elastic.co/docs/contribute-docs/how-to/cumulative-docs), because Elastic no longer publishes separate docs sets for every minor release.
**Example: Section tag**
<dropdown title="Syntax">
  ```markdown
  # Stack-only content
  ```{applies_to}
  stack:
  ```
  ```
</dropdown>

<dropdown title="Output">
  #### Stack-only content

  <applies-to>
    - Elastic Stack: Generally available
  </applies-to>
</dropdown>

For full syntax and more examples, refer to [the `applies_to` documentation](https://elastic.github.io/docs-builder/syntax/applies).
<tip>
  The syntax for `applies_to` metadata differs depending on whether it's added at the [page level](https://elastic.github.io/docs-builder/syntax/applies/#page-level) (in frontmatter), [section level](https://elastic.github.io/docs-builder/syntax/applies/#section-level) (after a heading), or [inline](https://elastic.github.io/docs-builder/syntax/applies/#inline-level).
</tip>

<tip>
  The `applies_to` tags are scope signals for readers, not comprehensive metadata. If a page contains general information that applies to all contexts, it doesn't need tags.
</tip>

**DOs**
✅ **Do:** Define a set of [page-level tags](https://elastic.github.io/docs-builder/syntax/applies#page-level) in a front matter block
✅ **Do:** Add section-level tags in an `{applies_to}` [directive](https://elastic.github.io/docs-builder/syntax/applies#section-level) after a heading
✅ **Do:** Indicate versions (`major.minor`) and release phases like `beta`
✅ **Do:** Describe critical patch-level differences in prose rather than using version tags
**DON'Ts**
❌ **Don't:** Add `applies_to` tags to general, broadly applicable content
❌ **Don't:** Overload pages with repetitive tags


---


## Applies switch

The `applies-switch` directive creates tabbed content where each tab displays an `applies_to` badge instead of a text title. Use this to show content that varies by deployment type or version. All applies switches on a page automatically sync together.
<dropdown title="Syntax">
  ```markdown
  ::::{applies-switch}

  :::{applies-item} stack: ga 9.0+
  Content for Stack
  :::

  :::{applies-item} serverless: ga
  Content for Serverless
  :::

  ::::
  ```
</dropdown>

<dropdown title="Output">
  <applies-switch>
    <applies-item title="stack: ga 9.0+" applies-to="Elastic Stack: Generally available since 9.0">
      Content for Stack
    </applies-item>

    <applies-item title="serverless: ga" applies-to="Elastic Cloud Serverless: Generally available">
      Content for Serverless
    </applies-item>
  </applies-switch>
</dropdown>

**DOs**
✅ **Do:** Use when content varies significantly by deployment type or version
✅ **Do:** Combine multiple `applies_to` definitions using YAML object notation: `{ ece: ga 4.0+, ess: ga }`
For more details, refer to [Applies switch](https://elastic.github.io/docs-builder/syntax/applies-switch).


---


## Code blocks

Multi-line blocks for code, commands, configuration, and similar content. Use three backticks ````` on separate lines to start and end the block. For syntax highlighting, add a language identifier after the opening backticks.
<dropdown title="Syntax">
  ```markdown
      ```yaml
      server.host: "0.0.0.0"
      elasticsearch.hosts: ["http://localhost:9200"]
      ```
  ```
</dropdown>

<dropdown title="Output">
  ```yaml
  server.host: "0.0.0.0"
  elasticsearch.hosts: ["http://localhost:9200"]
  ```
</dropdown>

**DOs**
✅ **Do:** Include code blocks within lists or other block elements as needed
✅ **Do:** Add language identifiers like `yaml`, `json`, `bash`
**DON'Ts**
❌ **Don't:** Place code blocks in admonitions
❌ **Don't:** Use inline code formatting (single backticks) for multi-line content
For more details, refer to [Code](https://elastic.github.io/docs-builder/syntax/code).


---


## Code callouts

Inline annotations that highlight or explain specific lines in a code block.

### Explicit callout

To explicitly create a code callout, add a number marker in angle brackets (`<1>`, `<2>`, and so on) at the end of a line. Add the corresponding callout text below the code block, in a numbered list that matches the markers.
<dropdown title="Syntax">
  ```markdown
      ```json
      {
        "match": {
          "message": "search text" <1>
        }
      }
      ```
      1. Searches the `message` field for the phrase "search text"
  ```
</dropdown>

<dropdown title="Output">
  ```json
  {
    "match": {
      "message": "search text" 
    }
  }
  ```
</dropdown>


### Automatic (comment-based) callout

Add comments with `//` or `#` to automatically create callouts.
<dropdown title="Syntax">
  ```markdown
    ```json
    {
      "match": {
        "message": "search text" // Searches the message field
      }
    }
    ```
  ```
</dropdown>

<dropdown title="Output">
  ```json
  {
    "match": {
      "message": "search text"
    }
  }
  ```
</dropdown>

**DOs**
✅ **Do:** Keep callout text short and specific
✅ **Do:** Use only one type of callout per code block (don't mix [explicit](#explicit-callout) and [automatic](#magic-callout))
✅ **Do:** Make sure there's a corresponding list item for each explicit callout marker in a code block
**DON'Ts**
❌ **Don't:** Overuse callouts — they can impede readability
For more details, refer to [Code callouts](https://elastic.github.io/docs-builder/syntax/code#code-callouts).


---


## Comments

Use `%` to add single-line comments. Use HTML-style `<!--` and `-->` for multi-line comments.
<dropdown title="Syntax">
  ```markdown
      % This is a comment
      This is regular text

      <!--
      so much depends
      upon
      a multi-line
      comment
      -->
      Regular text after multi-line comment
  ```
</dropdown>

<dropdown title="Output">
  This is regular textRegular text after multi-line comment
</dropdown>

**DOs**
✅ **Do:** Add a space after the `%` in single-line comments
**DON'Ts**
❌ **Don't:** Use `#` or `//` for comments (reserved for [magic callouts](#magic-callout))


---


## Dropdowns

Collapsible blocks for hiding and showing content.
<dropdown title="Syntax">
  ```markdown
      :::{dropdown} Title or label
      Collapsible content
      :::
  ```
</dropdown>

<dropdown title="Output">
  <dropdown title="Title or label">
    Collapsible content
  </dropdown>
</dropdown>

**DOs**
✅ **Do:** Use dropdowns for text, lists, images, code blocks, and tables
✅ **Do:** Add `:open:` to auto-expand a dropdown by default
**DON'Ts**
❌ **Don't:** Use dropdowns for very long paragraphs or entire sections
For more details, refer to [Dropdowns](https://elastic.github.io/docs-builder/syntax/dropdowns).


---


## Footnotes

Add notes and references without cluttering the main text. Footnotes are automatically numbered and linked. References appear as superscript numbers in the text, and the footnote content renders at the bottom of the page.
<dropdown title="Syntax">
  ```markdown
  Here's a simple footnote[^fn-1] and a named one[^fn-note].

  [^fn-1]: This is the first footnote.
  [^fn-note]: This footnote uses a named identifier.
  ```
</dropdown>

<dropdown title="Output">
  Here's a simple footnote and a named one.
</dropdown>

**DOs**
✅ **Do:** Use descriptive identifiers like `[^api-note]` for maintainability
✅ **Do:** Keep footnotes focused on a single piece of information
✅ **Do:** Place footnote definitions at the document level, not inside directives
**DON'Ts**
❌ **Don't:** Use footnotes for content important enough to be in the main text
❌ **Don't:** Write very long footnotes — consider using the main text instead
❌ **Don't:** Define footnotes inside tab-sets, admonitions, or other containers
For more details, refer to [Footnotes](https://elastic.github.io/docs-builder/syntax/footnotes).


---


## Headings

Headings mark the title of a page or section. To create a heading, add number signs `#` at the beginning of the line (one `#` for each heading level).
<dropdown title="Syntax">
  ```markdown
  # Heading 1
  ## Heading 2
  ### Heading 3
  #### Heading 4
  ```
</dropdown>

<dropdown title="Output">
  ![Heading levels](https://www.elastic.co/docs/contribute-docs/images/headings.png)
</dropdown>

**DOs**
✅ **Do:** Start every page with a Heading 1
✅ **Do:** Use only one Heading 1 per page
✅ **Do:** Define custom anchors for repeated headings
**DON'Ts**
❌ **Don't:** Use headings in tabs or dropdowns
❌ **Don't:** Go deeper than Heading 4
For more details, refer to [Headings](https://elastic.github.io/docs-builder/syntax/headings).


---


## Images

Standard Markdown image syntax: `![alt text]` in square brackets, followed by the image path in parentheses.
<dropdown title="Syntax">
  ```markdown
  ![Bear emerging from hibernation](images/bear.png)
  ```
</dropdown>

<dropdown title="Output">
  ![Bear emerging from hibernation](https://www.elastic.co/docs/contribute-docs/images/bear.png)
</dropdown>

**DOs**
✅ **Do:** Store images in a centralized directory
✅ **Do:** Follow v3 [best practices for screenshots](/docs/contribute-docs/how-to/cumulative-docs/badge-placement#images)
✅ **Do:** Specify `:screenshot:` in an [image directive](https://elastic.github.io/docs-builder/syntax/images#screenshots) to add a border
**DON'Ts**
❌ **Don't:** Use lots of UI screenshots that create a maintenance burden
❌ **Don't:** Include confidential info or PII in an image
❌ **Don't:** Add a drop shadow or torn edge effect
For more details, refer to [Images](https://elastic.github.io/docs-builder/syntax/images).


---


## Icons

Include icons inline using the `{icon}`icon-name`` syntax.
<dropdown title="Syntax">
  ```markdown
  Click the {icon}`gear` **Settings** icon.
  Status: {icon}`checkCircle` Success | {icon}`warning` Warning | {icon}`error` Error
  ```
</dropdown>

<dropdown title="Output">
  Click the `gear` **Settings** icon.Status: `checkCircle` Success | `warning` Warning | `error` Error
</dropdown>

**DOs**
✅ **Do:** Use icons in headings, lists, tables, and paragraphs
✅ **Do:** Pair icons with descriptive text for accessibility
**DON'Ts**
❌ **Don't:** Use icons without context or explanation
❌ **Don't:** Overuse icons — they should enhance, not clutter
For more details and the full icon list, refer to [Icons](https://elastic.github.io/docs-builder/syntax/icons).


---


## Inline formatting

Elastic Docs v3 supports standard Markdown inline formatting.

| Markdown              | Output            |
|-----------------------|-------------------|
| **strong**            | **strong**        |
| _emphasis_            | _emphasis_        |
| `monospace`           | `monospace`       |
| ~~strikethrough~~     | ~~strikethrough~~ |
| `\*escaped symbols\*` | *escaped symbols* |

**DOs**
✅ **Do:** Use `_emphasis_` to introduce a term
✅ **Do:** Use `monospace` in headings and other elements as needed
**DON'Ts**
❌ **Don't:** Overuse `**strong**` or `_emphasis_` — aim for readability


---


## Keyboard markup

Represent keyboard keys and shortcuts using the `{kbd}`key-name`` syntax. Combine keys with `+` and show alternatives with `|`.
<dropdown title="Syntax">
  ```markdown
  Press {kbd}`enter` to submit.
  Use {kbd}`cmd+shift+p` to open the command palette.
  Use {kbd}`ctrl|cmd+c` to copy text.
  ```
</dropdown>

<dropdown title="Output">
  Press <kbd>Enter</kbd> to submit.Use <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>p</kbd> to open the command palette.Use <kbd>Ctrl / Cmd</kbd> + <kbd>c</kbd> to copy text.
</dropdown>

**DOs**
✅ **Do:** Use keyword equivalents `plus` and `pipe` to render those literal keys
**DON'Ts**
❌ **Don't:** Use raw `+` or `|` characters when you mean to display them as keys
For more details and available key names, refer to [Keyboard markup](https://elastic.github.io/docs-builder/syntax/keyboard).


---


## Links

Standard Markdown links to doc pages, sections (anchors), or external content. Prefer absolute paths for links within the doc set.
<dropdown title="Syntax">
  ```markdown
      [link text](/absolute/file.md#anchor)
      [link text](https://external-site.com)
      [link text](other-repo://path/file.md)
      (#same-page-anchor)
  ```
</dropdown>

**DOs**
✅ **Do:** Use inline formatting in link text: `[**bold link**](https://elastic.github.io/docs-builder/syntax/bold-page)`
✅ **Do:** Autogenerate link text from the page or section title: `[](https://elastic.github.io/docs-builder/syntax/use-title#section)`
✅ **Do:** Define a custom [anchor](#anchors) by adding `[anchor-text]` at the end of a heading line
**DON'Ts**
❌ **Don't:** Use unclear, inaccessible link text like "click here" or "this"
❌ **Don't:** Include terminal punctuation in link text
For more details, refer to [Links](https://elastic.github.io/docs-builder/syntax/links).


---


## Lists

Standard Markdown ordered (numbered) and unordered (bulleted) lists. Indent with four spaces to nest paragraphs and other elements under a list item. Unordered lists can start with hyphens `-`, asterisks `*`, or plus signs `+`.
<dropdown title="Syntax">
  ```
      - Unordered item 1
      ····Paragraph within item 1
      - Unordered item 2
  ```

  ```
  1. Ordered item 1
  2. Ordered item 2
  ```
</dropdown>

**DOs** 
✅ **Do:** Add code blocks, images, admonitions, and other content within a list item
✅ **Do:** Nest lists, mixing ordered and unordered as needed
✅ **Do:** Use parallel structure and phrasing in list items
✅ **Do:** Capitalize only the first word of list items (sentence case)
✅ **Do:** Use terminal punctuation consistently and only for complete sentences
**DON'Ts** 
❌ **Don't:** Use lists solely for layout purposes 
❌ **Don't:** Use lists for structured data or comparisons — use tables instead
For more details, refer to [Lists](https://elastic.github.io/docs-builder/syntax/lists).


---


## Math

Render mathematical expressions using LaTeX syntax with the `{math}` directive. Expressions are rendered client-side using KaTeX.
<dropdown title="Syntax">
  ```markdown
  :::{math}
  E = mc^2
  :::
  ```
</dropdown>

<dropdown title="Output">
  `E = mc^2`
</dropdown>

**DOs**
✅ **Do:** Use LaTeX display delimiters (`\[` `\]`) or environments (`\begin{align}`) for complex expressions
✅ **Do:** Add labels with `:label:` for cross-referencing
For more details, refer to [Math](https://elastic.github.io/docs-builder/syntax/math).


---


## Mermaid diagrams

Create diagrams using [Mermaid](https://mermaid.js.org/) with standard fenced code blocks. Diagrams are rendered client-side in the browser.
<dropdown title="Syntax">
  ```markdown
  ```mermaid
  flowchart LR
      A[Start] --> B{Decision}
      B -->|Yes| C[Action]
      B -->|No| D[End]
  ```
  ```
</dropdown>

<dropdown title="Output">
  ```mermaid
  flowchart LR
      A[Start] --> B{Decision}
      B -->|Yes| C[Action]
      B -->|No| D[End]
  ```
</dropdown>

**DOs**
✅ **Do:** Use different types of diagrams, such as flowcharts, sequence diagrams, state diagrams, and so on
✅ **Do:** Keep diagrams focused on a single concept
✅ **Do:** Summarize complex diagrams in accompanying text
**DON'Ts**
❌ **Don't:** Use diagrams as the only way to convey important information
❌ **Don't:** Create overly complex diagrams with too many elements
For more details, refer to [Mermaid diagrams](https://elastic.github.io/docs-builder/syntax/mermaid).


---


## Navigation title

Optional [front matter](https://elastic.github.io/docs-builder/syntax/frontmatter) element that sets a custom title for navigation items. Appears in the left navigation (table of contents), breadcrumbs, and previous/next links. For information about page titles, refer to [Headings](#headings).
<dropdown title="Syntax">
  Page front matter (YAML):
  ```yaml
  ---
  navigation_title: "Minimalist identifier"
  ---
  ```
  Page title (Markdown H1):
  ```markdown
  # Full descriptive page title with product context
  ```
</dropdown>

<dropdown title="Output">
  ![Rendered nav title](https://www.elastic.co/docs/contribute-docs/images/nav-title.png)
</dropdown>

**DOs**
✅ **Do:** Use active phrasing and shorter forms
✅ **Do:** Make sure the navigation title clearly identifies the page topic
✅ **Do:** Omit product names that appear in the full H1 page title
**DON'Ts**
❌ **Don't:** Duplicate the H1 page title
❌ **Don't:** Use a long navigation title or lots of punctuation
❌ **Don't:** Abbreviate with periods or ellipses
For more details, refer to [Title](https://elastic.github.io/docs-builder/syntax/titles).


---


## Substitutions

Key-value pairs that define reusable variables. They help ensure consistency and enable short forms. To use a substitution (or "sub"), surround the key with double curly brackets: `{{variable}}`

### Define a sub

<dropdown title="Syntax">
  In `docset.yml`:
  ```
  subs:
    ccs: "cross-cluster search"
    ech: "Elastic Cloud Hosted"
    kib: "Kibana"
  ```
</dropdown>


### Use a sub

This example uses the sub defined in `docset.yml` above.
<dropdown title="Syntax">
  In `myfile.md`:
  ```
  {{ech}} supports most standard {{kib}} settings.
  ```
</dropdown>

<dropdown title="Output">
  Elastic Cloud Hosted supports most standard Kibana settings.
</dropdown>

**DOs** 
✅ **Do:** Check the global `docset.yml` file for existing product and feature name subs
✅ **Do:** Use substitutions in code blocks by setting `subs=true`  
✅ **Do:** Define new page-specific substitutions as needed
**DON'Ts**
❌ **Don't:** Override a `docset.yml` sub by defining a page-level sub with the same key (causes build errors)
❌ **Don't:** Use substitutions for common words that don't need to be standardized
For more details, refer to [Substitutions](https://elastic.github.io/docs-builder/syntax/substitutions).


---


## Stepper

Steppers provide a visual representation of sequential steps for tutorials or guides. Use steppers instead of numbered section headings when documenting complex procedures. Step titles automatically appear in the page's table of contents.
<dropdown title="Syntax">
  ```markdown
  :::::{stepper}

  ::::{step} Install
  First install the dependencies.
  ::::

  ::::{step} Build
  Then build the project.
  ::::

  ::::{step} Done
  ::::

  :::::
  ```
</dropdown>

<dropdown title="Output">
  <stepper>
    <step title="Install">
      First install the dependencies.
    </step>

    <step title="Build">
      Then build the project.
    </step>

    <step title="Done">
    </step>
  </stepper>
</dropdown>

**DOs**
✅ **Do:** Use steppers for multi-step tutorials or complex procedures
✅ **Do:** Add `:anchor:` to override the default anchor for a step
**DON'Ts**
❌ **Don't:** Nest steppers inside tabs, dropdowns, or other containers if you want step titles in the ToC
For more details, refer to [Stepper](https://elastic.github.io/docs-builder/syntax/stepper).


---


## Tabs

Block element that displays content in switchable tabs to help users find the right context (such as deployment type or programming language). [Synced tab groups](https://elastic.github.io/docs-builder/syntax/tabs#tab-groups) are supported.
<dropdown title="Syntax">
  ```markdown
      ::::{tab-set}

      :::{tab-item} Tab 1 title
      Tab 1 content
      :::

      :::{tab-item} Tab 2 title
      Tab 2 content
      :::

      ::::
  ```
</dropdown>

<dropdown title="Output">
  <tab-set>
    <tab-item title="Tab 1 title">
      Tab 1 content
    </tab-item>

    <tab-item title="Tab 2 title">
      Tab 2 content
    </tab-item>
  </tab-set>
</dropdown>

**DOs**
✅ **Do:** Use clear, descriptive tab labels
✅ **Do:** Make sure all tabs have the same type of content and similar goals
✅ **Do:** Keep tab content scannable and self-contained (don't make users switch tabs to follow steps or compare content)
✅ **Do:** Include other block elements in tabs, like [admonitions](#admonitions)
**DON'Ts**
❌ **Don't:** Nest tabs
❌ **Don't:** Split step-by-step procedures across tabs
❌ **Don't:** Use more than 6 tabs (use as few as possible)
❌ **Don't:** Use tabs in [dropdowns](#dropdowns)
For more details, refer to [Tabs](https://elastic.github.io/docs-builder/syntax/tabs).


---


## Tables

Standard table layout for structured data. Automatically scrolls horizontally if needed. The **header** row is optional.
<dropdown title="Syntax">
  ```markdown
      | Header | Header |
      | ------ | ------ |
      | Data   | Info   |
      | Info	 | Data   |
  ```
</dropdown>

<dropdown title="Output">
  | Header | Header |
  |--------|--------|
  | Data   | Info   |
  | Info   | Data   |
</dropdown>

**DOs**
✅ **Do:** Use leading and trailing pipes for clarity
✅ **Do:** Add spaces for readability (they're trimmed)
✅ **Do:** Keep cell content scannable and parallel
✅ **Do:** Use standard Markdown text alignment when necessary (`:-- --: :--:`)
**DON'Ts**
❌ **Don't:** Insert block elements or multiple paragraphs in a table cell
❌ **Don't:** Use a table solely for position or spacing purposes
For more details, refer to [Tables](https://elastic.github.io/docs-builder/syntax/tables).This is the first footnote.This footnote uses a named identifier.
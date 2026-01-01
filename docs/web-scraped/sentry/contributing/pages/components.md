---
---
title: MDX Components
---
---

## Alert

Render an alert (sometimes called a callout) to highlight important information.

  This is an info alert. Use this to emphasize information that users should
  read.

  This is a warning alert. Use this to alert users to potential risks they
  should be aware of.

  This is a success alert. Use this to provide optional information that can
  help users be more successful.

  This is an alert without a title. `warning` alerts should always have titles
  to emphasize their importance.

  This is a multi-line alert without a title. Keep information brief and to the
  point. If this is challenging, consider whether the topic needs documentation
  on another page or if using the [Expandable](#expandable) component would be a
  better fit.

  <ul>
    <li>You can create lists</li>
    <li>and **format** _your_ `text`</li>
  </ul>

```markdown {tabTitle:Info}

This is an info alert.

```

```markdown {tabTitle:Warning}

This is a warning alert.

```

```markdown {tabTitle:Success}

This is a success alert.

```

```markdown {tabTitle:No Title}

This is an info alert without a title.

```

Attributes:

- `title` (string) - optional
- `level` (string: `'info' | 'warning' | 'success'`) - optional, defaults to `'info'`

**Where to place alerts:**

Make sure your alerts aren't breaking the flow of the content. For example, don't put an alert between two paragraphs that explain a single concept. Use alerts sparingly; too many alerts on a single page can be overwhelming.

**When to use which alert level:**

- **Info**: Use this to emphasize information that users should read. For example:
  - information needed for users to succeed
  - information you'd typically wrap in a note callout
- **Warning**: Use this to alert users to potential risks they should be aware of. For example:

  - warnings about potential errors, such as ones caused by common oversights in project configuration
  - warnings regarding breaking changes

  Best practices:

  - always use a title with this alert level

- **Success**: Use this to provide optional information that can help users be more successful. For example:
  - information that helps improve an already successful task, such as a link to additional reading material
  - tips for best practices

## Arcade embeds

Render an [Arcade](https://arcade.software) embed.

```markdown {tabTitle:Example}

```

Attributes:

- `src` (string) - the URL of the Arcade embed

## Expandable

Render an expandable section to provide additional information to users on demand.

  This is an expandable section in an `'info'` alert style. Use this to provide
  additional information that is helpful, but not crucial.

  This is an expandable section in an `'info'` alert style with a title wrapped
  in a link.

  This is an expandable section in a `'warning'` alert style. Use this to warn
  users about minor potential risks.

  This is an expandable section in a `'success'` alert style. Use this to
  provide optional information that can help users be more successful.

  ```js const foo = 'bar'; ```

```markdown {tabTitle:Example}

  This is an expandable section in an `'info'` alert style.

```

```markdown {tabTitle:Permalink}

  This is an expandable section with a permalink.

```

```markdown {tabTitle:Warning}

  This is an expandable section in a `'warning'` alert style.

```

```markdown {tabTitle:Success}

  This is an expandable section in a `'success'` alert style.

```

Attributes:

- `title` (string)
- `permalink` (boolean) - optional: wraps the title in a link and shows it in the table of contents.

**When to use expandables:**

Expandables help keep our documentation clutter-free, allowing users to focus on important information while providing them the option to explore additional relevant details.

For example, use expandables to:

- offer information that is useful to some users but not all, like troubleshooting tips
- provide background information or insights into related concepts

**Best practices**

- Write the expandable title as a question or statement to clarify what users can expect from the content within:
  - Do you want to learn more about these features?
  - Are you using Node.js version 15 or lower?
  - Advanced configuration options for XY use case.
- When you need to share important information that users should read, consider using an [alert](#alert) instead since its content is visible by default.
- Avoid overusing this component and make sure to provide valuable information that is relevant to the current topic.

## Code Blocks

Consecutive code blocks will be automatically collapsed into a tabulated container. This behavior is generally useful if you want to define an example in multiple languages:

````markdown {tabTitle:Example}
```javascript
function foo() {
  return "bar";
}
```

```python
def foo():
  return 'bar'
```
````

Sometimes you may not want this behavior. To solve this, you can either break up the code blocks with some additional text, or use the `` component.

Additionally code blocks also support `tabTitle` and `filename` properties:

````markdown {tabTitle:Example}
```javascript {tabTitle: Hello} {filename: index.js}
var foo = "bar";
```
````

You can bring attention to specific lines in a code block using the `{fromLineA-toLineB}` for ranges,
or `{lineA,lineB}` for specific lines (or a combination of the two):

```javascript {2} {tabTitle:Example}
function foo() {
  let lookat = "me";
  return "bar";
}
```

````markdown {tabTitle:Source}
```javascript {2}
function foo() {
  let lookat = "me";
  return "bar";
}
```
````

You can also highlight diffs using the `diff` language:

````markdown {tabTitle:Example}
```diff
- minus one
+ plus one
```
````

If you want to preserve syntax highlighting, you can add `diff` metadata to any code block
then annotate the diff with `+` and `-`:

```javascript {diff} {tabTitle:Example}
function foo() {
-  return "bar";
+  return "baz";
}
```

````markdown {tabTitle:Source}
```javascript {diff}
function foo() {
-  return "bar";
+  return "baz";
}
```
````

## SdkOption

Render an SDK configuration option heading with a metadata table. Option names should be written in the platform's native casing (camelCase, PascalCase, or snake_case).

If `categorySupported` is specified, it will automatically hide the option when the platform does not support it.

```markdown {tabTitle:Example}

The sample rate for error events, as a number between `0.0` and `1.0` (inclusive).

```

Attributes:

- `name` (string) - **required** - the option name in the platform's native casing
- `type` (string) - optional - data type (e.g., `boolean`, `string`, `number`)
- `defaultValue` (string) - optional - default value for the option
- `envVar` (string) - optional - associated environment variable
- `availableSince` (string) - optional - SDK version when the option was introduced
- `categorySupported` (string[]) - optional - platform categories that support this option (e.g., `["browser", "server"]`)
- `categoryNotSupported` (string[]) - optional - platform categories that don't support this option

**Platform-native casing guidelines:**

- **camelCase**: JavaScript/TypeScript (all frameworks), Java, Kotlin, Dart/Flutter, Android, Apple (iOS/macOS)
- **PascalCase**: .NET (all frameworks), Unity, Unreal, PowerShell
- **snake_case**: Python, PHP, Ruby, Go, Rust, Elixir, Native (C/C++), Godot

Use the `` component to render option names with correct casing based on the platform's `case_style` setting.

## PageGrid

Render all `next_steps` of this document or default child pages, including their `description` if available.

You can specify `next_steps` in the frontmatter of a page to include them in the grid. It supports relative paths and will automatically resolve them.

```markdown {tabTitle:Example}

```

Attributes:

- `header` (string) - optional header value to include, rendered as an H2

- `nextPages` (boolean) - only render pages which come next based on sidebar ordering

- `exclude` (string[]) - an array of pages to exclude from the grid. Specify the file name of the page, for example, `"index"` for `index.mdx`.

## PlatformContent

Render an include based on the currently selected `platform` in context.

```markdown {tabTitle:Example}

```

Attributes:

- `includePath` (string) - the subfolder within `/includes` to map to
- `platform` (string) - defaults to the `platform` value from the page context

Some notes:

- When the current platform comes from the page context and no matching include is found, the content will be hidden.

- Similar to `PlatformSection`, you can embed content in the block which will render _before_ the given include, but only when an include is available.

- A file named `_default` will be used if no other content matches.

Note: This currently causes issues with tableOfContents generation, so its recommended to disable the TOC when using it.

## PlatformIdentifier

Render terms in the correct case within the body text of a page (not in code samples) based on the platform case_style setting:

```markdown {tabTitle:Example}

```

For example, if you use ``, it will render as:

- `beforeSend` if case_style=camelCase
- `before_send` if case_style=snake_case
- `BeforeSend` if case_style=PascalCase

This component only works properly in platform pages.

## PlatformLink

Useful for linking to platform-specific content when there's not a specific platform already selected.

```markdown {tabTitle:Example}

```

This will direct users to a page where they can choose the platform, and then to the appropriate link. If they're within a page that already has an active platform, it will simply link to the appropriate page and skip the redirect.

## PlatformSection

Render a section based on the currently selected `platform` in context. When the platform is not valid, the content will be hidden.

```markdown {tabTitle:Example}

Something that applies to all platforms, but not javascript or node.

```

Attributes:

- `platform` (string) - defaults to the `platform` value from the page context
- `supported` (string[])
- `notSupported` (string[])
- `noGuides` (boolean) - hide this on all guides (takes precedence over `supported`/`notSupported`)

## Onboarding Options

If you're writing product feature specific docs, you can specify markers within code blocks that enable or disable certain parts of snippets:

  Do not copy the following code snippet, the `___PRODUCT_OPTION_START___` and
  `___PRODUCT_OPTION_END___` markers have an extra character (zero width space)
  as a workaround to make them show up correctly in the example.

````markdown
```go
  // _​__PRODUCT_OPTION_START___ performance
  // your code here
  // _​__PRODUCT_OPTION_END___ performance
```
````

the syntax uses the standard comment style of the programming language you're documenting. For example:

- TypeScript/JavaScript: `// ___PRODUCT_OPTION_START___ feature`
- Python: `# ___PRODUCT_OPTION_START___ feature`

where `feature` is the feature id (e.g. `performance`, `profiling` or `session-replay`).

The range visibility will be controlled by the `OnboardingOptionButtons` component:

```jsx diff

```

- `options` can either be either an object of this shape:

```typescript
{
  id: 'error-monitoring' | 'performance' | 'profiling' | 'session-replay',
  disabled: boolean,
  checked: boolean
}
```

or a string (one of these `id`s 👆) for convenience when using defaults.

  The underlying implementation relies on the `onboardingOptions` metadata in
  the code blocks to be valid JSON syntax.

- default values: `checked: false` and `disabled: false` (`true` for `error-monitoring`).

Example (output of the above):

```go
import (
	"fmt"
	"net/http"

	"github.com/getsentry/sentry-go"
	sentrygin "github.com/getsentry/sentry-go/gin"
	"github.com/gin-gonic/gin"
)

// To initialize Sentry's handler, you need to initialize Sentry itself beforehand
if err := sentry.Init(sentry.ClientOptions{
	Dsn: "___PUBLIC_DSN___",
  // ___PRODUCT_OPTION_START___ performance
	EnableTracing: true,
	// Set TracesSampleRate to 1.0 to capture 100%
	// of transactions for performance monitoring.
	// We recommend adjusting this value in production,
	TracesSampleRate: 1.0,
  // ___PRODUCT_OPTION_END___ performance
  // Adds request headers and IP for users,
  // visit: https://docs.sentry.io/platforms/go/data-management/data-collected/ for more info
  SendDefaultPII: true,
}); err != nil {
	fmt.Printf("Sentry initialization failed: %v\n", err)
}

// Then create your app
app := gin.Default()

// Once it's done, you can attach the handler as one of your middleware
app.Use(sentrygin.New(sentrygin.Options{}))

// Set up routes
app.GET("/", func(ctx *gin.Context) {
	ctx.String(http.StatusOK, "Hello world!")
})

// And run it
app.Run(":3000")
```

You can conditionally render content based on the selected onboarding options using the
`OnboardingOption` component

Or you can use the `hideForThisOption` prop to hide the content for the selected option.

````markdown
```jsx

  Hide this section for `profiling` option.

```
````

Example:

- toggle the `performance` option above to see the effect:

    

  ```jsx
  
    This code block is wrapped in a `OnboardingOption` component and will only
    be rendered when the `performance` option is selected.
  
  ```

    

- toggle the `profiling` option above to see the effect:

    

  ```jsx
  
    This code block is wrapped in a `OnboardingOption` component and will only
    be rendered when the `profiling` option is NOT selected.
  
  ```

    

## GitHubCodePreview

Embed and display code directly from a GitHub repository. This component fetches code from GitHub and displays it with syntax highlighting.

```jsx {tabTitle:Example}

```

Output of above:

You can also link to specific lines:

```jsx {tabTitle:With Line Numbers}

```

Output of above:

Attributes:

- `url` (string) - **required** - GitHub blob URL with optional line numbers
  - Full file: `https://github.com/owner/repo/blob/main/src/file.ts`
  - Single line: `https://github.com/owner/repo/blob/main/src/file.ts#L10`
  - Line range: `https://github.com/owner/repo/blob/main/src/file.ts#L10-L20`

**Features:**

- Automatically detects language from file extension
- Displays filename with line numbers (if specified)
- Includes a link to view the source on GitHub
- Shows loading and error states

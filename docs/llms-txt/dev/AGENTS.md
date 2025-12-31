# Source: https://dev.writer.com/AGENTS.md

# null

# Developer documentation style guide

This guide covers how to write and organize documentation for Writer's developer platform. It combines content strategy with style rules to create docs that get developers productive quickly.

> \[!NOTE]
> This guide is for developer documentation. Writer maintains a [general style guide](https://writer.styleguide.com/) for other marketing and product writing.

## Foundation

* Follow [Google's developer documentation style guide](https://developers.google.com/style) as the base reference
* When in doubt, defer to Google's guidelines unless explicitly overridden below
* Check Vale rules and dictionaries for approved terminology and product names

## Content principles

### Core philosophy

Documentation should get developers productive as quickly as possible. Every piece of content should either help them complete a task or understand why that task matters.

Developers come to documentation to solve specific problems, like implementing a feature or debugging an issue. They scan for relevant information, jump between sections, and search for targeted solutions. They don't read docs cover-to-cover.

Documentation should be organized to support this problem-solving behavior with clear headings, easy navigation, and solutions that are quick to find.

### Content strategy

#### Start with outcomes, not features

* Lead every document with what the developer will accomplish
* Explain the business value or technical benefit upfront

#### Show, don't just tell

* Lead with working code examples, not conceptual explanations
* Use realistic data and scenarios in examples
* Demonstrate the "happy path" first, then cover edge cases

#### Progressive complexity

* Start with the smallest possible working example
* Build complexity gradually in logical steps
* Each section should build on knowledge from previous sections
* Layer on configuration options and advanced features incrementally

#### Focus on success paths

* Document the most common, successful implementation patterns
* Show working examples that developers can build on
* Provide clear verification steps so developers know they're on track
* Keep examples focused on core functionality rather than edge cases

### Content organization

#### Task-oriented structure

* Organize content around what developers need to do, not product features
* Use action-oriented headings that describe outcomes ("Chat with an LLM" not "Chat completions")
* Use descriptive headings that match how people search ("Fix authentication errors" not "Error handling")
* Group related tasks together logically
* Provide clear pathways between related tasks

#### Front-load solutions

* Put the most common answer or code example at the top of each section
* Lead with "here's how to do X" before explaining background theory
* Save conceptual explanations for later sections
* Each heading should solve one specific problem

#### Scannable structure

* Keep sections short and focused on single problems
* Use visual hierarchy with code blocks, bullet points, and bold text
* Break up walls of text to support scanning behavior
* Create quick reference sections for parameters, error codes, and common patterns

#### Prose after headings (required)

**Always include one or two prose sentences immediately after a heading before any structured content** (bulleted lists, code blocks, tables, etc.). Never jump directly from a heading to a list or code sample. Orient the reader to what the section contains and provide context.

❌ Bad (no prose after heading):

```markdown  theme={null}
## Best practices
- Do this
- Do that
```

✅ Good (prose after heading):

```markdown  theme={null}
## Best practices
Best practices include proper error handling, secure authentication, and efficient rate limiting. Follow these guidelines to ensure optimal performance and security.
- Do this
- Do that
```

#### Multiple entry points

* Optimize headings for search discoverability
* Cross-link between related content when someone might land on the wrong page
* Provide multiple ways to find the same information
* Structure content to support both search and browsing

#### Content reuse and consistency

* Use snippets for content that appears on multiple pages
* Keep shared information in reusable components
* Maintain consistency in explanations across different contexts
* Update snippets in one place to propagate changes everywhere

#### Minimize context switching

* Keep related information on the same page when possible
* Avoid forcing developers to jump between concept docs and API references
* Include inline parameter descriptions next to code examples
* Provide all necessary information to complete a task in one location

#### Avoid time-sensitive language

* Limit time references to changelog entries and deprecation warnings
  * Don't use "the new feature," "recently," "as of \[date]," or "latest version", which creates documentation debt and makes content feel outdated
  * Replace "As of November 2025, this feature is available..." with "This feature is available..." or "This feature provides..."
  * Replace "The new API endpoint..." with "The API endpoint..." or "This endpoint..."
  * Replace "Recently added support for..." with "Support for..." or "This includes support for..."

## Style rules

### Document structure requirements

#### Opening pattern (required)

Every documentation file must start with:

* What the reader will learn (specific outcomes)
* Why this matters (problem solved or benefit provided)

**Example format:**

```markdown  theme={null}
This guide shows you how to [specific action]. After completing these steps, you can [concrete outcome].
```

#### Closing pattern (required)

Every documentation file must end with "Next steps" section containing:

* Links to logical follow-up tutorials
* Related features to explore
* Advanced configuration options, if applicable

### Voice and language rules

#### Always use

* Active voice ("Configure the API" not "The API should be configured")
* Direct address with "you" and "your"
* Present tense for current features ("Add the code" not "You will add the code")
* Sentence case for all headings
* Direct, imperative instructions ("Install the SDK" not "You need to install the SDK")

#### Never use

* First person plural: "we," "us," "our"
  * Creates confusion about whether "we" means Writer or you and the reader
* "Please"
  * Overly polite for technical documentation
* Future tense with "will" for current features
  * Use present tense instead, which feels more immediate and actionable
* Subjective qualifiers: "simple," "basic," "easy," "trivial," "straightforward," "just," "simply," "obviously"
  * Makes people feel inadequate if they struggle with the task
* Marketing language: "powerful," "amazing," "revolutionary," "cutting-edge," "industry-leading," "seamlessly," "effortlessly," "instantly"
  * Sounds promotional rather than helpful
* Banned corporate buzzwords: "leverage," "utilize," "optimize," "robust," "streamline," "synergy," "paradigm," "game-changer," "low-hanging fruit"
  * Vague and overused
* Hyperbolic terms or marketing speak

#### Word replacements:

* "This simple API" → "This API"
* "You need to install X" → "Install X"
* "You need to configure Y" → "Configure Y"
* "Our powerful system" → "The system"
* "Just add the code" → "Add the code"
* "We recommend" → "Use" or "Consider using"
* "This tutorial will show you" → "This tutorial demonstrates"
* "You will be able to" → "You can"
* "Please install" → "Install"
* "Please configure" → "Configure"
* "Utilize" → "Use"
* "Leverage the API" → "Use the API"
* "Click the button" → "Select the button"
* "Since you need to..." → "Because you need to..."

### Content guidelines

#### Code examples:

* **Always provide complete, independently executable examples** - code must be runnable as-is without requiring additional setup
* Always provide complete, working examples with realistic data (not foo/bar placeholders)
* Lead with working code examples, not theory or lengthy explanations
* Include necessary imports and dependencies
* Use realistic variable names and values that match actual use cases
* Add comments for non-obvious code
* Test all examples in multiple environments before publishing
* **Use `<CodeGroup>` component for multi-language examples** (cURL, Python, JavaScript)
* Show multiple language examples when relevant (Python, JavaScript, curl)
* Focus on successful implementation patterns and happy paths
* Keep related code and explanations on the same page to prevent context switching
* Use snippets for code that appears on multiple pages to maintain consistency
* **Always include one or two prose sentences after headings and before code samples** to orient the reader - never jump directly from a heading to code

##### SDK initialization pattern (required for API/SDK examples)

For all API and SDK examples (not Agent Builder), always include the complete initialization pattern. Code samples must be independently executable.

**Python initialization:**

```python  theme={null}
from writerai import Writer

# Initialize the Writer client. If you don't pass the `api_key` parameter,
# the client looks for the `WRITER_API_KEY` environment variable.
client = Writer()
```

**JavaScript initialization:**

```javascript  theme={null}
import { Writer } from "writer-sdk";

// Initialize the Writer client. If you don't pass the `api_key` parameter,
// the client looks for the `WRITER_API_KEY` environment variable.
const client = new Writer();
```

**Note:** Agent Builder examples do not follow this pattern as they use the Agent Builder framework, not the SDK directly.

##### CodeGroup component usage

Always use `<CodeGroup>` for code samples, especially for cURL, Python, and JavaScript examples. This is not necessary for standalone JSON examples or Agent Builder content (which is Python-only), but is required for:

* API endpoint examples (include cURL, Python, and JavaScript)
* SDK usage examples (include Python and JavaScript where applicable)
* Any code that shows implementation across multiple languages

**Example:**

````mdx  theme={null}
<CodeGroup>
```bash cURL
curl -X POST https://api.writer.com/v1/chat/completions \
  -H "Authorization: Bearer <API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "palmyra-x-004",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

```python Python
from writerai import Writer

# Initialize the Writer client. If you don't pass the `api_key` parameter,
# the client looks for the `WRITER_API_KEY` environment variable.
client = Writer()

response = client.chat.chat(
    model="palmyra-x-004",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

```javascript JavaScript
import { Writer } from "writer-sdk";

// Initialize the Writer client. If you don't pass the `api_key` parameter,
// the client looks for the `WRITER_API_KEY` environment variable.
const client = new Writer();

const response = await client.chat.chat({
  model: "palmyra-x-004",
  messages: [{ role: "user", content: "Hello!" }]
});
```
</CodeGroup>
````

##### Mintlify component imports

**Important:** Built-in Mintlify components like `<CodeGroup>`, `<Steps>`, `<Card>`, `<Note>`, `<Warning>`, `<Tip>`, etc. do NOT need to be imported. They are available by default in all MDX files.

**Only snippets need to be imported.** For example:

```mdx  theme={null}
import feedback from '/snippets/agent-builder-feedback.mdx';
```

#### Alt text guidelines for images

* Alt text provides a concise description that replaces the image when it's not visible
* Alt text should consider the context of the image, not just its content
* The goal: replacing every image with its alt text should not change the page's meaning

##### When to use alt text

* **Informative images**: Images that convey information not present in surrounding text
* **Functional images**: Images that serve as interactive elements (buttons, links)
* **Complex images**: Charts, diagrams, or screenshots that need description

##### When to use empty alt text

You can leave the alt text empty `![](/images/image.png)` in the following cases, so screen readers skip the image:

* **Decorative images**: Images that exist only for visual appeal
* **Redundant images**: Images whose information is already expressed in surrounding text
* **UI screenshots**: Screenshots that exist just for visual reference
* **UI icons**: Interface icons that are decorative or have text labels
* **Visual aids**: Images that support information already present in text

##### Alt text writing guidelines

* **Length**: Keep alt text under 155 characters
* **Content**: Don't include "Image of" or "Photo of" phrases
* **Punctuation**: Include punctuation for natural speech pauses
* **Format**: Use full sentences or noun phrases
* **Capitalization**: Avoid all-caps (screen readers may read each letter individually)
* **Context**: Consider the image's purpose in the page, not just visual content
* **Consistency**: Use consistent alt text for repeated images (controls, status indicators, icons)

##### Examples of good alt text

* `![Architecture of an app that's built with Apps Script](/images/architecture.png)`
* `![A card message](/images/card-message.png)`
* `![User interface showing the login form with username and password fields](/images/login-form.png)`
* `![Flowchart showing the authentication process from login to dashboard](/images/flowchart.png)`

##### Examples of when to use empty alt text

* `![](/images/icon.png)` for decorative icons that have text labels
* `![](/images/screenshot.png)` for UI screenshots that are explained in surrounding text
* `![](/images/divider.png)` for visual dividers or decorative elements

#### API documentation:

* Start with what the endpoint does
* List required parameters before optional ones
* Include realistic request/response examples
* Document error conditions and responses

#### Tutorials:

* Use numbered steps for procedures
* Include verification steps ("You should see...")
* Provide troubleshooting for common issues
* End with clear next steps

### Formatting rules

#### Numbers and punctuation:

* Always use Oxford comma in lists
* Spell out numbers 0-9, use numerals for 10+ unless it would be mixing numerals and words (ex: "there are 2 people and 15 dogs" is correct so that the numerals are not mixed with words)
* Spell out numbers that start sentences
* No periods in acronyms (UK not U.K.)
* Use "generative AI" not "GenAI" or "gen AI"

#### Headings:

* Use sentence case for all headings: "Configure authentication" not "Configure Authentication"
* Only capitalize the first word and proper nouns
* Use action-oriented headings with imperative verbs that describe what the user will do
* Be specific and descriptive about what the user will accomplish

**Action-oriented heading patterns:**

Always start headings with imperative verbs. Headings should tell users what they will do, not describe what exists.

**Common transformations:**

* ❌ "Key differences" → ✅ "Compare the APIs"
* ❌ "Parameter mapping" → ✅ "Map your parameters"
* ❌ "Accessing data" → ✅ "Access your data"
* ❌ "Migration steps" → ✅ "Migrate your code"
* ❌ "Next steps" → ✅ "Explore related features"
* ❌ "Prerequisites" → ✅ "Prepare your environment"
* ❌ "Configuration" → ✅ "Configure the settings"
* ❌ "Installation" → ✅ "Install the SDK"
* ❌ "Overview" → ✅ "Understand the basics" or "Learn about \[feature]"
* ❌ "Authentication" → ✅ "Authenticate your requests"
* ❌ "Error handling" → ✅ "Handle errors"
* ❌ "Best practices" → ✅ "Follow best practices" or "Optimize your implementation"

**Examples of correct sentence case with action verbs:**

* ✅ "Set up your development environment"
* ✅ "Send your first message"
* ✅ "Stream responses in real-time"
* ✅ "Configure authentication"
* ✅ "Access translation metadata"
* ✅ "Map your parameters"
* ❌ "Set Up Your Development Environment"
* ❌ "Chat Completions"
* ❌ "API Reference"
* ❌ "Key differences"
* ❌ "Prerequisites"

**Avoid these patterns:**

* Gerunds as headings: "Configuring", "Installing", "Setting up"
* Noun phrases: "Configuration", "Installation", "Overview", "Introduction"
* Questions: "How do I configure X?" (just use the imperative: "Configure X")
* Passive constructions: "Getting started"

#### Links:

* Use descriptive link text, never "click here", "read more", or "this link". "Learn more about authentication methods" is good, but "click here for documentation" is not.
* Provide context for external links
* Ensure all links are current and accessible
* Run `mintlify broken-links` to check for broken links before publishing

## Example quality standards

### Realistic and tested examples

* Use actual product data and realistic scenarios
* Test all code examples in multiple environments
* Show examples in multiple programming languages (Python, JavaScript) if available

### Complete and runnable code

* Provide full working examples, not snippets that require guessing
* Include all necessary imports, dependencies, and setup steps
* Show the complete request/response cycle
* Include error handling in examples when appropriate

### Contextual examples

* Match examples to the specific use case being documented
* Use variable names and data that reflect real-world usage
* Show examples that developers can easily adapt to their own needs
* Include multiple examples when there are common variations

## Quality checklist

Before submitting documentation, verify:

* [ ] Opens with value statement (what, why, expectations)
* [ ] Uses sentence case for all headings
* [ ] No subjective qualifiers or marketing language
* [ ] Active voice and present tense throughout
* [ ] Direct address using "you" (no "we/us/our")
* [ ] Direct imperative instructions (no "you need to")
* [ ] Code examples are complete and tested
* [ ] All links work and are current
* [ ] Ends with actionable next steps
* [ ] Terminology matches Vale rules and approved dictionaries

## Examples

### Good opening:

```markdown  theme={null}
# Set up webhook notifications

This guide shows you how to configure webhooks to receive real-time updates when users complete actions in your application. After setting up webhooks, your application can respond immediately to events without polling Writer's API.
```

### Good closing:

```markdown  theme={null}
## Next steps

Now that you have webhooks configured, you can:
- [Handle webhook failures](link) to ensure reliable event processing
- [Secure your webhook endpoints](link) with signature verification
- [Set up webhook monitoring](link) to track delivery success
```

### Voice transformation:

❌ "Our powerful API makes it easy to integrate authentication. We've designed a simple system that will help you get started quickly."

✅ "The authentication API handles user login and token management. Follow these steps to integrate authentication into your application."

❌ "You need to install the Writer SDK before you can start building."

✅ "Install the Writer SDK before building your application."

***

*This guide is a living document. Submit suggestions and updates through the standard documentation review process.*


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://dev.writer.com/llms.txt
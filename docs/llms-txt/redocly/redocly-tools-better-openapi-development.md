# Source: https://redocly.com/blog/redocly-tools-better-openapi-development.md

One of the hardest problems when building APIs is getting the API description started. Whether you're designing a brand new API or retrofitting an existing API into an OpenAPI description, staring at a blank canvas can feel daunting. Recently, when working on a greenfield OpenAPI project, I faced this exact problem. Thankfully, my experience has taught me to reach for tools to help me work with OpenAPI more effectively.

In this blog post, I'll introduce the Museum API and examine the impact that best-in-class developer tools can have on your OpenAPI development process. I'll share my experience building the Museum API and how Redocly's open source tools were used along the way.

## Meet the Museum OpenAPI description

This post features the "Museum API", an OpenAPI description for an imaginary Museum. The Museum API is an iterative educational tool that Redocly can use to teach people about OpenAPI. Please feel free to [explore the repo](https://github.com/Redocly/museum-openapi-example).

While building the Museum OpenAPI, two tools had an outsized impact on my development process:

1. [redocly-vs-code](https://redocly.com/docs/redocly-openapi/) â Redocly's official extension for VS Code
2. [redocly-cli](https://redocly.com/docs/cli/) â a command-line tool that grants OpenAPI superpowers


## Build the foundation with Redocly's VS Code extension

Composing the initial structure for your OpenAPI description can be challenging. It takes time and energy to context switch between your coding environment, reading about OpenAPI, and searching for examples. Redocly's official [VS Code extension](https://redocly.com/docs/redocly-openapi/) was especially useful to me during this phase of working on the Museum API.

### Real-time validation

The immediate feedback the Redocly VS Code extension provides on OpenAPI syntax helped me write operations correctly, avoid breakages, and identify quality improvements. Besides making me more productive in my IDE, this validation allowed me to focus my problem-solving on larger issues rather than syntax errors.

![A validation error in an IDE with an OpenAPI file. The error is on a Get operation and says "Operation object should contain operationId field".](/assets/real-time-validation.464a09cc843e58c2279239f70bc7d678b42c575b0279530eaee914d60ca2e803.e1c8e504.png)

### Smart suggestions

Having intelliSense-like code completion allowed me to spend more time building and less time searching. After adding something to the spec, I could *assemble* the underlying object by selecting the child properties from the suggestion modal.

![Autocomplete options on a new line with a list of options and operationId being hovered.](/assets/code-completion.8f3529486a21fe33eaed0958baa3face7017b4d5a473406269b5b0d678947b68.e1c8e504.png)

## Refine and expand API descriptions with Redocly CLI

As your OpenAPI description grows in size and complexity, new challenges emerge quickly. That's why the usefulness of your OpenAPI tooling should grow with your needs. When developing the Museum API, I relied on the [Redocly CLI](https://redocly.com/docs/cli/) to ensure I was adding new, valuable features to the description as it grew in scope.

### Previewing the docs

The ability to [preview](https://redocly.com/docs/cli/commands/preview/) the API reference docs the same way an end-user will experience them is essential. Great docs need to be reviewed for *more* than just technical correctness. Previewing the API reference docs was especially useful when working with nested schemas and example payloads.

![Console output from running the "redocly preview docs" command. The output contains a hyperlink to localhost, where the preview is running locally.](/assets/preview-docs-console.814a873c9d9e3a60ce51b9efc9dda3005cebc98bb1563f230762e13f45ee511e.e1c8e504.png)
![The API reference docs preview for the Museum OpenAPI running on localhost.](/assets/preview-docs.87d5659a3877291e2e2d77a3b032fd559c267d1d3895d725cc131d8c1c3a518d.e1c8e504.png)

### Linting the description

The [linting](https://redocly.com/docs/cli/commands/lint/) feature enforced basic OpenAPI standards (using Redocly's [recommended ruleset](https://redocly.com/docs/cli/rules/recommended/)), but could be shaped to meet the unique needs of our project. For example, when a reviewer pointed out that I forgot to define tags, I turned on [operation-tag-defined](https://redocly.com/docs/cli/rules/operation-tag-defined/) (one of many [built-in rules](https://redocly.com/docs/cli/rules/built-in-rules/)) and the missing tags were picked up by the linter! Here's the rule:


```yaml
rules:
  operation-tag-defined: error
```

![Console output from the Redocly CLI linter with errors that say "Operation tags should be defined in global tags".](/assets/tag-lint-rule.a89968237793416ff006d47f6a178cf28b890b384de52dde86862c8ee9448b4d.e1c8e504.png)

## Better tools for better developer experience

One of the best parts of OpenAPI is the improvements in developer experience it unlocks. But that benefit isn't *only* for consumers; it's for builders, too! Reflecting on my journey building the Museum OpenAPI description, there were two standout moments where I was especially delighted by the tooling I was using: [creating payloads](#creating-example-payloads) and adding a [new linting rule](#adding-a-custom-linting-rule).

### Creating example payloads

When creating example request and response payloads, the real-time, schema-based validation felt like a superpower! Each property in the example payload is validated against the underlying schema, which made examples more accurate and easier to construct. Additionally, any changes to the schema immediately throws errors in the corresponding examples.

![A payload in an OpenAPI description with a validation error. The error calls out a property in the schema that is missing from the example payload.](/assets/payload-schema-validation.eb8b1797437fb6b37969b4a42eb776d24a474a4b7e675753062421335f2a3a58.e1c8e504.png)

### Adding a custom linting rule

We wanted to enforce sentence casing on Operation summaries, so I added a [configurable rule](https://redocly.com/docs/cli/rules/configurable-rules/). Right after adding the rule, the real-time validation errors were visible in my IDE!

#### Building the rule

Redocly has an API design preference -- Operation summaries should be "sentence cased", which means there's only one capital letter.

- ð¢ **Good** Operation summaries = Create special event, Get museum hours, Buy museum tickets
- ð´ **Bad** Operation summaries = Create Special Event, get Museum hours, buy museum tickets


I started by using [regexr](https://regexr.com/) to help build the regex: `/^[A-Z]+[^A-Z]+$/`, which matches strings that:

1. Start with an uppercase letter
2. Are followed by characters that are *not* uppercase letters
3. End with a character that is *not* an uppercase letter


Next, I added the following rule to the redocly configuration file:


```yaml
rules:
  rule/operation-summary-sentence-case:
    subject:
      type: Operation
      property: summary
    message: "Operation summary must be sentence cased."
    assertions:
      pattern: /^[A-Z]+[^A-Z]+$/
```

#### Example of sentence case linting

After adding the sentence casing rule, the errors were visible running the CLI linter *and* inside my IDE.

![A validation error in an IDE with an OpenAPI file. The error is on an Operation summary and says "Operation summary must be sentence cased".](/assets/sentence-case-linting.d49052b7236441908bbfbe647049fc6961355bfeb715ad7606a2308cff801dd3.e1c8e504.png)

## Redocly tooling improves OpenAPI development

For beginners and OpenAPI-experts alike, the right tools make all the difference. Redocly's open source tooling can unlock better, more productive ways of working with OpenAPI descriptions for both brand new projects or existing ones. The tools are powerful, but flexible, and often create significant value in unexpected ways -- we encourage you to experiment!

Hopefully this post inspired you to dig deeper into Redocly's OpenAPI tooling. Ready to explore? Try the following resources:

- [Museum OpenAPI spec](https://github.com/Redocly/museum-openapi-example) - The example OpenAPI description featured in this blog post.
- [Using Redocly CLI for API Management](https://nordicapis.com/using-redocly-cli-for-api-management/) - A blog post from Nordic APIs exploring the Redocly CLI.
- [Redocly CLI GitHub page](https://github.com/Redocly/redocly-cli) - See how our CLI is maintained and evolves over time.
# Verta Documentation

Source: https://vertana.org/llms-full.txt

---

---
url: /manuals/cli.md
description: >-
  Complete reference for the Vertana command-line interface, including
  installation, configuration, and all available options.
---

# CLI reference

Vertana provides a command-line interface for quick translations without
writing code.  This guide covers installation, configuration, and all
available commands.

## Installation

::: code-group

```bash [Deno]
deno install -g --name vertana --allow-all jsr:@vertana/cli
```

```bash [npm]
npm install -g @vertana/cli
```

```bash [pnpm]
pnpm add -g @vertana/cli
```

```bash [Bun]
bun add -g @vertana/cli
```

:::

## Configuration

Before using the CLI, you need to configure a language model and API key.

### Setting the model

Use the `config model` command to set the default language model:

```bash
vertana config model openai:gpt-4.1
```

The model code format is `PROVIDER:MODEL`.  Supported providers:

`openai`
:   OpenAI models (e.g., `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`)

`anthropic`
:   Anthropic models (e.g., `claude-sonnet-4-5-20250929`, `claude-opus-4-5-20251124`,
`haiku-4-5-20251015`)

`google`
:   Google Generative AI models (e.g., `gemini-3-flash`, `gemini-3-pro`)

To view the current model:

```bash
vertana config model
```

### Setting API keys

Use the `config api-key` command to store API keys securely in your system
keyring:

```bash
vertana config api-key openai sk-...
vertana config api-key anthropic sk-ant-...
vertana config api-key google AIza...
```

To view a masked version of the current API key:

```bash
vertana config api-key openai
```

> \[!TIP]
> API keys are stored in your system's secure keyring (Keychain on macOS,
> Secret Service on Linux, Credential Manager on Windows).  You can also
> set API keys via environment variables: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`,
> or `GOOGLE_GENERATIVE_AI_API_KEY`.

## Translating text

The `translate` command performs translation.  The basic syntax is:

```bash
vertana translate -t TARGET [OPTIONS] [FILE]
```

### Target language

The `-t` or `--target` option specifies the target language (required):

```bash
vertana translate -t ko document.md
vertana translate --target ja README.md
```

Language codes should be [BCP 47] language tags (e.g., `ko`, `ja`, `zh-Hans`,
`pt-BR`).

[BCP 47]: https://www.rfc-editor.org/info/bcp47

### Source language

The `-s` or `--source` option specifies the source language.  If omitted,
Vertana auto-detects the source language:

```bash
vertana translate -s en -t ko document.md
```

### Input sources

You can provide input in three ways:

```bash
# From a file
vertana translate -t ko document.md

# From stdin
echo "Hello, world!" | vertana translate -t ko

# Interactive input (type text, then Ctrl+D)
vertana translate -t ko
```

### Output options

By default, translated text goes to stdout.  Use `-o` or `--output` to save
to a file:

```bash
vertana translate -t ko -o output.md input.md
```

### Media type

The `-T` or `--type` option specifies the input format.  This affects how
the text is chunked for translation:

```bash
vertana translate -t ko -T text/markdown document.md
vertana translate -t ko -T text/html page.html
vertana translate -t ko -T text/plain notes.txt
```

Supported media types:

`text/plain`
:   Plain text (default).  Splits on paragraphs and sentences.

`text/markdown`
:   Markdown documents.  Preserves headings, code blocks, and formatting.

`text/html`
:   HTML documents.  Preserves tags and structure.

### Tone

The `--tone` option sets the translation tone:

```bash
vertana translate -t ko --tone formal document.md
```

Available tones: `formal`, `informal`, `technical`, `casual`, `professional`,
`literary`, `journalistic`.

### Domain

The `--domain` option provides domain context for specialized terminology:

```bash
vertana translate -t ko --domain medical report.md
vertana translate -t ja --domain legal contract.md
```

### Fetching linked pages

The `-L`/`--fetch-links` flag automatically fetches content from URLs
found in the source text and provides them as additional context:

```bash
vertana translate -t ko -L document.md
```

This is useful when translating documents that reference external articles
or resources.  The fetched content helps the LLM understand the context
of the references and translate them more accurately.

See the [*Web context*](./context-web.md) guide for more details on how
web context fetching works.

## Glossaries

Glossaries ensure consistent translation of specific terms.

### Inline glossary entries

Use `-g` or `--glossary` to define term mappings inline:

```bash
vertana translate -t ko -g "Vertana=버타나" -g "agentic=에이전틱" document.md
```

### Glossary files

Use `--glossary-file` to load a glossary from a JSON file:

```bash
vertana translate -t ko --glossary-file glossary.json document.md
```

The glossary file format:

```json
[
  { "original": "Vertana", "translated": "버타나" },
  { "original": "agentic", "translated": "에이전틱" },
  {
    "original": "chunk",
    "translated": "청크",
    "context": "In the context of text processing"
  }
]
```

Each entry has:

`original`
:   The source term to match.

`translated`
:   The target translation to use.

`context`
:   Optional context to clarify when this translation applies.

> \[!TIP]
> CLI glossary entries (`-g`) take precedence over file entries when the
> same term appears in both.

## Verbosity

Use `-v` or `--verbose` for more detailed output during translation:

```bash
vertana translate -t ko -v document.md
```

Add more `-v` flags for increased verbosity:

```bash
vertana translate -t ko -vv document.md   # Debug level
vertana translate -t ko -vvv document.md  # Trace level
```

## Examples

Translate a Markdown file to Korean:

```bash
vertana translate -t ko -T text/markdown README.md -o README.ko.md
```

Translate with domain context and glossary:

```bash
vertana translate -t ja \
  --domain medical \
  -g "patient=患者" \
  -g "diagnosis=診断" \
  report.md
```

Translate from stdin with formal tone:

```bash
cat document.txt | vertana translate -t ko --tone formal
```

Translate HTML while preserving structure:

```bash
vertana translate -t zh-Hans -T text/html page.html -o page.zh.html
```

---

---
url: /manuals/context.md
description: >-
  Guide to using context sources in Vertana to provide additional information
  for improved translation quality.
---

# Context sources

Context sources provide additional information to improve translation quality.
They can supply background knowledge, style guides, terminology databases, or
any external information relevant to the translation.

## What are context sources?

Context sources are functions that gather information before or during
translation.  This context helps the LLM make better translation decisions by
understanding:

* The author's writing style
* Domain-specific terminology
* Document metadata
* Related content or references

## Two modes of operation

Context sources operate in two modes:

`required`
:   Always invoked before translation begins.  Use for essential context like
author information or document metadata.

`passive`
:   Exposed as tools the LLM can call on demand.  Use for optional context the
LLM requests when needed, like looking up specific terms.

## Required context sources

Required sources run automatically before translation starts.  They provide
context that's always relevant.

### Creating a required source

```typescript twoslash
import type { RequiredContextSource } from "@vertana/core/context";

const authorBioSource: RequiredContextSource = {
  name: "author-bio",
  description: "Author biography and writing style notes",
  mode: "required",
  async gather(options) {
    // Fetch or compute the context
    const bio = await fetchAuthorBio();
    return {
      content: `Author: Jane Smith. Style: Technical but accessible.`,
      metadata: { authorId: "jane-smith" },
    };
  },
};

async function fetchAuthorBio(): Promise<string> {
  return "Jane Smith is a technical writer...";
}
```

### Using required sources

Pass context sources to the `translate()` function:

```typescript twoslash
import type { RequiredContextSource } from "@vertana/core/context";
const authorBioSource: RequiredContextSource = {
  name: "author-bio",
  description: "Author biography",
  mode: "required",
  async gather() { return { content: "" }; },
};
const document: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  document,
  {
    contextSources: [authorBioSource],
  }
);
```

## Passive context sources

Passive sources are tools the LLM can invoke when it needs specific
information.  They require a parameter schema so the LLM knows how to call
them.

### Creating a passive source

Passive sources need a parameter schema using Standard Schema:

```typescript twoslash
import type { PassiveContextSource } from "@vertana/core/context";
import { z } from "zod";

const termLookupSource: PassiveContextSource<{ term: string }> = {
  name: "term-lookup",
  description: "Look up the definition and translation of a technical term",
  mode: "passive",
  parameters: z.object({
    term: z.string().describe("The term to look up"),
  }),
  async gather(params, options) {
    const definition = await lookupTerm(params.term);
    return {
      content: definition,
      metadata: { term: params.term },
    };
  },
};

async function lookupTerm(term: string): Promise<string> {
  // Look up from a terminology database
  return `${term}: A technical concept...`;
}
```

### When passive sources are called

The LLM decides when to call passive sources based on:

* The source's `name` and `description`
* The translation content and domain
* Whether it encounters unfamiliar terms or concepts

For example, if translating technical documentation and encountering an
unfamiliar acronym, the LLM might call a term lookup source.

## Standard Schema compatibility

Passive sources use [Standard Schema] for parameter definitions.  This allows
you to use any compatible schema library:

[Standard Schema]: https://standardschema.dev/

### Using Zod

```typescript twoslash
import type { PassiveContextSource } from "@vertana/core/context";
import { z } from "zod";

const source: PassiveContextSource<{ query: string; limit: number }> = {
  name: "search",
  description: "Search for related articles",
  mode: "passive",
  parameters: z.object({
    query: z.string().describe("Search query"),
    limit: z.number().describe("Maximum results"),
  }),
  async gather(params) {
    return { content: `Results for: ${params.query}` };
  },
};
```

### Using Valibot

```typescript twoslash
import type { PassiveContextSource } from "@vertana/core/context";
import * as v from "valibot";

const source: PassiveContextSource<{ query: string }> = {
  name: "search",
  description: "Search for related articles",
  mode: "passive",
  parameters: v.object({
    query: v.pipe(v.string(), v.description("Search query")),
  }),
  async gather(params) {
    return { content: `Results for: ${params.query}` };
  },
};
```

### Using ArkType

```typescript twoslash
import type { PassiveContextSource } from "@vertana/core/context";
import { type } from "arktype";

const source: PassiveContextSource<{ query: string }> = {
  name: "search",
  description: "Search for related articles",
  mode: "passive",
  parameters: type({
    query: "string",
  }),
  async gather(params) {
    return { content: `Results for: ${params.query}` };
  },
};
```

## Helper functions

Vertana provides helper functions for working with context sources.

### Gathering required context

```typescript twoslash
import type { ContextSource } from "@vertana/core/context";
const sources: ContextSource[] = [];
// ---cut-before---
import { gatherRequiredContext } from "@vertana/core/context";

const results = await gatherRequiredContext(sources);
// Only required sources are invoked
```

### Combining context results

```typescript twoslash
import type { ContextResult } from "@vertana/core/context";
const results: ContextResult[] = [];
// ---cut-before---
import { combineContextResults } from "@vertana/core/context";

const combined = combineContextResults(results);
// Returns a single string with all context content
```

## Practical examples

### Style guide source

Provide a style guide for consistent tone:

```typescript twoslash
import type { RequiredContextSource } from "@vertana/core/context";

const styleGuideSource: RequiredContextSource = {
  name: "style-guide",
  description: "Company style guide for translations",
  mode: "required",
  async gather() {
    return {
      content: `
Style Guide:
- Use formal language (합쇼체 in Korean)
- Avoid idioms that don't translate well
- Keep sentences concise
- Use active voice when possible
      `.trim(),
    };
  },
};
```

### Document metadata source

Include metadata about the document:

```typescript twoslash
import type { RequiredContextSource } from "@vertana/core/context";

interface DocumentMetadata {
  readonly title: string;
  readonly author: string;
  readonly date: string;
  readonly category: string;
  readonly [key: string]: unknown;
}

function createMetadataSource(metadata: DocumentMetadata): RequiredContextSource {
  return {
    name: "document-metadata",
    description: "Information about the document being translated",
    mode: "required",
    async gather() {
      return {
        content: `
Document: ${metadata.title}
Author: ${metadata.author}
Date: ${metadata.date}
Category: ${metadata.category}
        `.trim(),
        metadata,
      };
    },
  };
}
```

### Terminology database lookup

Allow the LLM to look up terms on demand:

```typescript twoslash
import type { PassiveContextSource } from "@vertana/core/context";
import { z } from "zod";

interface TermEntry {
  term: string;
  definition: string;
  translation: string;
}

function createTermDatabaseSource(
  database: Map<string, TermEntry>,
): PassiveContextSource<{ term: string }> {
  return {
    name: "terminology-database",
    description: "Look up technical terms and their official translations",
    mode: "passive",
    parameters: z.object({
      term: z.string().describe("The term to look up"),
    }),
    async gather(params) {
      const entry = database.get(params.term.toLowerCase());
      if (entry == null) {
        return { content: `Term "${params.term}" not found in database.` };
      }
      return {
        content: `
Term: ${entry.term}
Definition: ${entry.definition}
Official translation: ${entry.translation}
        `.trim(),
        metadata: { found: true },
      };
    },
  };
}
```

## Built-in context sources

Vertana provides ready-to-use context sources through separate packages.

### Web context (`@vertana/context-web`)

The `@vertana/context-web` package provides context sources for fetching
and extracting content from web pages.  This is useful when translating
documents that reference external articles or resources.

```typescript twoslash
import type { LanguageModel } from "ai";
declare const model: LanguageModel;
// ---cut-before---
import { translate } from "@vertana/facade";
import { fetchLinkedPages, fetchWebPage } from "@vertana/context-web";

const text = `
Read the introduction at https://example.com/intro.
`;

const result = await translate(model, "ko", text, {
  contextSources: [
    // Pre-fetch all links in the text
    fetchLinkedPages({ text, mediaType: "text/plain" }),
    // Allow LLM to fetch additional URLs on demand
    fetchWebPage,
  ],
});
```

See the [Web context](/manuals/context-web) guide for detailed documentation.

## Best practices

### Keep context focused

Provide only relevant information.  Too much context can confuse the LLM:

```typescript twoslash
import type { RequiredContextSource } from "@vertana/core/context";

// Good: focused context
const focused: RequiredContextSource = {
  name: "domain-context",
  description: "Medical domain context",
  mode: "required",
  async gather() {
    return {
      content: "This is a medical case study. Use formal medical terminology.",
    };
  },
};
```

### Use passive sources for optional lookups

Don't make every source required.  Use passive sources for information the LLM
might not always need:

```typescript twoslash
import type { PassiveContextSource } from "@vertana/core/context";
import { z } from "zod";

// Good: passive source for on-demand lookup
const referenceLookup: PassiveContextSource<{ url: string }> = {
  name: "reference-lookup",
  description: "Fetch content from a referenced URL for context",
  mode: "passive",
  parameters: z.object({
    url: z.string().url().describe("The URL to fetch"),
  }),
  async gather(params) {
    const content = await fetch(params.url).then((r) => r.text());
    return { content: content.slice(0, 1000) };  // Limit content size
  },
};
```

### Include metadata for debugging

Add metadata to track which sources contributed to the translation:

```typescript twoslash
import type { RequiredContextSource } from "@vertana/core/context";

const source: RequiredContextSource = {
  name: "glossary",
  description: "Domain glossary",
  mode: "required",
  async gather() {
    const terms = await loadGlossary();
    return {
      content: formatGlossary(terms),
      metadata: {
        termCount: terms.length,
        lastUpdated: new Date().toISOString(),
      },
    };
  },
};

async function loadGlossary(): Promise<string[]> {
  return ["term1", "term2"];
}

function formatGlossary(terms: string[]): string {
  return terms.join("\n");
}
```

---

---
url: /start.md
description: Instructions for installing Vertana and basic usage examples.
---

# Getting started

Vertana is an LLM-powered agentic translation library for TypeScript.
It uses autonomous agent workflows to gather contextual information for
high-quality translations that preserve meaning, tone, and formatting.

## Installation

Vertana consists of two packages:

* *@vertana/facade*: High-level API for translation tasks
* *@vertana/core*: Core translation logic (used internally by facade)

For most use cases, you only need to install the *@vertana/facade* package:

::: code-group

```bash [Deno]
deno add jsr:@vertana/facade
```

```bash [npm]
npm add @vertana/facade
```

```bash [pnpm]
pnpm add @vertana/facade
```

```bash [Yarn]
yarn add @vertana/facade
```

```bash [Bun]
bun add @vertana/facade
```

:::

### Vercel AI SDK

Vertana uses the [Vercel AI SDK] for LLM interactions, so you'll also need to
install a model provider.  For example, to use OpenAI:

::: code-group

```bash [Deno]
deno add npm:@ai-sdk/openai
```

```bash [npm]
npm add @ai-sdk/openai
```

```bash [pnpm]
pnpm add @ai-sdk/openai
```

```bash [Yarn]
yarn add @ai-sdk/openai
```

```bash [Bun]
bun add @ai-sdk/openai
```

:::

### Switching providers

Vertana works with any provider supported by the Vercel AI SDK.  Simply install
the provider package and import it:

```typescript
// OpenAI
import { openai } from "@ai-sdk/openai";
const model = openai("gpt-5.1");

// Anthropic
import { anthropic } from "@ai-sdk/anthropic";
const model = anthropic("claude-opus-4-5-20251101");

// Google
import { google } from "@ai-sdk/google";
const model = google("gemini-3-flash-preview");
```

Each provider has its own package following the `@ai-sdk/<provider>` naming
convention:

| Provider  | Package                  | Example models                            |
| --------- | ------------------------ | ----------------------------------------- |
| OpenAI    | `@ai-sdk/openai`         | `gpt-5.1`, `gpt-4o`                       |
| Anthropic | `@ai-sdk/anthropic`      | `claude-opus-4-5-20251101`, `claude-sonnet-4-5-20241022` |
| Google    | `@ai-sdk/google`         | `gemini-3-flash-preview`, `gemini-3-pro`  |
| Mistral   | `@ai-sdk/mistral`        | `mistral-large-2512`                      |
| Amazon    | `@ai-sdk/amazon-bedrock` | `anthropic.claude-opus-4-5`               |

> \[!TIP]
> Model names are passed directly to the provider's API, so you need to use
> the exact model IDs from their documentation.  Check each provider's official
> docs for the full list of available models:
>
> * [OpenAI models](https://platform.openai.com/docs/models)
> * [Anthropic models](https://platform.claude.com/docs/en/about-claude/models/overview)
> * [Google Gemini models](https://ai.google.dev/gemini-api/docs/models)
> * [Mistral models](https://docs.mistral.ai/getting-started/models)
>
> See also the [Vercel AI SDK providers documentation] for integration details.

[Vercel AI SDK]: https://sdk.vercel.ai/

[Vercel AI SDK providers documentation]: https://sdk.vercel.ai/providers/ai-sdk-providers

## Basic usage

The main entry point is the `translate()` function.  Here's a minimal example:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",  // Target language (BCP 47 tag)
  "Hello, world! How are you today?"
);

console.log(result.text);
// => "안녕하세요! 오늘 기분이 어떠세요?"
```

The `translate()` function takes three required arguments:

1. A language model from the Vercel AI SDK
2. The target language (as a BCP 47 language tag or [`Intl.Locale`])
3. The text to translate

[`Intl.Locale`]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale

### With options

You can customize the translation with various options:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ja",
  "The patient presented with acute myocardial infarction.",
  {
    sourceLanguage: "en",
    domain: "medical",
    tone: "formal",
    context: "This is from a medical case study."
  }
);

console.log(result.text);
// => "患者は急性心筋梗塞を呈した。"
```

### Tracking progress

For long documents, you can track translation progress:

```typescript twoslash
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "es",
  longDocument,
  {
    onProgress: (progress) => {
      console.log(`Stage: ${progress.stage}, Progress: ${progress.progress}`);
    }
  }
);
```

Progress stages include `chunking`, `gatheringContext`, `translating`,
`refining`, and `selecting`.

## Command-line interface

Vertana also provides a CLI for quick translations.  Install it with:

::: code-group

```bash [Deno]
deno install -g --name vertana --allow-all jsr:@vertana/cli
```

```bash [npm]
npm install -g @vertana/cli
```

```bash [pnpm]
pnpm add -g @vertana/cli
```

```bash [Bun]
bun add -g @vertana/cli
```

:::

Then translate files directly from the terminal:

```bash
vertana translate -l ko document.md
```

---

---
url: /manuals/glossary.md
description: >-
  Guide to using glossaries in Vertana for consistent terminology across
  translations.
---

# Glossary deep dive

Glossaries ensure consistent translation of specific terms throughout your
documents.  This guide covers all glossary features, from basic usage to
dynamic extraction.

## Why use glossaries?

Without glossaries, the same term might be translated differently in different
parts of a document:

* "chunk" might become "청크" in one paragraph and "덩어리" in another
* Product names might be inconsistently transliterated
* Technical terms might lose their precise meaning

Glossaries solve this by defining explicit term mappings that Vertana applies
consistently throughout the translation.

## Basic usage

Provide a glossary through the `glossary` option:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  "Vertana uses an agentic workflow to improve translation quality.",
  {
    glossary: [
      { original: "Vertana", translated: "버타나" },
      { original: "agentic", translated: "에이전틱" },
    ],
  }
);
```

## Glossary entry structure

Each glossary entry has three fields:

```typescript twoslash
import type { GlossaryEntry } from "@vertana/core/glossary";

const entry: GlossaryEntry = {
  original: "chunk",
  translated: "청크",
  context: "In the context of text processing",
};
```

`original`
:   The term in the source language to match.

`translated`
:   The translation to use in the target language.

`context`
:   Optional description of when this translation applies.  This helps
disambiguate terms with multiple meanings.

## Context-aware entries

The `context` field helps when a term has multiple valid translations depending
on usage:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  "The bank processes transactions. We walked along the river bank.",
  {
    glossary: [
      {
        original: "bank",
        translated: "은행",
        context: "Financial institution",
      },
      {
        original: "bank",
        translated: "둑",
        context: "Edge of a river",
      },
    ],
  }
);
```

The LLM uses the context to choose the appropriate translation based on how
the term is used in each sentence.

## Dynamic glossary

For long documents, manually defining every term can be impractical.  The
dynamic glossary feature automatically extracts and accumulates terminology
as translation progresses.

Enable it with the `dynamicGlossary` option:

```typescript twoslash
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  longDocument,
  { dynamicGlossary: true }
);

// Access the accumulated glossary
console.log(result.accumulatedGlossary);
// [
//   { original: "Vertana", translated: "버타나" },
//   { original: "chunk", translated: "청크" },
//   ...
// ]
```

### How it works

1. After translating each chunk, Vertana extracts key terminology pairs
2. Extracted terms are added to a running glossary
3. Subsequent chunks receive the accumulated glossary, ensuring consistency
4. The final glossary is returned in `result.accumulatedGlossary`

### Customizing dynamic glossary

Fine-tune the extraction with `DynamicGlossaryOptions`:

```typescript twoslash
import type { LanguageModel } from "ai";
const extractorModel: LanguageModel = {} as LanguageModel;
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  longDocument,
  {
    dynamicGlossary: {
      maxTermsPerChunk: 15,          // Extract more terms per chunk
      extractorModel: extractorModel, // Use a different model for extraction
    },
  }
);
```

`maxTermsPerChunk`
:   Maximum terms to extract from each chunk (default: `10`).

`extractorModel`
:   The model to use for term extraction.  If not specified, uses the same
model as translation.

### Combining static and dynamic glossaries

You can provide an initial glossary while also enabling dynamic accumulation:

```typescript twoslash
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  longDocument,
  {
    glossary: [
      { original: "Vertana", translated: "버타나" },
    ],
    dynamicGlossary: true,
  }
);

// result.accumulatedGlossary includes both the initial entry
// and any new terms extracted during translation
```

## Glossary file format

For the CLI and reusable glossaries, store entries in a JSON file:

```json
[
  {
    "original": "Vertana",
    "translated": "버타나"
  },
  {
    "original": "agentic workflow",
    "translated": "에이전틱 워크플로우"
  },
  {
    "original": "chunk",
    "translated": "청크",
    "context": "A segment of text for processing"
  }
]
```

Use with the CLI:

```bash
vertana translate -t ko --glossary-file glossary.json document.md
```

Or load and use programmatically:

```typescript twoslash
import { readFileSync } from "node:fs";
import type { Glossary } from "@vertana/core/glossary";

const glossary: Glossary = JSON.parse(
  readFileSync("glossary.json", "utf-8")
);
```

## Best practices

### Focus on important terms

Don't include every word.  Focus on:

* Product names and brand terms
* Technical vocabulary specific to your domain
* Terms with multiple possible translations
* Proper nouns that need consistent transliteration

### Provide context for ambiguous terms

When a term can mean different things, add context:

```typescript twoslash
import type { Glossary } from "@vertana/core/glossary";

const glossary: Glossary = [
  {
    original: "model",
    translated: "모델",
    context: "Machine learning model",
  },
  {
    original: "model",
    translated: "모형",
    context: "Physical or conceptual representation",
  },
];
```

### Use dynamic glossary for long documents

For documents with many chunks, enable dynamic glossary to automatically
maintain consistency without manually defining every term.

### Reuse glossaries across projects

Save your domain-specific glossaries as JSON files and reuse them across
related projects to maintain consistent terminology.

---

---
url: /manuals/quality.md
description: >-
  Guide to improving translation quality with chunking, evaluation, iterative
  refinement, and best-of-N selection.
---

# Translation quality

Vertana provides several features to improve translation quality beyond a
single LLM pass.  This guide covers document chunking, quality evaluation,
iterative refinement, and best-of-N model selection.

## Document chunking

Long documents are split into smaller chunks for translation.  This improves
quality by keeping each translation request within the model's optimal context
window and allowing for chunk-level quality control.

### Why chunking matters

LLMs have context limits and tend to perform better with focused input.
Chunking:

* Keeps each request within optimal token limits
* Enables progress tracking for long documents
* Allows quality evaluation and refinement per chunk
* Enables parallel translation of independent chunks

### Media type-aware chunking

Vertana selects chunkers based on the document's media type:

`text/plain`
:   Splits on paragraph boundaries and sentences.

`text/markdown`
:   Preserves Markdown structure: headings, code blocks, lists.

`text/html`
:   Preserves HTML tags and structure.

```typescript twoslash
const markdownDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  markdownDocument,
  { mediaType: "text/markdown" }
);
```

### Controlling chunk size

The context window option controls chunk size:

```typescript twoslash
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  longDocument,
  {
    contextWindow: {
      type: "explicit",
      maxTokens: 4096,  // Tokens per chunk
    },
  }
);
```

### Disabling chunking

For short texts or when you want full-document context:

```typescript twoslash
const shortText: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  shortText,
  { chunker: null }
);
```

## Translation evaluation

Vertana can evaluate translation quality using an LLM judge.  Evaluation
produces a score and identifies specific issues.

### Evaluation criteria

Translations are evaluated on four dimensions:

`accuracy`
:   Does the translation accurately convey the original meaning?

`fluency`
:   Is the translation natural and readable in the target language?

`terminology`
:   Are domain-specific terms translated correctly and consistently?

`style`
:   Does the translation maintain the appropriate tone?

### Evaluation result structure

Evaluation returns a score and a list of issues:

```typescript twoslash
import type { EvaluationResult, TranslationIssue } from "@vertana/core/evaluation";

const result: EvaluationResult = {
  score: 0.85,  // 0-1, where 1 is perfect
  issues: [
    {
      type: "terminology",
      description: "Term 'chunk' inconsistently translated",
      location: { start: 45, end: 52 },
    },
  ],
};
```

### Score interpretation

| Score | Quality |
| ----- | ------- |
| 0.9+  | Excellent |
| 0.7-0.9 | Good |
| 0.5-0.7 | Acceptable |
| < 0.5 | Poor |

## Iterative refinement

The refinement feature iteratively improves translations through an
evaluate-fix loop.  Each iteration identifies issues and produces a
revised translation until the quality threshold is met.

### Enabling refinement

Enable refinement with the `refinement` option:

```typescript twoslash
const document: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  document,
  { refinement: true }
);

console.log(result.qualityScore);         // Final quality score
console.log(result.refinementIterations); // Number of iterations performed
```

### Customizing refinement

Fine-tune the refinement process with `RefinementOptions`:

```typescript twoslash
const document: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  document,
  {
    refinement: {
      maxIterations: 5,       // Maximum refinement passes (default: 3)
      qualityThreshold: 0.95, // Stop when score exceeds this (default: 0.9)
    },
  }
);
```

`maxIterations`
:   Maximum number of refinement attempts per chunk (default: `3`).

`qualityThreshold`
:   Target quality score; refinement stops when reached (default: `0.9`).

### How refinement works

1. Translate the document (or chunk)
2. Evaluate the translation quality
3. If score < threshold and iterations < max:
   * Identify specific issues
   * Generate improved translation addressing those issues
   * Re-evaluate
   * Repeat
4. Return the final refined translation

## Best-of-N selection

When you provide multiple language models, Vertana can generate translations
from each and automatically select the best one.

### Basic usage

Pass an array of models and enable best-of-N:

```typescript twoslash
const document: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";

const result = await translate(
  [openai("gpt-4o"), anthropic("claude-sonnet-4-20250514")],
  "ko",
  document,
  { bestOfN: true }
);

console.log(result.selectedModel); // The model that produced the best translation
```

### Specifying an evaluator model

By default, the first model evaluates all candidates.  Specify a different
evaluator:

```typescript twoslash
const document: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";
import { google } from "@ai-sdk/google";

const result = await translate(
  [openai("gpt-4o"), anthropic("claude-sonnet-4-20250514")],
  "ko",
  document,
  {
    bestOfN: {
      evaluatorModel: google("gemini-2.0-flash"),
    },
  }
);
```

### How selection works

1. Each model translates the text independently
2. The evaluator model scores each translation
3. Translations are ranked by score
4. The highest-scoring translation is selected
5. `result.selectedModel` indicates which model produced it

## Combining features

These features can be combined for maximum quality:

```typescript twoslash
const document: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";

const result = await translate(
  [openai("gpt-4o"), anthropic("claude-sonnet-4-20250514")],
  "ko",
  document,
  {
    mediaType: "text/markdown",
    glossary: [
      { original: "Vertana", translated: "버타나" },
    ],
    dynamicGlossary: true,
    refinement: {
      maxIterations: 3,
      qualityThreshold: 0.9,
    },
    bestOfN: true,
    onProgress: (progress) => {
      console.log(`${progress.stage}: ${(progress.progress * 100).toFixed(0)}%`);
    },
  }
);

console.log("Quality score:", result.qualityScore);
console.log("Selected model:", result.selectedModel);
console.log("Refinement iterations:", result.refinementIterations);
console.log("Accumulated terms:", result.accumulatedGlossary?.length);
```

The processing order is:

1. Chunk the document
2. For each chunk:
   * Gather context from sources
   * Translate with each model
   * Evaluate and select best
   * Refine if below threshold
   * Extract terms for dynamic glossary
3. Combine refined chunks

## Tracking progress

Monitor the translation process with the `onProgress` callback:

```typescript twoslash
import type { TranslationProgress } from "@vertana/facade";

function handleProgress(progress: TranslationProgress): void {
  switch (progress.stage) {
    case "chunking":
      console.log("Splitting document into chunks...");
      break;
    case "gatheringContext":
      console.log("Gathering context from sources...");
      break;
    case "translating":
      if (progress.totalChunks) {
        console.log(`Translating chunk ${progress.chunkIndex! + 1}/${progress.totalChunks}`);
      }
      break;
    case "refining":
      console.log(`Refining: iteration ${progress.iteration}/${progress.maxIterations}`);
      break;
    case "selecting":
      console.log(`Evaluating candidate ${progress.candidateIndex! + 1}/${progress.totalCandidates}`);
      break;
  }
}
```

---

---
url: /tutorial.md
description: >-
  This tutorial walks you through Vertana's features, from basic translation to
  advanced techniques like glossaries, refinement, and best-of-N selection.
---

# Tutorial

Vertana is an LLM-powered agentic translation library that goes beyond simple
text translation.  It uses autonomous agent workflows to gather contextual
information, maintain terminology consistency, and iteratively improve
translation quality.

This tutorial will guide you through Vertana's features progressively,
starting from basic translation and building up to advanced techniques.

## What makes Vertana different?

Most translation libraries treat translation as a simple input-output operation:
you provide text, and get translated text back.  This works for simple cases,
but falls short when you need:

* *Consistent terminology* across a document or project
* *Domain-specific accuracy* for technical, legal, or medical content
* *Quality assurance* with iterative improvement
* *Contextual awareness* from external sources like style guides or glossaries

Vertana addresses these challenges through an agentic approach.  Instead of
a single translation pass, Vertana orchestrates multiple steps:

1. *Chunking*: Splitting long documents into manageable pieces
2. *Context gathering*: Collecting relevant information from external sources
3. *Translation*: Generating translations with full context awareness
4. *Evaluation*: Assessing translation quality with specific criteria
5. *Refinement*: Iteratively improving translations based on feedback
6. *Selection*: Choosing the best result from multiple candidates

## Basic translation

Let's start with a simple translation.  The `translate()` function is your
main entry point:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  "The quick brown fox jumps over the lazy dog."
);

console.log(result.text);
// => "빠른 갈색 여우가 게으른 개를 뛰어넘습니다."
console.log(result.tokenUsed);
// => 142
console.log(result.processingTime);
// => 1523
```

The result object contains:

`text`
:   The translated text

`tokenUsed`
:   Total tokens consumed during translation

`processingTime`
:   Time taken in milliseconds

### Translation options

You can provide additional options to improve translation quality:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ja",
  "The patient exhibited signs of acute respiratory distress syndrome.",
  {
    // Specify source language (auto-detected if omitted)
    sourceLanguage: "en",

    // Provide domain context for accurate terminology
    domain: "medical",

    // Set the desired tone
    tone: "formal",

    // Add background information
    context: "This is from a clinical case report for a peer-reviewed journal.",

    // Include a title (will also be translated)
    title: "Case Study: ARDS Management"
  }
);

console.log(result.title);
// => "症例研究：ARDS管理"
console.log(result.text);
// => "患者は急性呼吸窮迫症候群の兆候を示した。"
```

Available tone options include:

| Tone           | Description                                  |
| -------------- | -------------------------------------------- |
| `formal`       | Professional, academic, or official contexts |
| `informal`     | Casual, conversational style                 |
| `technical`    | Precise, specialized terminology             |
| `casual`       | Friendly, easy-going language                |
| `professional` | Business-like, polished communication        |
| `literary`     | Artistic, expressive writing                 |
| `journalistic` | News and media style                         |

### Media types

Vertana can preserve formatting when translating structured content:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const markdown = `
# Getting Started

Welcome to our **documentation**. Here's what you'll learn:

- Installation steps
- Basic configuration
- Advanced features

> Note: Make sure you have Node.js 18+ installed.
`;

const result = await translate(
  openai("gpt-4o"),
  "ko",
  markdown,
  {
    mediaType: "text/markdown"
  }
);
```

Supported media types:

`text/plain` (default)
:   Plain text

`text/markdown`
:   Markdown documents

`text/html`
:   HTML content

## Using glossaries

Glossaries ensure consistent translation of specific terms throughout your
document.  This is essential for technical documentation, legal texts, and
any content with domain-specific vocabulary.

### Basic glossary

A glossary is an array of term mappings:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  "The React component uses hooks for state management. Each hook follows the rules of hooks.",
  {
    glossary: [
      { original: "React", translated: "React" },  // Keep as-is
      { original: "component", translated: "컴포넌트" },
      { original: "hook", translated: "훅" },
      { original: "state", translated: "상태" }
    ]
  }
);

console.log(result.text);
// => "React 컴포넌트는 상태 관리를 위해 훅을 사용합니다. 각 훅은 훅의 규칙을 따릅니다."
```

### Glossary with context

Some terms have different translations depending on context.  You can provide
disambiguation hints:

```typescript twoslash
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  "The bank approved the loan. We walked along the river bank.",
  {
    glossary: [
      {
        original: "bank",
        translated: "은행",
        context: "financial institution"
      },
      {
        original: "bank",
        translated: "강둑",
        context: "side of a river"
      }
    ]
  }
);

console.log(result.text);
// => "은행이 대출을 승인했습니다. 우리는 강둑을 따라 걸었습니다."
```

### Dynamic glossary

For long documents, Vertana can automatically extract and accumulate
terminology as it translates.  This ensures consistency even without
a predefined glossary:

```typescript twoslash
const longDocument: string = "";  // A long technical document
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ja",
  longDocument,
  {
    dynamicGlossary: true
  }
);

// View the automatically extracted terms
console.log(result.accumulatedGlossary);
// => [
//   { original: "machine learning", translated: "機械学習" },
//   { original: "neural network", translated: "ニューラルネットワーク" },
//   ...
// ]
```

You can customize dynamic glossary behavior:

```typescript twoslash
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ja",
  longDocument,
  {
    dynamicGlossary: {
      maxTermsPerChunk: 15,  // Extract up to 15 terms per chunk
      extractorModel: openai("gpt-4o-mini")  // Use a faster model for extraction
    }
  }
);
```

## Document chunking

Long documents are automatically split into chunks for processing.  This
ensures that each chunk fits within the model's context window and allows
for progress tracking.

### Default chunking

By default, Vertana selects an appropriate chunker based on the media type:

* **Markdown**: Splits at headings and preserves document structure
* **Plain text/HTML**: Splits at paragraph boundaries

```typescript twoslash
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  longDocument,
  {
    mediaType: "text/markdown",
    onProgress: (progress) => {
      if (progress.stage === "translating") {
        console.log(`Chunk ${progress.chunkIndex! + 1}/${progress.totalChunks}`);
      }
    }
  }
);
```

### Custom context window

You can control the maximum tokens per chunk:

```typescript twoslash
const longDocument: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  longDocument,
  {
    contextWindow: {
      type: "explicit",
      maxTokens: 8192  // Larger chunks for models with big context windows
    }
  }
);
```

### Disabling chunking

For short texts where you want to ensure single-pass translation:

```typescript twoslash
const shortText: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  shortText,
  {
    chunker: null  // Disable chunking entirely
  }
);
```

## Quality refinement

Refinement is an iterative process where Vertana evaluates the translation
and improves it based on identified issues.  This is particularly valuable
for high-stakes content where quality is critical.

### Enabling refinement

```typescript twoslash
const text: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  text,
  {
    refinement: true
  }
);

console.log(result.qualityScore);
// => 0.92
console.log(result.refinementIterations);
// => 2
```

When refinement is enabled, the result includes:

`qualityScore`
:   Final quality score (0 to 1)

`refinementIterations`
:   Number of improvement iterations performed

### Customizing refinement

You can control the refinement process:

```typescript twoslash
const text: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  text,
  {
    refinement: {
      maxIterations: 5,       // Up to 5 refinement passes
      qualityThreshold: 0.95  // Stop early if quality exceeds 95%
    }
  }
);
```

### Tracking refinement progress

```typescript twoslash
const text: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const result = await translate(
  openai("gpt-4o"),
  "ko",
  text,
  {
    refinement: true,
    onProgress: (progress) => {
      if (progress.stage === "refining") {
        console.log(
          `Refinement iteration ${progress.iteration}/${progress.maxIterations}`
        );
      }
    }
  }
);
```

## Best-of-N selection

When you need the highest quality translation, you can use multiple models
and let Vertana select the best result.  Each model generates a translation,
and an evaluator model scores them to pick the winner.

### Using multiple models

```typescript twoslash
const text: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";

const result = await translate(
  [
    openai("gpt-4o"),
    anthropic("claude-sonnet-4-20250514"),
    openai("gpt-4o-mini")
  ],
  "ko",
  text,
  {
    bestOfN: true
  }
);

console.log(result.selectedModel);
// => { modelId: "gpt-4o", ... }
```

### Custom evaluator

By default, the first model in the array is used for evaluation.  You can
specify a different evaluator:

```typescript twoslash
const text: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";

const result = await translate(
  [
    openai("gpt-4o"),
    anthropic("claude-sonnet-4-20250514")
  ],
  "ko",
  text,
  {
    bestOfN: {
      evaluatorModel: anthropic("claude-sonnet-4-20250514")  // Use Claude to judge
    }
  }
);
```

## Context sources

Context sources allow you to provide additional information to the translation
process.  They come in two modes:

`"required"`
:   Always executed before translation begins

`"passive"`
:   Available as tools that the LLM can invoke when needed

### Required context sources

Use required sources for information that's always relevant:

```typescript twoslash
const text: string = "";
// ---cut-before---
import type {
  ContextResult,
  RequiredContextSource,
} from "@vertana/core";
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

// Create a context source that fetches author information
const authorBioSource: RequiredContextSource = {
  name: "author-bio",
  description: "Author biography and writing style",
  mode: "required",
  async gather(): Promise<ContextResult> {
    // In practice, this might fetch from a database or API
    return {
      content: `
        Author: Jane Smith
        Style: Academic, formal tone
        Specialization: Environmental science
      `
    };
  }
};

const result = await translate(
  openai("gpt-4o"),
  "ko",
  text,
  {
    contextSources: [authorBioSource]
  }
);
```

### Passive context sources

Passive sources are exposed as tools that the LLM agent can invoke when it
determines they would be helpful:

```typescript twoslash
const text: string = "";
// ---cut-before---
import type { ContextResult, PassiveContextSource } from "@vertana/core";
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";
import { z } from "zod";

// A source that looks up technical terms
const termLookupSource: PassiveContextSource<{ term: string }> = {
  name: "term-lookup",
  description: "Looks up technical terms in the company glossary",
  mode: "passive",
  parameters: z.object({
    term: z.string().describe("The technical term to look up")
  }),
  async gather(params): Promise<ContextResult> {
    // Look up the term in your glossary database
    const definition = await lookupTerm(params.term);
    return { content: definition };
  }
};

const result = await translate(
  openai("gpt-4o"),
  "ko",
  text,
  {
    contextSources: [termLookupSource]
  }
);

declare function lookupTerm(term: string): Promise<string>;
```

> \[!NOTE]
> Passive context sources require a schema definition using a library that
> implements the [Standard Schema] specification, such as [Zod], [Valibot],
> or [ArkType].

[Standard Schema]: https://standardschema.dev/

[Zod]: https://zod.dev/

[Valibot]: https://valibot.dev/

[ArkType]: https://arktype.io/

## Cancellation

All translation operations support cancellation through [`AbortSignal`]:

```typescript twoslash
const text: string = "";
// ---cut-before---
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";

const controller = new AbortController();

// Cancel after 30 seconds
setTimeout(() => controller.abort(), 30000);

try {
  const result = await translate(
    openai("gpt-4o"),
    "ko",
    text,
    {
      signal: controller.signal
    }
  );
} catch (error) {
  if (error instanceof Error && error.name === "AbortError") {
    console.log("Translation was cancelled");
  }
}
```

[`AbortSignal`]: https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal

## Putting it all together

Here's a comprehensive example using multiple Vertana features:

```typescript twoslash
const longTechnicalDocument: string = "";
declare function fetchStyleGuide(): Promise<string>;
// ---cut-before---
import type { RequiredContextSource } from "@vertana/core";
import { translate } from "@vertana/facade";
import { openai } from "@ai-sdk/openai";
import { anthropic } from "@ai-sdk/anthropic";

// Style guide context source
const styleGuideSource: RequiredContextSource = {
  name: "style-guide",
  description: "Company translation style guide",
  mode: "required",
  async gather() {
    const guide = await fetchStyleGuide();
    return { content: guide };
  }
};

const result = await translate(
  // Use multiple models for best-of-N selection
  [
    openai("gpt-4o"),
    anthropic("claude-sonnet-4-20250514")
  ],
  "ja",
  longTechnicalDocument,
  {
    // Basic options
    sourceLanguage: "en",
    domain: "software engineering",
    tone: "technical",
    mediaType: "text/markdown",

    // Predefined glossary
    glossary: [
      { original: "dependency injection", translated: "依存性注入" },
      { original: "middleware", translated: "ミドルウェア" },
      { original: "callback", translated: "コールバック" }
    ],

    // Enable dynamic glossary for additional terms
    dynamicGlossary: true,

    // Enable iterative refinement
    refinement: {
      maxIterations: 3,
      qualityThreshold: 0.9
    },

    // Enable best-of-N selection
    bestOfN: true,

    // Add context from style guide
    contextSources: [styleGuideSource],

    // Track progress
    onProgress: (progress) => {
      switch (progress.stage) {
        case "gatheringContext":
          console.log("Gathering context...");
          break;
        case "chunking":
          console.log("Splitting document...");
          break;
        case "translating":
          console.log(
            `Translating chunk ${progress.chunkIndex! + 1}/${progress.totalChunks}`
          );
          break;
        case "selecting":
          console.log("Selecting best translation...");
          break;
        case "refining":
          console.log(
            `Refining (iteration ${progress.iteration}/${progress.maxIterations})`
          );
          break;
      }
    }
  }
);

console.log("Translation complete!");
console.log(`Quality score: ${result.qualityScore}`);
console.log(`Selected model: ${result.selectedModel}`);
console.log(`Terms extracted: ${result.accumulatedGlossary?.length}`);
```

---

---
url: /manuals/context-web.md
description: >-
  Guide to using @vertana/context-web for fetching and extracting content from
  linked web pages to provide additional translation context.
---

# Web context

The *@vertana/context-web* package provides context sources that fetch and
extract content from web pages.  This is useful when translating documents
that reference external articles or resources.

## Installation

::: code-group

```bash [Deno]
deno add jsr:@vertana/context-web
```

```bash [npm]
npm add @vertana/context-web
```

```bash [pnpm]
pnpm add @vertana/context-web
```

```bash [Yarn]
yarn add @vertana/context-web
```

```bash [Bun]
bun add @vertana/context-web
```

:::

## Overview

This package provides three main context sources:

[`fetchWebPage`](#fetchwebpage)
:   A passive context source that fetches a single URL on demand.
The LLM can call this tool when it needs additional context.

[`fetchLinkedPages`](#fetchlinkedpages)
:   A required context source factory that extracts all links from the
source text and fetches their content before translation begins.

[`searchWeb`](#searchweb)
:   A passive context source that performs a web search and returns a list
of results (title, URL, snippet).

`fetchWebPage` and `fetchLinkedPages` use [Mozilla's Readability] algorithm
to extract the main article content from web pages, filtering out navigation,
ads, and other noise.

[Mozilla's Readability]: https://github.com/mozilla/readability

## `fetchWebPage`

A passive context source that the LLM can invoke when it needs to fetch
a specific URL.

```typescript twoslash
import type { LanguageModel } from "ai";
declare const model: LanguageModel;
// ---cut-before---
import { translate } from "@vertana/facade";
import { fetchWebPage } from "@vertana/context-web";

const text = `
This article discusses the concept explained at https://example.com/guide.
`;

const result = await translate(model, "ko", text, {
  contextSources: [fetchWebPage],
});
```

When the LLM encounters a reference it wants to understand better, it can
call the `fetch-web-page` tool with the URL to retrieve the page content.

## `fetchLinkedPages`

A factory function that creates a required context source.  It extracts
all URLs from the source text and fetches their content before translation
begins.

```typescript twoslash
import type { LanguageModel } from "ai";
declare const model: LanguageModel;
// ---cut-before---
import { translate } from "@vertana/facade";
import { fetchLinkedPages } from "@vertana/context-web";

const text = `
Check out https://example.com/article for background.
Also see https://example.com/reference for more details.
`;

const result = await translate(model, "ko", text, {
  contextSources: [
    fetchLinkedPages({
      text,
      mediaType: "text/plain",
    }),
  ],
});
```

### Options

`text`
:   The source text to extract links from.

`mediaType`
:   The media type of the text (`"text/plain"`, `"text/markdown"`,
or `"text/html"`).  This affects how links are extracted.

`maxLinks`
:   Maximum number of links to fetch.  Defaults to `10`.

`timeout`
:   Timeout for each fetch request in milliseconds.  Defaults to `10000`.

## `searchWeb`

A passive context source that the LLM can invoke when it needs to perform
web search.  This source only returns a list of results and does not fetch
any result pages.

```typescript twoslash
import type { LanguageModel } from "ai";
declare const model: LanguageModel;
// ---cut-before---
import { translate } from "@vertana/facade";
import { searchWeb } from "@vertana/context-web";

const text = "Please translate this and cite sources.";

const result = await translate(model, "ko", text, {
  contextSources: [searchWeb],
});
```

When the LLM needs to find a relevant resource, it can call the `search-web`
tool with a query to obtain a list of results (title, URL, snippet).

### Options

`query`
:   The search query keyword(s).

`maxResults`
:   Maximum number of results to return.  Defaults to `10`.

`region`
:   DuckDuckGo region parameter (`kl`), e.g. `"kr-kr"` or `"us-en"`.

`timeRange`
:   Time range filter (`df`): `"d"` (day), `"w"` (week), `"m"` (month),
`"y"` (year).

## Combining sources

For best results, use these sources together:

1. `fetchLinkedPages` provides context from links already present in the input.
2. `searchWeb` helps the LLM find relevant pages when the input has no links.
3. `fetchWebPage` lets the LLM fetch a specific result URL for more detail.

```typescript twoslash
import type { LanguageModel } from "ai";
declare const model: LanguageModel;
// ---cut-before---
import { translate } from "@vertana/facade";
import { fetchLinkedPages, fetchWebPage, searchWeb } from "@vertana/context-web";

const text = `
Read the introduction at https://example.com/intro.
`;

const result = await translate(model, "ko", text, {
  contextSources: [
    // Pre-fetch all links in the text
    fetchLinkedPages({ text, mediaType: "text/plain" }),
    // Allow LLM to search the web and fetch additional URLs on demand
    searchWeb,
    fetchWebPage,
  ],
});
```

## extractLinks utility

The `extractLinks` function extracts URLs from text.  It's used internally
by `fetchLinkedPages` but is also exported for custom use cases.

```typescript twoslash
import { extractLinks } from "@vertana/context-web";

// From plain text
const plainUrls = extractLinks(
  "Check https://example.com for info.",
  "text/plain"
);
// => ["https://example.com"]

// From Markdown
const mdUrls = extractLinks(
  "See [this article](https://example.com/article).",
  "text/markdown"
);
// => ["https://example.com/article"]

// From HTML
const htmlUrls = extractLinks(
  '<a href="https://example.com">Link</a>',
  "text/html"
);
// => ["https://example.com"]
```

## CLI usage

The Vertana CLI includes the `-L` or `--fetch-links` flag that enables
web context fetching:

```bash
vertana translate -t ko -L document.md
```

This automatically:

1. Extracts all links from the input document
2. Fetches and extracts content from linked pages
3. Provides the content as context for translation

See the [*CLI reference*](./cli.md) for more details.

---

---
url: /about.md
description: 'Overview of Vertana''s goals, workflow, and package structure.'
---

# What is Vertana?

Vertana\[^1] is an LLM-powered agentic translation library for TypeScript.
It goes beyond a single “prompt in, text out” translation call by orchestrating
multiple steps—gathering context, enforcing terminology, evaluating quality, and
iteratively refining output.

Vertana is designed for applications where translation is part of a product or a
workflow: documentation sites, developer tools, localization pipelines, customer
support tooling, or internal knowledge bases.

\[^1]: The name *Vertana* is derived from the Sanskrit word *वर्तन* (*vartana*),
meaning *turning*, *moving*, or *abiding*.

## Why an agentic workflow?

A single-pass translation is often good enough for short, generic text.
It becomes fragile when you need:

* *Consistent terminology* across a document or project
* *Domain-aware accuracy* in technical, legal, or medical content
* *Style consistency* (tone, voice, formatting)
* *Quality control* beyond “sounds okay”

Vertana treats translation as a process.  It can gather supporting information,
use it during translation, and improve the result until it is acceptable.

## How Vertana works

Vertana composes a translation from multiple stages:

1. *Chunking*: Split long input into manageable pieces while preserving
   formatting and structure.
2. *Context gathering*: Collect relevant information from configured sources
   (required sources run up front; passive sources are exposed as tools).
3. *Translation*: Generate a draft translation with the available context.
4. *Evaluation*: Score and critique the translation against explicit criteria.
5. *Refinement*: Iteratively apply feedback to improve weak spots.
6. *Selection*: Optionally compare multiple candidates and pick the best.

Not every workflow uses every stage, but the building blocks are there when you
need tighter control.

## Key concepts

`context sources`
:   Pluggable functions that provide additional information.
They can inject style guides, background context, glossary databases, or
anything else that helps a model make better translation decisions.

`glossaries`
:   Term mappings used to enforce consistent translations.
Vertana can apply a predefined glossary and can also accumulate terminology
as it translates.

`refinement`
:   An iterative loop that evaluates quality and improves the translation until
it meets configured thresholds.

`best-of-N selection`
:   A workflow that generates multiple candidates (potentially from different
models) and chooses the most suitable result via comparative evaluation.

## Package overview

Vertana is a monorepo with several packages:

*@vertana/facade*
:   The high-level API.
Use this if you want a single `translate()` entry point and sensible
defaults.

*@vertana/core*
:   The underlying translation pipeline.
Use this if you need lower-level building blocks or custom orchestration.

*@vertana/context-web*
:   Helpers for web-based context gathering.
Use this to fetch and extract context from linked pages.

*@vertana/cli*
:   A command-line interface for translation without writing code.

## What Vertana is not

Vertana is intentionally focused on high-quality, product-grade translation.
It is not:

* A replacement for full localization platforms (string extraction,
  translation memory, review workflows, etc.)
* A guarantee of factual correctness (LLMs can still make mistakes)
* A single “magic prompt” that works for every domain without configuration

## Next steps

* Start with the [*Getting started*](./start.md) guide.
* Follow the [*Tutorial*](./tutorial.md) for an end-to-end walkthrough.
* Dive deeper in the [*Manuals*](./manuals/context.md) section.

# Source: https://lingui.dev/tools/introduction.md

# Source: https://lingui.dev/introduction.md

# Source: https://lingui.dev/tools/introduction.md

# Source: https://lingui.dev/introduction.md

# Introduction

📖 A readable, automated, and optimized internationalization for JavaScript

> **Internationalization** is the design and development of a product, application or document content that enables easy **localization** for target audiences that vary in culture, region, or language.
>
> — [W3C Web Internationalization FAQ](https://www.w3.org/International/questions/qa-i18n)

[![GitHub stars](https://img.shields.io/github/stars/lingui/js-lingui.svg?style=social\&label=Stars)](https://github.com/lingui/js-lingui/)

## Key Features[​](#key-features "Direct link to Key Features")

Lingui is an easy yet powerful internationalization framework for global projects.

### Clean and Readable[​](#clean-and-readable "Direct link to Clean and Readable")

Keep your code clean and readable, while the library uses battle-tested and powerful **ICU MessageFormat** under the hood.

### Universal[​](#universal "Direct link to Universal")

Use it everywhere. [`@lingui/core`](/ref/core.md) provides the essential intl functionality which works in any JavaScript project, while [`@lingui/react`](/ref/react.md) offers components for leveraging React rendering, including React Server Components (RSC) support.

### Full Rich-text Support[​](#full-rich-text-support "Direct link to Full Rich-text Support")

Seamlessly use React components within localized messages, without any restrictions. Creating rich-text messages feels just like writing JSX.

### Powerful Tooling[​](#powerful-tooling "Direct link to Powerful Tooling")

Manage your intl workflow with the Lingui [CLI](/ref/cli.md), [Vite Plugin](/ref/vite-plugin.md), and [ESLint Plugin](/ref/eslint-plugin.md). The CLI extracts, compiles and validates messages, while the Vite plugin compiles catalogs on the fly, and the ESLint plugin helps catch common usage errors.

### Unopinionated[​](#unopinionated "Direct link to Unopinionated")

Integrate Lingui into your existing workflow. It supports explicit message keys as well as auto-generated ones. Translations are stored either in JSON or standard PO file, which is supported in almost all translation tools.

### Lightweight and Optimized[​](#lightweight-and-optimized "Direct link to Lightweight and Optimized")

Core library is less than [2 kB gzipped](https://bundlephobia.com/result?p=@lingui/core), React components are additional [1.4 kB gzipped](https://bundlephobia.com/result?p=@lingui/react).

### AI Translations Ready[​](#ai-translations-ready "Direct link to AI Translations Ready")

For AI to do great translations for you, context is critical. Translating UI copy is difficult because it's usually a list of short strings without enough context. Lingui's localization formats allow developers to write descriptions of where and how your keys are used. This allows both human translators and AI to make better translations.

### Active Community[​](#active-community "Direct link to Active Community")

Join the growing [community of developers](/community) who are using Lingui to build global products.

## Workflow[​](#workflow "Direct link to Workflow")

Using Lingui for internationalization is a straightforward process. Here's a high-level overview of the workflow.

![Workflow scheme](/assets/images/lingui-workflow-4c23edf0d9cbf3c08849eb56f11a8bbb.svg)

### Define Messages[​](#define-messages "Direct link to Define Messages")

Write messages directly in your codebase using Lingui's components. This keeps your code clean and readable while embedding translations naturally.

### Extract[​](#extract "Direct link to Extract")

Use the Lingui CLI to extract all translatable messages from your codebase and create or update message catalogs. This step ensures that all messages are captured and ready for translation.

### Translate[​](#translate "Direct link to Translate")

Translate your message catalogs either manually or through integration with translation tools.

### Compile[​](#compile "Direct link to Compile")

Use the Lingui CLI to compile your message catalogs into a format that can be used in your application. This step minimizes the size of your translation bundle and ensures that only the necessary data is bundled.

### Deploy[​](#deploy "Direct link to Deploy")

Include the compiled message catalogs in your production build to ensure that users receive localized content based on their language preferences.

## Quick Overview[​](#quick-overview "Direct link to Quick Overview")

```
import React from "react";
import { Trans, Plural, useLingui } from "@lingui/react/macro";

export default function Lingui({ numUsers, name = "You" }) {
  const { t } = useLingui();

  return (
    <div>
      <h1>
        {/* Localized messages are simply wrapped in <Trans> */}
        <Trans>Internationalization in React</Trans>
      </h1>

      {/* Element attributes are translated using t macro */}
      <img src="./logo.png" alt={t`Logo of Lingui Project`} />

      <p>
        {/* Variables are passed to messages in the same way as in JSX */}
        <Trans>Hello {name}, Lingui is a readable, automated, and optimized i18n for JavaScript.</Trans>
      </p>

      {/* React Elements inside messages works in the same way as in JSX */}
      <p>
        <Trans>
          Read the <a href="https://lingui.dev">documentation</a>
          for more info.
        </Trans>
      </p>

      {/*
        Plurals are managed using ICU plural rules.
        Nesting of i18n components is allowed.
        Syntactically valid message in ICU MessageFormat is guaranteed.
      */}
      <Plural
        value={numUsers}
        one={
          <span>
            Only <strong>one</strong> user is using this library!
          </span>
        }
        other={
          <span>
            <strong>{numUsers}</strong> users are using this library!
          </span>
        }
      />
    </div>
  );
}
```

## See Also[​](#see-also "Direct link to See Also")

* [Installation and Setup](/installation.md)

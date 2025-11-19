# Lingui Documentation

Source: https://lingui.dev/llms-full.txt

---

# Lingui


## installation

- [Installation and Setup](/installation.md): Learn how to install Lingui in your project

## tutorials

- [JavaScript Apps Internationalization](/tutorials/javascript.md): Learn how to use Lingui's internationalization features in your vanilla JavaScript application
- [React Apps Internationalization](/tutorials/react.md): Learn how to add internationalization to a React application using Lingui
- [React Native Apps Internationalization](/tutorials/react-native.md): Learn how to add internationalization to a React Native application using Lingui
- [Lingui with React Server Components](/tutorials/react-rsc.md): Learn how to setup and use Lingui with RSC & Next.js

## guides

- [Custom Extractor](/guides/custom-extractor.md): Learn how to write a custom message extractor for your project
- [Custom Formatter](/guides/custom-formatter.md): Learn how to write a custom localization message formatter for your project
- [Dynamic Loading of Message Catalogs](/guides/dynamic-loading-catalogs.md): Learn how to set up dynamic loading of message catalogs in Lingui to reduce bundle size and improve performance
- [Explicit vs Generated IDs](/guides/explicit-vs-generated-ids.md): Learn about the differences between explicit and generated IDs and how to choose the right approach for your project
- [Lazy Translations](/guides/lazy-translations.md): Lazy translations allow you to defer translation of a message until it is actually displayed
- [Message Extraction](/guides/message-extraction.md): Learn about message extraction in i18n and how to use Lingui to extract messages from your application
- [ICU MessageFormat](/guides/message-format.md): ICU MessageFormat is a flexible and powerful syntax designed to express the grammatical nuances of different languages. Its flexibility ensures that your application can handle grammatical variations, making it essential for effective internationalization.
- [Monorepo](/guides/monorepo.md): If you're using lingui within a monorepo you need:
- [Keeping Your Bundle Small: How Lingui Optimizes for Performance](/guides/optimizing-bundle-size.md): When you're building a modern app with internationalization (i18n), it's easy to end up with a bloated bundle. The more languages and messages you have, the more it can grow — fast.
- [Pluralization](/guides/plurals.md): Learn about pluralization and how to use it in your application with Lingui
- [Pseudolocalization](/guides/pseudolocalization.md): Learn how to use pseudolocalization to test the internationalization aspects of your application with Lingui
- [Testing](/guides/testing.md): In a React application, components that use Trans or useLingui need access to the context provided by I18nProvider. How you wrap your component with the I18nProvider depends on the testing library you're using.

## ref

- [Catalog Formats](/ref/catalog-formats.md): Learn about the different catalog formats supported by Lingui
- [Lingui CLI](/ref/cli.md): Learn how to set up and use Lingui CLI to extract, merge and compile message catalogs
- [Configuration](/ref/conf.md): Learn how to configure Lingui for your project
- [Core API Reference](/ref/core.md): The package provides the main i18n object, which manages message catalogs, active locale, and message translation and formatting
- [ESLint Plugin](/ref/eslint-plugin.md): Lingui ESLint Plugin helps you find and prevent common i18n mistakes in your code
- [Vue.js Extractor](/ref/extractor-vue.md): The @lingui/extractor-vue package provides a custom extractor that handles Vue.js files.
- [Webpack Loader](/ref/loader.md): The @lingui/loader is a Webpack loader for Lingui message catalogs. It offers an alternative to the lingui compile and compiles catalogs on the fly.
- [Locale Detection](/ref/locale-detector.md): Detect the user's locale with the `@lingui/detect-locale` package
- [Macros](/ref/macro.md): Transform JavaScript objects and JSX elements into ICU MessageFormat messages
- [Metro Transformer](/ref/metro-transformer.md): Use Lingui with React Native and compile your message catalogs on the fly
- [React API Reference](/ref/react.md): Reference for the Lingui React API and components
- [SWC Plugin](/ref/swc-plugin.md): Use Lingui Macros in your SWC project
- [Vite Plugin](/ref/vite-plugin.md): Use Lingui with Vite and compile your message catalogs on the fly

## examples

- [Examples](/examples.md): Examples of using Lingui for internationalization (i18n) in various frameworks and libraries

## introduction

- [Introduction](/introduction.md): Lingui is a universal, clean and readable, lightweight and powerful internationalization framework for global projects

## tools

- [Crowdin](/tools/crowdin.md): Crowdin is a localization management platform that helps translate your LinguiJS-based product. Automate localization, release several multilingual versions of your app simultaneously, and provide an enhanced experience for your global customers.
- [Sync & Collaboration Tools](/tools/introduction.md): While Lingui provides a powerful API for managing your translations, it doesn't provide an integrated solution for managing synchronization and collaboration with your translators.
- [Translation.io](/tools/translation-io.md): Translation.io is a professional synchronization and collaboration platform that will assist your team in the translation of your Lingui application.


---

# Full Documentation Content

# Examples

To help you get started with Lingui, we've provided some example projects that demonstrate how Lingui can be integrated into various frameworks and libraries. These projects demonstrate Lingui's versatility and show you how to use it in real-world scenarios.

Check out the example projects below:

* [Create React App](https://github.com/lingui/js-lingui/tree/main/examples/create-react-app)
* [Vanilla JS](https://github.com/lingui/js-lingui/tree/main/examples/js)
* [Next.js with Babel](https://github.com/lingui/js-lingui/tree/main/examples/nextjs-babel)
* [Next.js with SWC and app router](https://github.com/lingui/js-lingui/tree/main/examples/nextjs-swc)
* [React Native (uses Expo)](https://github.com/lingui/js-lingui/tree/main/examples/react-native)
* [React with Vite and Babel](https://github.com/lingui/js-lingui/tree/main/examples/vite-project-react-babel)
* [React with Vite and SWC](https://github.com/lingui/js-lingui/tree/main/examples/vite-project-react-swc)
* [Rspack with SWC](https://github.com/lingui/js-lingui/tree/main/examples/rspack)
* [Remix with Vite and Babel](https://github.com/lingui/js-lingui/tree/main/examples/remix-vite-babel)
* [Tanstack Start with Vite and Babel](https://github.com/lingui/js-lingui/tree/main/examples/tanstack-start)


---

# Custom Extractor

Lingui's default extractor supports JavaScript (Stage 3), TypeScript, and Flow out of the box, covering most standard and modern syntax features. However, if your project relies on experimental ECMAScript syntax or custom file formats, a custom extractor gives you the flexibility to handle these scenarios.

### Why It Doesn't Use Your Babel Config?[​](#why-it-doesnt-use-your-babel-config "Direct link to Why It Doesn't Use Your Babel Config?")

Babel plugins from your configuration define transformations, and some of these may interfere with or slow down the extraction process. The extractor doesn't have to transform your code, it just analyzes it. Therefore, it's designed to understand different syntax without worrying about how the code is transpiled or down-levelled.

info

We are constantly updating the extractor to keep up with the latest ECMAScript features. However, if you find that a recently added Stage 3 feature doesn't work as expected, please [create an issue](https://github.com/lingui/js-lingui/issues/new/choose).

## Experimental ECMAScript Syntax[​](#experimental-ecmascript-syntax "Direct link to Experimental ECMAScript Syntax")

If you are using experimental features (Stage 0 - Stage 2), you'll need to configure a custom list of parser plugins. This can be done by overriding the default extractor and using the `extractFromFileWithBabel()` function:

lingui.config.ts

```
import { extractFromFileWithBabel, defineConfig } from "@lingui/cli/api";
import type { ParserPlugin } from "@babel/parser";

export function getBabelParserOptions(filename: string) {
  // https://babeljs.io/docs/en/babel-parser#latest-ecmascript-features
  const parserPlugins: ParserPlugin[] = ["importAttributes", "explicitResourceManagement"];

  if ([/\.ts$/, /\.mts$/, /\.cts$/, /\.tsx$/].some((r) => filename.match(r))) {
    parserPlugins.push("typescript");
  }

  if ([/\.js$/, /\.jsx$/, /\.tsx$/].some((r) => filename.match(r))) {
    parserPlugins.push("jsx");
  }

  return parserPlugins;
}

export default defineConfig({
  // [...]
  extractors: [
    {
      match(filename: string) {
        return filename.match(/\.[cm][tj]sx?$/);
      },
      async extract(filename, code, onMessageExtracted, ctx) {
        return extractFromFileWithBabel(filename, code, onMessageExtracted, ctx, {
          // https://babeljs.io/docs/babel-parser#plugins
          plugins: getBabelParserOptions(filename),
        });
      },
    },
  ],
});
```

## Other Frameworks or Custom Syntax[​](#other-frameworks-or-custom-syntax "Direct link to Other Frameworks or Custom Syntax")

If you're working with files that aren't valid JavaScript, you can create a custom extractor to handle them:

./my-custom-extractor.ts

```
import { extractor as defaultExtractor } from "@lingui/cli/api";

export const extractor: ExtractorType = {
  match(filename: string) {
    return filename.endsWith(".custom");
  },
  extract(filename: string, code: string, onMessageExtracted, ctx: ExtractorCtx) {
    // Transform the file to plain JS + Sourcemaps
    const { code: transformedCode, sourcemaps } = transformMyCustomFileToJs(filename, code);

    // Access Lingui config via `ctx.linguiConfig`
    // Reuse the default CLI extractor
    return defaultExtractor.extract(filename, transformedCode, onMessageExtracted, {
      sourcemaps,
      ...ctx,
    });
  },
};
```

### Adding the Custom Extractor to the Configuration[​](#adding-the-custom-extractor-to-the-configuration "Direct link to Adding the Custom Extractor to the Configuration")

To use the custom extractor, you need to add it to your Lingui configuration file:

lingui.config.ts

```
import { extractor } from "./my-custom-extractor.ts";
import { defineConfig } from "@lingui/cli";

export default defineConfig({
  // [...]
  extractors: [extractor],
});
```

Important

If you are using TypeScript to create your extractor, you should use the `.ts` extension for your Lingui configuration file.


---

# Custom Formatter

If your project requires a message catalog format that Lingui doesn't [natively support](/ref/catalog-formats.md), you can create a custom formatter to handle it. A custom formatter allows you to define how extracted strings are formatted into a custom catalog format, providing flexibility for specialized workflows and integration with unique file structures.

## Overview[​](#overview "Direct link to Overview")

A formatter is an object with two main functions, `parse` and `serialize`, which define how catalogs are read from and written to your custom format.

The formatter can be configured directly in your `lingui.config.{ts,js}` file - no separate package is needed:

lingui.config.{ts,js}

```
import { defineConfig } from "@lingui/cli";
import { extractor } from "./my-custom-extractor.ts";

export default defineConfig({
  // [...]
  format: {
    catalogExtension: "json",
    parse: (content: string): CatalogType => JSON.parse(content),
    serialize: (catalog: CatalogType): string => JSON.stringify(catalog),
  },
});
```

## Reference[​](#reference "Direct link to Reference")

The shape of formatter is the following:

```
export type CatalogFormatter = {
  catalogExtension: string;
  /**
   * Set extension used when extract to template
   * Omit if the extension is the same as catalogExtension
   */
  templateExtension?: string;
  parse(
    content: string,
    ctx: { locale: string | null; sourceLocale: string; filename: string }
  ): Promise<CatalogType> | CatalogType;
  serialize(
    catalog: CatalogType,
    ctx: { locale: string | null; sourceLocale: string; filename: string; existing: string | null }
  ): Promise<string> | string;
};
```

Lingui Catalog is an object with the following structure:

```
export type CatalogType = {
  [msgId: string]: MessageType;
};

type CatalogExtra = Record<string, unknown>;

export type MessageType<Extra = CatalogExtra> = {
  message?: string;
  origin?: MessageOrigin[];
  comments?: string[];
  obsolete?: boolean;
  context?: string;
  translation?: string;

  /**
   * the generic field where
   * formatters can store additional data
   */
  extra?: Extra;
};
```

Important

If you are using TypeScript to create your formatter, you should use the `.ts` extension for your Lingui configuration file.


---

# Dynamic Loading of Message Catalogs

Internationalization in modern applications requires careful handling of localized messages to avoid bloating the initial bundle size. By default, Lingui makes it easy to load all strings for a single active locale. For even greater efficiency, developers can selectively load only the messages needed on demand using [`i18n.load`](/ref/core.md#i18n.load), ensuring minimal resource usage.

The [`I18nProvider`](/ref/react.md#i18nprovider) component doesn't make assumptions about your app's structure, giving you the freedom to load only the necessary messages for the currently selected language.

This guide shows how to set up dynamic loading of message catalogs, ensuring only the needed catalogs are loaded, which reduces bundle size and improves performance.

## Final i18n Loader Helper[​](#final-i18n-loader-helper "Direct link to Final i18n Loader Helper")

The following code defines the complete logic for dynamically loading and activating message catalogs based on the selected locale. It ensures that only the required catalog is loaded at runtime, optimizing performance:

i18n.ts

```
import { i18n } from "@lingui/core";

export const locales = {
  en: "English",
  cs: "Česky",
};
export const defaultLocale = "en";

/**
 * We do a dynamic import of just the catalog that we need
 * @param locale any locale string
 */
export async function dynamicActivate(locale: string) {
  const { messages } = await import(`./locales/${locale}/messages`);
  i18n.load(locale, messages);
  i18n.activate(locale);
}
```

Important

Even the "default" locale requires a catalog to be loaded. Lingui aims to keep the internationalization footprint to a minimum by dropping default messages from the production build. This way, only the catalog for the active language is loaded, avoiding duplication.

Without this optimization, switching from the default language (e.g. EN) to another (e.g. FR) would require loading both language catalogs. This strategy ensures efficiency by loading only the necessary messages for one language at a time.

### Usage in Your Application[​](#usage-in-your-application "Direct link to Usage in Your Application")

To use the `dynamicActivate` function in your application, you must call it on application startup. The following example shows how to use it in a React application:

```
import React, { useEffect } from "react";
import App from "./App";

import { I18nProvider } from "@lingui/react";
import { i18n } from "@lingui/core";
import { defaultLocale, dynamicActivate } from "./i18n";

const I18nApp = () => {
  useEffect(() => {
    // With this method we dynamically load the catalogs
    dynamicActivate(defaultLocale);
  }, []);

  return (
    <I18nProvider i18n={i18n}>
      <App />
    </I18nProvider>
  );
};
```

### Optimized Bundle Structure[​](#optimized-bundle-structure "Direct link to Optimized Bundle Structure")

Looking at the contents of the build directory, we find a separate chunk for each language:

```
i18n-0.c433b3bd.chunk.js
i18n-1.f0cf2e3d.chunk.js
main.ab4626ef.js
```

When the page is first loaded, only the main bundle and the bundle for the first language are loaded:

![Requests during the first render](/assets/images/dynamic-loading-catalogs-1-142e71bb089432f649766b3077d504c3.png)

After changing the language in the UI, the second language bundle is loaded:

![Requests during the second render](/assets/images/dynamic-loading-catalogs-2-eade7ea8527b393f9da2a5053a493aa3.png)

## Dependency Tree Extractor (experimental)[​](#dependency-tree-extractor-experimental "Direct link to Dependency Tree Extractor (experimental)")

The Dependency Tree Extractor is an experimental feature designed to improve message extraction by analyzing the dependency tree of your application. This tool improves the efficiency of loading localized messages by identifying only the necessary messages for each component or page, rather than extracting all messages into a single catalog.

This allows for a more granular extraction process, resulting in smaller and more relevant message catalogs.

For detailed guidance on message extraction, refer to the [Message Extraction](/guides/message-extraction.md) guide.


---

# Explicit vs Generated IDs

When internationalizing your application, you may need to decide whether to use explicit or generated IDs for your messages.

In this guide, we explore the basic concepts of explicit and generated IDs, and then delve into a comprehensive comparison, highlighting the advantages and disadvantages of each approach.

## What are Explicit IDs and Generated IDs?[​](#what-are-explicit-ids-and-generated-ids "Direct link to What are Explicit IDs and Generated IDs?")

### Explicit ID[​](#explicit-id "Direct link to Explicit ID")

An explicit ID, often referred to as a user-defined or custom ID, is a manually assigned identifier associated with a specific message. These IDs are typically chosen by developers and are explicitly specified within your code.

The typical explicit id may look like `index.header.title` or `modal.buttons.cancel`.

Lingui example:

```
<Trans id="index.header.title">LinguiJS example</Trans>

// extracted as
{
  id: "index.header.title",
  message: "LinguiJS example",
}
```

### Generated IDs[​](#generated-ids "Direct link to Generated IDs")

On the other hand, generated IDs are created automatically by the internalization library. In Lingui, such IDs are created based on the source message and [context](#context).

Lingui example:

```
<Trans>LinguiJS example</Trans>

// extracted as
{
  id: "uxV9Xq",
  message: "LinguiJS example",
}
```

### Benefits of Generated IDs[​](#benefits-of-generated-ids "Direct link to Benefits of Generated IDs")

* **Avoiding the "naming things" problem:** You don't need to come up with a name for each single phrase in the app. Lingui generates the IDs (in the form of short hashes) from the messages.
* **Better developer experience:** Developers can focus on coding without needing to manually assign IDs, leading to a more streamlined development process. Searching for a user-facing string will lead to the place in code where it's used, as opposed to taking you to a (typically JSON) file full of translations.
* **Avoiding duplicates:** Duplicate messages are merged together automatically. Your translators will not have to translate the same phrases again and again. This could lead to cost savings, especially if translators charge by word count.
* **Smaller bundle:** Lingui generates short IDs such as `uxV9Xq` which are typically shorter than manually crafted IDs like `index.header.title`. This results in a smaller bundle size, optimizing your application's performance.
* **Preventing ID collisions:** As your application scales, explicit IDs can potentially lead to conflicts. Lingui's generated IDs ensure you steer clear of such collisions.

### Benefits of Explicit IDs[​](#benefits-of-explicit-ids "Direct link to Benefits of Explicit IDs")

* **Control:** Developers have full control over the naming and assignment of explicit IDs. This control allows for precise targeting and easy maintenance of internationalization keys.
* **Loose coupling:** Explicit IDs are loosely coupled with the messages (as opposed to when they are generated from the messages). This means that if the message changes, the ID remains the same. When your team uses a TMS (Translation Management System), this makes it easier even for non-technical people to update the strings.
* **Readability:** Explicit IDs often have meaningful names, making it easier for developers, translators, and content creators to understand their purpose within the codebase.
* **Predictability:** Since explicit IDs are manually assigned, they remain stable across different versions of your application, reducing the likelihood of breaking changes during updates.

In conclusion, the choice between these two strategies depends on your project requirements and priorities. However, it's important to note that Lingui provides the full range of benefits, especially with generated IDs.

note

You don't have to worry about the readability of the IDs because you would hardly see them. When extracted into a PO file, translators would see the source string and its corresponding translation, while the IDs remain behind the scenes:

```
#: src/App.tsx:1
msgid "LinguiJS example"
msgstr "LinguiJS przyklad"
```

## Context[​](#context "Direct link to Context")

By default, when using generated IDs, the same text elements are extracted with the same ID, and then translated once. However, this might not always be desirable since the same text can have different meanings and translations. For example, consider the word "right" and its two possible meanings:

* correct as in "you are right"
* direction as in "turn right"

To distinguish these two cases, you can add `context` to messages. The same text elements with different contexts are extracted with different IDs. Then, they can be translated differently and merged back into the application as different translation entries.

Regardless of whether you use generated IDs or not, adding context makes the translation process less challenging and helps translators interpret the source accurately. You, in return, get translations of better quality faster and decrease the number of context-related issues you would need to solve.

Examples:

```
import { Trans } from "@lingui/react/macro";
<Trans context="direction">right</Trans>;
<Trans context="correctness">right</Trans>;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";
<Trans id={"d1wX4r"} message="right" />;
<Trans id={"16eaSK"} message="right" />;
```

or with non-JSX macro:

```
import { msg } from "@lingui/core/macro";

const ex1 = msg({
  message: `right`,
  context: "direction",
});

const ex2 = msg({
  message: `right`,
  context: "correctness",
});

// ↓ ↓ ↓ ↓ ↓ ↓

const ex1 = {
  id: "d1wX4r",
  message: `right`,
};
const ex2 = {
  id: "16eaSK",
  message: `right`,
};
```

## Using Generated IDs[​](#using-generated-ids "Direct link to Using Generated IDs")

### With JSX Macro[​](#with-jsx-macro "Direct link to With JSX Macro")

```
import { Trans } from "@lingui/react/macro";

function render() {
  return (
    <>
      <h1>
        <Trans>LinguiJS example</Trans>
      </h1>
      <p>
        <Trans>
          Hello <a href="/profile">{name}</a>.
        </Trans>
      </p>
    </>
  );
}
```

In the example code above, the content of [`Trans`](/ref/macro.md#trans) is transformed into a message in MessageFormat syntax. By default, this message is used for generating the ID. Considering the example above, the catalog would contain these entries:

```
const catalog = [
  {
    id: "uxV9Xq",
    message: "LinguiJS example",
  },
  {
    id: "9/omjw",
    message: "Hello <0>{name}</0>.",
  },
];
```

### With Core Macro[​](#with-core-macro "Direct link to With Core Macro")

In the following example, the message `Hello World` will be extracted and used to create an ID:

```
import { msg } from "@lingui/core/macro";

msg`Hello World`;
```

## Using Custom IDs[​](#using-custom-ids "Direct link to Using Custom IDs")

### With JSX Macro[​](#with-jsx-macro-1 "Direct link to With JSX Macro")

To use custom IDs in JSX macros, pass the ID as a prop to the component:

```
import { Trans } from "@lingui/react/macro";

function render() {
  return (
    <>
      <h1>
        <Trans id="msg.header">LinguiJS example</Trans>
      </h1>
      <p>
        <Trans id="msg.hello">
          Hello <a href="/profile">{name}</a>.
        </Trans>
      </p>
    </>
  );
}
```

The messages with IDs `msg.header` and `msg.hello` will be extracted with their default values as `LinguiJS example` and `Hello <0>{name}</0>.` respectively.

### With Core Macro[​](#with-core-macro-1 "Direct link to With Core Macro")

To use custom IDs in non-JSX macros, call the [`msg`](/ref/macro.md#definemessage) function with a message descriptor object, passing the ID using the `id` property:

```
import { msg } from "@lingui/core/macro";

msg({ id: "msg.greeting", message: `Hello World` });
```

Message `msg.greeting` will be extracted with default value `Hello World`.

For all other js macros ([`plural`](/ref/macro.md#plural), [`select`](/ref/macro.md#select), [`selectOrdinal`](/ref/macro.md#selectordinal), use them inside [`msg`](/ref/macro.md#definemessage) macro to pass ID (in this case, `'msg.caption'`).

```
import { msg, plural } from "@lingui/core/macro";

msg({
  id: "msg.caption",
  message: plural(count, {
    one: "# image caption",
    other: "# image captions",
  }),
});
```

## See Also[​](#see-also "Direct link to See Also")

* [Message Extraction](/guides/message-extraction.md)
* [Macros Reference](/ref/macro.md)


---

# Lazy Translations

Lazy translation allows you to defer translation of a message until it's rendered, giving you flexibility in how and where you define messages in your code. With lazy translation, you can tag a string with the [`msg`](/ref/macro.md#definemessage) macro to create a *message descriptor* that can be saved, passed around as a variable, and rendered later.

## Usage Example[​](#usage-example "Direct link to Usage Example")

To render the message descriptor as a string-only translation, pass it to the [`i18n._()`](/ref/core.md#i18n._) method:

```
import { msg } from "@lingui/core/macro";
import { i18n } from "@lingui/core";

const favoriteColors = [msg`Red`, msg`Orange`, msg`Yellow`, msg`Green`];

export function getTranslatedColorNames() {
  return favoriteColors.map((color) => i18n._(color));
}
```

## Usage in React[​](#usage-in-react "Direct link to Usage in React")

To render the message descriptor in a React component, pass its `id` to the [`Trans`](/ref/react.md#trans) component as a value of the `id` prop:

```
import { msg } from "@lingui/core/macro";
import { Trans } from "@lingui/react";

const favoriteColors = [msg`Red`, msg`Orange`, msg`Yellow`, msg`Green`];

export default function ColorList() {
  return (
    <ul>
      {favoriteColors.map((color) => (
        <li>
          <Trans id={color.id} />
        </li>
      ))}
    </ul>
  );
}
```

Important

Please note that we import the `<Trans>` component from `@lingui/react` to use the runtime version, as the message is already defined and we don't need the compile-time macro here.

### Picking a Message Based on a Variable[​](#picking-a-message-based-on-a-variable "Direct link to Picking a Message Based on a Variable")

Sometimes you need to choose between different messages to display depending on the value of a variable. For example, imagine you have a numeric "status" code that comes from an API, and you need to display a message that represents the current status.

An easy way to do this is to create an object that maps the possible values of "status" to message descriptors (tagged with the [`msg`](/ref/macro.md#definemessage) macro) and render them as needed with deferred translation:

```
import { msg } from "@lingui/core/macro";
import { useLingui } from "@lingui/react";

const statusMessages = {
  ["STATUS_OPEN"]: msg`Open`,
  ["STATUS_CLOSED"]: msg`Closed`,
  ["STATUS_CANCELLED"]: msg`Cancelled`,
  ["STATUS_COMPLETED"]: msg`Completed`,
};

export default function StatusDisplay({ statusCode }) {
  const { _ } = useLingui();
  return <div>{_(statusMessages[statusCode])}</div>;
}
```

### Memoization Pitfall[​](#memoization-pitfall "Direct link to Memoization Pitfall")

In the following contrived example, we document how a welcome message will or will not be updated when locale changes. The documented behavior may not be intuitive at first, but it is expected, because of the way the `useMemo` dependencies work.

To avoid bugs with stale translations, use the `t` function returned from the [`useLingui`](/ref/macro.md#uselingui) macro: it is safe to use with memoization because its reference changes whenever the Lingui context updates.

Keep in mind that `useMemo` is primarily a performance optimization tool in React. Because of this, there might be no need to memoize your translations. Additionally, this issue is not present when using the `Trans` component, which we recommend using whenever possible.

```
import { i18n } from "@lingui/core";
import { msg } from "@lingui/core/macro";
import { useLingui } from "@lingui/react/macro";

const welcomeMessage = msg`Welcome!`;

// ❌ Bad! This code won't work
export function Welcome() {
  const buggyWelcome = useMemo(() => {
    return i18n._(welcomeMessage);
  }, []);

  return <div>{buggyWelcome}</div>;
}

// ❌ Bad! This code won't work either because the reference to i18n does not change
export function Welcome() {
  const { i18n } = useLingui();

  const buggyWelcome = useMemo(() => {
    return i18n._(welcomeMessage);
  }, [i18n]);

  return <div>{buggyWelcome}</div>;
}

// ✅ Good! `useMemo` consumes the `t` function from the `useLingui` macro
export function Welcome() {
  const { t } = useLingui();

  const welcome = useMemo(() => {
    return t(welcomeMessage);
  }, [t]);

  return <div>{welcome}</div>;
}
```


---

# Message Extraction

Message extraction is a key part of the internationalization process. It involves scanning your codebase to identify and extract all the defined messages, ensuring that your message catalogs stay synchronized with the source code.

In practice, developers define messages directly in the source code, and the extraction tool automatically collects these messages and stores them in a message catalog for translation.

Read more about the [`lingui extract`](/ref/cli.md#extract) command.

## Supported Patterns[​](#supported-patterns "Direct link to Supported Patterns")

The extractor operates at a static level, meaning that it analyzes the source code without executing it. As a result, it doesn't support complex patterns or dynamic code, and only simple, statically defined messages are collected.

### Macros Usage[​](#macros-usage "Direct link to Macros Usage")

> Macros are JavaScript transformers that run at build time. The value returned by a macro is inlined into the bundle instead of the original function call.

The Lingui Macro provides powerful macros to transform JavaScript objects and JSX elements into [ICU MessageFormat](/guides/message-format.md) messages at compile time.

Extractor supports all macro usage, such as the following examples:

```
import { t } from "@lingui/core/macro";
import { Trans } from "@lingui/react/macro";

t`Message`;

t({
  id: "custom.id",
  message: "Message with custom ID",
});

const jsx = <Trans>Hi, my name is {name}</Trans>;
```

The extractor matches the `t` and `Trans` macro calls and extracts the messages from them.

For more usage examples, see to the [Macros](/ref/macro.md) reference.

### Non-Macros Usage[​](#non-macros-usage "Direct link to Non-Macros Usage")

Non-macro use is also supported, but it's not common. It's recommended to use macros.

The extractor matches `i18n._` or `i18n.t` function calls. It also matches when these functions are called from other member expressions, such as `ctx.i18n.t()`.

caution

The extractor only matches calls by name. It doesn't check if they are really imported from Lingui packages.

For example:

```
i18n._("message.id");
i18n._({ id: "message.id" });

ctx.i18n._("message.id");
ctx.i18n.t("message.id");

ctx.request.i18n.t("message.id");

// and so on
```

To ignore a specific call expression during extraction, you can add a `lingui-extract-ignore` comment:

```
/* lingui-extract-ignore */
ctx.i18n._("Message");
```

Messages marked with this comment will be excluded from extraction.

### Explicitly Marking Messages[​](#explicitly-marking-messages "Direct link to Explicitly Marking Messages")

In addition to call expressions, which are the most commonly used method, the extractor tool also supports simple string literals and message descriptors with explicit annotations.

To do this, simply prefix your expression with the `/*i18n*/` comment, like so:

```
const messageDescriptor: MessageDescriptor = /*i18n*/ { id: "Description", comment: "description" };
const stringLiteral = /*i18n*/ "Message";
```

## Unsupported Patterns[​](#unsupported-patterns "Direct link to Unsupported Patterns")

The extractor is limited to extracting messages from code that is written a certain way. It cannot extract messages from variables or function calls. It also cannot follow the program structure and get the value of a variable defined elsewhere.

This means that in order for a message to be extracted, it must be defined directly in the function call:

```
// ❌ This message will not be extracted
const message = "Message";
i18n._(message);

// ✅ This message will be extracted
i18n._("Message");
```

## Defining Sources for Analyzing[​](#defining-sources-for-analyzing "Direct link to Defining Sources for Analyzing")

The extractor can locate source files in two ways: by specifying a glob pattern or by crawling the dependency tree.

### Glob Pattern[​](#glob-pattern "Direct link to Glob Pattern")

By default, `lingui extract` uses a glob pattern to search for source files containing messages.

The pattern is defined in the [`catalogs`](/ref/conf.md#catalogs) property of the Lingui configuration file in your project's root directory.

![Scheme of discovering by glob pattern](/assets/images/extractor-glob-scheme-450bc42bb7a09c538a20e45badbf087f.svg)

### Dependency Tree Crawling[​](#dependency-tree-crawling "Direct link to Dependency Tree Crawling")

While the glob-based extraction process works well for most projects, it can be challenging for multi-page applications (MPAs) such as Next.js. In such cases, the glob approach generates a single catalog that includes all messages from each page, which may not be ideal for effectively managing translations.

This means that the entire catalog must be loaded for each page or navigation, resulting in unnecessary loading of messages that aren't utilized on that specific page.

To address this issue, an `experimental-extractor` has been introduced in Lingui v4.

Experimental

This is an experimental feature. Experimental features are not covered by semver and may be subject to change.

This extractor uses the dependency tree of files, rather than just a glob pattern, to crawl imports and discover files more accurately.

By doing so, it creates a more optimized catalog that only contains the messages needed for each page.

The catalogs would still contain duplicate messages for common components, but it would be much better than the current approach.

![Scheme of discovering by dependencies](/assets/images/extractor-deps-scheme-a1918925811db3a4184d2a616a262e8f.svg)

To start using `experimental-extractor`, add the following section to your Lingui configuration:

```
/**
 *
 * @type {import('@lingui/conf').LinguiConfig}
 */
module.exports = {
  // remove everethying from `catalogs` property
  catalogs: [],
  experimental: {
    extractor: {
      // glob pattern of entrypoints
      // this will find all nextjs pages
      entries: ["<rootDir>/src/pages/**/*.tsx"],
      // output pattern, this instruct extractor where to store catalogs
      // src/pages/faq.tsx -> src/pages/locales/faq/en.po
      output: "<rootDir>/{entryDir}/locales/{entryName}/{locale}",
    },
  },
};
```

Then run the following command in your terminal:

```
lingui extract-experimental
```

#### Important Notes[​](#important-notes "Direct link to Important Notes")

It's worth noting that the accuracy of the catalog depends heavily on tree-shaking, a technique used by modern bundlers to remove unused code from the final bundle.

If the code passed to the extractor is written in a tree-shakeable way, the user will get highly accurate catalogs.

While you may think that your code is tree-shakeable, in practice tree-shaking may work differently than you expect, and some unwanted strings may be included in the catalogs.

To illustrate, let's consider the following code:

```
import { msg } from "@lingui/core/macro";

export const species = {
  Cardano: [
    {
      startsAt: 0,
      name: msg`Ghost`,
      icon: "Ghost",
    },
    {
      startsAt: 0.000001,
      name: msg`Plankton`,
      icon: "Plankton",
    },
  ],
};
```

On the surface, it may appear that this code can be safely removed from the final bundle if it isn't used. However, the `msg` function call may have a side effect that prevents the bundler from removing the entire `species` object from the final bundle. As a result, messages defined in this snippet may be included in more catalogs than expected.

tip

To avoid this issue, one solution is to wrap the `species` object inside an *Immediately Invoked Function Expression* (IIFE) and add the `/* @__PURE__ */` annotation.

By adding this annotation to the IIFE, we tell the bundler that the entire `species` object can be safely removed if it is not used or exported elsewhere in the code.

## Supported Source Types[​](#supported-source-types "Direct link to Supported Source Types")

The extractor supports TypeScript, Flow, and JavaScript (Stage 3) out of the box.

If you are using some experimental features (Stage 0 - Stage 2) or frameworks with custom syntax such as Vue.js or Svelte, you may want to implement your own custom extractor.

Visit [Custom Extractor](/guides/custom-extractor.md) to learn how to create a custom extractor.

## See Also[​](#see-also "Direct link to See Also")

* [Lingui CLI Reference](/ref/cli.md)
* [Macros Reference](/ref/macro.md)
* [Catalog Formats](/ref/catalog-formats.md)


---

# ICU MessageFormat

ICU MessageFormat is a flexible and powerful syntax designed to express the grammatical nuances of different languages. Its flexibility ensures that your application can handle grammatical variations, making it essential for effective internationalization.

## Overview[​](#overview "Direct link to Overview")

### Simple text[​](#simple-text "Direct link to Simple text")

Example: `Refresh inbox`

### Variables[​](#variables "Direct link to Variables")

Example: `Attachment {name} saved`

### Plurals[​](#plurals "Direct link to Plurals")

> Using language specific plural forms (`one`, `other`):

```
{count, plural, one {Message} other {Messages}}
```

> Using exact matches for specific counts (`=0`):

```
{count, plural, =0 {No messages}
                one {# message}
                other {# messages}}
```

> Offsetting plural forms:

```
{count, plural, offset:1
                =0 {Nobody read this message}
                =1 {Only you read this message}
                one {You and # friend read this message}
                other {You and # friends read this message}
```

### Select[​](#select "Direct link to Select")

```
{gender, select, male {He replied to your message}
                 female {She replied to your message}
                 other {They replied to your message}}
```

### Ordinals[​](#ordinals "Direct link to Ordinals")

```
{count, selectOrdinal, one {#st message}
                       two {#nd message}
                       few {#rd message}
                       other {#th message}}
```

## See Also[​](#see-also "Direct link to See Also")

* [Pluralization](/guides/plurals.md)
* [ICU Playground](https://format-message.github.io/icu-message-format-for-translators/editor.html)


---

# Monorepo

If you're using lingui within a monorepo you need:

* 1x `babel.config.js` within root
* 1x `lingui.config.js` within root
* And **n**-times `lingui.config.js` per package which extends/overrides from root


---

# Keeping Your Bundle Small: How Lingui Optimizes for Performance

When you're building a modern app with internationalization (i18n), it's easy to end up with a bloated bundle. The more languages and messages you have, the more it can grow — fast.

Lingui helps you avoid this by aggressively optimizing how translations are handled in your code and in production builds. But these optimizations can also surprise you if you're not aware of how they work.

This guide walks you through:

* How Lingui shrinks your bundle
* What tradeoffs are involved
* Why development and production behave differently
* How to avoid common pitfalls
* And how to configure Lingui to fit your workflow

## Why does this matter?[​](#why-does-this-matter "Direct link to Why does this matter?")

Imagine you have a simple message:

```
<Trans>Hello world</Trans>
```

If this message is included *as-is* in your code and translations, you might end up with:

* The message string `"Hello world"` in your source code
* The same string as a key in your translation catalog
* And again as a value in your default language catalog

That's three copies of the same thing — and you'll have that for *every* message.

Now multiply that by hundreds of messages and a few languages, and you can see where this is going.

## So how does Lingui fix that?[​](#so-how-does-lingui-fix-that "Direct link to So how does Lingui fix that?")

### 1. It replaces messages with compact IDs[​](#1-it-replaces-messages-with-compact-ids "Direct link to 1. It replaces messages with compact IDs")

When you build your app, Lingui transforms:

```
<Trans>Hello world</Trans>
```

into something like:

```
<Trans id="zfhb1" />
```

The message is no longer part of the bundle. Instead, it's replaced by a short ID. This does two things:

* Saves space (IDs are shorter than full strings)
* Prevents duplication (only the translation needs to exist, not the original text)

### 2. It removes the message compiler from production[​](#2-it-removes-the-message-compiler-from-production "Direct link to 2. It removes the message compiler from production")

Messages like this:

```
"{count, plural, one {# item} other {# items}}";
```

use [ICU MessageFormat](https://formatjs.io/docs/core-concepts/icu-syntax), which needs to be *compiled* into something the Lingui runtime can use.

Lingui includes a message compiler for this, but it's not small.

Instead of sending that to the browser, Lingui compiles messages **ahead of time** during your build when you compile your catalogs. That way, you don't need the compiler in production at all.

That's why you need to always compile your catalogs, even if they are in JSON format (not `.po` files). Compilation isn't about converting file formats — it's about transforming messages into a form the runtime can execute.

note

✅ Tip: If you use the `@lingui/vite-plugin`, `@lingui/loader` or `@lingui/metro-transformer`, you don't need to run `lingui compile` manually — these plugins compile your catalogs automatically when you import catalogs.

## But wait... why does everything still work in development?[​](#but-wait-why-does-everything-still-work-in-development "Direct link to But wait... why does everything still work in development?")

Here's the clever part: Lingui works differently in dev vs prod.

In **development**, Lingui:

* Keeps the original message (`Hello world`) in the bundle
* Includes the message compiler so new messages work immediately

This makes it fast to iterate. You can add a new `<Trans>` and see the string in the browser right away — even if you haven't extracted or compiled anything yet.

In **production**, Lingui:

* Strips out all original messages
* Removes the message compiler completely

This means you **must** extract and compile all messages ahead of time — otherwise, Lingui won't know how to render them.

## Common Problem: “Why am I seeing weird message IDs in production?”[​](#common-problem-why-am-i-seeing-weird-message-ids-in-production "Direct link to Common Problem: “Why am I seeing weird message IDs in production?”")

Let's say you add a new message:

```
<Trans>This is a new message</Trans>
```

Everything looks fine locally, but when you deploy, users see something like:

```
z3fd2
```

This usually means one thing: the message wasn't extracted before building.

When Lingui compiles your catalogs, it tries to match each message ID to a source message. If the message isn't there, there's nothing to fall back to — and the raw ID ends up in the UI.

### ✅ Solution: Always extract before building[​](#-solution-always-extract-before-building "Direct link to ✅ Solution: Always extract before building")

Make sure your build script extracts the latest messages:

```
"build": "lingui extract-template && vite build"
```

This ensures your catalogs are in sync with your source code.

## But what if I want to load translations dynamically?[​](#but-what-if-i-want-to-load-translations-dynamically "Direct link to But what if I want to load translations dynamically?")

That's where the tradeoffs come in.

Lingui's design is optimized for build-time static analysis. It's great for most apps, but it can get tricky if you want to:

* Load translations from a CMS
* Support over-the-air (OTA) delivery of catalogs
* Inject new messages at runtime

In these cases, you can't rely on precompiled catalogs alone — you'll need the **runtime message compiler** again.

To bring it back, use:

```
import { compileMessage } from "@lingui/message-utils/compileMessage";

i18n.setMessagesCompiler(compileMessage);
```

Just keep in mind that this will increase your bundle size again.

## Configuring Lingui for your needs[​](#configuring-lingui-for-your-needs "Direct link to Configuring Lingui for your needs")

Here are a few ways to customize Lingui's behavior depending on your goals:

### 1. I want production to behave like development[​](#1-i-want-production-to-behave-like-development "Direct link to 1. I want production to behave like development")

You want to keep original messages and use runtime compilation, even in production — maybe for debugging or dynamic catalogs.

**How to configure:**

```
// Macro config
stripMessageField: false;

// Runtime setup
i18n.setMessagesCompiler(compileMessage);
```

### 2. I want full consistency between dev and prod[​](#2-i-want-full-consistency-between-dev-and-prod "Direct link to 2. I want full consistency between dev and prod")

You want everything to be stripped in both environments. Useful for catching issues early.

**How to configure:**

```
// Macro config
stripMessageField: true;

// Runtime setup
i18n.setMessagesCompiler(null);
```

### 3. I want to use default Lingui behavior[​](#3-i-want-to-use-default-lingui-behavior "Direct link to 3. I want to use default Lingui behavior")

You don't change anything. Lingui automatically strips messages in production and keeps them in development.

Just make sure to always run `extract-template` before building.

## Macro Configuration: A quick note[​](#macro-configuration-a-quick-note "Direct link to Macro Configuration: A quick note")

Depending on your setup, Lingui macros can be used in different ways:

* As a standalone **Babel plugin**
* As a [**SWC plugin**](https://github.com/lingui/swc-plugin)
* Through [**babel-plugin-macros**](https://github.com/kentcdodds/babel-plugin-macros/blob/main/other/docs/user.md#config)

Each one configures slightly differently, so check their docs for details.


---

# Pluralization

Pluralization is essential for effective internationalization, allowing applications to display messages or select options based on the number. In this article, we explore various categories of pluralization, see implementation examples, and learn how to customize your application for different languages.

Lingui uses the [CLDR Plural Rules](https://www.unicode.org/cldr/charts/42/supplemental/language_plural_rules.html) to determine the correct plural form for each language.

In general, there are 6 plural forms (taken from the [CLDR Plurals](https://cldr.unicode.org/index/cldr-spec/plural-rules) page):

* zero
* one (singular)
* two (dual)
* few (paucal)
* many (also used for fractions if they have a separate class)
* other (required — general plural form — also used if the language only has a single form)

info

Only the *other* form is required, because it's the only common plural form used in all languages.

All other plural forms depend on the language. For example, English has only two forms: *one* and *other* (1 book vs. 2 books). In Czech, we have four: *one*, *few*, *many* and *other* (1 kniha, 2 knihy, 1,5 knihy, 5 knih). Some languages have even more, such as Arabic.

## Using Plural Forms[​](#using-plural-forms "Direct link to Using Plural Forms")

The good thing is that **as developers, we only need to know the plural forms of the source language**.

When we use English in the source code, we'll only use *one* and *other*:

```
plural(numBooks, {
  one: "# book",
  other: "# books",
});
```

When `numBooks == 1`, this will render as *1 book* and for `numBook == 2` it will be *2 books*. Interestingly, for `numBooks == -1`, it will be *-1 book*. This is because the "one" plural form also applies to -1. It is therefore important to remember that the plural forms (such as "one" or "two") do not represent the numbers themselves, but rather *categories* of numbers.

Under the hood, the [`plural`](/ref/macro.md#plural) macro is replaced with a low-level [`i18n._`](/ref/core.md#i18n._) call. In production, the example will look like this:

```
i18n._({
  id: "d1wX4r",
  // stripped on production
  // message: '{numBooks, plural, one {# book} other {# books}}',
  values: { numBooks },
});
```

When we extract messages from the source code using the [Lingui CLI](/ref/cli.md), we get:

```
{numBooks, plural, one {# book} other {# books}}
```

This is then translated by our Czech translator as:

```
{numBooks, plural, one {# kniha} few {# knihy} many {# knihy} other {# knih}}
```

Important

The important thing is that *we don't have to change our code to support languages with different plural rules*.

## Source Code in Language Other than English[​](#source-code-in-language-other-than-english "Direct link to Source Code in Language Other than English")

As developers, we only need to be aware of the plural forms for the source language. Check the [plural forms](https://www.unicode.org/cldr/charts/42/supplemental/language_plural_rules.html) for your language, and then you can use them accordingly. Here's an example in Czech:

```
plural(numBooks, {
  one: "# kniha",
  few: "# knihy",
  many: "# knihy",
  other: "# knih",
});
```

This makes Lingui also valuable for monolingual projects, meaning that you can benefit from it even if you don't translate your application. Pluralization, along with number and date formatting, is relevant to all languages.


---

# Pseudolocalization

Pseudo-localization is a method used to check the software's readiness to be localized. This method shows how the product's UI will look after translation. Use this feature to reduce potential rework by checking whether any source strings should be altered before the translation process begins.

It also makes it easy to identify hard-coded strings and improperly concatenated strings so that they can be localized properly.

> Example: Ţĥĩś ţēxţ ĩś ƥśēũďōĺōćàĺĩźēď

## Configuration[​](#configuration "Direct link to Configuration")

To configure pseudolocalization, add the [`pseudoLocale`](/ref/conf.md#pseudolocale) property to your Lingui configuration file:

lingui.config.{ts,js}

```
import { defineConfig } from "@lingui/cli";

export default defineConfig({
  locales: ["en", "pseudo-LOCALE"],
  pseudoLocale: "pseudo-LOCALE",
  fallbackLocales: {
    "pseudo-LOCALE": "en",
  },
});
```

The `pseudoLocale` option must be set to any string that matches a value in the [`locales`](/ref/conf.md#locales) configuration. If this is not set correctly, no folder or pseudolocalization will be created.

If the `fallbackLocales` is configured, the pseudolocalization will be generated from the translated fallback locale instead.

## Generate Pseudolocalization[​](#generate-pseudolocalization "Direct link to Generate Pseudolocalization")

After running the [`extract`](/ref/cli.md#extract) command, verify that the folder for the pseudolocale has been created.

Pseudolocalization is automatically generated during the [`compile`](/ref/cli.md#compile) process, using the messages.

## Switch Browser Into Specified Pseudolocale[​](#switch-browser-into-specified-pseudolocale "Direct link to Switch Browser Into Specified Pseudolocale")

You can switch your browser to a pseudolocale either by adjusting the browser settings or by using extensions. Extensions provide flexibility by allowing you to use any locale, while browser settings are usually limited to valid language tags (BCP 47).

In such cases, the pseudolocale must be a standard locale that isn't already used in your application. For example, you could use `zu-ZA` (Zulu - South Africa).

Chrome:

* With extension (valid locale) - [Locale Switcher](https://chrome.google.com/webstore/detail/locale-switcher/kngfjpghaokedippaapkfihdlmmlafcc).
* Without extension (valid locale) - <chrome://settings/?search=languages>.

Firefox:

* With extension (any string) - [Quick Accept-Language Switcher](https://addons.mozilla.org/en-GB/firefox/addon/quick-accept-language-switc/?src=search).
* Without extension (valid locale) - [about](about:preferences#general)
  <!-- -->
  [:preferences](about:preferences#general)
  <!-- -->
  [#general](about:preferences#general) > *Language*.


---

# Testing

In a React application, components that use [`Trans`](/ref/react.md#trans) or [`useLingui`](/ref/react.md#uselingui) need access to the context provided by [`I18nProvider`](/ref/react.md#i18nprovider). How you wrap your component with the I18nProvider depends on the testing library you're using.

Below is an example using [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/) and its [wrapper-property](https://testing-library.com/docs/react-testing-library/api#wrapper):

index.js

```
import React from "react";
import { getByText, render, act } from "@testing-library/react";
import { i18n } from "@lingui/core";
import { I18nProvider } from "@lingui/react";

import { messages } from "./locales/en/messages";
import { messages as csMessages } from "./locales/cs/messages";
import App from "./App";

i18n.load({
  en: messages,
  cs: csMessages,
});

const TestingProvider = ({ children }: any) => <I18nProvider i18n={i18n}>{children}</I18nProvider>;

test("Content should be translated correctly in English", () => {
  act(() => {
    i18n.activate("en");
  });
  const { getByTestId, container } = render(<App />, { wrapper: TestingProvider });
  expect(getByTestId("h3-title")).toBeInTheDocument();
  expect(getByText(container, "Language switcher example:")).toBeDefined();
});

test("Content should be translated correctly in Czech", () => {
  act(() => {
    i18n.activate("cs");
  });
  const { getByTestId, container } = render(<App />, { wrapper: TestingProvider });
  expect(getByTestId("h3-title")).toBeInTheDocument();
  expect(getByText(container, "Příklad přepínače jazyků:")).toBeDefined();
});
```

To avoid repeating the `TestingProvider` setup in multiple tests, consider defining a custom renderer. You can find more about this in the [react testing library - Custom Render](https://testing-library.com/docs/react-testing-library/setup#custom-render) documentation.


---

# Installation and Setup

Lingui is more than just a package; it's a comprehensive suite of tools designed to simplify internationalization. You have the flexibility to choose the specific tools that best fit your project's needs.

Learn how to install Lingui in your project, whether you use JavaScript, React (including RSC) or React Native. Lingui also supports various transpilers and build tools, such as Babel, SWC, and Vite.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

* Make sure you have [Node.js](https://nodejs.org/) installed (v20 or higher).
* Install [Lingui CLI](/ref/cli.md) to manage your translations and catalogs.

tip

Don't miss the [Lingui ESLint Plugin](/ref/eslint-plugin.md) which can help you find and prevent common i18n mistakes in your code.

## Choosing a Transpiler[​](#choosing-a-transpiler "Direct link to Choosing a Transpiler")

> A transpiler converts code within a language, transforming newer features into older equivalents for compatibility, or expanding concise syntax into more verbose implementations.

Lingui needs a transpiler to work. It's responsible for transforming Lingui's JS/JSX components into [ICU MessageFormat](/guides/message-format.md) and extracting message IDs. Both Babel and SWC transpilers are supported. Follow the Babel or SWC setup depending on what transpiler your project already uses.

* Babel
* SWC

> Babel is a JavaScript transpiler that converts modern code into backward-compatible versions and allows custom syntax transformations.

Lingui requires `@lingui/babel-plugin-lingui-macro` (recommended) or [`babel-plugin-macros`](https://github.com/kentcdodds/babel-plugin-macros) to perform the transformation.

If you are using a framework that doesn't allow you to change the Babel configuration (e.g. Create React App > 2.0), these frameworks may support `babel-plugin-macros` out of the box.

Follow these steps to set up Lingui with Babel:

1. Install the `@lingui/babel-plugin-lingui-macro` package as a development dependency:

   * npm
   * Yarn
   * pnpm

   ```
   npm install --save-dev @lingui/babel-plugin-lingui-macro
   ```

   ```
   yarn add --dev @lingui/babel-plugin-lingui-macro
   ```

   ```
   pnpm add --save-dev @lingui/babel-plugin-lingui-macro
   ```

2. Add `@lingui/babel-plugin-lingui-macro` to the top of the `plugins` section of your Babel config (e.g. `.babelrc`):

   ```
   {
     "plugins": ["@lingui/babel-plugin-lingui-macro"]
   }
   ```

tip

When using a preset, first check if it includes the `macros` plugin. If so, then you don't need to install and set up `@lingui/babel-plugin-lingui-macro`. For example, `react-scripts` already includes the `macros` plugin.

caution

If you're using [React Compiler](https://react.dev/learn/react-compiler), make sure that `@lingui/babel-plugin-lingui-macro` comes **before** the React Compiler plugin in the Babel plugins list. This ensures macros are expanded correctly before the compiler processes the code.

> SWC is an extensible Rust-based platform for the next generation of fast developer tools.

Lingui supports SWC with a dedicated plugin [`@lingui/swc-plugin`](/ref/swc-plugin.md). SWC is significantly faster than Babel and is a good choice for large projects.

Follow these steps to set up Lingui with SWC:

1. Install `@lingui/swc-plugin` as a development dependency:

   * npm
   * Yarn
   * pnpm

   ```
   npm install --save-dev @lingui/swc-plugin
   ```

   ```
   yarn add --dev @lingui/swc-plugin
   ```

   ```
   pnpm add --save-dev @lingui/swc-plugin
   ```

2. [Add necessary configurations](/ref/swc-plugin.md#usage).

caution

SWC Plugin support is still experimental. Semver backwards compatibility between different `@swc/core` versions is not guaranteed. See the [SWC compatibility](/ref/swc-plugin.md#swc-compatibility) for more information.

caution

If you're using [React Compiler](https://react.dev/learn/react-compiler) with SWC, the `@lingui/swc-plugin` must run **before** the React Compiler plugin. This is necessary because Lingui macros need to be expanded before the React Compiler processes your code.

However, in Next.js, the React Compiler is enabled via a simple boolean flag (`reactCompiler: true`) in `next.config.js`, and there's currently no way to control plugin ordering. As a result, Lingui may not work correctly with the React Compiler in SWC-based setups like Next.js.

## Basic Configuration[​](#basic-configuration "Direct link to Basic Configuration")

Lingui needs a configuration file to work. The configuration file specifies the source files, message catalogs, and other settings.

Let's create a basic configuration file in the root of your project (next to `package.json`):

lingui.config.js

```
import { defineConfig } from "@lingui/cli";

export default defineConfig({
  sourceLocale: "en",
  locales: ["cs", "en"],
  catalogs: [
    {
      path: "<rootDir>/src/locales/{locale}/messages",
      include: ["src"],
    },
  ],
});
```

The configuration above specifies the source locale as English and the target locales as Czech and English.

According to this configuration, Lingui will extract messages from source files in the `src` directory and write them to message catalogs in `src/locales` (the English catalog would be in `src/locales/en/messages.po`, for example). See [Configuration](/ref/conf.md) for a complete reference.

note

Replace `src` with the name of the directory where you have the source files.

The PO format is the default and recommended format for message catalogs. See the [Catalog Formats](/ref/catalog-formats.md) for other available formats.

## Build Tools[​](#build-tools "Direct link to Build Tools")

### Vite[​](#vite "Direct link to Vite")

> Vite is a blazing fast frontend build tool powering the next generation of web applications.

Lingui supports Vite with a dedicated plugin [`@lingui/vite-plugin`](/ref/vite-plugin.md). This plugin is responsible for extracting messages from your source code and compiling message catalogs.

There are two ways to set up Lingui with Vite by using the [`@vitejs/plugin-react`](https://www.npmjs.com/package/@vitejs/plugin-react) or [`@vitejs/plugin-react-swc`](https://www.npmjs.com/package/@vitejs/plugin-react-swc). You need to choose the one that fits your project setup.

* Babel (plugin-react)
* SWC (plugin-react-swc)

The `@vitejs/plugin-react` plugin uses Babel to transform your code. To use Lingui with Vite and Babel, follow these steps:

1. Follow the [Choosing a Transpiler](#choosing-a-transpiler) instructions.

2. Install `@lingui/vite-plugin` as a development dependency and `@lingui/react` as a runtime dependency:

   * npm
   * Yarn
   * pnpm

   ```
   npm install --save-dev @lingui/vite-plugin
   npm install --save @lingui/react
   ```

   ```
   yarn add --dev @lingui/vite-plugin
   yarn add @lingui/react
   ```

   ```
   pnpm add --save-dev @lingui/vite-plugin
   pnpm add @lingui/react
   ```

3. Setup Lingui in `vite.config.ts`:

   vite.config.ts

   ```
   import { defineConfig } from "vite";
   import react from "@vitejs/plugin-react";
   import { lingui } from "@lingui/vite-plugin";

   export default defineConfig({
     plugins: [
       react({
         babel: {
           plugins: ["@lingui/babel-plugin-lingui-macro"],
         },
       }),
       lingui(),
     ],
   });
   ```

info

The `@vitejs/plugin-react` does not use the Babel config (e.g. `babel.rc`) from your project by default. You have to enable it manually or specify Babel options directly in `vite.config.ts`.

The `@vitejs/plugin-react-swc` plugin uses SWC to transform your code, which is significantly faster than Babel. To use Lingui with Vite and SWC, follow these steps:

1. Follow the [Choosing a Transpiler](#choosing-a-transpiler) instructions.

2. Install `@lingui/vite-plugin`, `@lingui/swc-plugin` as development dependencies and `@lingui/react` as a runtime dependency:

   * npm
   * Yarn
   * pnpm

   ```
   npm install --save-dev @lingui/vite-plugin @lingui/swc-plugin
   npm install --save @lingui/react
   ```

   ```
   yarn add --dev @lingui/vite-plugin @lingui/swc-plugin
   yarn add @lingui/react
   ```

   ```
   pnpm add --save-dev @lingui/vite-plugin @lingui/swc-plugin
   pnpm add @lingui/react
   ```

3. Setup Lingui in `vite.config.ts`:

   vite.config.ts

   ```
   import { defineConfig } from "vite";
   import react from "@vitejs/plugin-react-swc";
   import { lingui } from "@lingui/vite-plugin";

   export default defineConfig({
     plugins: [
       react({
         plugins: [["@lingui/swc-plugin", {}]],
       }),
       lingui(),
     ],
   });
   ```

## See Also[​](#see-also "Direct link to See Also")

* [React i18n Tutorial](/tutorials/react.md)
* [React Server Components Tutorial](/tutorials/react-rsc.md)
* [React Native i18n Tutorial](/tutorials/react-native.md)
* [JavaScript i18n Tutorial](/tutorials/javascript.md)


---

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


---

# Catalog Formats

Catalog format (configured by the [`format`](/ref/conf.md#format) option) refers to the offline catalog file format. This format is never used in production, because the catalog is compiled into a JS module.

The reason for this build step is that the choice of catalog format depends on the individual internationalization workflow. On the other hand, the runtime catalog should be as simple as possible so that it can be parsed quickly without additional overhead.

## PO[​](#po "Direct link to PO")

PO files are translation files used by [gettext](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html) internationalization system. This is the **recommended** and the **default** catalog format in Lingui.

[![Version](https://img.shields.io/npm/v/@lingui/format-po.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-po) [![Downloads](https://img.shields.io/npm/dw/@lingui/format-po.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-po)

The advantages of this format are:

* readable even for large messages
* supports comments for translators
* supports metadata (origin, flags)
* supports contexts
* standard format supported by many localization tools

### Installation[​](#po-installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/format-po
```

```
yarn add --dev @lingui/format-po
```

```
pnpm add --save-dev @lingui/format-po
```

### Usage[​](#po-usage "Direct link to Usage")

lingui.config.{js,ts}

```
import { defineConfig } from "@lingui/cli";
import { formatter } from "@lingui/format-po";

export default defineConfig({
  // [...]
  format: formatter({ lineNumbers: false }),
});
```

### Configuration[​](#po-configuration "Direct link to Configuration")

PO formatter accepts the following options:

| Option                        | Type                            | Default | Description                                                                                                                                                                            |
| ----------------------------- | ------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `origins`                     | boolean                         | `true`  | Include comments in the PO file that indicate where each message is used in the source code. This provides additional context during the translation                                   |
| `lineNumbers`                 | boolean                         | `true`  | Include line numbers in the origin comments. This makes it easier to locate messages in the source code                                                                                |
| `printLinguiId`               | boolean                         | `false` | Add a `js-lingui-id: hash` comment to each message in the PO file. This ID is a hash generated by Lingui                                                                               |
| `explicitIdAsDefault`         | boolean                         | `false` | Use the `msgid` as is for messages with explicit IDs. The formatter will add the `js-lingui-explicit-id` flag for such strings                                                         |
| `customHeaderAttributes`      | `{[key: string]: string}`       | `{}`    | Allows adding custom key-value pairs to the PO file header                                                                                                                             |
| `printPlaceholdersInComments` | boolean \| `{ limit?: number }` | `true`  | Print values for unnamed placeholders as comments for each message. This can give translators more context for better translations. By default, the first 3 placeholders are displayed |

### Examples[​](#po-examples "Direct link to Examples")

```
#: src/App.js:3
#. Comment for translators
msgid "messageId"
msgstr "Translated Message"

#: src/App.js:3
#, obsolete
msgid "obsoleteId"
msgstr "Obsolete Message"
```

Messages with context are exported in the following way:

```
#: src/Inbox.js:12
msgctxt "my context"
msgid "msg.inbox"
msgstr "Message Inbox"
```

Messages with plurals are exported in [ICU MessageFormat](/guides/message-format.md):

```
msgid "{count, plural, one {Message} other {Messages}}"
msgstr "{count, plural, one {Message} other {Messages}}"
```

Messages with placeholders:

```
t`Hello ${user.name} ${value}`;
```

are exported as:

```
#. placeholder {0}: user.name
msgid "Hello {0} {value}"
msgstr "Hello {0} {value}"
```

## PO with gettext Plurals[​](#po-gettext "Direct link to PO with gettext Plurals")

When using localization backends that don't understand the ICU plural syntax exported by the default `po` formatter, **po-gettext** can be used to read and write to PO files using gettext-native plurals.

[![Version](https://img.shields.io/npm/v/@lingui/format-po-gettext.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-po-gettext) [![Downloads](https://img.shields.io/npm/dw/@lingui/format-po-gettext.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-po-gettext)

### Installation[​](#po-gettext-installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/format-po-gettext
```

```
yarn add --dev @lingui/format-po-gettext
```

```
pnpm add --save-dev @lingui/format-po-gettext
```

### Usage[​](#po-gettext-usage "Direct link to Usage")

lingui.config.{js,ts}

```
import { defineConfig } from "@lingui/cli";
import { formatter } from "@lingui/format-po-gettext";

export default defineConfig({
  // [...]
  format: formatter({ lineNumbers: false }),
});
```

### Configuration[​](#po-gettext-configuration "Direct link to Configuration")

The PO Gettext formatter accepts the following options:

| Option                 | Type    | Default        | Description                                                                                                                                                              |
| ---------------------- | ------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `origins`              | boolean | `true`         | Include comments in the PO file that indicate where each message is used in the source code. This provides additional context during the translation                     |
| `lineNumbers`          | boolean | `true`         | Include line numbers in the origin comments. This makes it easier to locate messages in the source code                                                                  |
| `disableSelectWarning` | boolean | `false`        | Disable warnings about unsupported `Select` features encountered in catalogs. This can be useful if you're aware of the limitation and want to suppress related warnings |
| `customICUPrefix`      | string  | `"js-lingui:"` | Override the default prefix for ICU and plural comments in the final PO catalog                                                                                          |

### Examples[​](#po-gettext-examples "Direct link to Examples")

With this format, plural messages are exported in the following ways, depending on whether an explicit ID is set:

* Message **with custom ID "my\_message"** that is pluralized on property "*someCount*".

  ```
  #. js-lingui:pluralize_on=someCount
  msgid "my_message"
  msgid_plural "my_message_plural"
  msgstr[0] "Singular case"
  msgstr[1] "Case number {someCount}"
  ```

  Note that `msgid_plural` was created by appending a `_plural` suffix.

* Message **without custom ID** that is pluralized on property "*anotherCount*".

  To allow matching this PO item to the appropriate catalog entry when deserializing, the original ICU message is also stored in the generated comment.

  ```
  #. js-lingui:icu=%7BanotherCount%2C+plural%2C+one+%7BSingular+case%7D+other+%7BCase+number+%7BanotherCount%7D%7D%7D&pluralize_on=anotherCount
  msgid "Singular case"
  msgid_plural "Case number {anotherCount}"
  msgstr[0] "Singular case"
  msgstr[1] "Case number {anotherCount}"
  ```

  Note how `msgid` and `msgid_plural` were extracted from the original message.

* Message **with a custom comment prefix**.

  Some TMS might modify the ICU comment by attempting to split lines to be 80 characters or less, or have trouble reading lingui comments because of the `js-lingui:` prefix. To change the prefix, set `customICUPrefix` to modify the prefix for ICU comments.

  ```
  # with default prefix
  #. js-
  #. lingui:icu=%7BanotherCount%2C+plural%2C+one+%7BSingular+case%7D+other+%7BCase+number+%7BanotherCount%7D%7D%7D&pluralize_on=anotherCount

  # customICUPrefix = jsi18n:
  #. jsi18n:icu=%7BanotherCount%2C+plural%2C+one+%7BSingular+case%7D+other+%7BCase+number+%7BanotherCount%7D%7D%7D&pluralize_on=anotherCount
  ```

### Limitations[​](#po-gettext-limitations "Direct link to Limitations")

This format comes with several caveats and should only be used when using ICU plurals in PO files is not an option:

* Nested/multiple plurals in a message as shown in [`plural`](/ref/macro.md#plural) are not supported because they cannot be expressed with gettext plurals. Messages containing nested/multiple formats will not be output correctly.
* The [`select`](/ref/macro.md#select) and [`selectOrdinal`](/ref/macro.md#selectordinal) cannot be expressed with gettext plurals, but the original ICU format is still stored in the `msgid`/`msgstr` properties. To disable the warning that this may not be the expected behavior, add `{ disableSelectWarning: true }` to the [`format`](/ref/conf.md#format) options.
* Source/development languages with more than two plurals could experience difficulties when no custom IDs are used, as gettext cannot have more than two plurals cases identifying an item (`msgid` and `msgid_plural`).
* Gettext doesn't support plurals for negative and fractional numbers even though some languages have special rules for these cases.

## JSON[​](#json "Direct link to JSON")

This format is used to store messages in a JSON file. There are two types of JSON format: [minimal](#minimal-style) and [lingui](#lingui-style).

[![Version](https://img.shields.io/npm/v/@lingui/format-json.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-json) [![Downloads](https://img.shields.io/npm/dw/@lingui/format-json.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-json)

### Installation[​](#json-installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/format-json
```

```
yarn add --dev @lingui/format-json
```

```
pnpm add --save-dev @lingui/format-json
```

### Usage[​](#json-usage "Direct link to Usage")

lingui.config.{js,ts}

```
import { defineConfig } from "@lingui/cli";
import { formatter } from "@lingui/format-json";

export default defineConfig({
  // [...]
  format: formatter({ style: "lingui" }),
});
```

### Configuration[​](#json-configuration "Direct link to Configuration")

JSON formatter accepts the following options:

| Option        | Type                      | Default    | Description                                                                                                                                       |
| ------------- | ------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `style`       | `"lingui"` \| `"minimal"` | `"lingui"` | Specify the output style of the JSON file. `lingui` includes full Lingui-specific metadata, while `minimal` may output a more compact format      |
| `origins`     | boolean                   | `true`     | Include information in the JSON file about where each message is used in the source code. This provides additional context during the translation |
| `lineNumbers` | boolean                   | `true`     | Include line numbers in the origin comments. This makes it easier to locate messages in the source code                                           |
| `indentation` | number                    | `2`        | Set the number of spaces to use for indentation in the output JSON file. This affects the readability of the file when opened in a text editor    |

### Examples[​](#json-examples "Direct link to Examples")

#### Minimal style[​](#minimal-style "Direct link to Minimal style")

A simple JSON file where each key is a message ID and the value is the translation. The JSON is flat, and there's no reason to use nested keys. The usual motivation behind nested JSON is to save file space, but this file format is only used offline.

The downside of this format is that all metadata about the message is lost. This includes the default message, the origin of the message, and any message flags (obsolete, fuzzy, etc.).

```
{
  "messageId": "translation"
}
```

#### Lingui style[​](#lingui-style "Direct link to Lingui style")

This file format simply outputs all internal data in JSON format. It's the original file format used by Lingui before support for other catalog formats was added. It might be useful for tools build on top of Lingui CLI which needs to further process catalog data.

```
{
  "messageId": {
    "translation": "Translated message",
    "message": "Default message",
    "description": "Comment for translators",
    "origin": [["src/App.js", 3]]
  },
  "obsoleteId": {
    "translation": "Obsolete message",
    "origin": [["src/App.js", 3]],
    "obsolete": true
  }
}
```

## CSV[​](#csv "Direct link to CSV")

The CSV format is a simple format that can be used to import and export messages from spreadsheets or other tools that support CSV files. It has two columns: message ID and message (source or translation).

[![Version](https://img.shields.io/npm/v/@lingui/format-csv.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-csv) [![Downloads](https://img.shields.io/npm/dw/@lingui/format-csv.svg?cacheSeconds=86400)](https://www.npmjs.com/package/@lingui/format-csv)

### Installation[​](#csv-installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/format-csv
```

```
yarn add --dev @lingui/format-csv
```

```
pnpm add --save-dev @lingui/format-csv
```

### Usage[​](#csv-usage "Direct link to Usage")

lingui.config.{js,ts}

```
import { defineConfig } from "@lingui/cli";
import { formatter } from "@lingui/format-csv";

export default defineConfig({
  // [...]
  format: formatter(),
});
```

This formatter has no configurable options.

### Examples[​](#csv-examples "Direct link to Examples")

```
messageId,Message
msg.common,String for translation
```

## See Also[​](#see-also "Direct link to See Also")

* [Custom Formatter](/guides/custom-formatter.md)


---

# Lingui CLI

The `@lingui/cli` tool provides the `lingui` command which allows you to extract messages from source files into message catalogs and compile these catalogs for production use.

## Installation[​](#installation "Direct link to Installation")

1. Install `@lingui/cli` as a development dependency:

   * npm
   * Yarn
   * pnpm

   ```
   npm install --save-dev @lingui/cli
   ```

   ```
   yarn add --dev @lingui/cli
   ```

   ```
   pnpm add --save-dev @lingui/cli
   ```

2. Add the following scripts to your `package.json`:

   package.json

   ```
   {
     "scripts": {
       "extract": "lingui extract",
       "compile": "lingui compile"
     }
   }
   ```

tip

If you use TypeScript, you can add the `--typescript` flag to the `compile` script to produce compiled message catalogs with TypeScript types:

package.json

```
{
  "scripts": {
    "compile": "lingui compile --typescript"
  }
}
```

## Global Options[​](#global-options "Direct link to Global Options")

### `--config <config>`[​](#--config-config "Direct link to --config-config")

Path to the configuration file. If not set, the default file is loaded as described in the [Configuration](/ref/conf.md) reference.

## Commands[​](#commands "Direct link to Commands")

### `extract`[​](#extract "Direct link to extract")

```
lingui extract [files...]
        [--clean]
        [--overwrite]
        [--format <format>]
        [--locale <locale, [...]>]
        [--convert-from <format>]
        [--verbose]
        [--watch [--debounce <delay>]]
        [--workers]
```

The `extract` command scans source files to locate and extract messages, generating separate message catalogs for each language.

This process involves:

1. Extracting messages from files based on the `include` and `exclude` settings in the [`catalogs`](/ref/conf.md#catalogs) section of the configuration file.
2. Merging the newly extracted messages with any existing message catalogs.
3. Updating and saving the message catalogs.
4. Printing extraction statistics for each language, including the total number of messages and any missing translations.

tip

Refer to the [Message Extraction](/guides/message-extraction.md) guide to learn more about this process and the options available.

#### `files`[​](#extract-files "Direct link to extract-files")

Filter source paths to extract messages only from specific files. For example:

```
lingui extract src/components
```

This command extracts messages from files within the `src/components/**/*` path. You can also pass multiple paths for extraction.

This feature is useful when you want to extract messages from files that are staged for commit. For example, you can use husky to automatically extract messages from staged files before committing:

package.json

```
{
  "husky": {
    "hooks": {
      "pre-commit": "lingui extract $(git diff --name-only --staged)"
    }
  }
}
```

#### `--clean`[​](#extract-clean "Direct link to extract-clean")

By default, the extract command merges messages extracted from source files with existing message catalogs, ensuring that translated messages are preserved and not accidentally lost.

However, over time, some messages may be removed from the source code. You can use the following option to clean up your message catalogs and remove obsolete messages.

#### `--overwrite`[​](#extract-overwrite "Direct link to extract-overwrite")

Update translations for [`sourceLocale`](/ref/conf.md#sourcelocale) from source.

#### `--format <format>`[​](#extract-format "Direct link to extract-format")

Extract message catalogs to the specified file format (see the [`format`](/ref/conf.md#format) option for more details).

#### `--locale <locale, [...]>`[​](#extract-locale "Direct link to extract-locale")

Extract data for the specified locales only.

#### `--convert-from <format>`[​](#extract-convert-from "Direct link to extract-convert-from")

Convert message catalogs from the previous format (see the [`format`](/ref/conf.md#format) option for more details).

#### `--verbose`[​](#extract-verbose "Direct link to extract-verbose")

Print additional information.

#### `--watch`[​](#extract-watch "Direct link to extract-watch")

Enable watch mode to monitor changes in files located in the paths specified in the configuration file or in the command itself. Note that this feature is intended for development use only, as it does not remove obsolete translations.

#### `--debounce <delay>`[​](#extract-debounce "Direct link to extract-debounce")

Delay the extraction by `<delay>` milliseconds, bundling multiple file changes together.

#### `--workers`[​](#extract-workers "Direct link to extract-workers")

Specifies the number of worker threads to use.

Pass `--workers 1` to disable workers and run everything in a single process.

By default, the tool uses a simple heuristic:

* On machines with more than 2 cores → `cpu.count - 1` workers
* On 2-core machines → all cores

Use the `--verbose` flag to see the actual pool size.

Worker threads can significantly improve performance on large projects. However, on small projects they may provide little benefit or even be slightly slower due to thread startup overhead.

A larger worker pool also increases memory usage. Adjust this value for your project to achieve the best performance.

### `extract-template`[​](#extract-template "Direct link to extract-template")

```
lingui extract-template [--verbose]
```

This command extracts messages from your source files and generates a `.pot` template file. Any artifacts created by this command can be safely ignored in version control.

If your message catalogs are not synchronized with the source and some messages are missing, the application will fallback to the template file. Running this command before building the application is recommended to ensure all messages are accounted for.

#### `--verbose`[​](#extract-template-verbose "Direct link to extract-template-verbose")

Print additional information.

### `compile`[​](#compile "Direct link to compile")

```
lingui compile
    [--strict]
    [--format <format>]
    [--verbose]
    [--typescript]
    [--namespace <namespace>]
    [--watch [--debounce <delay>]]
    [--workers]
```

Once you have all the catalogs ready and translated, you can use this command to compile all the catalogs into minified JS/TS files. It compiles message catalogs located in the [`path`](/ref/conf.md#catalogs) directory and generates minified JavaScript files. The resulting file is a string that is parsed into a plain JS object using `JSON.parse`.

The output looks like this:

```
export const messages = JSON.parse(`{
// object with keys (translation ids) and values (translations)
}`);
```

Messages added to the compiled file are collected in a specific order:

1. Translated messages from the specified locale.
2. Translated messages from the fallback locale for the specified locale.
3. Translated message from default fallback locale.
4. Message key.

It is also possible to merge the translated catalogs into a single file per locale by specifying [`catalogsMergePath`](/ref/conf.md#catalogsmergepath) in the configuration.

tip

The compiled files can be safely ignored by your version control system, since these files must be created each time you deploy to production. We recommend you to create the compiled catalogs in CI as part of your deployment process. Always remember to **use compiled catalogs** in deployments.

.gitignore

```
your_locale_folder/**/*.js
```

#### `--overwrite`[​](#compile-overwrite "Direct link to compile-overwrite")

Overwrite source locale translations from source.

#### `--strict`[​](#compile-strict "Direct link to compile-strict")

Fail if a catalog has missing translations.

#### `--format <format>`[​](#compile-format "Direct link to compile-format")

Format of message catalogs (see the [`format`](/ref/conf.md#format) option for more details).

#### `--verbose`[​](#compile-verbose "Direct link to compile-verbose")

Print additional information.

#### `--namespace`[​](#compile-namespace "Direct link to compile-namespace")

Specify the namespace for compiled message catalogs (see also [`compileNamespace`](/ref/conf.md#compilenamespace) for global configuration).

#### `--typescript`[​](#compile-typescript "Direct link to compile-typescript")

Is the same as using [`compileNamespace`](/ref/conf.md#compilenamespace) with the value "ts". Generates a `{compiledFile}.ts` file and the exported object is typed using TS.

#### `--watch`[​](#compile-watch "Direct link to compile-watch")

Watch mode. Watches only for changes in locale files in your defined locale catalogs. For example, `locales\en\messages.po`.

#### `--debounce <delay>`[​](#compile-debounce "Direct link to compile-debounce")

Delays compilation by `<delay>` milliseconds to avoid multiple compilations for subsequent file changes.

#### `--workers`[​](#compile-workers "Direct link to compile-workers")

Specifies the number of worker threads to use. Pass `--workers 1` to disable workers and run everything in a single process.

By default, the tool uses a simple heuristic:

* On machines with more than 2 cores → `cpu.count - 1` workers
* On 2-core machines → all cores

Use the `--verbose` flag to see the actual pool size.

Worker threads can significantly improve performance on large projects. However, on small projects they may provide little benefit or even be slightly slower due to thread startup overhead.

A larger worker pool also increases memory usage. Adjust this value for your project to achieve the best performance.

## Configuring the Source Locale[​](#configuring-the-source-locale "Direct link to Configuring the Source Locale")

One limitation of checking for missing translations is that the English message catalog typically does not require translations since our source code is in English. This issue can be resolved by configuring the [`sourceLocale`](/ref/conf.md#sourcelocale) in the configuration file.

## Compiling Catalogs in CI[​](#compiling-catalogs-in-ci "Direct link to Compiling Catalogs in CI")

If you're using CI, it's a good idea to add the `compile` command to your build process. Alternatively, you can also use a [Webpack loader](/ref/loader.md), [Vite plugin](/ref/vite-plugin.md) or [Metro transformer](/ref/metro-transformer.md).

Depending on your localization setup, you might also want to run the `extract` command in CI and upload the extracted messages to a [translation service](/tools/introduction.md).

## See Also[​](#see-also "Direct link to See Also")

* [Lingui Configuration](/ref/conf.md)
* [Message Extraction](/guides/message-extraction.md)
* [Catalog Formats](/ref/catalog-formats.md)
* [Custom Extractor](/guides/custom-extractor.md)


---

# Configuration

The following reference covers all supported configuration options in Lingui. To learn more about configuring Lingui, read the [Installation and Setup](/installation.md) guide.

By default, Lingui looks for the configuration in the following locations:

* `lingui.config.js` or `lingui.config.ts` file exporting a configuration object (recommended).
* `.linguirc` file in JSON format.
* `lingui` section in `package.json`.

You can also define the environment variable `LINGUI_CONFIG` with the path to your config file.

In the case of TypeScript-based config you can use ESM format and *export default*.

## catalogs[​](#catalogs "Direct link to catalogs")

Default value:

```
[
  {
    path: "<rootDir>/locale/{locale}/messages",
    include: ["<rootDir>"],
    exclude: ["**/node_modules/**"],
  },
];
```

The `catalogs` configuration defines the location of message catalogs and specifies which files are included when the [`extract`](/ref/cli.md#extract) command scans for messages.

* `path`: the directory where the message catalogs are located. It should not end with a slash and must not include a file extension, which depends on the [`format`](#format) configuration. The `{locale}` token will be replaced by the catalog's locale.
* `include` and `exclude`: these patterns specify which files to include or exclude during the extraction process. They are passed to [minimatch](https://github.com/isaacs/minimatch) for pattern matching.
* [`<rootDir>`](#rootdir): represents the root directory of the project. It is replaced with the actual root directory when the configuration is loaded. By default, [`<rootDir>`](#rootdir) represents the configuration file's location.

The `path`, `include`, and `exclude` patterns are interpreted relative to the current process CWD (current working directory).

The `{name}` token in the `path` will be replaced with the catalog name. Be sure to include the `{name}` pattern in the source path as well, as it acts like a `*` glob pattern:

```
{
  "catalogs": [
    {
      "path": "<rootDir>/components/{name}/locale/{locale}",
      "include": ["<rootDir>/components/{name}/"]
    }
  ]
}
```

#### Examples[​](#examples "Direct link to Examples")

Let's assume we use `locales: ["en", "cs"]` and `format: "po"` in all examples.

#### All catalogs in one directory[​](#all-catalogs-in-one-directory "Direct link to All catalogs in one directory")

```
{
  "catalogs": [
    {
      "path": "locales/{locale}"
    }
  ]
}
```

```
locales/
├── en.po
└── cs.po
```

#### Catalogs in separate directories[​](#catalogs-in-separate-directories "Direct link to Catalogs in separate directories")

```
{
  catalogs: [
    {
      path: "locales/{locale}/messages",
    },
  ];
}
```

```
locales
├── en/
│   └── messages.po
└── cs/
    └── messages.po
```

#### Separate catalogs per component, placed inside component directory[​](#separate-catalogs-per-component-placed-inside-component-directory "Direct link to Separate catalogs per component, placed inside component directory")

```
{
  "catalogs": [
    {
      "path": "components/{name}/locale/{locale}",
      "include": ["components/{name}/"]
    }
  ]
}
```

```
components/
├── RegistrationForm/
│   ├── locale/
│   │  ├── en.po
│   │  └── cs.po
│   ├── RegistrationForm.test.js
│   └── RegistrationForm.js
└── LoginForm/
    ├── locale/
    │  ├── en.po
    │  └── cs.po
    ├── LoginForm.test.js
    └── LoginForm.js
```

#### Separate catalogs per component, placed inside shared directory[​](#separate-catalogs-per-component-placed-inside-shared-directory "Direct link to Separate catalogs per component, placed inside shared directory")

```
{
  "catalogs": [
    {
      "path": "locale/{locale}/{name}",
      "include": ["components/{name}/"]
    }
  ]
}
```

```
.
├── locale/
│   ├── en/
│   │   ├── RegistrationForm.po
│   │   └── LoginForm.po
│   └── cs/
│       ├── RegistrationForm.po
│       └── LoginForm.po
└── components/
    ├── RegistrationForm/
    │   ├── RegistrationForm.test.js
    │   └── RegistrationForm.js
    └── LoginForm/
        ├── LoginForm.test.js
        └── LoginForm.js
```

## locales[​](#locales "Direct link to locales")

Default value: `[]`

The locale tags used in the project. The [`extract`](/ref/cli.md#extract) and [`compile`](/ref/cli.md#compile) commands write a catalog for each locale specified. Each locale should be a valid [BCP-47 code](http://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html):

```
{
  "locales": ["en", "cs"]
}
```

## fallbackLocales[​](#fallbacklocales "Direct link to fallbackLocales")

Default value: `{}`

Translations from `fallbackLocales` are used if the translation for the given locale is missing. It uses [CLDR Parent Locales](https://github.com/unicode-cldr/cldr-core/blob/master/supplemental/parentLocales.json) by default, unless you override it with a `false` to use the default message or message ID instead:

```
{
  "fallbackLocales": false
}
```

The `fallbackLocales` object allows to configure fallback locales for each locale instance:

```
{
  "fallbackLocales": {
    "en-US": ["en-GB", "en"],
    "es-MX": "es"
  }
}
```

In this example, if any translation isn't found on `en-US`, then it will search on `en-GB`, after that if not found we'll search in `en`.

it's also possible to configure a `default` fallback locale for all locales:

```
{
  "fallbackLocales": {
    "en-US": ["en-GB", "en"],
    "es-MX": "es",
    "default": "en"
  }
}
```

## sourceLocale[​](#sourcelocale "Direct link to sourceLocale")

Default value: `""`

`sourceLocale` specifies the default language of message IDs in your source files. The catalog for `sourceLocale` doesn't need actual translations since message IDs are used as-is by default. However, you can still override any message ID by providing a custom translation.

The main difference between `sourceLocale` and [`fallbackLocales`](#fallbacklocales) is their purpose: `sourceLocale` defines the language used for message IDs, while `fallbackLocales` provides alternative translations when specific messages are missing for a particular locale.

## pseudoLocale[​](#pseudolocale "Direct link to pseudoLocale")

Default value: `""`

Locale used for pseudolocalization. For example, when you set `pseudoLocale: "en"`, all messages in the `en` catalog will be pseudo-localized. The locale must be included in the `locales` config.

Read more about [Pseudolocalization](/guides/pseudolocalization.md).

## catalogsMergePath[​](#catalogsmergepath "Direct link to catalogsMergePath")

Default value: `""`

Define the path where translated catalogs are merged into a single file per locale during the [`compile`](/ref/cli.md#compile) process.

#### Example[​](#example "Direct link to Example")

Let's assume we have [separate catalogs per component, placed inside shared directory](#separate-catalogs-per-component-placed-inside-shared-directory).

Using the `catalogsMergePath`, separate catalogs can be merged into a single file:

```
{
  "catalogs": [
    {
      "path": "/locale/{locale}/{name}",
      "include": ["components/{name}/"]
    }
  ],
+ "catalogsMergePath": "locales/{locale}"
}
```

```
.
  ├── locale/
  │   ├── en/
  │   │   ├── RegistrationForm.po
- │   │   ├── RegistrationForm.js
  │   │   ├── LoginForm.po
- │   │   └── LoginForm.js
  │   └── cs/
  │       ├── RegistrationForm.po
- │       ├── RegistrationForm.js
  │       ├── LoginForm.po
- │       └── LoginForm.js
+ ├── locales/
+ │   ├── en.js
+ │   └── cs.js
  └── components/
      ├── RegistrationForm/
      │   ├── RegistrationForm.test.js
      │   └── RegistrationForm.js
      └── LoginForm/
          ├── LoginForm.test.js
          └── LoginForm.js
```

## compileNamespace[​](#compilenamespace "Direct link to compileNamespace")

Default value: `cjs`

Specify namespace for exporting compiled messages. See [`compile`](/ref/cli.md#compile) command.

#### cjs[​](#cjs "Direct link to cjs")

Use CommonJS exports:

```
/* eslint-disable */module.exports={messages: {"..."}}
```

#### es[​](#es "Direct link to es")

Use ES6 named export:

```
/* eslint-disable */export const messages = {"..."}
```

#### ts[​](#ts "Direct link to ts")

Use ES6 named export + `.ts` file with an additional `{compiledFile}.d.ts` file:

```
/* eslint-disable */export const messages = {"..."}
```

```
import { Messages } from '@lingui/core';
declare const messages: Messages;
export { messages };
```

#### json[​](#json "Direct link to json")

```
{"messages": {"..."}}
```

#### (window|global).(.\*)[​](#windowglobal "Direct link to (window|global).(.*)")

Assign compiled messages to `window` or `global` object. Specify an identifier after `window` or `global` to which the catalog is assigned, e.g. `window.i18n`.

For example, setting [`compileNamespace`](#compilenamespace) to `window.i18n` creates file similar to this:

```
/* eslint-disable */window.i18n={messages: {"..."}}
```

## extractorParserOptions[​](#extractorparseroptions "Direct link to extractorParserOptions")

Default value: `{}`

Specify additional options used to parse source files when extracting messages.

```
{
  "extractorParserOptions": {
    "tsExperimentalDecorators": false,
    "flow": false
  }
}
```

#### tsExperimentalDecorators[​](#tsexperimentaldecorators "Direct link to tsExperimentalDecorators")

Default value: `false`

By default, standard decorators (Stage3) are applied to TS files. Enable this if you want to use TypeScript's experimental decorators.

#### flow[​](#flow "Direct link to flow")

Default value: `false`

Lingui does not ship with [Flow](https://flow.org/) typing. However, you can use Lingui in projects written in Flow. Enable this option to tell the extractor that your sources use Flow syntax.

## compilerBabelOptions[​](#compilerbabeloptions "Direct link to compilerBabelOptions")

Default value:

```
{
  "minified": true,
  "jsescOption": {
    "minimal": true
  }
}
```

Specify extra babel options used to generate files when messages are being compiled. We use internally `@babel/generator` that accepts some configuration for generating code with/out ASCII characters. These are all the options available: [jsesc](https://github.com/mathiasbynens/jsesc).

```
{
  "compilerBabelOptions": {
    "jsescOption": {
      "minimal": false
    }
  }
}
```

This example configuration will compile with escaped ASCII characters ([jsesc#minimal](https://github.com/mathiasbynens/jsesc#minimal)).

## format[​](#format "Direct link to format")

Default value: `po`

Message catalog format. The `po` formatter is used by default. Other formatters are available as separate packages.

lingui.config.{js,ts}

```
import { defineConfig } from "@lingui/cli";
import { formatter } from "@lingui/format-po";

export default defineConfig({
  // [...]
  format: formatter({ lineNumbers: false }),
});
```

Read more about available formatters in [Catalog Formats](/ref/catalog-formats.md) or create your own [Custom Formatter](/guides/custom-formatter.md).

## orderBy[​](#orderby "Direct link to orderBy")

Default value: `message`

Order of messages in catalog:

#### message[​](#message "Direct link to message")

Sort by source message.

#### messageId[​](#messageid "Direct link to messageId")

Sort by the message ID, `js-lingui-id` will be used if no custom id provided.

#### origin[​](#origin "Direct link to origin")

Sort by message origin (e.g. `App.js:3`)

## rootDir[​](#rootdir "Direct link to rootDir")

Default: The root of the directory containing your Lingui configuration file or the `package.json`.

This is the directory where the Lingui CLI scans for messages in your source files during the extraction process.

Note that using `<rootDir>` as a string token in any other path-based config settings will refer back to this value.

## runtimeConfigModule[​](#runtimeconfigmodule "Direct link to runtimeConfigModule")

Default value: `["@lingui/core", "i18n"]`

This setting specifies the module path for the exported `i18n` object. The first value in the array is the module path, and the second is the name of the import. This configuration is essential for [macros](/ref/macro.md) that need to reference the global `i18n` object.

You only need to set this value if you use custom object created using [`setupI18n`](/ref/core.md#setupi18n):

For example, if you have a custom module that exports the `i18n` object:

```
import { i18n } from "./custom-i18n-config";
```

```
{
  "runtimeConfigModule": ["./custom-i18n-config", "i18n"]
}
```

You may use a different named export:

```
import { myI18n } from "./custom-i18n-config";
```

```
{
  "runtimeConfigModule": ["./custom-i18n-config", "myI18n"]
}
```

In more advanced scenarios, you may need to change the module from which the [`Trans`](/ref/macro.md#trans) or [`useLingui`](/ref/macro.md#uselingui) macros are imported:

```
import { Trans, useLingui } from "./custom-config";
```

```
{
  "runtimeConfigModule": {
    "Trans": ["./custom-config", "Trans"],
    "useLingui": ["./custom-config", "useLingui"]
  }
}
```

## extractors[​](#extractors "Direct link to extractors")

Default value: `[babel]`

Extractors it's the way to customize which extractor you want for your codebase.

```
{
   "extractors": [
      myCustomExtractor,
   ]
}
```

See the [Custom Extractor](/guides/custom-extractor.md) guide for instructions on creating your own extractor.

## macro.corePackage[​](#macrocorepackage "Direct link to macro.corePackage")

Default value: `["@lingui/macro", "@lingui/core/macro"]`

Allows customizing the Core Macro package name that the Lingui macro detects.

```
// lingui.config
{
  macro: {
    corePackage: ["@lingui/myMacro"];
  }
}

// app.tsx
import { msg } from "@lingui/myMacro";

msg`Hello`; // <-- would be correctly picked up by macro
```

This setting mostly useful for external framework integrations.

## macro.jsxPackage[​](#macrojsxpackage "Direct link to macro.jsxPackage")

Default value: `["@lingui/macro", "@lingui/react/macro"]`

Allows customizing the JSX Macro package name that the Lingui macro detects.

```
// lingui.config
{
  macro: {
    jsxPackage: ["@lingui/myMacro"];
  }
}

// app.tsx
import { Trans } from "@lingui/myMacro";

<Trans>Hello</Trans>; // <-- would be correctly picked up by macro
```

This setting mostly useful for external framework integrations.


---

# Core API Reference

The `@lingui/core` package provides the main i18n object which manages message catalogs, active locale as well as translation and formatting of messages.

## Installation[​](#installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save @lingui/core
```

```
yarn add @lingui/core
```

```
pnpm add @lingui/core
```

## Overview[​](#overview "Direct link to Overview")

The `@lingui/core` package provides a global instance of the `i18n` object, which you can import and use directly:

```
import { i18n } from "@lingui/core";

/**
 * Load messages for the requested locale and activate it.
 * This function isn't part of the Lingui because there are
 * many ways how to load messages — from REST API, from file, from cache, etc.
 */
async function activate(locale: string) {
  const { messages } = await import(`${locale}/messages.js`);
  i18n.loadAndActivate({ locale, messages });
}

activate("cs");

// returns the Czech translation of "Hello World"
const translation = i18n._("Hello World");
```

Advanced

If you prefer not to use the global `i18n` instance and want to set up your own, you can utilize the [`setupI18n`](#setupi18n) method. Additionally, you'll need to configure the [`runtimeConfigModule`](/ref/conf.md#runtimeconfigmodule) to ensure that macros work properly.

## Class `i18n()`[​](#i18n "Direct link to i18n")

### `i18n.loadAndActivate(options)`[​](#i18n.loadAndActivate "Direct link to i18n.loadAndActivate")

The `options` parameter is an object with the following properties:

* `locale`: The initial active locale.
* `locales`: A list of alternative locales ([BCP-47](http://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html) language tags) used for number and date formatting.
* `messages`: The **compiled** message catalog.

It allows to set (overwrite) the catalog for a given locale and activate the locale:

```
import { i18n } from "@lingui/core";

const { messages } = await import(`${locale}/messages.js`);
i18n.loadAndActivate({ locale, messages });
```

### `i18n.load(allMessages: AllMessages)`[​](#i18n.load\(allMessages\) "Direct link to i18n.load(allMessages)")

### `i18n.load(locale: string, messages: Messages)`[​](#i18n.load "Direct link to i18n.load")

Load messages for given locale or load multiple message catalogs at once.

When some messages for the provided locale are already loaded, calling `i18n.load` will merge the new messages with the existing ones using `Object.assign`.

```
import { i18n } from "@lingui/core";

/**
 * This is just an example of what the catalog looks like internally.
 * Formatting of string messages only works in development. See note below.
 */
const messagesEn = {
  Hello: "Hello",
  "Good bye": "Good bye",
  "My name is {name}": "My name is {name}",
};

const messagesCs = {
  Hello: "Ahoj",
  "Good bye": "Nashledanou",
  "My name is {name}": "Jmenuji se {name}",
};

i18n.load({
  en: messagesEn,
  cs: messagesCs,
});

// This is the same as loading message catalogs separately per language:
// i18n.load('en', messagesEn)
// i18n.load('cs', messagesCs)
```

tip

Don't write catalogs manually. The code above is an example of message catalogs. In real applications, messages are loaded from external message catalogs generated by the [`compile`](/ref/cli.md#compile) command or by using tools such as [Vite Plugin](/ref/vite-plugin.md), [Webpack Loader](/ref/loader.md), or [Metro Transformer](/ref/metro-transformer.md).

Formatting of messages as strings (e.g: `"My name is {name}"`) works in development only, when messages are parsed on the fly. In production, however, messages must be compiled using the [`compile`](/ref/cli.md#compile) command.

Here's how the same example would look in a real application:

```
import { i18n } from "@lingui/core";

// File generated by `lingui compile`
import { messages as messagesEn } from "./locale/en/messages.js";

i18n.load("en", messagesEn);
```

### `i18n.setMessagesCompiler(compiler)`[​](#i18n.setMessagesCompiler "Direct link to i18n.setMessagesCompiler")

Registers a `MessageCompiler` to enable the use of uncompiled catalogs at runtime.

In production builds, the `MessageCompiler` is typically excluded to reduce bundle size.

By default, message catalogs should be precompiled during the build process. However, if you need to compile catalogs at runtime, you can use this method to set a message compiler.

Example usage:

```
import { compileMessage } from "@lingui/message-utils/compileMessage";

i18n.setMessagesCompiler(compileMessage);
```

### `i18n.activate(locale[, locales])`[​](#i18n.activate "Direct link to i18n.activate")

Activate the specified locale and any alternate locales. After calling this method, calling `i18n._` will return messages in the activated locale.

```
import { i18n } from "@lingui/core";

i18n.activate("en");
i18n._("Hello"); // Return "Hello" in English

i18n.activate("cs");
i18n._("Hello"); // Return "Hello" in Czech
```

### `i18n._(messageId[, values[, options]])`[​](#i18n._ "Direct link to i18n._")

The core method for translating and formatting messages.

* `messageId`: a unique message ID which identifies message in catalog.
* `values`: an object containing variables used in translated message.
* `options.message`: the default translation (optional). This is mostly used when application doesn't use message IDs in natural language (e.g.: `msg.id` or `Component.title`).
* `options.formats`: custom format definitions for dates and times (optional). An object where keys are format names and values are either `Intl.DateTimeFormatOptions` or `Intl.NumberFormatOptions`.

```
import { i18n } from "@lingui/core";

// Simple message
i18n._("Hello");

// Message with variables
i18n._("My name is {name}", { name: "Tom" });

// Message with custom messageId
i18n._("msg.id", { name: "Tom" }, { message: "My name is {name}" });

const date = new Date("2014-12-06");
const time = new Date("2014-12-06T17:40:00Z");

// Short date format
i18n._("It starts on {someDate, date, short}", { someDate: date });

// Short time format
i18n._("It starts on {someTime, time, short}", { someTime: time });

// Date skeleton format
i18n._("It starts on {someDate, date, ::GrMMMdd}", { someDate: date });

// Custom date format
i18n._("It starts on {someDate, date, myStyle}", { someDate: date }, { formats: { myStyle: { day: "numeric" } } });
```

### `i18n._(messageDescriptor)`[​](#i18n_messagedescriptor "Direct link to i18n_messagedescriptor")

`messageDescriptor` is an object with a message ID, default message and other parameters. It's useful when you need to use the declared message later in the code.

```
import { i18n } from "@lingui/core";

// Simple message
i18n._({ id: "Hello" });

// Simple message using custom ID
i18n._({ id: "msg.hello", message: "Hello" });

// Message with variable
i18n._({ id: "My name is {name}", values: { name: "Tom" } });

// Message with comment, custom ID and variable
i18n._({
  id: "msg.name",
  message: "My name is {name}",
  comment: "Message showing the passed in name",
  values: { name: "Tom" },
});
```

Read more about [Message Descriptor](/ref/macro.md#core-macros).

### `i18n.t(...)`[​](#i18n.t "Direct link to i18n.t")

Alias for [`i18n._`](#i18n._).

```
import { i18n } from "@lingui/core";

i18n.t({ id: "Hello" });
```

### `i18n.date(value: string | Date | number[, format: Intl.DateTimeFormatOptions])`[​](#i18n.date "Direct link to i18n.date")

Format a date using the conventional format for the active language.

* `value`: the date to be formatted, as accepted by [`Intl.DateTimeFormat.prototype.format`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/format#parameters). When `value` is a string, a `Date` object is created using `new Date(date)`.
* `format`: an optional object that is passed to the `options` argument of the [`Intl.DateTimeFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat/DateTimeFormat) constructor. This allows for customization of the date formatting.

```
import { i18n } from "@lingui/core";

const d = new Date("2021-07-23T16:23:00");

i18n.activate("en");
i18n.date(d);
// Returns "7/23/2021"

i18n.date(d, { timeStyle: "medium" });
// Returns "4:23:00 PM"

i18n.date(d, { dateStyle: "medium", timeStyle: "medium" });
// Returns "Jul 23, 2021, 4:23:00 PM"

i18n.activate("cs");
i18n.date(d);
// Returns "23. 7. 2021"
```

### `i18n.number(value: number | bigint | Intl.StringNumericLiteral[, format: Intl.NumberFormatOptions])`[​](#i18n.number "Direct link to i18n.number")

Format a number using the conventional format for the active language.

* `value`: the number to be formatted, as accepted by [`Intl.NumberFormat.prototype.format`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/format#parameters).
* `format`: an optional object that is passed to the `options` argument of the [`Intl.NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat/NumberFormat) constructor. This allows for customization of the date formatting.

```
import { i18n } from "@lingui/core";

i18n.activate("en");
i18n.number(12345.678);
// Returns "12,345.678"

i18n.number(12345.678, { style: "currency", currency: "USD" });
// Returns "$12,345.68"

i18n.activate("cs");
i18n.number(12345.678);
// Returns "12 345,678"

i18n.number(12345.678, { style: "currency", currency: "CZK" });
// Returns "12 345,68 Kč"
```

## `setupI18n([options])`[​](#setupi18n "Direct link to setupi18n")

Initialize and return a new `I18n` instance. Typically, you should call this function only once and then use the returned `i18n` object throughout your entire codebase.

info

You typically don't need to set up your own `i18n` instance. In most cases, you can use the global `i18n` object exported from `@lingui/core` directly.

However, if you need to do this, make sure to also configure the [`runtimeConfigModule`](/ref/conf.md#runtimeconfigmodule) to ensure macros work properly.

```
import { setupI18n } from "@lingui/core";

const i18n = setupI18n();
```

The factory function accepts an optional `options` parameter, which can be used to configure the initial state of the `i18n` instance.

### `options.locale`[​](#optionslocale "Direct link to optionslocale")

Initial active locale.

```
import { setupI18n } from "@lingui/core";

const i18n = setupI18n({ locale: "en" });

// This is a shortcut for:
// const i18n = setupI18n()
// i18n.activate("en")
```

### `options.locales`[​](#optionslocales "Direct link to optionslocales")

List of alternative locales ([BCP-47](http://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html) language tags) which are used for number and date formatting (some countries use more than one number/date format). If not set, the active locale is used instead.

```
import { setupI18n } from "@lingui/core";

const i18n = setupI18n({
  locale: "ar",
  locales: ["en-UK", "ar-AS"],
});

// This is a shortcut for:
// const i18n = setupI18n()
// i18n.activate("ar", ["en-UK", "ar-AS"])
```

### `options.messages`[​](#optionsmessages "Direct link to optionsmessages")

Initial [`Messages`](#messages).

```
import { setupI18n } from "@lingui/core";

const messages = {
  en: require("./locale/en/messages").messages, // your path to compiled messages here
  cs: require("./locale/cs/messages").messages, // your path to compiled messages here
};
const i18n = setupI18n({ messages });

// This is a shortcut for:
// const i18n = setupI18n()
// i18n.load(messages)
```

### `options.missing`[​](#optionsmissing "Direct link to optionsmissing")

A custom message to be returned when a translation is missing. This feature is useful for debugging:

```
import { setupI18n } from "@lingui/core";

const i18n = setupI18n({ missing: "🚨" });
i18n._("missing translation") === "🚨"; // Returns the custom missing message
```

Alternatively, `missing` can be a function that receives the active locale and message ID as arguments:

```
import { setupI18n } from "@lingui/core";

function missing(locale, id) {
  alert(`Translation in ${locale} for ${id} is missing!`);
  return id;
}

const i18n = setupI18n({ missing });
i18n._("missing translation"); // Triggers an alert
```

## AllMessages[​](#allmessages "Direct link to AllMessages")

The `AllMessages` parameter in the [`I18n.load`](#i18n.load) method is of the following type:

```
type AllMessages = { [locale: string]: CompiledMessage };

// Example
const messages: AllMessages = {
  en: {
    messages: {
      Hello: "Hello",
      "Good bye": "Good bye",
    },
  },
  cs: {
    messages: {
      Hello: "Ahoj",
      "Good bye": "Nashledanou",
    },
  },
};
```

## Messages[​](#messages "Direct link to Messages")

Type of messages in [`AllMessages`](#allmessages). It's a mapping of a message ID to a translation in given language. This may be a function if messages are compiled.

```
type Messages = { [messageId: string]: string | Function };

// Example
const messagesEn: Messages = {
  Hello: "Hello",
  "Good bye": "Good bye",
};
```

## Events[​](#events "Direct link to Events")

### `change`[​](#change "Direct link to change")

The `change` event is triggered **after** changing the locale or loading a new message catalog. No arguments are passed to this event.

### `missing`[​](#missing "Direct link to missing")

The `missing` event is triggered when a translation is requested using [`i18n._`](/ref/core.md#i18n._) that does not exist in the messages of the active locale.The event provides information about the locale and the missing message ID.

```
i18n.on("missing", (event) => {
  alert(`Translation in ${event.locale} for ${event.id} is missing!`);
});
```


---

# ESLint Plugin

Lingui provides an ESLint plugin to help you find common Lingui usage errors in your code.

[![npm-version](https://img.shields.io/npm/v/eslint-plugin-lingui?logo=npm\&cacheSeconds=1800)](https://www.npmjs.com/package/eslint-plugin-lingui) [![npm-downloads](https://img.shields.io/npm/dt/eslint-plugin-lingui?cacheSeconds=500)](https://www.npmjs.com/package/eslint-plugin-lingui)

## Installation[​](#installation "Direct link to Installation")

Install [ESLint](http://eslint.org):

* npm
* Yarn
* pnpm

```
npm install --save-dev eslint
```

```
yarn add --dev eslint
```

```
pnpm add --save-dev eslint
```

Next, install `eslint-plugin-lingui`:

* npm
* Yarn
* pnpm

```
npm install --save-dev eslint-plugin-lingui
```

```
yarn add --dev eslint-plugin-lingui
```

```
pnpm add --save-dev eslint-plugin-lingui
```

info

If you have installed ESLint globally (using the `-g` flag), you must also install `eslint-plugin-lingui` globally.

## Usage[​](#usage "Direct link to Usage")

### Flat Config (`eslint.config.js`)[​](#flat-config "Direct link to flat-config")

Version 8 of ESLint introduced a new configuration format called [Flat Config](https://eslint.org/docs/latest/use/configure/configuration-files). Flat config files represent plugins and parsers as JavaScript objects.

#### Recommended Setup[​](#recommended-setup "Direct link to Recommended Setup")

To enable all the recommended rules for the plugin, add the following config:

```
import pluginLingui from "eslint-plugin-lingui";

export default [
  pluginLingui.configs["flat/recommended"],
  // Any other config...
];
```

#### Custom Setup[​](#custom-setup "Direct link to Custom Setup")

Alternatively, you can load the plugin and configure only the rules you want to use:

```
import pluginLingui from "eslint-plugin-lingui";

export default [
  {
    plugins: {
      lingui: pluginLingui,
    },
    rules: {
      "lingui/t-call-in-function": "error",
    },
  },
  // Any other config...
];
```

### Legacy Config (`.eslintrc`)[​](#legacy-eslintrc "Direct link to legacy-eslintrc")

The legacy configuration format has been deprecated by ESLint, but it's still supported. If you're using the legacy format, you can use the following configuration.

#### Recommended Setup[​](#recommended-setup-1 "Direct link to Recommended Setup")

To enable all the recommended rules for the plugin, add `plugin:lingui/recommended` to the `extends` section:

```
{
  "extends": ["plugin:lingui/recommended"]
}
```

#### Custom Setup[​](#custom-setup-1 "Direct link to Custom Setup")

Alternatively, add `lingui` to the `plugins` section of your `.eslintrc` configuration file. You can omit the `eslint-plugin-` prefix:

```
{
  "plugins": ["lingui"]
}
```

In the rules section, configure the rules you want to use:

```
{
  "rules": {
    "lingui/no-unlocalized-strings": 2,
    "lingui/t-call-in-function": 2,
    "lingui/no-single-variables-to-translate": 2,
    "lingui/no-expression-in-message": 2,
    "lingui/no-single-tag-to-translate": 2,
    "lingui/no-trans-inside-trans": 2
  }
}
```

tip

See the [official repository](https://github.com/lingui/eslint-plugin) for more information about the rules.


---

# Vue.js Extractor

The `@lingui/extractor-vue` package provides a custom extractor that handles Vue.js files.

## Installation[​](#installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/extractor-vue
```

```
yarn add --dev @lingui/extractor-vue
```

```
pnpm add --save-dev @lingui/extractor-vue
```

## Usage[​](#usage "Direct link to Usage")

It is required that you use JavaScript or TypeScript for your Lingui configuration.

lingui.config.{js,ts}

```
import { defineConfig } from "@lingui/cli";
import { vueExtractor } from "@lingui/extractor-vue";
import babel from "@lingui/cli/api/extractors/babel";

export default defineConfig({
  locales: ["en", "nb"],
  sourceLocale: "en",
  catalogs: [
    {
      path: "<rootDir>/src/{locale}",
      include: ["<rootDir>/src"],
    },
  ],
  extractors: [babel, vueExtractor],
});
```

## See Also[​](#see-also "Direct link to See Also")

* [Message Extraction](/guides/message-extraction.md)
* [Custom Extractor](/guides/custom-extractor.md)


---

# Webpack Loader

The `@lingui/loader` is a Webpack loader for Lingui message catalogs. It offers an alternative to the [`lingui compile`](/ref/cli.md#compile) and compiles catalogs on the fly.

It enables you to `import` `.po` files directly, instead of running `lingui compile` and `import`ing the resulting JavaScript (or TypeScript) files.

## Installation[​](#installation "Direct link to Installation")

Install `@lingui/loader` as a development dependency:

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/loader
```

```
yarn add --dev @lingui/loader
```

```
pnpm add --save-dev @lingui/loader
```

## Usage[​](#usage "Direct link to Usage")

Simply prepend `@lingui/loader!` in front of path to message catalog you want to import.

Here's an example of dynamic import:

```
export async function dynamicActivate(locale: string) {
  const { messages } = await import(`@lingui/loader!./locales/${locale}/messages.po`);
  i18n.load(locale, messages);
  i18n.activate(locale);
}
```

Remember that the file extension is mandatory.

note

Catalogs with the `.json` extension are treated differently by Webpack. They load as ES module with default export, so your import should look like this:

```
const { messages } = (await import(`@lingui/loader!./locales/${locale}/messages.json`)).default;
```

## See Also[​](#see-also "Direct link to See Also")

* [Dynamic Loading of Message Catalogs](/guides/dynamic-loading-catalogs.md)
* [Catalog Formats](/ref/catalog-formats.md)


---

# Locale Detection

The `@lingui/detect-locale` is a lightweight package *(only \~1 kB Gzip)* providing several methods and helpers to determine the user's locale using different detection strategies.

Most of the detectors accept custom document, location or window objects as parameters, which is especially useful for testing purposes or when implementing server-side detection strategies.

## Installation[​](#installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save @lingui/detect-locale
```

```
yarn add @lingui/detect-locale
```

```
pnpm add @lingui/detect-locale
```

## Reference[​](#reference "Direct link to Reference")

### `detect`[​](#detect "Direct link to detect")

The `detect` method accepts multiple detectors as arguments and returns the first valid locale detected.

### `multipleDetect`[​](#multipledetect "Direct link to multipledetect")

The `multipleDetect` method also accepts multiple detectors as arguments and returns an array with all locales detected by each detector.

### `fromCookie(key: string)`[​](#fromCookie "Direct link to fromCookie")

Accepts a key as a parameter and retrieves the locale value from the browser's cookies based on that key.

### `fromHtmlTag(tag: string)`[​](#fromHtmlTag "Direct link to fromHtmlTag")

Looks for the specified attribute in the HTML document (commonly `lang` or `xml:lang`) to detect the locale.

### `fromNavigator()`[​](#fromNavigator "Direct link to fromNavigator")

Retrieves the user's language setting from the browser, compatible with older browsers such as IE11.

### `fromPath(localePathIndex: number)`[​](#fromPath "Direct link to fromPath")

Splits `location.pathname` into an array, requiring you to specify the index where the locale is located.

### `fromStorage(key: string, { useSessionStorage: boolean })`[​](#fromStorage "Direct link to fromStorage")

Searches for the item with the specified key in `localStorage` by default. If the `useSessionStorage` parameter is passed, it will search in `sessionStorage`.

### `fromSubdomain(localeSubdomainIndex: number)`[​](#fromSubdomain "Direct link to fromSubdomain")

Splits `location.href` by subdomain segments, requiring the index where the locale is specified.

### `fromUrl(parameter: string)`[​](#fromUrl "Direct link to fromUrl")

Uses a query string parser to find the locale by the specified parameter in the URL.

## Usage Examples[​](#usage-examples "Direct link to Usage Examples")

### Usage with `detect`[​](#usage-with-detect "Direct link to usage-with-detect")

```
import { detect, fromUrl, fromStorage, fromNavigator } from "@lingui/detect-locale";

// can be a function with custom logic or just a string, `detect` method will handle it
const DEFAULT_FALLBACK = () => "en";

const result = detect(fromUrl("lang"), fromStorage("lang"), fromNavigator(), DEFAULT_FALLBACK);

console.log(result); // "en"
```

### Usage with `multipleDetect`[​](#usage-with-multipledetect "Direct link to usage-with-multipledetect")

```
import { multipleDetect, fromUrl, fromStorage, fromNavigator } from "@lingui/detect-locale";

// can be a function with custom logic or just a string, `detect` method will handle it
const DEFAULT_FALLBACK = () => "en";

const result = multipleDetect(fromUrl("lang"), fromStorage("lang"), fromNavigator(), DEFAULT_FALLBACK);

console.log(result); // ["en", "es"]
```


---

# Macros

Lingui Macro provides powerful macros to transform JavaScript objects and JSX elements into [ICU MessageFormat](/guides/message-format.md) messages at compile time. It provides a more efficient and developer-friendly way to handle internationalization in your project.

The benefits of using macros:

* You don't have to learn ICU MessageFormat syntax. You always use familiar JS and JSX code.
* Components and functions are type checked.
* Short IDs are generated for your messages.
* Additional validation of plural rules is performed during transformation.
* Non-essential data is removed from the production build (e.g. comments and default messages) to save a few bytes.

There are two types of macros: [Core Macros](#core-macros) (JS) and [React Macros](#react-macros) (JSX).

## Core Macros[​](#core-macros "Direct link to Core Macros")

Core (JS) Macros can be used in any JavaScript context (e.g. outside JSX). All JS macros are transformed into a *Message Descriptor* wrapped inside of [`i18n._`](/ref/core.md#i18n._) call:

```
import { t } from "@lingui/core/macro";
t`Attachment ${name} saved`;

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
i18n._(
  /*i18n*/ {
    id: "nwR43V",
    message: "Attachment {name} saved",
    values: { name },
  }
);
```

`/*i18n*/` comment

In the example above you may notice the `/*i18n*/` comment in the macro output. This comment tells the extract plugin that the following object should be collected into the message catalog.

*Message Descriptor* is an object with a message ID, default message and other parameters:

```
type MessageDescriptor = {
  id: string;
  message?: string;
  values?: Record<string, any>;
  comment?: string;
};
```

The `id` is the message ID and is the only parameter required. The `id` and `message` are extracted into the message catalog. Only `id` and `values` are used at runtime, all other attributes are removed from the production code for size optimization.

You don't need to specify the ID manually. By default, Macro will automatically create a short ID from your message. However, you can explicitly specify a custom ID. Read more about [Explicit vs Generated IDs](/guides/explicit-vs-generated-ids.md).

### `t`[​](#t "Direct link to t")

The most common macro for messages. It transforms tagged template literal into message in ICU MessageFormat:

```
import { t } from "@lingui/core/macro";
const message = t`Hello World`;

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "mY42CM",
    message: "Hello World",
  }
);
```

Message variables are supported:

```
import { t } from "@lingui/core/macro";
const message = t`My name is ${name}`;

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "mVmaLu",
    message: "My name is {name}",
    values: { name },
  }
);
```

In fact, any expression can be used inside template literal. However, only simple variables are referenced by name in a transformed message. All other expressions are referenced by their numeric index:

```
import { t } from "@lingui/core/macro";
const message = t`Today is ${new Date()}`;

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";

const message = i18n._(
  /*i18n*/ {
    id: "2aJT27",
    message: "Today is {0}",
    values: { 0: new Date() },
  }
);
```

info

By default the `i18n` object is imported from [`@lingui/core`](/ref/core.md). If you are using a custom instance of the `i18n` object, you need to set [`runtimeConfigModule`](/ref/conf.md#runtimeconfigmodule) or pass a custom instance to [`t`](/ref/macro.md#t).

It's also possible to pass custom `id` and `comment` for translators by calling `t` macro with a message descriptor:

```
import { t } from "@lingui/core/macro";
const message = t({
  id: "msg.hello",
  comment: "Greetings at the homepage",
  message: `Hello ${name}`,
});

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "msg.hello",
    comment: "Greetings at the homepage",
    message: "Hello {name}",
    values: { name },
  }
);
```

In this case, `message` is used as the default message, and it's transformed as if it were wrapped in a `t` macro. `message` also accepts any other macros:

```
import { t } from "@lingui/core/macro";
const message = t({
  id: "msg.plural",
  message: plural(value, { one: "...", other: "..." }),
});

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "msg.plural",
    message: "{value, plural, one {...} other {...}}",
    values: { value },
  }
);
```

### `plural`[​](#plural "Direct link to plural")

Pluralization is a common problem in i18n. Different languages have different rules for plural form (e.g. English has only `one` and `other`, while Czech has `one`, `few`, `many` and `other`). The `plural` macro is used to handle this.

```
plural(value: string | number, options: Object)
```

The `value` specifies the plural form or cardinal number. The second argument, `options`, is an object with available plural forms:

```
import { plural } from "@lingui/core/macro";
const message = plural(count, {
  one: "# Book",
  other: "# Books",
});

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "V/M0Vc",
    message: "{count, plural, one {# Book} other {# Books}}",
    values: { count },
  }
);
```

tip

Choose the plural forms used in your source code based on the pluralization rules of your source locale.

If you need to add variables in plural form, you can use template string literals. This time you don't need the [`t`](/ref/macro.md#t) macro, because template strings are transformed automatically:

```
import { plural } from "@lingui/core/macro";
const message = plural(count, {
  one: `${name} has # friend`,
  other: `${name} has # friends`,
});

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "CvuUwE",
    message: "{count, plural, one {{name} has # friend} other {{name} has # friends}}",
    values: { count, name },
  }
);
```

Plurals can also be nested to form complex messages. Here's an example using two counters:

```
import { plural } from "@lingui/core/macro";
const message = plural(numBooks, {
  one: plural(numArticles, {
    one: `1 book and 1 article`,
    other: `1 book and ${numArticles} articles`,
  }),
  other: plural(numArticles, {
    one: `${numBooks} books and 1 article`,
    other: `${numBooks} books and ${numArticles} articles`,
  }),
});

// ↓ ↓ ↓ ↓ ↓ ↓
// Generated message was wrapped for better readability

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "XnUh4j",
    message: `{numBooks, plural,
         one {{numArticles, plural,
            one {1 book and 1 article}
            other {1 book and {numArticles} articles}
         }}
         other {{numArticles, plural,
            one {{numBooks} books and 1 article}
            other {{numBooks} books and {numArticles} articles}
         }}
      }`,
    values: { numBooks, numArticles },
  }
);
```

This is just one example of how macros can be combined to create a complex message. However, simple is better, because in the end it's the translator who has to translate these long and complex strings.

tip

Use `plural` inside [`t`](#t) or [`defineMessage`](#definemessage) macro if you want to add custom `id`, `context` or `comment` for translators.

```
const message = t({
  id: "my.custom.id",
  comment: "My Comment",
  message: plural(count, {
    one: "# Book",
    other: "# Books",
  }),
});
```

### `selectOrdinal`[​](#selectordinal "Direct link to selectordinal")

SelectOrdinal is a variation of the [`plural`](#plural) macro. It's used to handle ordinal numbers (e.g. 1st, 2nd, 3rd, 4th, etc.).

```
selectOrdinal(value: string | number, options: Object)
```

The `value` specifies the ordinal number. The second argument, `options`, is an object with available ordinal forms:

```
import { selectOrdinal } from "@lingui/core/macro";
const message = selectOrdinal(count, {
  one: "#st",
  two: "#nd",
  few: "#rd",
  other: "#th",
});

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";
const message = i18n._(
  /*i18n*/ {
    id: "V8xI3w",
    message: "{count, selectOrdinal, one {#st} two {#nd} few {#rd} other {#th}}",
    values: { count },
  }
);
```

tip

Use `selectOrdinal` inside [`t`](#t) or [`defineMessage`](#definemessage) macro if you want to add custom `id`, `context` or `comment` for translators.

```
const message = t({
  id: "my.custom.id",
  comment: "My Comment",
  message: selectOrdinal(count, {
    one: "#st",
    two: "#nd",
    few: "#rd",
    other: "#th",
  }),
});
```

### `select`[​](#select "Direct link to select")

The `select` macro is used to handle different forms of a message based on a value.

```
select(value: string | number, options: Object)
```

It works like a switch statement - it selects one of the forms provided in the `options` object based on the `value`:

```
import { select } from "@lingui/core/macro";
const message = select(gender, {
  male: "he",
  female: "she",
  other: "they",
});

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";

const message = i18n._(
  /*i18n*/ {
    id: "VRptzI",
    message: "{gender, select, male {he} female {she} other {they}}",
    values: { gender },
  }
);
```

tip

Use `select` inside [`t`](#t) or [`defineMessage`](#definemessage) macro if you want to add custom `id`, `context` or `comment` for translators.

```
const message = t({
  id: "my.custom.id",
  comment: "My Comment",
  message: select(gender, {
    male: "he",
    female: "she",
    other: "they",
  }),
});
```

### `defineMessage` / `msg`[​](#definemessage "Direct link to definemessage")

The `defineMessage` (alias: `msg`) macro allows to define a message for later use. It has the same signature as `t` and returns a `MessageDescriptor` that you can pass to `i18n._` to get a translated string at any time later. This is useful for [Lazy Translations](/guides/lazy-translations.md).

In other words, `t` returns a translated string at the time when it's called, while `msg` returns a `MessageDescriptor` that can produce translated strings later:

```
import { i18n } from "@lingui/core";
import { defineMessage } from "@lingui/core/macro";

// define message
const message = defineMessage`Hello World`;

// use it later
i18n._(message);

// ↓ ↓ ↓ ↓ ↓ ↓

import { i18n } from "@lingui/core";

const message = /*i18n*/ {
  id: "mY42CM",
  message: "Hello World",
};

// use it later
i18n._(message);
```

You can also use a shorter alias of the `defineMessage` macro:

```
import { msg } from "@lingui/core/macro";
const message = msg`Hello World`;

// ↓ ↓ ↓ ↓ ↓ ↓

const message = /*i18n*/ {
  id: "mY42CM",
  message: "Hello World",
};
```

The `defineMessage` macro also supports a `MacroMessageDescriptor` object as input. This can be used to provide additional information for the message such as comment or context:

```
type MacroMessageDescriptor = {
  id?: string;
  message?: string;
  comment?: string;
  context?: string;
};
```

Either the `id` or `message` property is required. `id` is a custom message ID. If it isn't set, the `message` (and `context` if present) will be used to generate an ID. Read more about [Explicit vs Generated IDs](/guides/explicit-vs-generated-ids.md).

```
import { defineMessage } from "@lingui/core/macro";
const message = defineMessage({
  id: "Navigation / About",
  message: "About us",
});

// ↓ ↓ ↓ ↓ ↓ ↓

const message = /*i18n*/ {
  id: "Navigation / About",
  message: "About us",
};
```

The `message` is a default message. Any JS macro can be used here. Template string literals don't need to be tagged with [`t`](#t).

```
import { defineMessage } from "@lingui/core/macro";
const name = "Joe";
const message = defineMessage({
  message: `Welcome, ${name}!`,
});

// ↓ ↓ ↓ ↓ ↓ ↓

const message = /*i18n*/ {
  id: "dgJjNB",
  message: "Welcome, {name}",
  values: {
    name,
  },
};
```

The `comment` is a comment for translators. It's extracted into the message catalog, and it gives translators additional information about the message. It's removed from the production code:

```
import { defineMessage } from "@lingui/core/macro";
const message = defineMessage({
  comment: "Link in navigation pointing to About page",
  message: "About us",
});

// ↓ ↓ ↓ ↓ ↓ ↓

const message = /*i18n*/ {
  id: "+mNwru",
  comment: "Link in navigation pointing to About page",
  message: "About us",
};
```

Note

In the production build, the macro is stripped of `message`, `comment` and `context` properties:

```
import { defineMessage } from "@lingui/core/macro";
const message = defineMessage({
  id: "msg.navigation.about",
  comment: "Link in navigation pointing to About page",
  message: "About us",
  context: "Context about the link",
});

// process.env.NODE_ENV === "production"
// ↓ ↓ ↓ ↓ ↓ ↓

const message = /*i18n*/ {
  id: "msg.navigation.about",
};
```

`message` and `comment` are used in message catalogs only. `context` is used only for generating ID and is stripped from the output.

## React Macros[​](#react-macros "Direct link to React Macros")

React (JSX) Macros are used in JSX elements and are transformed into the [`Trans`](/ref/react.md#trans) component imported from the [`@lingui/react`](/ref/react.md) package.

### `Trans`[​](#trans "Direct link to trans")

The `Trans` macro is used to translate static messages, messages with variables and messages with inline markup:

```
import { Trans } from "@lingui/react/macro";
<Trans>Refresh inbox</Trans>;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";
<Trans id="EsCV2T" message="Refresh inbox" />;
```

Available Props:

| Prop Name | Type   | Description                                            |
| --------- | ------ | ------------------------------------------------------ |
| `id`      | string | Custom message ID                                      |
| `comment` | string | Comment for translators                                |
| `context` | string | Allows to extract the same messages with different IDs |
| `render`  | func   | Custom render callback to render translation           |

#### `id`[​](#id "Direct link to id")

Each message in the catalog is identified by a message ID. While macro uses message (and `context` property if provided) to generate the ID, it's possible to provide custom ID. Read more about [Explicit vs Generated IDs](/guides/explicit-vs-generated-ids.md).

```
import { Trans } from "@lingui/react/macro";
<Trans id="message.attachment_saved">Attachment {name} saved.</Trans>;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";
<Trans id="message.attachment_saved" message="Attachment {name} saved." />;
```

#### `comment`[​](#comment "Direct link to comment")

Comment for translators to give them additional information about the message. It will be visible in the [TMS](/tools/introduction.md) if it is supported, and in the [catalog format](/ref/catalog-formats.md). It will be removed from production code.

#### `context`[​](#context "Direct link to context")

Allows to extract the same messages with different IDs. It is useful when the same message has different meanings in different contexts. See [Context](/guides/explicit-vs-generated-ids.md#context) for more details.

Similarly to [`comment`](#comment), it will be added to the message catalog, visible in TMS and will be removed from the production code:

```
import { Trans } from "@lingui/react/macro";
<Trans context="direction">right</Trans>;
<Trans context="correctness">right</Trans>;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";
<Trans id={"d1wX4r"} message="right" />;
<Trans id={"16eaSK"} message="right" />;
```

This macro is particularly useful if the message contains inline markup:

```
import { Trans } from "@lingui/react/macro";

<Trans>
  Read the <a href="/docs">docs</a>.
</Trans>;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";
<Trans id={"mk8bSG"} message="Read the <0>docs</0>." components={{ 0: <a href="/docs" /> }} />;
```

Components and HTML tags are replaced by dummy indexed tags (`<0></0>`) which has several advantages:

* Both custom React components and built-in HTML tags are supported.
* Changing component props doesn't break translation.
* The message is extracted as a whole sentence (this seems to be obvious, but most i18n libs simply split the message into pieces by tags and translate them separately).

#### `render`[​](#render "Direct link to render")

Custom render callback to render translation. This prop is passed directly to the [`Trans`](/ref/react.md#trans) component from the [`@lingui/react`](/ref/react.md) package.

### `Plural`[​](#plural-1 "Direct link to plural-1")

The `Plural` JSX macro is used to handle plural forms. It's similar to the [`plural`](#plural) core macro, but is used in JSX elements.

```
import { Plural } from "@lingui/react/macro";
<Plural value={numBooks} one="Book" other="Books" />;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";
<Trans id={"is7n96"} message="{numBooks, plural, one {Book} other {Books}}" values={{ numBooks }} />;
```

Available Props:

| Prop name   | Type           | Description                                                                                                                                             |
| ----------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `other`     | string         | *(required)* general *plural* form                                                                                                                      |
| `value`     | number         | *(required)* Value is mapped to plural form below                                                                                                       |
| `format`    | string\|Object | Number format passed as options to [`Intl.NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NumberFormat) |
| `offset`    | number         | Offset of value when calculating plural forms                                                                                                           |
| `zero`      | string         | Form for empty `value`                                                                                                                                  |
| `one`       | string         | *Singular* form                                                                                                                                         |
| `two`       | string         | *Dual* form                                                                                                                                             |
| `few`       | string         | *Paucal* form                                                                                                                                           |
| `many`      | string         | *Plural* form                                                                                                                                           |
| `_<number>` | string         | Exact match form, corresponds to `=N` rule                                                                                                              |
| `id`        | string         | Custom message ID                                                                                                                                       |
| `comment`   | string         | Comment for translators                                                                                                                                 |
| `context`   | string         | Allows to extract the same messages with different IDs                                                                                                  |
| `render`    | func           | Custom render callback to render translation                                                                                                            |

Exact matches in MessageFormat syntax are expressed as `=int` (e.g. `=0`), but in React this isn't a valid prop name. Therefore, exact matches are expressed as `_int` prop (e.g. `_0`). This is commonly used in combination with `offset` prop. `offset` affects only plural forms, not exact matches.

```
import { Plural } from "@lingui/react/macro";

<Plural
  value={count}
  offset={1}
  // when value == 0
  _0="Nobody arrived"
  // when value == 1
  _1="Only you arrived"
  // when value == 2
  // value - offset = 1 -> `one` plural form
  one="You and # other guest arrived"
  // when value >= 3
  other="You and # other guests arrived"
/>;

/*
  This is transformed to Trans component with ID:
  {count, plural, offset:1 _0    {Nobody arrived}
                           _1    {Only you arrived}
                           one   {You and # other guest arrived}
                           other {You and # other guests arrived}}
*/
```

### `SelectOrdinal`[​](#selectordinal-1 "Direct link to selectordinal-1")

The `SelectOrdinal` JSX macro is used to handle ordinal numbers. It's similar to the [`selectOrdinal`](#selectordinal) core macro, but is used in JSX elements.

```
import { SelectOrdinal } from "@lingui/react/macro";

// count == 1 -> 1st
// count == 2 -> 2nd
// count == 3 -> 3rd
// count == 4 -> 4th
<SelectOrdinal value={count} one="#st" two="#nd" few="#rd" other="#th" />;
```

Available Props:

| Prop name   | Type           | Description                                                                                                                                             |
| ----------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `value`     | number         | *(required)* Value is mapped to plural form below                                                                                                       |
| `other`     | string         | *(required)* general *plural* form                                                                                                                      |
| `offset`    | number         | Offset of value for plural forms                                                                                                                        |
| `zero`      | string         | Form for empty `value`                                                                                                                                  |
| `one`       | string         | *Singular* form                                                                                                                                         |
| `two`       | string         | *Dual* form                                                                                                                                             |
| `few`       | string         | *Paucal* form                                                                                                                                           |
| `many`      | string         | *Plural* form                                                                                                                                           |
| `_<number>` | string         | Exact match form, correspond to `=N` rule. (e.g: `_0`, `_1`)                                                                                            |
| `format`    | string\|Object | Number format passed as options to [`Intl.NumberFormat`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NumberFormat) |

### `Select`[​](#select-1 "Direct link to select-1")

The `Select` JSX macro is used to handle different forms of a message based on a value. It's similar to the [`select`](#select) core macro, but is used in JSX elements.

```
import { Select } from "@lingui/react/macro";

// gender == "female"      -> Her book
// gender == "male"        -> His book
// gender == "non-binary"  -> Their book
<Select value={gender} _male="His book" _female="Her book" other="Their book" />;
```

Available Props:

| Prop name | Type   | Description                                            |
| --------- | ------ | ------------------------------------------------------ |
| `value`   | number | *(required)* Value determines which form is output     |
| `other`   | number | *(required)* Default, catch-all form                   |
| `_<case>` | string | Form for specific case                                 |
| `id`      | string | Custom message ID                                      |
| `comment` | string | Comment for translators                                |
| `context` | string | Allows to extract the same messages with different IDs |
| `render`  | func   | Custom render callback to render translation           |

The select cases except `other` should be prefixed with underscore: `_male` or `_female`.

### `useLingui`[​](#uselingui "Direct link to uselingui")

The `useLingui` React macro gives access to a [`t`](/ref/macro.md#t) macro that is bound to the local `i18n` object passed from the React context.

It returns an object with the following content:

| Key                | Type                  | Description                                                       |
| ------------------ | --------------------- | ----------------------------------------------------------------- |
| `i18n`             | `I18n`                | The `I18n` object instance passed to `I18nProvider`               |
| `t`                | `t`                   | Reference to the `t` macro described above                        |
| `defaultComponent` | `React.ComponentType` | the same `defaultComponent` passed to `I18nProvider`, if provided |

Example usage:

```
import { useLingui } from "@lingui/react/macro";

function MyComponent() {
  const { t } = useLingui();
  const a = t`Text`;
}

// ↓ ↓ ↓ ↓ ↓ ↓

import { useLingui } from "@lingui/react";

function MyComponent() {
  const { _ } = useLingui();
  const a = _(
    /*i18n*/
    {
      id: "xeiujy",
      message: "Text",
    }
  );
}
```

caution

The `useLingui` React macro is available from **Lingui v5**.

## Important Notes[​](#important-notes "Direct link to Important Notes")

### Using Macros[​](#using-macros "Direct link to Using Macros")

All Core Macros cannot be used at the module level:

```
import { t } from "@lingui/core/macro";

// ❌ Bad! This won't work because the `t` macro is used at the module level.
// The `t` macro returns a string, and once this string is assigned, it won't react to locale changes.
const colors = [t`Red`, t`Orange`, t`Yellow`, t`Green`];

// ✅ Good! Every time the function is executed, the `t` macro will be re-executed as well,
// and the correctly translated color labels will be returned.
function getColors() {
  return [t`Red`, t`Orange`, t`Yellow`, t`Green`];
}
```

tip

There is an [ESLint Plugin](/ref/eslint-plugin.md) rule designed to check for this misuse: [`t-call-in-function`](https://github.com/lingui/eslint-plugin/blob/main/docs/rules/t-call-in-function.md).

A better option would be to use the [Lazy Translations](/guides/lazy-translations.md) pattern.

### Global `i18n` Instance[​](#global-i18n-instance "Direct link to global-i18n-instance")

When you use the [`t`](#t) macro (or [`plural`](#plural), [`select`](#select), [`selectOrdinal`](#selectordinal)), it uses a global [`i18n`](/ref/core.md#i18n) instance. While this generally works, there are situations, such as server-side rendering (SSR) applications, where it may not be the best solution.

For better control and flexibility, it's a good idea to avoid the global `i18n` instance and instead use a specific instance tailored to your needs:

```
import { msg } from "@lingui/core/macro";
import { useLingui } from "@lingui/react/macro";

export function showAlert(i18n) {
  alert(i18n._(msg`...`));
}

function MyComponent() {
  // Get i18n instance from React Context
  const { i18n } = useLingui();

  // Pass the instance from outside
  showAlert(i18n);
}
```

## More Examples[​](#more-examples "Direct link to More Examples")

### Examples of JS macros[​](#examples-of-js-macros "Direct link to Examples of JS macros")

```
t`Refresh inbox`;

// ↓ ↓ ↓ ↓ ↓ ↓

i18n._(
  /*i18n*/ {
    id: "EsCV2T",
    message: "Refresh inbox",
  }
);
```

```
customI18n._(msg(`Refresh inbox`));

// ↓ ↓ ↓ ↓ ↓ ↓

customI18n._(
  /*i18n*/ {
    id: "EsCV2T",
    message: "Refresh inbox",
  }
);
```

```
t(customI18n)`Attachment ${name} saved`;

// ↓ ↓ ↓ ↓ ↓ ↓

customI18n._(
  /*i18n*/ {
    id: "nwR43V",
    message: "Attachment {name} saved",
    values: { name },
  }
);
```

```
plural(count, {
  one: "# Message",
  other: "# Messages",
});

// ↓ ↓ ↓ ↓ ↓ ↓

i18n._(
  /*i18n*/ {
    id: "4w2nim",
    message: "{count, plural, one {# Message} other {# Messages}}",
    values: { count },
  }
);
```

```
t({
  id: "msg.refresh",
  message: "Refresh inbox",
});

// ↓ ↓ ↓ ↓ ↓ ↓

i18n._(
  /*i18n*/ {
    id: "msg.refresh",
    message: "Refresh inbox",
  }
);
```

```
const msg = defineMessage`Refresh inbox`;

// ↓ ↓ ↓ ↓ ↓ ↓

const msg = /*i18n*/ {
  id: "EsCV2T",
  message: "Refresh inbox",
};
```

```
const msg = defineMessage({
  id: "msg.refresh",
  message: "Refresh inbox",
});

// ↓ ↓ ↓ ↓ ↓ ↓

const msg = /*i18n*/ {
  id: "msg.refresh",
  message: "Refresh inbox",
};
```

```
const msg = defineMessage({
  id: "msg.plural",
  message: plural(count, {
    one: "# Message",
    other: "# Messages",
  }),
});

// ↓ ↓ ↓ ↓ ↓ ↓

const msg = /*i18n*/ {
  id: "msg.plural",
  message: "{count, plural, one {# Message} other {# Messages}}",
  values: { count },
};
```

### Examples of JSX macros[​](#examples-of-jsx-macros "Direct link to Examples of JSX macros")

```
<Trans>Attachment {name} saved</Trans>

// ↓ ↓ ↓ ↓ ↓ ↓

<Trans
   id={"nwR43V"}
   message="Attachment {name} saved"
   values={{ name }}
/>
```

```
<Plural
   value={count}
   one="# Message"
   other="# Messages"
/>

// ↓ ↓ ↓ ↓ ↓ ↓

<Trans
   id={"4w2nim"}
   message="{count, plural, one {# Message} other {# Messages}}"
   values={{ count }}
/>
```

```
<Trans id="msg.refresh">
   Refresh inbox
</Trans>

// ↓ ↓ ↓ ↓ ↓ ↓

<Trans
   id="msg.refresh"
   message="Refresh inbox"
/>
```


---

# Metro Transformer

[Metro bundler](https://metrobundler.dev/) is a JavaScript bundler used in React Native apps. The `@lingui/metro-transformer` offers an alternative to the [`lingui compile`](/ref/cli.md#compile) command: a transformer that enables Metro to compile `.po` files on the fly.

The transformer enables you to `import` `.po` files directly, instead of running `lingui compile` and `import`ing the resulting JavaScript (or TypeScript) files.

## Installation[​](#installation "Direct link to Installation")

> Only Expo SDK 50 and React Native v0.73.0 or newer are supported.

Install `@lingui/metro-transformer` as a development dependency:

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/metro-transformer
```

```
yarn add --dev @lingui/metro-transformer
```

```
pnpm add --save-dev @lingui/metro-transformer
```

Set up the transformer in your `metro.config.js` by specifying [`babelTransformerPath`](https://metrobundler.dev/docs/configuration/#babeltransformerpath) and updating `sourceExts`.

If you need to combine multiple transformers, use [this approach](https://stackoverflow.com/a/57660231/2070942):

<!-- -->

* Expo
* Plain React Native

metro.config.js

```
// Learn more https://docs.expo.io/guides/customizing-metro
const { getDefaultConfig } = require("expo/metro-config");

const config = getDefaultConfig(__dirname);
const { transformer, resolver } = config;

config.transformer = {
  ...transformer,
  babelTransformerPath: require.resolve("@lingui/metro-transformer/expo"),
};
config.resolver = {
  ...resolver,
  sourceExts: [...resolver.sourceExts, "po", "pot"],
};

module.exports = config;
```

metro.config.js

```
const { getDefaultConfig, mergeConfig } = require("@react-native/metro-config");

const defaultConfig = getDefaultConfig(__dirname);
const { assetExts, sourceExts } = defaultConfig.resolver;

/**
 * Metro configuration
 * https://reactnative.dev/docs/metro
 *
 * @type {import('metro-config').MetroConfig}
 */
const config = {
  transformer: {
    babelTransformerPath: require.resolve("@lingui/metro-transformer/react-native"),
  },
  resolver: {
    sourceExts: [...sourceExts, "po", "pot"],
  },
};

module.exports = mergeConfig(defaultConfig, config);
```

## Usage[​](#usage "Direct link to Usage")

tip

Take a look at the [example app](https://github.com/lingui/js-lingui/tree/main/examples/react-native) that uses the transformer. The transformer only supports catalogs based on `po` and `pot` files.

The library is currently in beta. If you encounter any issues, please [report them](https://github.com/lingui/js-lingui/issues).

1. Import `.po` files directly in your code:

   ```
   -import { messages } from "./src/locales/en/messages.ts";
   +import { messages } from "./src/locales/en/messages.po";
   ```

2. If you are using TypeScript, you need to add `.po` file declaration so that TypeScript understands the file extension:

   src/po-types.d.ts

   ```
   declare module "*.po" {
     import type { Messages } from "@lingui/core";
     export const messages: Messages;
   }
   ```

3. Restart Metro bundler with `expo start -c` or `yarn start --reset-cache` to clear the transformer cache.

4. Profit! 🎉

danger

Whenever you make a change to the Lingui config file (this should not happen often), restart Metro bundler.

## See Also[​](#see-also "Direct link to See Also")

* [React Native i18n Tutorial](/tutorials/react-native.md)
* [Lingui React Native Example App](https://github.com/lingui/js-lingui/tree/main/examples/react-native)


---

# React API Reference

The Lingui React API, provided by the `@lingui/react` package, integrates Lingui's core JavaScript functionality directly into React, extending React components with the ability to dynamically manage localization.

This API provides React-specific components that automatically update the user interface when the active language or interpolated variables change, simplifying translation management and reactivity in the application.

## Installation[​](#installation "Direct link to Installation")

* npm
* Yarn
* pnpm

```
npm install --save @lingui/react
```

```
yarn add @lingui/react
```

```
pnpm add @lingui/react
```

## Rendering of Translations[​](#rendering-translations "Direct link to Rendering of Translations")

All i18n components render translations as plain text by default, without a wrapping tag. You can customize this behavior in two ways:

* Globally: Set the `defaultComponent` prop on the [`I18nProvider`](#i18nprovider) component.
* Locally: Use the `render` or `component` props on individual i18n components.

### Global Configuration[​](#global-configuration "Direct link to Global Configuration")

You can set a default rendering component using the `defaultComponent` prop in [`I18nProvider`](#i18nprovider). This is especially useful in cases like React Native, where you may want translations to be rendered inside a `<Text>` component by default.

### Local Configuration[​](#local-configuration "Direct link to Local Configuration")

You can customize how translations are rendered locally within individual i18n components using the following props:

| Prop name   | Type                                 | Description                                                   |
| ----------- | ------------------------------------ | ------------------------------------------------------------- |
| `className` | string                               | Class name to be added to `<span>` element                    |
| `render`    | Function(props) -> Element \| `null` | Custom render callback to render translation                  |
| `component` | Component \| `null`                  | React component to wrap the translation                       |
| `comment`   | string                               | Comment picked up by extractor to provide translation context |

The `className` prop is applicable only to built-in components when the `render` prop is specified as a string.

When using the `render` callback, it accepts an object of type `TransRenderProps` as an argument:

```
type TransRenderProps = {
  id: string;
  translation: React.ReactNode;
  children: React.ReactNode;
  message?: string | null;
};
```

* `id` - The message ID.
* `translation` - The translated message.
* `children` - The same as `translation`, provided for compatibility with components that expect a `children` prop.
* `message` - The compiled message (generally not needed).

If you choose to use the `component` prop, the same object will be passed as a prop to your custom component. This allows you to access the necessary information for rendering translations directly within your component.

#### Important Notes[​](#important-notes "Direct link to Important Notes")

* You cannot use both `render` and `component` props simultaneously.
* Both `render` and `component` can be set to `null` to override the global `defaultComponent` and render a string without a wrapping component.
* The `component` supports nested elements with the `asChild` pattern.

#### Examples[​](#examples "Direct link to Examples")

Using a custom component:

```
import { Text } from "react-native";

<Trans component={Text}>Link to docs</Trans>;
// renders as <Text>Link to docs</Text>
```

Using render prop for custom rendering logic:

```
<Trans render={({ translation }) => <Icon label={translation} />}>Sign in</Trans>
// renders as <Icon label="Sign in" />
```

## Lingui Context[​](#lingui-context "Direct link to Lingui Context")

Message catalogs and the active locale are provided through the context in the [`I18nProvider`](#i18nprovider). You can access this context using the [`useLingui`](#uselingui) hook.

The `LinguiContext` object is exported from the `@lingui/react` package. While most users will not need to interact with it directly, it can be useful for advanced scenarios where the default behavior of `I18nProvider` doesn't meet your specific needs.

### `I18nProvider`[​](#i18nprovider "Direct link to i18nprovider")

The `I18nProvider` provides Lingui context to all components in the subtree. It should be rendered as top-level component of your application.

It ensures that its children are only rendered after a locale has been activated, guaranteeing that any components relying on `i18n` have access to the translations. Additionally, the `I18nProvider` subscribes to change events emitted by the `i18n` object, automatically re-rendering all components that consume the Lingui context whenever messages are updated or a new locale is activated.

| Prop name          | Type                  | Description                                                                    |
| ------------------ | --------------------- | ------------------------------------------------------------------------------ |
| `i18n`             | `I18n`                | The `I18n` object instance (usually the one imported from `@lingui/core`)      |
| `children`         | `React.ReactNode`     | React Children node                                                            |
| `defaultComponent` | `React.ComponentType` | A React component within which translation strings will be rendered (optional) |

The `defaultComponent` serves the same purpose as the `component` prop in other i18n components. For a detailed explanation of how translations are rendered, see the [Rendering of Translations](#rendering-translations) section at the beginning of this document.

#### Examples[​](#examples-1 "Direct link to Examples")

```
import React from "react";
import { I18nProvider } from "@lingui/react";
import { i18n } from "@lingui/core";
import { messages as messagesEn } from "./locales/en/messages.js";

i18n.load({
  en: messagesEn,
});
i18n.activate("en");

const DefaultI18n = ({ children }) => <span>{children}</span>;

const App = () => {
  return (
    <I18nProvider i18n={i18n} defaultComponent={DefaultI18n}>
      // rest of the app
    </I18nProvider>
  );
};
```

### `useLingui`[​](#uselingui "Direct link to uselingui")

The `useLingui` hook provides access to the Lingui context. It returns an object with the following properties:

| Key                | Type                  | Description                                                                |
| ------------------ | --------------------- | -------------------------------------------------------------------------- |
| `i18n`             | `I18n`                | The `I18n` object instance that you passed to `I18nProvider`               |
| `_`                | `I18n[_]`             | Reference to the [`i18n._`](/ref/core.md#i18n._) function, explained below |
| `defaultComponent` | `React.ComponentType` | The same `defaultComponent` you passed to `I18nProvider`, if provided      |

Components that use `useLingui` hook will re-render when locale and / or catalogs change. However, the reference to the `i18n` object is stable and doesn't change between re-renders. This can lead to unexpected behavior with memoization (see [memoization pitfall](/guides/lazy-translations.md#memoization-pitfall)).

To alleviate the issue, `useLingui` provides the `_` function, which is the same as [`i18n._`](/ref/core.md#i18n._) but *its reference changes* with each update of the Lingui context. Thanks to that, you can safely use this `_` function as a hook dependency:

```
import React from "react";
import { msg } from "@lingui/core/macro";
import { useLingui } from "@lingui/react";

const CurrentLocale = () => {
  const { _, i18n } = useLingui();

  return (
    <span>
      {_(msg`Current locale`)}: {i18n.locale}
    </span>
  );
};
```

tip

There is a [macro version](/ref/macro.md#uselingui) of the `useLingui` hook which supports all features of the [`t` macro](/ref/macro.md#t) and uses the runtime `useLingui` hook (from `@lingui/react`) under the hood:

```
import { useLingui } from "@lingui/react/macro";

const CurrentLocale = () => {
  const { t } = useLingui();

  const userName = "Tim";
  return <span>{t`Hello ${userName}`}</span>;
};
```

You also can safely use the returned `t` function in a dependency array of React hooks.

## Components[​](#components "Direct link to Components")

The `@lingui/react` package provides the `Trans` component for rendering translations in your application. It is a low-level component that allows you to render translations with dynamic values and components.

caution

While this component is available, you will likely find [Macros](/ref/macro.md) to be more convenient and developer-friendly. Macros simplify the translation process and reduce boilerplate code.

This section serves as a reference for those who prefer to use the components directly.

### `Trans`[​](#trans "Direct link to trans")

| Prop name | Type     | Description                               |
| --------- | -------- | ----------------------------------------- |
| `id`      | `string` | Key, the message ID                       |
| `message` | `string` | Default message                           |
| `values`  | `object` | Variables to interpolate into the message |

The `values` and `components` props allow to pass dynamic values and components used for formatting the translation. In addition, the `comment` prop provides context to translators, helping them to understand the intent behind the message.

tip

Import the [`Trans`](/ref/macro.md#trans) macro instead if you use macros. It will be transformed into the runtime `Trans` component automatically:

```
import { Trans } from "@lingui/react/macro";
<Trans>Refresh inbox</Trans>;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";
<Trans id="EsCV2T" message="Refresh inbox" />;
```

It's also possible to use the `Trans` component directly without macros. In this case `id` identifies the message to be translated.

#### Examples[​](#examples-2 "Direct link to Examples")

```
import React from "react";
import { Trans } from "@lingui/react";

const MyComponent = () => {
  return (
    <div>
      {/* Simple translation without dynamic values */}
      <Trans id="my.message" message="Hello World" />

      {/* Translation with dynamic values */}
      <Trans id="greeting" message="Hello {name}" values={{ name: "Arthur" }} />

      {/* Translation with a comment for translators */}
      <Trans id="hello.world" message="Hello world" comment="A message that greets the user" />

      {/* Translation with a component for formatting */}
      <Trans
        id="link"
        message="Read <link>Description</link> below."
        components={{ link: <a href="/docs">Documentation</a> }}
      />
    </div>
  );
};
```

#### Plurals[​](#plurals "Direct link to Plurals")

If for some reason you cannot use [Macros](/ref/macro.md), you can render plurals using the simple `Trans` component by passing the [ICU MessageFormat](/guides/message-format.md) string as the `message` prop:

```
import React from "react";
import { Trans } from "@lingui/react";

const CarCount = ({ cars }) => {
  return (
    <Trans
      id="application.pages.carsList"
      message="{count, plural, =1 {# car} other {# cars}}"
      values={{ count: cars.length }}
    />
  );
};
```


---

# SWC Plugin

[SWC](https://swc.rs/) is an extensible Rust-based platform for the next generation of fast developer tools.

If you're using SWC in your project, you can opt for the `@lingui/swc-plugin`. This plugin, designed for SWC, is a Rust version of [Lingui Macros](/ref/macro.md).

[![npm-version](https://img.shields.io/npm/v/@lingui/swc-plugin?logo=npm\&cacheSeconds=1800)](https://www.npmjs.com/package/@lingui/swc-plugin) [![npm-downloads](https://img.shields.io/npm/dt/@lingui/swc-plugin?cacheSeconds=500)](https://www.npmjs.com/package/@lingui/swc-plugin)

## SWC Compatibility[​](#swc-compatibility "Direct link to SWC Compatibility")

SWC Plugin support is still experimental. Semver backwards compatibility between different `@swc/core` versions [is not guaranteed](https://github.com/swc-project/swc/issues/5060). You need to choose an appropriate version of the `@lingui/swc-plugin` to match the compatible `@swc/core` version.

tip

It is recommended to check the [plugins.swc.rs](https://plugins.swc.rs/) site to find the compatible version.

## Installation[​](#installation "Direct link to Installation")

Install `@lingui/swc-plugin` as a development dependency:

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/swc-plugin
```

```
yarn add --dev @lingui/swc-plugin
```

```
pnpm add --save-dev @lingui/swc-plugin
```

To ensure that the resolved version of `@swc/core` is one of the supported versions, you can use the `resolutions` field in the `package.json` file, which is supported by Yarn:

package.json

```
"resolutions": {
  "@swc/core": "1.3.56"
}
```

or `overrides` for >npm\@8.3

package.json

```
"overrides": {
  "@swc/core": "1.3.56"
}
```

## Usage[​](#usage "Direct link to Usage")

Add the following configuration to your [`.swcrc`](https://swc.rs/docs/configuration/swcrc) file:

.swcrc

```
{
  "$schema": "https://json.schemastore.org/swcrc",
  "jsc": {
    "experimental": {
      "plugins": [
        [
          "@lingui/swc-plugin",
          {
            // Additional Configuration
          }
        ]
      ]
    }
  }
}
```

If you use Next.js, add the following to your `next.config.js`:

next.config.js

```
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  experimental: {
    swcPlugins: [
      [
        "@lingui/swc-plugin",
        {
          // Additional Configuration
        },
      ],
    ],
  },
};

module.exports = nextConfig;
```

## Additional Configuration[​](#additional-configuration "Direct link to Additional Configuration")

### Runtime Modules Configuration[​](#runtime-modules-configuration "Direct link to Runtime Modules Configuration")

You can configure the plugin by passing the `runtimeModules` option. This option is an object that maps runtime module names to their corresponding module paths and export names. It is essential for macros, which rely on referencing the global `i18n` object.

```
[
  "@lingui/swc-plugin",
  {
    "runtimeModules": {
      "i18n": ["@lingui/core", "i18n"],
      "trans": ["@lingui/react", "Trans"]
    }
  }
]
```

For more details, refer to the [Runtime Configuration](/ref/conf.md#runtimeconfigmodule) section of the documentation.

### Strip Non-Essential Fields[​](#strip-non-essential-fields "Direct link to Strip Non-Essential Fields")

Lingui strips non-essential fields from builds if `NODE_ENV` is set to `production`. You can override this behavior by using the `stripNonEssentialFields` option. For example, if you want to keep all fields regardless of the environment, you can set:

```
[
  "@lingui/swc-plugin",
  {
    "stripNonEssentialFields": false
  }
]
```

## Examples[​](#examples "Direct link to Examples")

* [React with Vite and SWC](https://github.com/lingui/js-lingui/tree/main/examples/vite-project-react-swc)
* [Next.js with SWC](https://github.com/lingui/js-lingui/tree/main/examples/nextjs-swc)

info

If you would like to suggest a new feature or report a bug, please [open an issue](https://github.com/lingui/swc-plugin/issues) on the GitHub repository.


---

# Vite Plugin

Vite is a blazing fast frontend build tool powering the next generation of web applications.

The `@lingui/vite-plugin` is a Vite plugin that compiles Lingui catalogs on the fly and provides the necessary configuration for seamless integration with Vite.

[![npm-version](https://img.shields.io/npm/v/@lingui/vite-plugin?logo=npm\&cacheSeconds=1800)](https://www.npmjs.com/package/@lingui/vite-plugin) [![npm-downloads](https://img.shields.io/npm/dt/@lingui/vite-plugin?cacheSeconds=500)](https://www.npmjs.com/package/@lingui/vite-plugin)

## Installation[​](#installation "Direct link to Installation")

Install `@lingui/vite-plugin` as a development dependency:

* npm
* Yarn
* pnpm

```
npm install --save-dev @lingui/vite-plugin
```

```
yarn add --dev @lingui/vite-plugin
```

```
pnpm add --save-dev @lingui/vite-plugin
```

For a complete installation guide, see [Installation and Setup](/installation.md#vite).

## Usage[​](#usage "Direct link to Usage")

To integrate Lingui with Vite, add the `@lingui/vite-plugin` inside your `vite.config.ts` as follows:

vite.config.ts

```
import { UserConfig } from "vite";
import { lingui } from "@lingui/vite-plugin";

const config: UserConfig = {
  plugins: [lingui()],
};
```

Then use [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import#dynamic_imports) in your code to load only necessary catalog:

```
export async function dynamicActivate(locale: string) {
  const { messages } = await import(`./locales/${locale}.po`);

  i18n.load(locale, messages);
  i18n.activate(locale);
}
```

Remember that the file extension is mandatory.

tip

If you are using a format that has a different extension than `*.po`, you need to specify the `?lingui` suffix:

```
const { messages } = await import(`./locales/${language}.json?lingui`);
```

## See Also[​](#see-also "Direct link to See Also")

* [Dynamic Loading](/guides/dynamic-loading-catalogs.md)
* [Dynamic Import in Vite](https://vitejs.dev/guide/features.html#dynamic-import)


---

# Crowdin

![Crowdin agile localization for developers](https://support.crowdin.com/assets/logos/crowdin-dark-symbol.png#gh-light-mode-only)![Crowdin agile localization for developers](https://support.crowdin.com/assets/logos/symbol/png/crowdin-symbol-cWhite.png#gh-dark-mode-only)

Crowdin is a localization management platform that helps translate your LinguiJS-based product. Automate localization, release several multilingual versions of your app simultaneously, and provide an enhanced experience for your global customers.

[Website](https://crowdin.com/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) | [GitHub](https://github.com/crowdin) | [Support](https://crowdin.com/contacts?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev)

## Features[​](#features "Direct link to Features")

### Keep all translations in one place while connecting your teams via Crowdin[​](#keep-all-translations-in-one-place-while-connecting-your-teams-via-crowdin "Direct link to Keep all translations in one place while connecting your teams via Crowdin")

Connect with your content, marketing, and translation teams in one collaborative space:

* Screenshots for additional context.
* Highlight HTML, placeholders, plurals, and more.
* Describe the context and set character limits to ensure the translation fits the UI.
* All translations are done online or can be uploaded to the platform.
* Jira integration to notify you about source string issues.
* Tips for translators to ensure there is no extra space or broken code.

### Ship faster with localization running in parallel[​](#ship-faster-with-localization-running-in-parallel "Direct link to Ship faster with localization running in parallel")

Keep developing new features and improvements while translators receive new texts in real-time. Release multilingual versions for customers around the globe simultaneously.

### Release your product in several languages at once[​](#release-your-product-in-several-languages-at-once "Direct link to Release your product in several languages at once")

Help users from different regions use the latest version of your product in their language:

* Get feature branches translated independently from the master branch.
* Translators work together in one place to boost productivity.
* Never deal with translations in spreadsheets or email attachments.
* Source texts are updated for translators automatically and in real-time.
* Automatically pull completed translations that are ready to be merged.

### Seamlessly integrate localization during any phase of your development cycle[​](#seamlessly-integrate-localization-during-any-phase-of-your-development-cycle "Direct link to Seamlessly integrate localization during any phase of your development cycle")

Automate the integration of source texts and translations between Crowdin and your source code with one-click integration or customizable solutions.

### Define your translation strategy[​](#define-your-translation-strategy "Direct link to Define your translation strategy")

Decide who will translate your content:

* Invite your team of translators (in-house translators, freelancers, or translation agencies you already work with).
* Order professional translations from a vendor (translation agency) from Crowdin Vendors Marketplace.
* Configure machine translation engines.
* Engage your community.

### VCS: GitHub, GitLab, Bitbucket[​](#vcs-github-gitlab-bitbucket "Direct link to VCS: GitHub, GitLab, Bitbucket")

Source strings are pulled automatically and are always up to date for your translators. Translated content is automatically pushed to your repository as a request.

![Automatically pull source strings to Crowdin and push translated content to your repository](/assets/images/Crowdin__js-lingui-vcs-a0145c95baafee2bd889e6d08d7ec993.png)

## CLI[​](#cli "Direct link to CLI")

Connect cross-platform [Crowdin CLI](https://crowdin.github.io/crowdin-cli/) directly to your code repository and never deal with localization files manually again.

With Crowdin CLI, you can:

* Automate the process of updating your source files in your Crowdin project.
* Download translations from Crowdin and automatically save them in the correct locations.
* Upload all your existing translations to Crowdin in minutes.

### Create the `crowdin.yml` configuration file[​](#create-the-crowdinyml-configuration-file "Direct link to create-the-crowdinyml-configuration-file")

crowdin.yml

```
project_id: "123456" # Your Crowdin project ID
api_token_env: CROWDIN_PERSONAL_TOKEN

preserve_hierarchy: true

files: # Paths to the source and translation files
  - source: /**/locales/en/*
    translation: /**/locales/%two_letters_code%/%original_file_name%
```

### Install the Crowdin CLI as an npm package[​](#install-the-crowdin-cli-as-an-npm-package "Direct link to Install the Crowdin CLI as an npm package")

* npm
* Yarn
* pnpm

```
npm install --save-dev @crowdin/cli
```

```
yarn add --dev @crowdin/cli
```

```
pnpm add --save-dev @crowdin/cli
```

### Add the synchronization scripts[​](#add-the-synchronization-scripts "Direct link to Add the synchronization scripts")

Add the following scripts to your `package.json`:

package.json

```
{
  "scripts": {
    "crowdin": "crowdin",
    "sync": "crowdin push && crowdin pull",
    "sync:sources": "crowdin push",
    "sync:translations": "crowdin pull"
  }
}
```

### Configuration[​](#configuration "Direct link to Configuration")

Set the `CROWDIN_PERSONAL_TOKEN` env variable on your computer, to allow the CLI to authenticate with the Crowdin API.

#### Usage[​](#usage "Direct link to Usage")

Test that you can run the Crowdin CLI:

* npm
* Yarn
* pnpm

```
npm run crowdin --version
```

```
yarn crowdin --version
```

```
pnpm run crowdin --version
```

Upload all the source files to Crowdin:

* npm
* Yarn
* pnpm

```
npm run sync:sources
```

```
yarn sync:sources
```

```
pnpm run sync:sources
```

Download translation files from Crowdin:

* npm
* Yarn
* pnpm

```
npm run sync:translations
```

```
yarn sync:translations
```

```
pnpm run sync:translations
```

Upload sources to Crowdin and download translations from Crowdin:

* npm
* Yarn
* pnpm

```
npm run sync
```

```
yarn sync
```

```
pnpm run sync
```

To run other Crowdin CLI commands you can use the following command:

* npm
* Yarn
* pnpm

```
npm run crowdin <command> <options>
```

```
yarn crowdin <command> <options>
```

```
pnpm run crowdin <command> <options>
```

To see the full list of possible commands and options:

* npm
* Yarn
* pnpm

```
npm run crowdin -h
```

```
yarn crowdin -h
```

```
pnpm run crowdin -h
```

## Over-The-Air Content Delivery[​](#over-the-air-content-delivery "Direct link to Over-The-Air Content Delivery")

Over-the-Air Content Delivery is a feature that allows you to instantly update sources and translations in your mobile, server, desktop, or web apps with a single click without preparing a new release.

Visit the following pages to learn more about how to integrate Over-The-Air Content Delivery into your Lingui project:

* [Lingui tutorial - Crowdin OTA JS Client](https://crowdin.github.io/ota-client-js/tutorials/lingui/)
* [Lingui String Exporter - Crowdin Marketplace](https://store.crowdin.com/lingui-string-exporter?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev)

## API and Webhooks[​](#api-and-webhooks "Direct link to API and Webhooks")

Customize your experience. Automate and scale your localization workflow. Seamlessly add new content for translation to your Crowdin project, check translation status, merge new content, etc.

See the [API](https://support.crowdin.com/developer/api/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) and [Webhooks](https://support.crowdin.com/developer/webhooks/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) documentation for more information.

## Next Steps[​](#next-steps "Direct link to Next Steps")

To get started, register a [Crowdin.com](https://accounts.crowdin.com/register?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) or [Crowdin Enterprise](https://accounts.crowdin.com/workspace/create?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev) account. Once you have signed up, [create your localization project](https://support.crowdin.com/creating-project/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).

Depending on how you'd like to work with Crowdin, you have the following options:

1. [Integrate Crowdin with GitHub](https://support.crowdin.com/github-integration/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).
2. Manage and synchronize your localization resources with [Crowdin CLI](https://developer.crowdin.com/cli-tool/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).
3. [Upload files for the test via UI](https://support.crowdin.com/uploading-files/?utm_source=lingui.dev\&utm_medium=referral\&utm_campaign=lingui.dev).


---

# Sync & Collaboration Tools

While Lingui provides a powerful API for managing your translations, it doesn't provide an integrated solution for managing synchronization and collaboration with your translators.

This guide covers tools that can help you manage your localization process. You may come across acronyms like TMS (Translation Management System) or CAT (Computer Aided Translation) that are sometimes used to describe these tools.

## Workflows[​](#workflows "Direct link to Workflows")

The easiest way to translate your application is to translate your message catalogs directly in a text editor, or with a tool like [Poedit](https://poedit.net).

This solution may be good enough when your application is small and doesn't evolve much, but it quickly becomes hard work as the number of sentences to translate and target languages to manage increases over time.

It becomes increasingly difficult and time-consuming to manage the back-and-forth with translators while keeping your application's message catalogs up to date with the current state of a codebase that does not stop evolving.

### Regular Workflow[​](#regular-workflow "Direct link to Regular Workflow")

![Translation workflow without sync and collaboration tool](/assets/images/without-collaboration-tool-c754b37fb89866426c7e758c06a9e8f7.svg)

This is the most basic workflow which involves sending the `.po` files to your translators (usually by email) and syncing them back manually into your application.

This workflow is manageable when your application is still quite small, doesn't contain a lot of text, and doesn't evolve much.

### Sync & Collaboration Tool Workflow[​](#sync--collaboration-tool-workflow "Direct link to Sync & Collaboration Tool Workflow")

![Translation workflow with sync and collaboration tool](/assets/images/with-collaboration-tool-0a2b67b7ad85e0a266ae26c5d3d2a8e6.svg)

When the amount of text to translate increases, and the number of target languages grows, it becomes more efficient to use a sync and collaboration tool to assist you with the management of your team of translators, and co-evolution between your code and the translated files.

Instead of manually sending and receiving many emails and fixing the inconsistencies with your code, a `sync` method is called and your `.po` and `.js` files are directly updated with the latest translations. Your translators will also be notified when there are new text to translate.

## Benefits[​](#benefits "Direct link to Benefits")

* **Synchronization**: unique `yarn sync` or `npm run sync` command to synchronize your project with all your translators and update your local `.po` and `.js` files with the latest translations.
* **Translation Interface**: provide a professional and flexible interface to translators.
* **Translation Memory**: assist translators by suggesting previously translated sentences that are similar.
* **Machine Translation**: auto-translate with Google Translate, DeepL, etc. and human-proofread later.
* **Smart Plural Management**: allows to translate `Message` and `Messages` instead of `{count, plural, one {Message} other {Messages}}`.
* **Consistency**: assist translators with `{variable}` interpolation and HTML formatting.

## Available Tools[​](#available-tools "Direct link to Available Tools")

* [Crowdin](/tools/crowdin.md)
* [Translation.io](/tools/translation-io.md)


---

# Translation.io

![Translation.io - Localization made simple for tech companies](https://translation.io/logo.png)

Translation.io is a professional synchronization and collaboration platform that will assist your team in the translation of your Lingui application.

[Website](https://translation.io/lingui) | [GitHub](https://github.com/translation/lingui) | <contact@translation.io>

## Features[​](#features "Direct link to Features")

### Smooth Team Management[​](#smooth-team-management "Direct link to Smooth Team Management")

Invite collaborators using their email or username, and assign them a role and a target language. They will be brought on board and kept informed about any new activity in their language.

![Smooth Team Management on Translation.io](https://translation.io/gifs/lingui/translation-collaborators.gif)

Learn more:

* [Fine-Grained Authorizations](https://translation.io/blog/fine-grained-authorization-and-role-management?default_stack=lingui)
* [Activity Digests](https://translation.io/blog/better-history-and-activity-email-digests?default_stack=lingui)

### Elegant Translation Process[​](#elegant-translation-process "Direct link to Elegant Translation Process")

Our interface was designed to be the most ergonomic way to translate. It provides translation suggestions (from [TM](https://en.wikipedia.org/wiki/Translation_memory), Google Translate or DeepL), context, discussion and history.

Keyboard shortcuts allow translators to stay focused on their work, visual hints indicate when something went wrong, for example when an interpolated variable or HTML tag is missing.

![Elegant Translation Process on Translation.io](https://translation.io/gifs/lingui/translation-interface.gif)

Learn more:

* [Keyboard Shortcuts](https://translation.io/blog/shortcuts-and-translation?default_stack=lingui)
* [History and Activity Digests](https://translation.io/blog/better-history-and-activity-email-digests?default_stack=lingui)

### Syntax Highlighting[​](#syntax-highlighting "Direct link to Syntax Highlighting")

Sometimes you have no choice but to confront your translators with HTML or interpolated variables. The problem is that translators do not necessarily know the meaning of these notations and may be tempted to translate them or may inadvertently alter them.

`Hello {name}` should never be translated as `Bonjour {nom}`, and several mechanisms are in place to ensure this, such as warnings and auto-completion:

![Syntax Highlighting warning on Translation.io](https://translation.io/_articles/translation/2019-10-11-highlighting-of-html-tags-and-interpolated-variables/highlight-interpolated-variable-lingui.png)

***

![Syntax Highlighting auto-completion on Translation.io](https://translation.io/gifs/lingui/translation-highlights.gif)

### Smart Plural Management[​](#smart-plural-management "Direct link to Smart Plural Management")

Lingui allows to write plurals using the [ICU MessageFormat](/guides/message-format.md) syntax that looks like this:

```
{count, plural, =0 {No messages}
                one {# message}
                other {# messages}}
```

But you can't ask a translator to understand this syntax, and he or she would be tempted to translate `one` or `other` keywords in other languages, breaking your code at the same time.

That's why plural syntaxes are deconstructed to make translation easier, and then reconstructed in the local `.po` files.

If the target language has more plural forms than the source language, examples are also provided to the translator, as it may be unclear which plural form the `few` or `other` keyword refers to in that specific target language (for instance, Czech has three plural forms).

![Smart Plural Management on Translation.io](/assets/images/translation-lingui-plural-forms-cfe7f08db002ef78fb4b12b5fb5a2f0f.png)

### Efficient Search[​](#efficient-search "Direct link to Efficient Search")

Our powerful search helps translators to maintain consistency of terms throughout their work. In addition, they are able to filter depending on a particular source file or context. To provide a more enjoyable experience, this lightning-fast search works without any page reloading.

![Efficient Search on Translation.io](https://translation.io/gifs/lingui/translation-search.gif)

Learn more:

* [Smart URLs](https://translation.io/blog/smart-urls-in-translation-interface?default_stack=lingui)

### Adaptive Workflows using Tags[​](#adaptive-workflows-using-tags "Direct link to Adaptive Workflows using Tags")

Our interface is flexible enough to adapt to your own translation workflows. Add custom tags to your segments and you'll be directly able to filter them. Moreover, these tags will appear in the statistics page so you can use them for reporting.

![Adaptive Workflows using Tags on Translation.io](https://translation.io/gifs/lingui/translation-tags.gif)

Learn more:

* [How to Use Tags](https://translation.io/blog/tags-work-better-as-a-team?default_stack=lingui)
* [Project Statistics](https://translation.io/blog/translation-project-statistics?default_stack=lingui)

## Installation[​](#installation "Direct link to Installation")

### Create your Lingui project[​](#create-your-lingui-project "Direct link to Create your Lingui project")

Create an account on [Translation.io](https://translation.io/lingui) and create a new Lingui project.

### Configure your application[​](#configure-your-application "Direct link to Configure your application")

Copy the `.linguirc` configuration file that was generated for you to the root of your application.

The configuration file looks like this:

.linguirc

```
{
  [...]
  "format": "po",
  "service": {
    "name": "TranslationIO",
    "apiKey": "abcdefghijklmnopqrstuvwxyz012345"
  }
}
```

The synchronization will then be part of the [`extract`](/ref/cli.md#extract) command.

### Add the following scripts[​](#add-the-following-scripts "Direct link to Add the following scripts")

Add these lines to your `package.json` to make your life easier.

package.json

```
{
  "scripts": {
    "sync": "lingui extract --overwrite && lingui compile",
    "sync_and_purge": "lingui extract --overwrite --clean && lingui compile"
  }
}
```

### Initialize your project[​](#initialize-your-project "Direct link to Initialize your project")

Initialize your project and upload your source text and potential existing translations with:

* npm
* Yarn
* pnpm

```
npm run sync
```

```
yarn sync
```

```
pnpm run sync
```

## Usage[​](#usage "Direct link to Usage")

### Sync[​](#sync "Direct link to Sync")

To send new translatable strings and get new translations from Translation.io, and at the same time generate the minified JavaScript catalog files, simply run:

* npm
* Yarn
* pnpm

```
npm run sync
```

```
yarn sync
```

```
pnpm run sync
```

### Sync and Purge[​](#sync-and-purge "Direct link to Sync and Purge")

If you need to remove unused strings from Translation.io, using the current branch as reference.

As the name says, this operation will also perform a sync at the same time.

**Warning**: all strings that are not present in the current local branch will be **permanently deleted from Translation.io**.

* npm
* Yarn
* pnpm

```
npm run sync_and_purge
```

```
yarn sync_and_purge
```

```
pnpm run sync_and_purge
```


---

# JavaScript Apps Internationalization

This tutorial will walk you through using Lingui's internationalization (i18n) features in a vanilla JavaScript application. We'll cover the essentials of the `@lingui/core` package, which handles all translation and message catalog management.

Example

If you're looking for a working solution, check out the [Vanilla JS example](https://github.com/lingui/js-lingui/tree/main/examples/js). This example application shows a complete setup using Lingui and vanilla JavaScript.

## Installing Lingui[​](#installing-lingui "Direct link to Installing Lingui")

1. Follow the [Installation and Setup](/installation.md) page for initial setup.
2. Install the [`@lingui/core`](/ref/core.md) package, which is responsible for translation and message catalog handling.

## Setting up i18n[​](#setting-up-i18n "Direct link to Setting up i18n")

First, we need to set up the i18n singleton, which is pretty simple:

```
import { i18n } from "@lingui/core";
import { messages } from "path-to-locale/en/messages.js";

i18n.load("en", messages);
i18n.activate("en");
```

The `messages.js` is generated by the Lingui CLI and contains compiled message catalogs.

tip

Alternatively, you can load catalogs dynamically using the [`@lingui/loader`](/ref/loader.md) or [`@lingui/vite-plugin`](/ref/vite-plugin.md) without the need to import compiled messages manually.

## Localizing Your App[​](#localizing-your-app "Direct link to Localizing Your App")

To localize your application, you need to wrap your localizable texts in [Macros](/ref/macro.md). Lingui provides a set of Core Macros that transform tagged template literals and can be used in any JavaScript context.

Let's wrap our text in the [`t`](/ref/macro.md#t) macro:

```
import { t } from "@lingui/core/macro";

t`Hello World!`;
// becomes "Salut le monde!"

const name = "Fred";
t`My name is ${name}`;
// becomes "Je m'appelle Fred"
```

Plurals and selections are possible using [`plural`](/ref/macro.md#plural) and [`select`](/ref/macro.md#select) macros:

```
import { plural } from "@lingui/core/macro";

const count = 42;

plural(count, {
  one: "# book",
  other: "# books",
});
// becomes "42 livres"
```

It's also possible to nest message formats. Each message format method in `i18n` has a standalone companion, which only returns message without performing the translation:

```
import { t, select, plural } from "@lingui/core/macro";

select(gender, {
  offset: 1,
  female: plural(numOfGuests, {
    offset: 1,
    0: t`${host} does not give a party.`,
    1: t`${host} invites ${guest} to her party.`,
    2: t`${host} invites ${guest} and one other person to her party.`,
    other: t`${host} invites ${guest} and # other people to her party.`
  }),
  male: plural(value, {...}),
  other: plural(value, {...}),
});
```

caution

All Core Macros cannot be used at the module level. They must be used within a component or function. See the [Macros](/ref/macro.md#using-macros) documentation for more information.

## See Also[​](#see-also "Direct link to See Also")

* [Message Extraction Guide](/guides/message-extraction.md)
* [Pluralization Guide](/guides/plurals.md)
* [Dynamic Loading of Message Catalogs](/guides/dynamic-loading-catalogs.md)
* [Lingui CLI Reference](/ref/cli.md)


---

# React Apps Internationalization

In this tutorial, we'll learn how to add internationalization (i18n) to an existing React JS application. We'll focus on the most common patterns and best practices for using Lingui in React.

Example

If you're looking for a working solution, check out the [Examples](/examples.md) page. It contains several sample projects with the complete setup using Lingui and React.

It includes examples for *Create React App*, *React with Vite and Babel*, *React with Vite and SWC*, and more.

## Installing Lingui[​](#installing-lingui "Direct link to Installing Lingui")

1. Follow the [Installation and Setup](/installation.md) page for initial setup.
2. Install the [`@lingui/core`](/ref/core.md) and [`@lingui/react`](/ref/react.md) packages.

## Example Component[​](#example-component "Direct link to Example Component")

We're going to translate the following one-page mailbox application:

src/index.js

```
import React from "react";
import ReactDOM from "react-dom/client";
import Inbox from "./Inbox";

const App = () => <Inbox />;

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

src/Inbox.js

```
import React from "react";

export default function Inbox() {
  const messages = [{}, {}];
  const messagesCount = messages.length;
  const lastLogin = new Date();
  const markAsRead = () => {
    alert("Marked as read.");
  };

  return (
    <div>
      <h1>Message Inbox</h1>

      <p>
        See all <a href="/unread">unread messages</a>
        {" or "}
        <a onClick={markAsRead}>mark them</a> as read.
      </p>

      <p>
        {messagesCount === 1
          ? `There's ${messagesCount} message in your inbox.`
          : `There are ${messagesCount} messages in your inbox.`}
      </p>

      <footer>Last login on {lastLogin.toLocaleDateString()}.</footer>
    </div>
  );
}
```

This application is a simple mailbox with a header, a paragraph with a link and a button, another paragraph with a message count, and a footer with the last login date. We will use it as the basis for our tutorial.

## Setup[​](#setup "Direct link to Setup")

We will start translating the `Inbox` component right away, but we need to do one more step to set up our application.

Components need to read information about current language and message catalogs from the [`i18n`](/ref/core.md#i18n) instance. Lingui uses the [`I18nProvider`](/ref/react.md#i18nprovider) to pass the `i18n` instance to your React components.

Let's add all required imports and wrap our app inside [`I18nProvider`](/ref/react.md#i18nprovider):

src/index.js

```
import React from "react";
import ReactDOM from "react-dom/client";

import { i18n } from "@lingui/core";
import { I18nProvider } from "@lingui/react";
import { messages } from "./locales/en/messages";
import Inbox from "./Inbox";

i18n.load("en", messages);
i18n.activate("en");

const App = () => (
  <I18nProvider i18n={i18n}>
    <Inbox />
  </I18nProvider>
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

info

You might be wondering: how are we going to change the active language? That's what the [`I18n.load`](/ref/core.md#i18n.load) and [`i18n.activate`](/ref/core.md#i18n.activate) calls are for! However, we cannot change the language unless we have the translated message catalog. And to get the catalog, we first need to extract all messages from the source code.

## Introducing Internationalization[​](#introducing-internationalization "Direct link to Introducing Internationalization")

Now we're finally going to *translate* our application. Actually, we're not going to *translate* from one language to another right now. Instead, we're going to *prepare* our app for translation. This process is called *internationalization*.

Let's start with the basics - static messages. These messages don't have any variables, HTML or components inside. Just some text:

```
<h1>Message Inbox</h1>
```

To make this heading translatable, simply wrap it in the [`Trans`](/ref/macro.md#trans) macro:

```
import { Trans } from "@lingui/react/macro";

<h1>
  <Trans>Message Inbox</Trans>
</h1>;
```

Using JSX Macros is the easiest way to translate your React components. It handles translations of messages, including variables and other React components.

### Macros vs. Components[​](#macros-vs-components "Direct link to Macros vs. Components")

If you're wondering what [Macros](/ref/macro.md) are and the difference between macros and runtime components, here's a quick explanation.

In general, macros are executed at compile time and serve to transform the source code to make the message writing process easier. Under the hood, all JSX macros are transformed into the runtime component [`Trans`](/ref/react.md#trans) (imported from `@lingui/react`).

Below is a brief example demonstrating this transformation:

```
import { Trans } from "@lingui/react/macro";

<Trans>Hello {name}</Trans>;

// ↓ ↓ ↓ ↓ ↓ ↓

import { Trans } from "@lingui/react";

<Trans id="OVaF9k" message="Hello {name}" values={{ name }} />;
```

As you can see, the [`Trans`](/ref/react.md#trans) runtime component gets `id` and `message` props with a message in [ICU MessageFormat](/guides/message-format.md) syntax. We could write it manually, but it's just easier and shorter to write JSX as we're used to and let macros generate the message for us.

Bundle Size Impact

Another advantage of using macros is that all non-essential properties are excluded from the production build. This results in a significant reduction in the size footprint for internationalization:

```
// NODE_ENV=production
import { Trans } from "@lingui/react";

<Trans id="OVaF9k" values={{ name }} />;
```

### Extracting Messages[​](#extracting-messages "Direct link to Extracting Messages")

Back to our project. It's nice to use JSX and let macros generate messages under the hood. Let's check that it actually works correctly.

All messages from the source code must be extracted into external message catalogs. Message catalogs are interchange files between developers and translators. We're going to have one file per language.

info

Refer to the [Message Extraction](/guides/message-extraction.md) guide for more information about various message extraction concepts and strategies.

Let's switch to the command line for a moment. Execute the [`extract`](/ref/cli.md#extract) CLI command. If everything is set up correctly, you should see the extracted message statistics in the output:

```
> lingui extract

Catalog statistics:
┌──────────┬─────────────┬─────────┐
│ Language │ Total count │ Missing │
├──────────┼─────────────┼─────────┤
│ cs       │      1      │    1    │
│ en       │      1      │    1    │
└──────────┴─────────────┴─────────┘
```

As a result, we have two new files in the `locales` directory: `en/messages.po` and `cs/messages.po`. These files contain extracted messages from the source code.

Let's take a look at the Czech message catalog:

src/locales/cs/messages.po

```
msgid ""
msgstr ""
"POT-Creation-Date: 2021-07-22 21:44+0900\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=utf-8\n"
"Content-Transfer-Encoding: 8bit\n"
"X-Generator: @lingui/cli\n"
"Language: cs\n"

#: src/Inbox.js:12
msgid "Message Inbox"
msgstr ""
```

It contains the message we wrapped in the [`Trans`](/ref/macro.md#trans) macro. Let's add the Czech translation:

src/locales/cs/messages.po

```
#: src/Inbox.js:12
msgid "Message Inbox"
msgstr "Příchozí zprávy"
```

If we run the [`extract`](/ref/cli.md#extract) command again, we'll see that all the Czech messages have been translated:

```
> lingui extract

Catalog statistics:
┌──────────┬─────────────┬─────────┐
│ Language │ Total count │ Missing │
├──────────┼─────────────┼─────────┤
│ cs       │      1      │    0    │
│ en       │      1      │    1    │
└──────────┴─────────────┴─────────┘
```

That's great! So how do we load it into your application? Lingui introduces the concept of compiled message catalogs. Before we load messages into our application, we need to compile them.

Use the [`compile`](/ref/cli.md#compile) command to do this:

```
> lingui compile

Compiling message catalogs…
Done!
```

If you look inside the `locales/<locale>` directory, you'll see that there is a new file for each locale: `messages.js`. This file contains the compiled message catalog.

tip

If you use TypeScript, you can add the `--typescript` flag to the `compile` command to produce compiled message catalogs with TypeScript types.

Let's load this file into our app and set active language to `cs`:

src/index.js

```
import React from "react";
import ReactDOM from "react-dom/client";

import { i18n } from "@lingui/core";
import { I18nProvider } from "@lingui/react";
import { messages as enMessages } from "./locales/en/messages";
import { messages as csMessages } from "./locales/cs/messages";
import Inbox from "./Inbox";

i18n.load({
  en: enMessages,
  cs: csMessages,
});
i18n.activate("cs");

const App = () => (
  <I18nProvider i18n={i18n}>
    <Inbox />
  </I18nProvider>
);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
```

When we run the app, we see the inbox header is translated into Czech.

tip

Alternatively, you can load catalogs dynamically using the [`@lingui/loader`](/ref/loader.md) or [`@lingui/vite-plugin`](/ref/vite-plugin.md) without the need to import compiled messages manually.

### Summary of Basic Workflow[​](#summary-of-basic-workflow "Direct link to Summary of Basic Workflow")

Let's go through the workflow again:

1. Add an [`I18nProvider`](/ref/react.md#i18nprovider), this component provides the active language and catalog(s) to other components.
2. Wrap messages in the [`Trans`](/ref/macro.md#trans) macro.
3. Run [`extract`](/ref/cli.md#extract) command to generate message catalogs.
4. Translate message catalogs (send them to translators usually).
5. Run [`compile`](/ref/cli.md#compile) to create runtime catalogs.
6. Load runtime catalog.
7. Profit! 🎉

It's not necessary to extract/translate messages one by one. This is usually done in batches. When you finish your work or PR, run [`extract`](/ref/cli.md#extract) to generate the latest message catalogs, and before building the application for production, run [`compile`](/ref/cli.md#compile).

## Formatting[​](#formatting "Direct link to Formatting")

Let's move on to another paragraph in our project. The following paragraph has some variables, some HTML and components inside:

```
<p>
  See all <a href="/unread">unread messages</a>
  {" or "}
  <a onClick={markAsRead}>mark them</a> as read.
</p>
```

Although it looks complex, there's really nothing special here. Just wrap the content of the paragraph in [`Trans`](/ref/macro.md#trans) and let the macro do the magic:

```
<p>
  <Trans>
    See all <a href="/unread">unread messages</a>
    {" or "}
    <a onClick={markAsRead}>mark them</a> as read.
  </Trans>
</p>
```

Let's see how this message actually looks in the message catalog. Run the [`extract`](/ref/cli.md#extract) command and take a look at the message:

```
#: src/Inbox.js:20
msgid "See all <0>unread messages</0> or <1>mark them</1> as read."
msgstr ""
```

You may notice that components and html tags are replaced with indexed tags (`<0>`, `<1>`). This is a little extension to the ICU MessageFormat which allows rich-text formatting inside translations. Components and their props remain in the source code and don't scare our translators. Also, in case we change a `className`, we don't need to update our message catalogs.

### JSX to MessageFormat Transformations[​](#jsx-to-messageformat-transformations "Direct link to JSX to MessageFormat Transformations")

At first glance, these transformations might seem somewhat unconventional; however, they are straightforward, intuitive, and align well with React principles. There is no need to focus on MessageFormat, as the library handles its creation for us. We can write our components as we typically would and simply wrap the text in the [`Trans`](/ref/macro.md#trans) macro.

Let's see some examples with MessageFormat equivalents:

```
<Trans>Hello {name}</Trans>
// Hello {name}
```

Any expressions are allowed, not just simple variables. The only difference is, only the variable name will be included in the extracted message:

* Any expression -> positional argument:

  ```
  <Trans>Hello {user.name}</Trans>
  // Hello {0}
  ```

* Object, arrays, function calls -> positional argument:

  ```
  <Trans>The random number is {Math.rand()}</Trans>
  // The random number is {0}
  ```

* Components might get tricky, but like we saw, it's really easy:

  ```
  <Trans>
    Read <a href="/more">more</a>.
  </Trans>
  // Read <0>more</0>.
  ```

  ```
  <Trans>
    Dear Watson,
    <br />
    it's not exactly what I had in my mind.
  </Trans>
  // Dear Watson,<0/>it's not exactly what I had in my mind.
  ```

caution

Try to keep your messages simple and avoid complex expressions. During extraction, these expressions will be replaced by placeholders, resulting in a lack of context for translators. There is also a special rule in Lingui [ESLint Plugin](/ref/eslint-plugin.md) to catch these cases: [`no-expression-in-message`](https://github.com/lingui/eslint-plugin/blob/main/docs/rules/no-expression-in-message.md).

### Dates and Numbers[​](#dates-and-numbers "Direct link to Dates and Numbers")

Take a look at the message in the footer of our component. It is a bit special because it contains a date:

```
<footer>Last login on {lastLogin.toLocaleDateString()}.</footer>
```

Dates (as well as numbers) are formatted differently in different languages, but we don't have to do this manually. The heavy lifting is done by the [`Intl` object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl), we'll just use the [`i18n.date()`](/ref/core.md#i18n.date) function.

The `i18n` object can be accessed with the [`useLingui`](/ref/react.md#uselingui) hook:

src/Inbox.js

```
import { useLingui, Trans } from "@lingui/react/macro";

export default function Inbox() {
  const { i18n } = useLingui();

  return (
    <div>
      <footer>
        <Trans>Last login on {i18n.date(lastLogin)}.</Trans>
      </footer>
    </div>
  );
}
```

This will format the date using the conventional format for the active language. To format numbers, use the [`i18n.number()`](/ref/core.md#i18n.number) function.

### Message ID[​](#message-id "Direct link to Message ID")

At this point, we'll explain what the message ID is and how to set it manually. Translators work with *message catalogs*. No matter what format we use, it's just a mapping of a message ID to the translation.

Here's an example of a simple message catalog in **Czech** language:

| Message ID | Translation |
| ---------- | ----------- |
| Monday     | Pondělí     |
| Tuesday    | Úterý       |
| Wednesday  | Středa      |

... and the same catalog in **French** language:

| Message ID | Translation |
| ---------- | ----------- |
| Monday     | Lundi       |
| Tuesday    | Mardi       |
| Wednesday  | Mercredi    |

The message ID is *what all catalogs have in common* – "Lundi" and "Pondělí" represent the same message in different languages.

There are two approaches for creating a message ID:

* Automatically generated from message (e.g. `Monday`) and context, if available.
* Explicit message ID set by the developer (e.g. `days.monday`).

info

Refer to the [Explicit vs Generated IDs](/guides/explicit-vs-generated-ids.md) guide for more information about the pros and cons of each approach.

## Plurals[​](#plurals "Direct link to Plurals")

Let's take a closer look at the following code in our component:

```
<p>
  {messagesCount === 1
    ? `There's ${messagesCount} message in your inbox.`
    : `There are ${messagesCount} messages in your inbox.`}
</p>
```

This message is a bit special, because it depends on the value of the `messagesCount` variable. Most languages use different forms of words when describing quantities - this is called [pluralization](/guides/plurals.md).

What's tricky is that different languages use different number of plural forms. For example, English has only two forms - singular and plural - as we can see in the example above. However, Czech language has three plural forms. Some languages have up to 6 plural forms and some don't have plurals at all!

info

Lingui uses `Intl.PluralRules` which is supported in [every modern browser](https://caniuse.com/intl-pluralrules) and can be polyfilled for older. So you don't need to setup anything special.

### English Plural Rules[​](#english-plural-rules "Direct link to English Plural Rules")

How do we know which plural form we should use? It's very simple: we, as developers, only need to know plural forms of the language we use in our source. Our component is written in English, so looking at [English plural rules](http://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html#en) we'll need just two forms:

`one`

> Singular form

`other`

> Plural form

We don't need to select these forms manually. We'll use [`Plural`](/ref/macro.md#plural-1) component, which takes a `value` prop and based on the active language, selects the right plural form:

```
import { Plural } from "@lingui/react/macro";

<p>
  <Plural value={messagesCount} one="There's # message in your inbox" other="There are # messages in your inbox" />
</p>;
```

This component will render `There's 1 message in your inbox` when `messageCount = 1` and `There are # messages in your inbox` for any other values of `messageCount`. `#` is a placeholder, which is replaced with `value`.

Let's run the [`extract`](/ref/cli.md#extract) command to see the extracted message:

```
{messagesCount, plural,
  one {There's # message in your inbox}
  other {There are # messages in your inbox}
}
```

In the catalog, you'll see the message in a single line. Here we have wrapped it to make it more readable.

### Beware of Zeroes\![​](#beware-of-zeroes "Direct link to Beware of Zeroes!")

Just a short detour, because it's a common misunderstanding. You may wonder why the following code doesn't work as expected:

```
<p>
  <Plural
    value={messagesCount}
    zero="There are no messages"
    one="There's # message in your inbox"
    other="There are # messages in your inbox"
  />
</p>
```

This component will render `There are 0 messages in your inbox` for `messagesCount = 0`. Why so? Because English doesn't have `zero` plural form. Looking at [English plural rules](http://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html#en), it's:

| N | Form                  |
| - | --------------------- |
| 0 | other                 |
| 1 | one                   |
| n | other (anything else) |

However, decimal numbers (even `1.0`) always use the `other` form:

```
There are 0.0 messages in your inbox.
```

### Exact Forms[​](#exact-forms "Direct link to Exact Forms")

Going back to our example, what if we specifically want to display `There are no messages` when `messagesCount = 0`? This is where exact forms come in handy:

```
<p>
  <Plural
    value={messagesCount}
    _0="There are no messages"
    one="There's # message in your inbox"
    other="There are # messages in your inbox"
  />
</p>
```

tip

MessageFormat allows exact forms, like `=0`. However, React props can't start with `=` and can't be numbers either, so we need to write `_N` instead of `=0`.

It works with any number, allowing for extensive customization as follows:

```
<p>
  <Plural
    value={messagesCount}
    _0="There are no messages"
    _1="There's one message in your inbox"
    _2="There are two messages in your inbox, that's not much!"
    other="There are # messages in your inbox"
  />
</p>
```

Exact matches always take precedence over plural forms.

### Variables and Components[​](#variables-and-components "Direct link to Variables and Components")

Let's go back to our original pluralized message:

```
<p>
  <Plural value={messagesCount} one="There's # message in your inbox" other="There are # messages in your inbox" />
</p>
```

To include variables or components within messages, simply wrap them in the [`Trans`](/ref/macro.md#trans) macro or use template literals (for example, with a variable `name`):

```
<p>
  <Plural
    value={messagesCount}
    one={`There's # message in your inbox, ${name}`}
    other={
      <Trans>
        There are <strong>#</strong> messages in your inbox, {name}
      </Trans>
    }
  />
</p>
```

Nested macros, components, variables, and expressions are all supported, providing the flexibility needed for any use case.

## Internationalization Outside of React[​](#internationalization-outside-of-react "Direct link to Internationalization Outside of React")

So far, we have learned how to translate strings within a JSX element. However, what if we need to translate content that is outside JSX or pass a translation as a prop to another component?

In our example, we have the following code:

```
const markAsRead = () => {
  alert("Marked as read.");
};
```

To translate it, we will use the [`useLingui`](/ref/macro.md#uselingui) macro hook:

```
import { useLingui } from "@lingui/react/macro";

const { t } = useLingui();

const markAsRead = () => {
  alert(t`Marked as read.`);
};
```

Now the `Marked as read.` message would be picked up by the extractor, and available for translation in the catalog.

You could also pass variables and use any other macro in the message:

```
const { t } = useLingui();

const markAsRead = () => {
  const userName = "User1234";
  alert(t`Hello ${userName}, your messages marked as read!`);
};
```

tip

You can also use this approach to translate element attributes, such as `alt` in an `img` tag:

```
import { useLingui } from "@lingui/react/macro";

export default function ImageWithCaption() {
  const { t } = useLingui();

  return <img src="..." alt={t`Image caption`} />;
}
```

caution

All Core Macros cannot be used at the module level. They must be used within a component or function. See the [Macros](/ref/macro.md#using-macros) documentation for more information.

## Review[​](#review "Direct link to Review")

After all modifications, the final i18n-ready component looks like this:

src/Inbox.js

```
import React from "react";
import { Trans, Plural, useLingui } from "@lingui/react/macro";

export default function Inbox() {
  const { i18n, t } = useLingui();
  const messages = [{}, {}];
  const messagesCount = messages.length;
  const lastLogin = new Date();
  const markAsRead = () => {
    alert(t`Marked as read.`);
  };

  return (
    <div>
      <h1>
        <Trans>Message Inbox</Trans>
      </h1>

      <p>
        <Trans>
          See all <a href="/unread">unread messages</a>
          {" or "}
          <a onClick={markAsRead}>mark them</a> as read.
        </Trans>
      </p>

      <p>
        <Plural
          value={messagesCount}
          one="There's # message in your inbox"
          other="There are # messages in your inbox"
        />
      </p>

      <footer>
        <Trans>Last login on {i18n.date(lastLogin)}.</Trans>
      </footer>
    </div>
  );
}
```

That's it for this tutorial! For more details, see the reference documentation or check out additional tutorials. Happy Internationalizing!

## See Also[​](#see-also "Direct link to See Also")

* [React Server Components Tutorial](/tutorials/react-rsc.md)
* [React Native i18n Tutorial](/tutorials/react-native.md)
* [`@lingui/react` Reference](/ref/react.md)


---

# React Native Apps Internationalization

In this tutorial, we'll learn how to add internationalization to an existing application in React Native.

The React Native tutorial is similar to the one for [React](/tutorials/react.md) and we highly recommend you read that one first because it goes into greater detail on many topics. Here, we will only cover parts that are relevant for React Native.

Example

If you're looking for a working solution, check out the [React Native example](https://github.com/lingui/js-lingui/tree/main/examples/react-native). This example application shows a complete setup using Lingui and React Native.

This tutorial assumes you use Lingui >= 5.0 and React Native >=0.76 or Expo >=52, with the Hermes JavaScript Engine.

`@lingui/core` depends on several APIs exposed by the [`Intl` object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl). Support of the `Intl` object can vary across React Native and OS versions. If some `Intl` feature is not supported by your runtime, you can [polyfill it](#polyfilling-intl-apis).

## Installing Lingui[​](#installing-lingui "Direct link to Installing Lingui")

1. Follow the [Installation and Setup](/installation.md?transpiler=babel) page for initial setup (for Babel).
2. Install the [`@lingui/core`](/ref/core.md) and [`@lingui/react`](/ref/react.md) packages.
3. *(optional)* Install and configure the [`@lingui/metro-transformer`](/ref/metro-transformer.md) package that enables Metro to compile `.po` files on the fly.

Warning

With the dependencies installed and set up, before running your app, please clear your Metro bundler cache with `npx expo start -c` or `npx react-native start --reset-cache` (if you do not use Expo).

## Polyfilling Intl APIs[​](#polyfilling-intl-apis "Direct link to Polyfilling Intl APIs")

React Native's JS engine may not support all `Intl` features out of the box. As of 08/2024, we need to polyfill [`Intl.Locale`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/Locale) using [`@formatjs/intl-locale`](https://formatjs.io/docs/polyfills/intl-locale/) and [`Intl.PluralRules`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/PluralRules) using [`@formatjs/intl-pluralrules`](https://formatjs.io/docs/polyfills/intl-pluralrules). Please note that importing the `Intl` polyfills can significantly increase the amount of JS that needs to be `require`d by your app. At the same time, modern i18n libraries rely on its presence.

Follow the polyfill installation instructions before proceeding further. Import polyfills from `/polyfill-force` to avoid [slow initialization time on low-end devices](https://github.com/formatjs/formatjs/issues/4463).

## Example Component[​](#example-component "Direct link to Example Component")

We're going to translate the following contrived example:

```
import React from "react";
import { StyleSheet, Text, View, Alert, SafeAreaView, Button } from "react-native";

export const AppRoot = () => {
  const [messages, setMessages] = useState<string[]>([]);

  const markAllAsRead = () => {
    Alert.alert("", "Do you want to set all your messages as read?", [
      {
        text: "OK",
        onPress: () => {
          setMessages([]);
        },
      },
    ]);
  };

  return (
    <Inbox
      markAsRead={markAllAsRead}
      messages={messages}
      addMessage={() => {
        setMessages((msgs) => msgs.concat([`message # ${msgs.length + 1}`]));
      }}
    />
  );
};

const Inbox = ({ messages, markAsRead }) => {
  const messagesCount = messages.length;

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.container2}>
        <Text style={styles.heading}>Message Inbox</Text>

        <Button onPress={markAsRead} title="Mark all messages as read" />

        <Text>
          {messagesCount === 1
            ? `There's {messagesCount} message in your inbox.`
            : `There are ${messagesCount} messages in your inbox.`}
        </Text>
        {/* additional code for adding messages, etc.*/}
      </View>
    </SafeAreaView>
  );
};
```

As you can see, it's a simple mailbox application with only one screen.

## Internationalization in React (Native)[​](#internationalization-in-react-native "Direct link to Internationalization in React (Native)")

TL;DR

There are several ways to render translations: You may use the [`Trans`](/ref/react.md#trans) component or the [`useLingui`](/ref/react.md#uselingui) hook together with the [`t`](/ref/macro.md#t) or [`msg`](/ref/macro.md#definemessage) macros. When you change the active locale or load new messages, all components that consume the Lingui context provided by [`I18nProvider`](/ref/react.md#i18nprovider) will re-render, making sure the UI shows the correct translations.

Not surprisingly, this part isn't too different from the [React tutorial](/tutorials/react.md).

First, we need to wrap our app with [`I18nProvider`](/ref/react.md#i18nprovider) and then we can use the [`Trans`](/ref/macro.md#trans) macro to translate the screen heading:

```
import { I18nProvider, TransRenderProps } from "@lingui/react";
import { Trans } from "@lingui/react/macro";
import { i18n } from "@lingui/core";
import { Text } from "react-native";

i18n.loadAndActivate({ locale: "en", messages });

const DefaultComponent = (props: TransRenderProps) => {
  return <Text>{props.children}</Text>;
};

<I18nProvider i18n={i18n} defaultComponent={DefaultComponent}>
 <AppRoot />
</I18nProvider>

// later in the React element tree:
<Text style={styles.heading}><Trans>Message Inbox</Trans></Text>
```

Hint

We're importing the default `i18n` object from `@lingui/core`. Read more about the `i18n` object in the [reference](/ref/core.md).

Translating the heading is done. Now, let's translate the `title` prop in the `<Button title="mark messages as read" />` element. In this case, `Button` expects to receive a `string`, so we cannot use the [`Trans`](/ref/macro.md#trans) macro here!

The solution is to use the `t` macro which we can obtain from the `useLingui` hook. We use it like this to get a translated string:

```
import { useLingui } from '@lingui/react/macro';

const { t } = useLingui();
...
<Button title={t`this will be translated and rerendered with locale changes`}/>
```

Under the hood, [`I18nProvider`](/ref/react.md#i18nprovider) takes the instance of the `i18n` object and passes it to `Trans` components through React context. `I18nProvider` will update the context value (which then rerenders components that consume the provided context value) when locale or message catalogs are updated.

The `Trans` component uses the `i18n` instance to get the translations from it. If we cannot use `Trans`, we can use the `useLingui` hook to get hold of the `i18n` instance ourselves and get the translations from there.

The interplay of `I18nProvider` and `useLingui` is shown in the following simplified example:

```
import { I18nProvider } from "@lingui/react";
import { Trans, useLingui } from "@lingui/react/macro";
import { i18n } from "@lingui/core";

<I18nProvider i18n={i18n}>
  <AppRoot />
</I18nProvider>;
//...
const Inbox = ({ markAsRead }) => {
  const { t } = useLingui();
  return (
    <View>
      <Text style={styles.heading}>
        <Trans>Message Inbox</Trans>
      </Text>
      <Button onPress={markAsRead} title={t`Mark messages as read`} />
    </View>
  );
};
```

## Internationalization Outside of React[​](#internationalization-outside-of-react "Direct link to Internationalization Outside of React")

Until now, we have covered the [`Trans`](/ref/react.md#trans) macro and the [`useLingui`](/ref/react.md#uselingui) hook. Using them will make sure our components are always in sync with the currently active locale and message catalog.

However, you may want to show localized strings outside of React, for example when you want to show an Alert from some business logic code.

In that case you'll also need access to the `i18n` object, but you don't need to pass it around from some React component. By default, Lingui uses an `i18n` object instance that you can import as follows:

```
import { i18n } from "@lingui/core";
```

This instance is the source of truth for the active locale. For string constants that will be translated at runtime, use the [`msg`](/ref/macro.md#definemessage) macro as follows:

```
const deleteTitle = msg`Are you sure to delete this?`
...
const showDeleteConfirmation = () => {
  Alert.alert(i18n._(deleteTitle))
}
```

## Changing the Active Locale[​](#changing-the-active-locale "Direct link to Changing the Active Locale")

The last remaining piece of the puzzle is changing the active locale. The `i18n` object exposes [`i18n.loadAndActivate()`](/ref/core.md#i18n.loadAndActivate) for that. Call the method and the [`I18nProvider`](/ref/react.md#i18nprovider) will re-render the translations. It all becomes clear when you take a look at the [final code](https://github.com/lingui/js-lingui/tree/main/examples/react-native/src/MainScreen.tsx#L29).

However, we don't recommend that you change the locale like this in mobile apps, as it can cause conflicts in how your app ui is localized. This is further [explained here](https://www.youtube.com/live/uLicTDG5hSs?feature=share\&t=9088).

## Choosing the Default Locale[​](#choosing-the-default-locale "Direct link to Choosing the Default Locale")

Lingui does not ship with functionality that would allow you to determine the best locale you should activate by default.

Instead, please refer to [Expo localization](https://docs.expo.dev/versions/latest/sdk/localization/#localizationgetlocales) or [react-native-localize](https://github.com/zoontek/react-native-localize#getlocales). Both packages will provide you with information about the locales that the user prefers. Combining that information with the locales that your app supports will give you the locale you should use by default.

## Rendering and Styling of Translations[​](#rendering-and-styling-of-translations "Direct link to Rendering and Styling of Translations")

As described in the [reference](/ref/react.md#rendering-translations), by default, translation components render translation as text without a wrapping tag. In React Native though, all text must be wrapped in the `Text` component. This means we would need to use the [`Trans`](/ref/macro.md#trans) component like this:

```
<Text>
  <Trans>Message Inbox</Trans>
</Text>
```

You'll surely agree the `Text` component looks a little redundant. That's why the [`I18nProvider`](/ref/react.md#i18nprovider) component accepts a `defaultComponent` prop. Just supply the `Text` component as the `defaultComponent` prop and the previous example can be simplified to:

```
<Trans>Message Inbox</Trans>
```

Alternatively, you may override the default locally on the i18n components, using the `render` or `component` props, as documented in the [reference](/ref/react.md#rendering-translations). Use them to apply styling to the rendered string.

## Nesting Components[​](#nesting-components "Direct link to Nesting Components")

The [`Trans`](/ref/macro.md#trans) macro and `Text` component may be nested, for example to achieve the effect shown in the picture. This is thanks to how React Native [handles nested text](https://facebook.github.io/react-native/docs/text#nested-text).

![image](/assets/images/rn-component-nesting-333bb3aa1e3e03a1e3e29035c93fcb4f.png)

This can be achieved by the following code:

```
<Trans>
  <Text style={{ fontSize: 20 }}>
    <Text>Concert of </Text>
    <Text style={{ color: "green" }}>Green Day</Text>
    <Text style={{ fontWeight: "bold" }}> tonight!</Text>
  </Text>
</Trans>
```

The extracted string for translation will look like this:

`"<0><1>Concert of </1><2>Green Day</2><3> tonight!</3></0>"`

The important point here is that the sentence isn't broken into pieces but remains together - that will allow the translator to deliver a quality result.

## See Also[​](#see-also "Direct link to See Also")

* [React i18n Tutorial](/tutorials/react.md)
* [Message Extraction Guide](/guides/message-extraction.md)
* [`@lingui/react` Reference](/ref/react.md)
* [Lingui CLI Reference](/ref/cli.md)
* [Localizing React Native apps talk from React Native EU 2022](https://www.youtube.com/live/uLicTDG5hSs?feature=share\&t=7512)

***

This guide originally authored and contributed in full by [Vojtech Novak](https://twitter.com/vonovak).


---

# Lingui with React Server Components

Lingui provides support for React Server Components (RSC) as of v4.10.0. In this tutorial, we'll learn how to add internationalization to an application with the Next.js [App Router](https://nextjs.org/docs/app). However, the same principles are applicable to any RSC-based solution.

Example

There's a working example available [here](https://github.com/lingui/js-lingui/tree/main/examples/nextjs-swc). We will make references to the important parts of it throughout the tutorial. The example is more complete than this tutorial.

The example uses both Pages Router and App Router, so you can see how to use Lingui with both in [this commit](https://github.com/lingui/js-lingui/pull/1944/commits/100fc74abb49cff677f4b1cac1dfd5da60262b67).

Before going further, please follow the [Installation and Setup](/installation.md?transpiler=swc) instructions (for SWC or Babel depending on which you use - most likely it's SWC). You may also need to configure your `tsconfig.json` according to [this visual guide](https://twitter.com/mattpocockuk/status/1724462050288587123). This is so that TypeScript understands the values exported from `@lingui/react` package.

### Adding i18n Support to Next.js[​](#adding-i18n-support-to-nextjs "Direct link to Adding i18n Support to Next.js")

Firstly, your Next.js app needs to be ready for routing and rendering of content in multiple languages. This is done through the middleware (see the [example app's middleware](https://github.com/lingui/js-lingui/blob/main/examples/nextjs-swc/src/middleware.ts)). Please read the [official Next.js docs](https://nextjs.org/docs/app/building-your-application/routing/internationalization) for more information.

After configuring the middleware, make sure your page and route files are moved from `app` to `app/[lang]` folder (example: `app/[lang]/layout.tsx`). This enables the Next.js router to dynamically handle different locales in the route, and forward the `lang` parameter to every layout and page.

### Next.js Config[​](#nextjs-config "Direct link to Next.js Config")

Secondly, add the `swc-plugin` to the `next.config.js`, so that you can use [Lingui Macros](/ref/macro.md).

next.config.js

```
/** @type {import('next').NextConfig} */
module.exports = {
  // to use Lingui macros
  experimental: {
    swcPlugins: [["@lingui/swc-plugin", {}]],
  },
};
```

### Setup with Server Components[​](#setup-with-server-components "Direct link to Setup with Server Components")

With Lingui, the experience of localizing React is the same in client and server components: `Trans` and `useLingui` can be used identically in both worlds, even though internally there are two implementations.

Under the hood

Translation strings, one way or another, are obtained from an [I18n](/ref/core.md) object instance. In client components, this instance is passed around using React context. Because context is not available in Server components, instead [`cache`](https://react.dev/reference/react/cache) is used to maintain an I18n instance for each request.

To make Lingui work in both server and client components, we need to take the `lang` prop which Next.js passes to our layouts and pages, and create a corresponding instance of the I18n object. We then make it available to the components in our app. This is a 2-step process:

1. given `lang`, take an I18n instance and store it in the [`cache`](https://react.dev/reference/react/cache) so it can be used server-side
2. given `lang`, take an I18n instance and make it available to client components via `I18nProvider`

This is how step (1) can be implemented:

src/app/\[lang]/layout.tsx

```
import { setI18n } from "@lingui/react/server";
import { getI18nInstance } from "./appRouterI18n";
import { LinguiClientProvider } from "./LinguiClientProvider";

type Props = {
  params: {
    lang: string;
  };
  children: React.ReactNode;
};

export default function RootLayout({ params: { lang }, children }: Props) {
  const i18n = getI18nInstance(lang); // get a ready-made i18n instance for the given locale
  setI18n(i18n); // make it available server-side for the current request

  return (
    <html lang={lang}>
      <body>
        <LinguiClientProvider initialLocale={lang} initialMessages={i18n.messages}>
          <YourApp />
        </LinguiClientProvider>
      </body>
    </html>
  );
}
```

Step (2) is implemented in `LinguiClientProvider`, which is a client component:

LinguiClientProvider.tsx

```
"use client";

import { I18nProvider } from "@lingui/react";
import { type Messages, setupI18n } from "@lingui/core";
import { useState } from "react";

export function LinguiClientProvider({
  children,
  initialLocale,
  initialMessages,
}: {
  children: React.ReactNode;
  initialLocale: string;
  initialMessages: Messages;
}) {
  const [i18n] = useState(() => {
    return setupI18n({
      locale: initialLocale,
      messages: { [initialLocale]: initialMessages },
    });
  });
  return <I18nProvider i18n={i18n}>{children}</I18nProvider>;
}
```

tip

Why are we not passing the I18n instance directly from `RootLayout` to the client via `LinguiClientProvider`? It's because the I18n object isn't serializable, and cannot be passed from server to client.

Lastly, there's the `appRouterI18n.ts` file, which is only executed on server and holds one instance of I18n object for each locale of our application. See [here](https://github.com/lingui/js-lingui/blob/main/examples/nextjs-swc/src/appRouterI18n.ts) how it's implemented in the example app.

### Rendering Translations in Server and Client Components[​](#rendering-translations-in-server-and-client-components "Direct link to Rendering Translations in Server and Client Components")

Below you can see an example of a React component. This component can be rendered **both with RSC and on client**. This is great if you're migrating a Lingui-based project from pages router to App Router because you can keep the same components working in both worlds.

In fact, if you swapped the html tags for their more universal alternatives, this component could also be used in React Native.

app/\[lang]/components/SomeComponent.tsx

```
import { Trans, useLingui } from "@lingui/react/macro";

export function SomeComponent() {
  const { t } = useLingui();
  return (
    <div>
      <p>
        <Trans>Some Item</Trans>
      </p>
      <p>{t`Other Item`}</p>
    </div>
  );
}
```

As you may recall, hooks are not supported in RSC, so you might be surprised that this works. Under RSC, `useLingui` is actually not a hook but a simple function call which reads from the React `cache` mentioned above.

The [RSC implementation](https://github.com/lingui/js-lingui/blob/ec49d0cc53dbc4f9e0f92f0edcdf59f3e5c1de1f/packages/react/src/index-rsc.ts#L12) of `useLingui` uses `getI18n`, which is another way to obtain the I18n instance on the server.

### Pages, Layouts and Lingui[​](#pages-layouts-and-lingui "Direct link to Pages, Layouts and Lingui")

There's one last caveat: in a real-world app, you will need to localize many pages, and layouts. Because of the way the App Router is designed, the `setI18n` call needs to happen not only in layouts, but also in pages. Read more in:

* [Why do nested layouts/pages render before their parent layouts?](https://github.com/vercel/next.js/discussions/53026)
* [On navigation, layouts preserve state and do not re-render](https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts#layouts)

This means you need to repeat the `setI18n` in every page and layout. Luckily, you can easily factor it out into a simple function call, or create a HOC with which you'll wrap pages and layouts [as seen here](https://github.com/lingui/js-lingui/blob/main/examples/nextjs-swc/src/initLingui.tsx). Please let us know if there's a known better way.

### Changing the Active Language[​](#changing-the-active-language "Direct link to Changing the Active Language")

Most likely, your users will not need to change the language of the application because it will render in their preferred language (obtained from the `accept-language` header in the [middleware](https://github.com/lingui/js-lingui/blob/2f1c1c3ae9e079c1c0e1a2ff617b1d0775af3170/examples/nextjs-swc/src/middleware.ts#L30)), or with a fallback.

To change language, redirect users to a page with the new locale in the url. We do not recommend [dynamic](/guides/dynamic-loading-catalogs.md) switching because server-rendered locale-dependent content would become stale.

### Static Rendering Pitfall[​](#static-rendering-pitfall "Direct link to Static Rendering Pitfall")

Next.js can use [static rendering](https://nextjs.org/docs/app/building-your-application/rendering/server-components#static-rendering-default) where it renders your pages only once at build time and then serves them to all users.

To ensure static rendering takes into account the supported locales, implement [generateStaticParams](https://nextjs.org/docs/app/api-reference/functions/generate-static-params) which will build the content for all locales.

It's important that you do not create any locale-dependent strings at a place in the app where locale may not be initialized correctly at build time. This could result in the content being generated only for one locale, and for this reason we do not recommend using the global i18n object in such scenarios. For example:

```
import { i18n } from "@lingui/core";
import { t } from "@lingui/core/macro";
// 😰 if this code runs at build time, it'll always be in the locale
// which the imported global i18n object had at that time
const immutableGreeting = t(i18n)`Hello World`;

// ✅ this component will be statically rendered for each locale
// (specified with `generateStaticParams`)
export default function SomePage() {
  return (
    <>
      <Trans>Hello world</Trans> {/* this is fine */}
    </>
  );
}
```

Read more about [Lazy Translation](/guides/lazy-translations.md) to see how to handle translation defined on the module level.

## See Also[​](#see-also "Direct link to See Also")

* [React i18n Tutorial](/tutorials/react.md)
* [`@lingui/react` Reference](/ref/react.md)


---


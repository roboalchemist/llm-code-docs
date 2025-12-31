# Source: https://lingui.dev/ref/conf.md

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

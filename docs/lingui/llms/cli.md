# Source: https://lingui.dev/ref/cli.md

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
    [--output-prefix <prefix>]
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

#### `--output-prefix <prefix>`[​](#compile-output-prefix "Direct link to compile-output-prefix")

Adds a custom string to the beginning of compiled message catalogs (a header/prefix). By default, Lingui adds `/*eslint-disable*/` to prevent linters from reporting issues in generated files.

Use this option for other tools that rely on header directives (e.g., different linters, coverage tools, or formatters). Provide the full prefix exactly as it should appear in the output.

**Default value:** `/*eslint-disable*/`

**Examples:**

```
# For Oxlint
lingui compile --output-prefix "/*oxlint-disable*/"

# For Biome
lingui compile --output-prefix "/*biome-ignore lint: auto-generated*/"

# For no prefix at all
lingui compile --output-prefix ""
```

The generated file header will look like:

```
/*your-prefix-here*/ export const messages = JSON.parse("{}");
```

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

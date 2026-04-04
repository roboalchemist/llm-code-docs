# Vale Documentation

Source: https://docs.vale.sh/llms-full.txt

---

# Introduction

Learn about what Vale is (and isn't).

Vale is a command-line tool that brings code-like linting to prose. Vale is cross-platform (Windows, macOS, and Linux), written in Go, and available on GitHub.

> *Linting* is the process of ensuring that written work (source code or prose) adheres to a particular style—for example, Python’s [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide (code) or the Google’s [Documentation Style Guide](https://developers.google.com/style/) (prose).

Before getting into the details of what makes Vale useful, there’s one point that needs clarification: **Vale is not a general-purpose writing aid**.

It doesn’t teach you *how* to write; it’s a tool *for* writers.

More specifically, Vale focuses (primarily) on the style of writing rather than its grammatical correctness—making it fundamentally different from, for example, Grammarly.

![A diagram demonstrating Vale's purpose.](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/BiOoKinfNDgQpiqDHF8e/flow.png)

In other words, Vale focuses on ensuring consistency across multiple authors (according to customizable guidelines) rather than the general “correctness” of a single author’s work.

This distinction is particularly important to understand because Vale doesn’t offer any of its own advice. Instead, it offers a framework for creating and enforcing [custom rules](https://docs.vale.sh/topics/styles). Its approach is much more similar to code linters than it is to traditional grammar checkers.

## [Your style, our editor](#your-style-our-editor)

One of Vale’s most important features is its ability to support external styles through its extension system, which only requires some familiarity with the YAML file format (and, optionally, regular expressions).

![A diagram comparing Vale to other tools.](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/dKhZPW18Q1bWZIJxCi1E/output.png)

To get a better idea of how this works, let’s look at an example from the [Linode documentation](https://github.com/linode/docs/blob/master/ci/vale/styles/Linode/Terms.yml):

{% code title="Terms.yml" %}

```yaml
# `extends` specifies the extension point you're using. Here, we're
# using `substitution` to ensure correct usage of some technical and
# brand-specifc terminology.
extends: substitution
# `message` allows you to customize the output shown to your users.
message: Use '%s' instead of '%s'.
# We're setting this rule's severity to `error`, which will cause
# CI builds to fail.
level: error
# We're using case-insensitive patterns.
ignorecase: true
swap:
  "(?:LetsEncrypt|Let's Encrypt)": Let's Encrypt
  'node[.]?js': Node.js
  'Post?gr?e(?:SQL)': PostgreSQL
  'java[ -]?scripts?': JavaScript
  linode cli: Linode CLI
  linode manager: Linode Manager
  linode: Linode
  longview: Longview
  nodebalancer: NodeBalancer
```

{% endcode %}

In the above example, we’ve defined a few terms that have a particular capitalization style. If Vale finds an instance of a term that matches a pattern on the left of swap (case-insensitive) but doesn’t exactly match the value on the right, it issues an error. So, for example, `Nodebalancer`, `nodebalancer` or any other variation that doesn’t exactly match `NodeBalancer` will be flagged as an error.

While this example may appear quite simple, it’s possible to achieve fairly high coverage on complete editorial style guides. Check out the [Explorer](https://vale.sh/explorer) for more examples.

## [Syntax- and context-aware linting](#syntax--and-context-aware-linting)

Another feature that separates Vale from other linters is its ability to understand its input at both a syntactic and contextual level.

![A diagram showcases Vale's ability to understand markup.](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/UzufH69nB24NtdtZOvU5/syntax.png)

This level of understanding gives you fine-grained control over the linting process, including the ability to limit rules to certain sections (e.g., only headings) or ignore sections entirely (block and inline code are ignored by default).

Additionally, since Vale is built on top of an NLP library, you can also target specific segments of text—allowing you to, for example, warn about paragraphs that exceed a certain number of words or sentences that end with prepositions.

## [Tech stack](#tech-stack)

Vale is a 100% open-source, MIT-licensed project that consists of multiple parts:

| Name                                                      | Tech       | Info                                                                                                         |
| --------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------ |
| [`vale`](https://github.com/errata-ai/vale)               | Go         | The main repository containing the Vale command-line interface.                                              |
| [`vale-ls`](https://github.com/errata-ai/vale-ls)         | Rust       | An implementation of the Language Server Protocol (LSP) for the Vale command-line tool.                      |
| [`vale.sh`](https://github.com/errata-ai/vale.sh)         | Svelte     | Website and documentation for the Vale CLI and related projects.                                             |
| [`vale-action`](https://github.com/errata-ai/vale-action) | TypeScript | The official GitHub Action for Vale -- install, manage, and run Vale with ease.                              |
| [`packages`](https://github.com/errata-ai/packages)       | YAML       | A collection of pre-packaged, Vale-compatible style guides and configurations.                               |
| [`vale-native`](https://github.com/errata-ai/vale-native) | Go         | A native messaging host for the Vale CLI: Use your local configurations in Chrome, Firefox, Opera, and Edge. |

[Install](https://docs.vale.sh/topics/installation)

# Installation

Get started with Vale in just a few minutes.

## [Package Managers](#package-managers)

In general, the recommended approach on all platforms is to use a package manager such as [Chocolatey](https://chocolatey.org/packages/vale) (Windows), [Homebrew](https://formulae.brew.sh/formula/vale) (macOS), or [Snapcraft](https://snapcraft.io/vale) (Linux).

{% tabs %}
{% tab title="Windows" %}

```powershell
> choco install vale
```

{% endtab %}

{% tab title="macOS" %}

```bash
brew install vale
```

{% endtab %}

{% tab title="Linux" %}

```bash
snap install vale
```

{% endtab %}
{% endtabs %}

This will ensure that Vale is available on your `$PATH` and allow you to stay up to date with new releases.

Vale can also be found at a number of [other package repositories](https://repology.org/project/vale/versions). These are community-maintained, so please read the package’s documentation before installing.

## [GitHub Releases](#github-releases)

[Archives of precompiled binaries](https://github.com/errata-ai/vale/releases) are available for Windows, macOS, and Linux. To use one of these, you’ll need to download the archive for your platform, extract it to a local directory, and (optionally) add the extracted directory to your `$PATH`.

## [Docker](#docker)

Vale is available on Docker Hub at [jdkato/vale](https://hub.docker.com/r/jdkato/vale):

```bash
docker pull jdkato/vale
```

Vale requires three components: a `.vale.ini` config file, a `StylesPath` directory (specified in the config file), and a document or directory to lint.

Here’s an example of calling Vale with locally-defined components (assuming `$(pwd)/fixtures/styles/demo` contains a config file):

```bash
$ docker run --rm \
             -v $(pwd)/styles:/styles \
             -v $(pwd)/fixtures/styles/demo:/docs \
             -w /docs \
             jdkato/vale .
```

By default, the image supports HTML, Markdown, AsciiDoc, and reStructuredText content. If you need support for DITA as well, you’ll need to add the relevant dependencies—for example,

```dockerfile
# Choose a version to pin:
FROM jdkato/vale:v2.15.2

# Copy a local installation of the DITA Open Toolkit:
COPY bin/dita-ot-3.6 /
ENV PATH="/dita-ot-3.6/bin:$PATH"

ENTRYPOINT ["/bin/vale"]
```

## [Other options](#other-options)

| Source | Documentation                                                                    | Status       |
| ------ | -------------------------------------------------------------------------------- | ------------ |
| `PyPI` | [`project/vale`](https://pypi.org/project/vale/)                                 | active       |
| `NPM`  | [`package/@ocular-d/vale-bin`](https://www.npmjs.com/package/@ocular-d/vale-bin) | unmaintained |

# .vale.ini

Learn how to configure Vale for your specific needs.

## [Creating a `.vale.ini` File](#creating-a-valeini-file)

After installing Vale, you’ll need to create a `.vale.ini` file in your project’s root directory. This file is used to configure Vale’s behavior and can be used to specify which rules to use, which directories to lint, and more.

The fastest way to get started with Vale is to use the [Config Generator](https://vale.sh/generator) to create a `.vale.ini` configuration file.

Once you have your local `.vale.ini` created in the directory of your choice, run `vale sync` from the command line to initialize it:

```bash
$ cd some-project
# You'll need to create this file
$ cat .vale.ini
...
$ vale sync
...
$ ls styles
...
$ vale README.md
```

Check out our [sample repository](https://github.com/errata-ai/vale-boilerplate) for a complete example of the required components of a Vale configuration.

## [File structure](#file-structure)

Vale’s configuration is read from a `.vale.ini` file. This file is [INI-formatted](https://ini.unknwon.io/docs/intro) and consists of multiple sections: core settings, format associations, and format-specific settings:

```ini
# Core settings appear at the top
# (the "global" section).

[formats]
# Format associations appear under
# the optional "formats" section.

[*]
# Format-specific settings appear
# under a user-provided "glob"
# pattern.
```

### [Core settings](#core-settings)

| Name                                                     | Type       | Description                               |
| -------------------------------------------------------- | ---------- | ----------------------------------------- |
| [StylesPath](https://docs.vale.sh/keys/stylespath)       | `string`   | Path to all Vale-related resources.       |
| [Packages](https://docs.vale.sh/keys/packages)           | `string[]` | List of packages to download and install. |
| [Vocab](https://docs.vale.sh/keys/vocabularies)          | `string[]` | List of vocabularies to load.             |
| [MinAlertLevel](https://docs.vale.sh/keys/minalertlevel) | `enum`     | Minimum alert level to display.           |
| [IgnoredScopes](https://docs.vale.sh/keys/ignoredscopes) | `enum`     | List of inline-level HTML tags to ignore. |
| [SkippedScopes](https://docs.vale.sh/keys/skippedscopes) | `enum`     | List of block-level HTML tags to ignore.  |

Core settings appear at the top of the file and apply to the application itself rather than a specific file format.

### [Format associations](#format-associations)

Format associations allow you to associate an “unknown” file extension with a supported one:

```ini
[formats]
mdx = md
```

In the example above, we’re telling Vale to treat MDX files as Markdown files. Note that this is merely an extension-level substitution and is not a means of adding support for a new file type.

### [Format-specific settings](#format-specific-settings)

| Name                                                             | Type        | Description                                     |
| ---------------------------------------------------------------- | ----------- | ----------------------------------------------- |
| [BasedOnStyles](https://docs.vale.sh/keys/basedonstyles)         | `string[]`  | List of styles to load.                         |
| [BlockIgnores](https://docs.vale.sh/keys/blockignores)           | `string[]`  | List regexes to ignore in block-level content.  |
| [TokenIgnores](https://docs.vale.sh/keys/tokenignores)           | `string[]`  | List regexes to ignore in inline-level content. |
| [CommentDelimiters](https://docs.vale.sh/keys/commentdelimiters) | `string[2]` | Comment delimiters to replace at runtime.       |
| [Transform](https://docs.vale.sh/keys/transform)                 | `string`    | A version 1.0 XSL Transformation (XSLT).        |

Format-specific sections apply their settings only to files that match their associated glob pattern. For example, `[*]` matches all files while `[*.{md,txt}]` only matches files that end with either `.md` or `.txt.`

You can have as many format-specific sections as you’d like and settings defined under a more specific section will override those in `[*]`.

See [Globbing](https://docs.vale.sh/guides/globbing) for more information on how to use glob patterns with Vale.

## [Search process](#search-process)

{% hint style="warning" %}
Heads up!

You can override the default search process by manually specifying a path using the `--config` option or by defining a `VALE_CONFIG_PATH` environment variable.
{% endhint %}

Vale expects its configuration to be in a file named `.vale.ini` or `_vale.ini`. It’ll start looking for this file in the directory that the `vale` command was run from and then search up the file tree until it finds one.

If no ancestor of the current directory has a configuration file, Vale will use a global configuration file (see below).

## [Global configuration](#global-configuration)

In addition to project-specific configurations, Vale also supports a global configuration file. The expected location of the global configuration depends on your operating system:

| OS      | Search Locations                                   |
| ------- | -------------------------------------------------- |
| Windows | `%LOCALAPPDATA%\vale\.vale.ini`                    |
| macOS   | `$HOME/Library/Application Support/vale/.vale.ini` |
| Unix    | `$XDG_CONFIG_HOME/vale/.vale.ini`                  |

(Run the `vale ls-dirs` command to see the exact locations on your system.)

This is different from the other config-defining options (`--config`, `VALE_CONFIG_PATH`, etc.) in that it’s loaded in addition to, rather than instead of, any other configuration sources.

In other words, this config file is *always* loaded and is read after any other sources to allow for project-agnostic customization.

## [Cascading overrides](#cascading-overrides)

Vale’s configuration system supports using multiple configuration files at the same time. Typically, this is done in cases where you are contributing to a project that already has an established configuration but you want to make local changes.

For example, let’s say you’re working on a project that uses the following configuration:

```ini
StylesPath = styles
MinAlertLevel = error

[*.md]
BasedOnStyles = ProjectStyle
```

Now, let’s say you want to add the `write-good` style to your local configuration.

Create a global configuration file—for macOS, this would be `~/Library/Application Support/vale/.vale.ini` (see above for other OSes).

```ini
StylesPath = localpath

Packages = write-good

[*.md]
BasedOnStyles = write-good
```

Now, when you run Vale, it will show results from both the `ProjectStyle` and `write-good` styles locally.

You’ll notice that multi-valued settings (like `BasedOnStyles`) are merged together, while single-valued settings (like `MinAlertLevel`) are overridden.

This allows you to contribute to projects with established styles while still being able to make local changes.

# CLI

Learn about the Vale command-line interface.

The Vale CLI is a powerful tool for linting your content in a variety of formats. To get started, try running with no arguments:

![Vale's help text](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/JU6lZokySTeBWnu1fWp0/help2.png)

## [Environment variables](#environment-variables)

The following list of environment variables are supported by the `vale` command-line interface:

| Variable           | Description                                                         |
| ------------------ | ------------------------------------------------------------------- |
| `VALE_CONFIG_PATH` | Override the default search process by specifying a .vale.ini file. |
| `VALE_STYLES_PATH` | Specify the location of the default StylesPath.                     |

You can inspect the current environment variables by running:

```
vale ls-vars
```

The exact steps for setting environment variables depend on your operating system, but here are some useful links for [Windows](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/setx) and [macOS](https://support.apple.com/guide/terminal/use-environment-variables-apd382cc5fa-4f58-4449-b20a-41c53c006f8f/mac).

## [CLI options](#cli-options)

| Name              | Description                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sync`            | <p>Download and install packages. See <a href="../keys/packages">Packages</a> for more information.<br><code>\<br>$ vale sync\<br></code></p>                                  |
| `ls-config`       | <p>Print the current configuration options as JSON.<br><code>\<br>$ vale ls-config\<br></code></p>                                                                             |
| `ls-metrics`      | <p>Print the computed metrics for the given file. See <a href="../checks/metric">metric</a> for more information.<br><code>\<br>$ vale ls-metrics path/to/file\<br></code></p> |
| `ls-dirs`         | <p>Print the location of default configuration directories.<br><code>\<br>$ vale ls-dirs\<br></code></p>                                                                       |
| `ls-vars`         | <p>Print the supported environment variables.<br><code>\<br>$ vale ls-vars\<br></code></p>                                                                                     |
| `--config`        | <p>Override the default configuration search process.<br><code>\<br>$ vale --config='path/to/.vale.ini' README.md\<br></code></p>                                              |
| `--ext`           | <p>Assign a file extension to stdin.<br>\`\`\`<br>$ echo "<em>This</em> is Markdown"</p>                                                                                       |
| `--filter`        | <p>An expression to filter rules by. See <a href="filters">Filters</a> for more information.<br><code>\<br>$ vale --filter='"heading" in .Scope' test.md\<br></code></p>       |
| `--glob`          | <p>A glob pattern to match files against. See <a href="../guides/globbing">Globbing</a> for more information.<br><code>\<br>$ vale --glob='\*.md' some-dir\<br></code></p>     |
| `--ignore-syntax` | <p>Treat all input as plain text.<br><code>\<br>$ vale --ignore-syntax README.md\<br></code></p>                                                                               |
| `--no-exit`       | <p>Do not return a non-zero exit code if there are errors.<br><code>\<br>$ vale --no-exit README.md\<br></code></p>                                                            |
| `--no-wrap`       | <p>Do not wrap output.<br><code>\<br>$ vale --no-wrap README.md\<br></code></p>                                                                                                |
| `--no-global`     | <p>Do not load the global configuration.<br><code>\<br>$ vale --no-global README.md\<br></code></p>                                                                            |
| `--output`        | <p>Change the output format. See <a href="templates">Templates</a> for more information.<br><code>\<br>$ vale --output=JSON README.md\<br></code></p>                          |
| `--version`       | <p>Print the version of Vale.<br><code>\<br>$ vale --version\<br></code></p>                                                                                                   |

## [Return codes](#return-codes)

The `vale` CLI returns the following exit codes:

| Code | Description                                                                                  |
| ---- | -------------------------------------------------------------------------------------------- |
| `0`  | No error(s) were found.                                                                      |
| `1`  | Linting error(s) were found. Useful for failing CI builds; can be disabled with `--no-exit`. |
| `2`  | Runtime error(s) occurred.                                                                   |

It will try to respect the value of `--output` when printing to `stderr`. For example:

![Vale's exit codes](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/0e5zXEYacO87tfH7lxBH/error.png)

# Styles

Learn about the primary component of Vale's configuration system.

Vale has a powerful extension system that doesn’t require knowledge of any programming language. Instead, it uses collections of individual [YAML](http://yaml.org/) files (or “rules”) to enforce particular writing constructs.

```yaml
# An example rule from the "Microsoft" style.
extends: existence
message: "Don't use end punctuation in headings."
link: https://docs.microsoft.com/en-us/style-guide/punctuation/periods
nonword: true
level: warning
scope: heading
action:
  name: edit
  params:
    - remove
    - '.?!'
tokens:
  - '[a-z0-9][.?!](?:\s|$)'
```

These collections are referred to as *styles* and are organized in a nested folder structure at a user-specified location. For example,

```
$ tree styles
styles/
├── base/
│   ├── ComplexWords.yml
│   ├── SentenceLength.yml
│   ...
├── blog/
│   ├── TechTerms.yml
│   ...
└── docs/
    ├── Branding.yml
```

where *base*, *blog*, and *docs* are your styles that each contain certain rules.

## [Rules](#rules)

{% hint style="warning" %}
Heads up!

Make sure your rule files end in extension `.yml`. Do not end them in `.yaml`, as Vale will not detect them.
{% endhint %}

The building blocks of styles are called *rules* (YAML files ending in `.yml`), which utilize *checks* to perform specific tasks.

The structure of a rule consists header followed by check-specific arguments. Every rule supports the following header fields:

| Name      | Required | Default      | Description                                                                                                                                                                                      |
| --------- | -------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `extends` | Yes      | `N/A`        | <p>The name of the check to extend in the particular rule. See <a href="../checks/existence">Rules</a> for more information.<br><code>\<br>extends: existence\<br></code></p>                    |
| `message` | Yes      | `N/A`        | <p>The message to display when the rule is triggered. Each extension point has different formatting options.<br><code>\<br>message: "Don't use '%s' headings."\<br></code></p>                   |
| `level`   | No       | `suggestion` | <p>The severity of the rule. The available options are <code>suggestion</code>, <code>warning</code>, and <code>error</code>.<br><code>\<br>level: warning\<br></code></p>                       |
| `scope`   | No       | `text`       | <p>The scope of the rule. See <a href="scopes">Scopes</a> for more information.<br><code>\<br>scope: heading\<br></code></p>                                                                     |
| `link`    | No       | `N/A`        | <p>A URL to associate with the rule. This is useful for providing more information about the rule.<br><code>\<br>link: [https://example.com\&#x3C;br>](https://example.com\&#x3C;br>)</code></p> |
| `limit`   | No       | `N/A`        | <p>The maximum number of times the rule can be triggered in a single file.<br><code>\<br>limit: 3\<br></code></p>                                                                                |
| `vocab`   | No       | `true`       | <p>If set to false, any active vocabularies will be disabled for the rule.<br><code>\<br>vocab: false\<br></code></p>                                                                            |

## [Checks](#checks)

Each rule *extends* a specific check, which is a built-in function that performs a particular task. For example, the `existence` check ensures that a given pattern is present in the content.

| Name                                                         | Description                                                                               |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| [existence](https://docs.vale.sh/checks/existence)           | Check for the presence of a specific regex pattern.                                       |
| [substitution](https://docs.vale.sh/checks/substitution)     | Replace a regex pattern with a specific string.                                           |
| [occurrence](https://docs.vale.sh/checks/occurrence)         | Ensure the presence of a regex pattern a specific number of times.                        |
| [repetition](https://docs.vale.sh/checks/repetition)         | Avoid repeating a regex pattern a specific number of times.                               |
| [consistency](https://docs.vale.sh/checks/consistency)       | Ensure that a regex pattern is used consistently.                                         |
| [conditional](https://docs.vale.sh/checks/conditional)       | Check for the presence of a regex pattern based on a condition.                           |
| [capitalization](https://docs.vale.sh/checks/capitalization) | Ensure that a regex pattern is capitalized in a specific way.                             |
| [metric](https://docs.vale.sh/checks/metric)                 | Check the readability (or other metrics) of your content using custom forumulas.          |
| [spelling](https://docs.vale.sh/checks/spelling)             | Spell check using Hunspell-compatible dictionaries.                                       |
| [sequence](https://docs.vale.sh/checks/sequence)             | Ensure that a regex pattern is used in a specific order. Supports part-of-speech tagging. |
| [script](https://docs.vale.sh/checks/script)                 | Run a custom Tengo script to check your content.                                          |

## [Regex](#regex)

Many rules will require the use of regular expressions to match specific patterns in your content. Vale uses [a superset](https://github.com/dlclark/regexp2?tab=readme-ov-file#compare-regexp-and-regexp2) of Go’s [regexp/syntax](https://pkg.go.dev/regexp/syntax) package to provide a powerful and flexible regex engine.

In addition to the standard Go regex syntax, Vale also supports positive lookahead (`(?=re)`), negative lookahead (`(?!re)`), positive lookbehind (`(?<=re)`), and negative lookbehind (`(?<!re)`).

See the [Regex](https://docs.vale.sh/guides/regex) guide for more information.

## [Vale](#vale)

Vale comes with a single built-in style named `Vale` that implements a few rules, as described in the table below.

| Name              | Description                                                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `Vale.Spelling`   | Checks for spelling errors in your content. Consumes any Hunspell-compatible dictionaries stored in `<StylesPath>/config/dictionaries`. |
| `Vale.Terms`      | Enforces the current project's accepted [Vocabulary](https://docs.vale.sh/keys/vocabularies) terms.                                     |
| `Vale.Avoid`      | Enforces the current project's rejected [Vocabulary](https://docs.vale.sh/keys/vocabularies) terms.                                     |
| `Vale.Repetition` | Flags repeated words such as "the the" or "and and".                                                                                    |

# Scopes

Learn about Vale's advanced markup-specific scoping system.

Vale is “markup aware,” which means that it’s capable of both applying rules to and ignoring certain sections of text. This functionality is implemented through a scoping system.

A scope is specified through a selector such as `paragraph.rst`, which indicates that the rule applies to all paragraphs in reStructuredText files.

Here are a few examples:

* `comment` matches all source code comments;
* `comment.line` matches all source code line comments;
* `heading.md` matches all Markdown headings; and
* `text.html` matches all HTML scopes.

Vale classifies files into one of three types—`markup`, `code`, or `text`—that determines what scopes are available.

Within each type, there can be multiple supported *formats*—such as Markdown and AsciiDoc under `markup`. Since each format has access to the same scopes, rules are compatible across all formats within a particular type.

## [Markup](#markup)

The default behavior for markup files is to apply rules to all non-ignored sections of the file. This means that for most rules you don’t need to specify a scope.

For rules that need to target specific sections of the file, you can use the following scopes:

| Name             | Description                                                                                                                                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `heading`        | <p>Matches all <code>h{1,...}</code> tags. You can specify an exact level by<br>appending tags—for example, <code>heading.h1</code> matches all <code>h1</code> tags.</p>                                           |
| `table.header`   | Matches all `th` tags.                                                                                                                                                                                              |
| `table.cell`     | Matches all `td` tags.                                                                                                                                                                                              |
| `table.caption`  | Matches all `caption` tags.                                                                                                                                                                                         |
| `figure.caption` | Matches all `figcaption` tags.                                                                                                                                                                                      |
| `list`           | Matches all `li` tags.                                                                                                                                                                                              |
| `paragraph`      | Matches all paragraphs (segments of text separated by two newlines).                                                                                                                                                |
| `sentence`       | Matches all sentences.                                                                                                                                                                                              |
| `blockquote`     | Matches all `blockquote` tags.                                                                                                                                                                                      |
| `alt`            | Matches all alt attributes.                                                                                                                                                                                         |
| `summary`        | <p>Matches all body text (excluding headings, code spans, code blocks, and<br>table cells). This scope is useful for rules that need to match only<br>sentence-level text content (such as readability scores).</p> |
| `raw`            | <p>Uses the raw, unprocessed markup source instead of a specific scope. This<br>scope is useful for regex-based rules that need to match against the<br>original source text.</p>                                   |

The supported formats for markup files are:

* [AsciiDoc](https://docs.vale.sh/formats/asciidoc)
* [Markdown](https://docs.vale.sh/formats/markdown) Built-in
* [reStructuredText](https://docs.vale.sh/formats/restructuredtext)
* [HTML](https://docs.vale.sh/formats/html) Built-in
* [XML](https://docs.vale.sh/formats/xml)
* [Org](https://docs.vale.sh/formats/org) Built-in
* [DITA](https://docs.vale.sh/formats/dita)
* [MDX](https://docs.vale.sh/formats/mdx)

The formats marked as `Built-in` are included with Vale by default. The other formats require a third-party dependency to be installed. See each format’s documentation for more information and installation instructions.

## [Code](#code)

There are two `code` scopes: `comment.line` and `comment.block`.

See the [Code](https://docs.vale.sh/formats/code) documentation for more information.

## [Selectors](#selectors)

Rules may define multiple scopes by using a YAML array:

```yaml
scope:
  # h1 OR h2
  - heading.h1
  - heading.h2
```

Any scope prefaced with `~` is negated:

```yaml
scope:
  # all scopes != h2
  - ~heading.h2
```

You can chain multiple scopes together using `&`:

```yaml
scope:
  # any scope that is NOT a blockquote or a heading
  - ~blockquote & ~heading
```

# Actions

Create dynamic suggestions for your rules with Actions.

{% hint style="info" %}
Heads up!

See [`vale-ls`](https://docs.vale.sh/guides/lsp) for an easy way to integrate Actions into your favorite text editor.
{% endhint %}

Actions provide a way for users to define dynamic fixes for their custom rules that show up in the CLI and LSP-based integrations.

![Actions](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/TwYY3qcoRCdqRoNp4mPw/action.png)

In the Sublime Text example above, the “Quick Fix” menu is powered by the action defined in the rule definition:

{% code title="rule.yml" %}

```yaml
action:
  name: replace
```

{% endcode %}

See the documentation on each `action` type for more information:

| Name                                            | Description                                                                                  |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [`suggest`](https://docs.vale.sh/fixes/suggest) | An array of dynamically-computed suggestions.                                                |
| [`replace`](https://docs.vale.sh/fixes/replace) | An array of static suggestions. Supported by default in `substitution` and `capitalization`. |
| [`remove`](https://docs.vale.sh/fixes/remove)   | Remove the matched text.                                                                     |
| [`edit`](https://docs.vale.sh/fixes/edit)       | In-place edits of the matched text.                                                          |

## [CLI](#cli)

Most Vale rules are based on *static* suggestions—for example,

{% code title="rule.yml" %}

```yaml
extends: substitution
message: "Use '%s' instead of '%s'."
level: error
action:
  name: replace
swap:
  Javascript: JavaScript
```

{% endcode %}

Here, the `action` is a to *replace*`Javascript` with `JavaScript`. In such cases, we know what we want to suggest to the user ahead of time and Vale can easily generate the appropriate output message.

However, there are cases in which we *don’t* know the appropriate suggestion ahead of time. For example, consider the following rule:

{% code title="rule.yml" %}

```yaml
extends: existence
message: "'%s' should be '%s'."
level: error
action:
  name: edit
  params:
    - regex
    - '(\w+)_(\w+)'
    - '$1-$2'
tokens:
  - '\w+_\w+'
```

{% endcode %}

This rule is designed to catch instances of `snake_case` and suggest that the user convert to `kebab-case`. In this case, the exact suggestion is dependent on a string transformation that needs to be computed at runtime.

Using the `edit` action allows us to define a rule that can dynamically generate suggestions based on the matched text in CLI output:

![CLI](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/AlAJw1s9hA1dsGPiGzd1/snake.png)

As you can see, the CLI output is dynamically computing the suggestion based on the matched text.

## [LSP](#lsp)

In both static and dynamic cases, any application that uses the [Vale Language Server](https://docs.vale.sh/guides/lsp) will be able to provide the user with a list of “Quick Fixes” that can be applied to the document.

[Scopes](https://docs.vale.sh/topics/scopes) [Filters](https://docs.vale.sh/topics/filters)

# Filters

Learn about Vale's rule filtering system.

The `--filter` CLI option allows you to report an arbitrary subset of your `.vale.ini` configuration.

![Filters](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/7THgoo94gwy5gXWgZaZF/filter.png)

A filter is an [expression](https://expr-lang.org/docs/language-definition) targeting one of the following keys defined in the rule definition: `.Name`, `.Level`, `.Scope`, `.Message`, `.Description`, `.Extends`, or `.Link`.

## Saving filters

You can save a filter for reuse by storing it in `<StylesPath>/config/filters`. Then, you can reference it by name when using the `--filter` option:

```bash
vale --filter=headings.expr docs/
```

Where `headings.expr` is a file containing the filter expression, such as:

```tengo
"heading" in .Scope
```

## Examples

* Filter by `.Level` and `.Name`:

```tengo
.Level in ["error", "suggestion"] and .Name != "demo.Cap"
```

* Filter by `.Extends`:

```tengo
.Extends=="existence"
```

* Only run a specific rule:

```tengo
.Name=="demo.Cap"
```

See the [documentation](https://expr-lang.org/docs/language-definition#operators) for a list of all supported operators.

[Actions](https://docs.vale.sh/topics/actions) [Templates](https://docs.vale.sh/topics/templates)

# Templates

Learn about Vale's output templates.

By default, Vale includes support for three output styles: `line`, `JSON`, and `CLI` (the default). You can specify which style to use via the `--output` flag:

```bash
vale --output=line README.md
```

In addition to the three provided output styles, Vale also supports *custom* output styles powered by Go’s [`text/template`](https://golang.org/pkg/text/template/) package.

To use a custom format, pass the path to a template file through the `--output` option:

```bash
vale --output='template.tmpl' somefile.md
```

Where `template.tmpl` is a file that contains a valid Go template stored in the `<StylesPath>/config/templates` directory.

## [Templating](#templating)

Templates have access to the following data structures:

```go
type ProcessedFile struct {
    Alerts []core.Alert
    Path   string
}

type Data struct {
    Files       []ProcessedFile
    LintedTotal int
}
```

Where `core.Alert` has the same information as Vale’s `--output=JSON` object.

Templates can also access the following functions:

| Name          | Argument(s) | Description                                                                                                                                                                                                                                           |
| ------------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `red`         | `string`    | Returns the given `string` with an ANSI-formatted red foreground color.                                                                                                                                                                               |
| `blue`        | `string`    | Returns the given `string` with an ANSI-formatted blue foreground color.                                                                                                                                                                              |
| `yellow`      | `string`    | Returns the given `string` with an ANSI-formatted yellow foreground color.                                                                                                                                                                            |
| `underline`   | `string`    | Returns the given `string` with an ANSI-formatted underline.                                                                                                                                                                                          |
| `newTable`    | `bool`      | Creates a new [`tablewriter`](https://github.com/olekukonko/tablewriter#ascii-table-writer) struct. `newTable` accepts one boolean value representing [`SetAutoWrapText`](https://godoc.org/github.com/olekukonko/tablewriter#Table.SetAutoWrapText). |
| `addRow`      | `[]string`  | Appends the given row to a table.                                                                                                                                                                                                                     |
| `renderTable` | `Table`     | Prints the table-formatted output to `stdout`.                                                                                                                                                                                                        |
| `jsonEscape`  | `string`    | Ensure the given `STRING` is valid JSON.                                                                                                                                                                                                              |

See the [Sprig Function Documentation](http://masterminds.github.io/sprig/) for the full list.

## [Examples](#examples)

### [Customizing the default output](#customizing-the-default-output)

The following example re-implements Vale’s default output style using a template.

```go
{{- /* Keep track of our various counts */ -}}

{{- $e := 0 -}}
{{- $w := 0 -}}
{{- $s := 0 -}}
{{- $f := 0 -}}

{{- /* Range over the linted files */ -}}

{{- range .Files}}
{{$table := newTable true}}

{{- $f = add1 $f -}}
{{- .Path | underline | indent 1 -}}

{{- /* Range over the file's alerts */ -}}

{{- range .Alerts -}}

{{- $error := "" -}}
{{- if eq .Severity "error" -}}
    {{- $error = .Severity | red -}}
    {{- $e = add1 $e  -}}
{{- else if eq .Severity "warning" -}}
    {{- $error = .Severity | yellow -}}
    {{- $w = add1 $w -}}
{{- else -}}
    {{- $error = .Severity | blue -}}
    {{- $s = add1 $s -}}
{{- end}}

{{- $loc := printf "%d:%d" .Line (index .Span 0) -}}
{{- $row := list $loc $error .Message .Check | toStrings -}}

{{- $table = addRow $table $row -}}
{{end -}}

{{- $table = renderTable $table -}}
{{end}}
{{- $e}} {{"errors" | red}}, {{$w}} {{"warnings" | yellow}} and {{$s}} {{"suggestions" | blue}} in {{$f}} {{$f | int | plural "file" "files"}}.
```

### [Creating a RDJSONL template](#creating-a-rdjsonl-template)

The following example converts Vale’s output to [RDJSONL](https://github.com/reviewdog/reviewdog?tab=readme-ov-file#reviewdog-diagnostic-format-rdformat), which you can then pass to [Reviewdog](https://github.com/reviewdog/reviewdog) to display on pull request. This can be useful when the [Vale action](https://github.com/errata-ai/vale-action) is not suitable for your workflow.

```go
{{- /* Range over the linted files */ -}}

{{- range .Files}}

{{- $path := .Path -}}

{{- /* Range over the file's alerts */ -}}

{{- range .Alerts -}}

{{- $error := "" -}}
{{- if eq .Severity "error" -}}
    {{- $error = "ERROR" -}}
{{- else if eq .Severity "warning" -}}
    {{- $error = "WARNING" -}}
{{- else -}}
    {{- $error = "INFO" -}}
{{- end}}

{{- /* Variables setup */ -}}

{{- $line := printf "%d" .Line -}}
{{- $col := printf "%d" (index .Span 0) -}}
{{- $check := printf "%s" .Check -}}
{{- $message := printf "%s" .Message -}}

{{- /* Output */ -}}

{"message": "[{{ $check }}] {{ $message | jsonEscape }}", "location": {"path": "{{ $path }}", "range": {"start": {"line": {{ $line }}, "column": {{ $col }}}}}, "severity": "{{ $error }}"}
{{end -}}
{{end -}}
```

[Filters](https://docs.vale.sh/topics/filters) [Views](https://docs.vale.sh/topics/views)

# Views

Customize the file-processing pipeline with Views.

Views represent a virtual, filtered perspective of a structured file. They define a series of transformation steps that extract specific, named [scopes](https://docs.vale.sh/topics/scopes), effectively changing how the file is represented for linting purposes. By focusing only on relevant sections, Views let you control exactly what content is analyzed—and enable rules that apply only to specific parts of a file.

Each View is defined in a YAML file and consists of a series of steps that are executed in order. Each step includes the following fields:

* `name`: The name of the step. If no `type` is provided, the name is used as the only scope for the value. Otherwise, the `name` is used as a metascope and will be appended to the active scope – such as `heading.<name>.md`.
* `expr`: An expression that selects the data to be linted. The expression is evaluated by the active [engine](#engines).
* `type`: The type of the data. Supported types are `md`, `adoc`, `html`, `rst`, or `org`.

Here’s an example of a View that extracts the `title` and `description` fields from an OpenAPI document:

```yaml
engine: dasel
scopes:
  - name: title
    expr: info.title
    type: md

  - expr: info.description
    type: md

  - expr: servers.all().description
    type: md
```

Views are stored in `<StylesPath>/config/views` and can be referenced in the `.vale.ini` file under any syntax-specific section:

```ini
[*.json]
BasedOnStyles = Vale

View = MyView
```

## [Engines](#engines)

Each step in a View contains a query that is processed by [Dasel](https://github.com/TomWright/dasel) (JSON, YAML, or TOML), [tree-sitter](https://tree-sitter.github.io/tree-sitter/) (source code), or TextFSM (text).

### [Dasel](#dasel)

[Dasel](https://github.com/TomWright/dasel) is a command-line tool that allows you to query and modify data structures using selectors. It works with JSON, YAML, TOML, XML, and more.

Vale uses Dasel to query structured data in files and extract the relevant content. For example, given the following JSON:

```json
{
 "title": "Vale",
 "version": "3.0.0",
 "features": [
  {
   "title": "Views",
   "description": "Customize the file-processing pipeline with Views."
  },
  {
   "title": "Styles",
   "description": "Define custom linting rules with Styles."
  }
 ]
}
```

You could use the following View to extract the `name` and `description` fields from each feature:

```yaml
engine: dasel
scopes:
  # The `name` field is used as the metascope, allowing us to
  # write rules that specifically target the `title` field by
  # using the custom `feature` scope.
  - name: feature
    expr: features.all().title
    type: md

  - expr: features.all().description
    type: md
```

Check out the [playground](https://dasel.tomwright.me/) to experiment with Dasel queries.

### [Tree-sitter](#tree-sitter)

[Tree-sitter](https://tree-sitter.github.io/tree-sitter/) is a parser generator tool and an incremental parsing library. It can be used to build parsers for source code in any language.

Vale uses tree-sitter to parse source code and extract structured data. For example, given the following Python code:

```python
# This a comment.
def hello(name: str) -> str:
    """
    This is a docstring.
    """
    return f"Hello, {name}!"
```

You could use the following View to extract all comments and function docstrings:

```yaml
engine: tree-sitter
scopes:
  - name: comment
    expr: (comment)+ @comment

  - expr: |
      ((function_definition
        body: (block . (expression_statement (string) @docstring)))
      (#offset! @docstring 0 3 0 -3))
```

See [Pattern Matching with Queries](https://tree-sitter.github.io/tree-sitter/using-parsers/queries/index.html) for more information.

### [TextFSM](#textfsm)

Coming soon!

[Templates](https://docs.vale.sh/topics/templates) [StylesPath](https://docs.vale.sh/keys/stylespath)

# StylesPath

Learn about Vale's resource directory.

{% hint style="info" %}
You can override the default `StylesPath` by manually defining a `VALE_STYLES_PATH` environment variable.
{% endhint %}

The `StylesPath` specifies where Vale should look for its external resources (e.g., styles and ignore files). The path value may be absolute or relative to the location of the parent `.vale.ini` file.

```ini
# Here's an example of a relative path:
#
# .vale.ini
# ci/
# ├── vale/
# │   ├── styles/
StylesPath = ci/vale/styles

[*.md]
# `MyStyle` is a directory within
# `ci/vale/styles`.
BasedOnStyles = MyStyle
```

If you don’t specify a `StylesPath` in your `.vale.ini` file, Vale will use its default location:

| OS      | Search Locations                                |
| ------- | ----------------------------------------------- |
| Windows | `%LOCALAPPDATA%\vale\styles`                    |
| macOS   | `$HOME/Library/Application Support/vale/styles` |
| Unix    | `$XDG_DATA_HOME/vale/styles`                    |

(Run the `vale ls-dirs` command to see the exact locations on your system.)

## [Structure](#structure)

A `StylesPath` contains two types of entries: *styles* and the special `config` directory.

```console
$ tree styles
├───config     <-- Special directory
└───write-good <-- A style
```

The `config` directory is used internally by Vale and contains the following:

| Directory                                                | Description                                |
| -------------------------------------------------------- | ------------------------------------------ |
| [`vocabularies`](https://docs.vale.sh/keys/vocabularies) | Project-specific terminology lists.        |
| [`dictionaries`](https://docs.vale.sh/checks/spelling)   | Hunspell-compatible spelling dictionaries. |
| [`templates`](https://docs.vale.sh/topics/templates)     | Output format templates.                   |
| [`actions`](https://docs.vale.sh/topics/actions)         | Solutions to your custom rules.            |
| [`filters`](https://docs.vale.sh/topics/filters)         | Configuration filters.                     |
| [`scripts`](https://docs.vale.sh/checks/script)          | Tengo scripts.                             |

[Views](https://docs.vale.sh/topics/views) [Packages](https://docs.vale.sh/keys/packages)

# Packages

Learn about Vale's configuration distribution system.

```ini
Packages = Google, write-good

[*.md]
BasedOnStyles = Vale, Google, write-good
```

Packages provide a means of sharing, extending, syncing, and updating Vale configurations.

![Packages](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/pTuYpl1QMqcvh3Mn4d6R/package.png)

In the example above, projects 1 and 2 will have identical configurations (as inherited from the upstream package). Any changes to the upstream package will propagate to both projects.

## [Structure and hosting](#structure-and-hosting)

A package is a `.zip` file that contains a `.vale.ini` file, a `StylesPath` folder, or both. You include a package by using the top-level `Packages` key in your local `.vale.ini` file:

```ini
StylesPath = .github/styles
MinAlertLevel = suggestion

Packages = Microsoft,
https://github.com/errata-ai/errata.ai/releases/download/v1.0.0/Test.zip

[README.md]
BasedOnStyles = Vale
```

{% stepper %}
{% step %}

### Package types — four accepted values

The `Packages` key accepts four types of values:

* A name of a package hosted in the official [Package Explorer](https://vale.sh/explorer);
* a URL to an externally-hosted package;
* an absolute or relative path to a `.zip` file located in the local file system; or
* an absolute or relative path to a directory containing package files.
  {% endstep %}

{% step %}

### Style-only

Style-only (such as [write-good](https://github.com/errata-ai/write-good)) packages are a `.zip` archive of a single style folder:

```console
$ unzip write-good.zip
Archive:  write-good.zip
   creating: write-good/
  inflating: write-good/README.md
  inflating: write-good/Cliches.yml
  inflating: write-good/ThereIs.yml
  inflating: write-good/Weasel.yml
  inflating: write-good/TooWordy.yml
  inflating: write-good/Passive.yml
  inflating: write-good/So.yml
  inflating: write-good/Illusions.yml
  inflating: write-good/E-Prime.yml
  inflating: write-good/meta.json
```

After running the `sync` command, the style will be added to the active `StylesPath`.
{% endstep %}

{% step %}

### Config-only

Config-only (such as [Hugo](https://github.com/errata-ai/Hugo)) packages are a `.zip` archive of a single `.vale.ini` file:

```console
$ unzip Hugo.zip
Archive:  Hugo.zip
   creating: Hugo/
  inflating: Hugo/.vale.ini
```

After running the `sync` command, the configuration file will be added to `StylesPath/.vale-config` according to the order in which it was loaded.
{% endstep %}

{% step %}

### Complete

Complete packages contain both a `.vale.ini` file and an associated `StylesPath` folder:

```console
$ tree MyPackage
MyPackage
├── .vale.ini
└── styles
    ├── MyStyle
    │   └── MyRule.yml
    └── config
        ├── dictionaries
        │   └── MyDic.dic
        ├── scripts
        │   └── MyScript.tengo
        └── vocabularies
            └── MyVocab
                ├── accept.txt
                └── reject.txt
```

The `StylesPath` should be named “styles” and can contain any typically-supported subfolder—such as [styles](https://docs.vale.sh/topics/styles) and [vocabularies](https://docs.vale.sh/keys/vocabularies). The `.vale.ini` file should reference the included `StylesPath`:

```ini
# This is subfolder included in our .zip archive.
StylesPath = styles

# Complete packages can include other, externally-defined
# packages.
Packages = proselint

# Normal configuration ...
[*.{md,adoc}]
Test.Rule = YES
```

The packaged `StylesPath` will be merged with the active local `StylesPath` and any included configuration files will be added to the local `StylesPath/.vale-config` folder.
{% endstep %}
{% endstepper %}

## [Ordering](#ordering)

In the case of conflicting configuration, the order in which packages are loaded is important:

```ini
Packages = pkg1, pkg2

# Local configuration ...
[*.{md,adoc}]
Test.Rule = YES
```

In the above example, `pkg2` will override any conflicting configuration from `pkg1`. Similarly, local configuration will override any conflicting package.

## [VCS](#vcs)

You’ll want to add any packaged configuration components to your `.gitignore` (or equivalent) file.

While this can be as simple as ignoring your entire `StylesPath`, it’s likely that you’ll also have some local components as well.

```gitignore
# We want to ignore our StylesPath *except* for our local
# `vocabularies/Base` directory.

.github/styles/*
!.github/styles/config/

.github/styles/config/*
!.github/styles/config/vocabularies/

.github/styles/config/vocabularies/*
!.github/styles/config/vocabularies/Base
```

The above example ignores the entire `.github/styles/` folder *except* for `.github/styles/config/vocabularies/Base` (which we want to track changes for).

[StylesPath](https://docs.vale.sh/keys/stylespath) [Vocab](https://docs.vale.sh/keys/vocabularies)

# Vocabularies

Learn about Vale's terminology management system.

Vocabularies allow you to maintain custom lists of terminology independent of your styles.

```ini
StylesPath = "..."

# Here's were we define the exceptions to use in *all*
# `BasedOnStyles`.
Vocab = Some-Name

[*]
# 'Vale' and 'MyStyle' automatically respect all
# custom exceptions.
#
# The built-in 'Vale' style is required for using
# `Vale.Terms`, `Vale.Avoid`, or `Vale.Spelling`.
BasedOnStyles = Vale, MyStyle
```

Each `Vocab` is a single folder (stored at `<StylesPath>/config/vocabularies/<name>/`) consisting of two plain-text files—`accept.txt` and `reject.txt`—that contain one regular expression per line.

The effects of using a custom `Vocab` are as follows:

* Entries in `accept.txt` are added to every exception list in all styles listed in `BasedOnStyles`—meaning that you now only need to update your project’s *vocabulary* to customize third-party styles.
* Entries in `accept.txt` are automatically added to a substitution rule (`Vale.Terms`), ensuring that any occurrences of these words or phrases exactly match their corresponding entry in `accept.txt`.
* Entries in `reject.txt` are automatically added to an existence rule (`Vale.Avoid`) that will flag all occurrences as errors.
* Entries in `accept.txt` and `reject.txt` should need little overlap, if any. For example, if you add `JavaScript` to `accept.txt`, then you do not need to add an overlapping regular expression entry of `[Jj]avascript` in `reject.txt`. Vale will enforce correct casing by virtue of the entry’s presence in `accept.txt`. See the section “Case sensitivity” for details.

This means that your exceptions can be developed independent of a style, allowing you to use the same exceptions with multiple styles or switch styles without having to re-implement them.

{% hint style="warning" %}
Heads up!

In versions of Vale prior to 3.0, vocabularies were stored in `<StylesPath>/Vocab`. When upgrading from an older version of Vale, you'll need to move your vocabularies to the new `<StylesPath>/config/vocabularies` location.
{% endhint %}

Vocabulary entries are stored in `<StylesPath>/config/vocabularies/<name>/` and are then referenced by `<name>` in `.vale.ini`. For example, consider the following folder structure:

```
$ tree styles
├───MyStyle
├───config
│   └───vocabularies
│       ├───Blog
│       │   ├───accept.txt
│       │   └───reject.txt
│       └───Marketing
│           ├───accept.txt
│           └───reject.txt
└───MyOtherStyle
```

Here, our `StylesPath` (`/styles`) contains two styles (`MyStyle` and `MyOtherStyle`) and two vocabularies (`Blog` and `Marketing`). You can then reference these entries by their folder name:

```ini
StylesPath = styles

Vocab = Blog

[*]
BasedOnStyles = Vale, MyStyle
```

## File format

Both `accept.txt` and `reject.txt` are plain-text files that take one entry per line:

```
first
[pP]y.*\b
third
```

The entries are evaluated as case-sensitive (except for rules extending `spelling`, as mentioned above) regular expressions.

Lines starting with `#` are treated as comments and are ignored.

## Case sensitivity

An important factor in successfully implementing a custom vocabulary is understanding how Vale handles case sensitivity.

While most spell-checking tools ignore case altogether, Vale’s vocabulary files are case-aware by default. This means that, for example, a vocabulary consisting of

```
MongoDB
```

will enforce the *exact* use of “MongoDB”: “mongoDB,” “MongoDb,” etc., will all result in errors. There are two ways around this.

First, you can indicate that a given entry should be case-insensitive by providing an appropriate regular expression:

```
(?i)MongoDB
[Oo]bservability
```

The first entry, `(?i)MongoDB`, marks the entire pattern as case-insensitive while the second, `[Oo]bservability`, provides two acceptable options.

You can also disable `Vale.Terms` and just use `Vale.Spelling`:

```ini
[*.md]
BasedOnStyles = Vale

Vale.Terms = NO
```

This will provide a more traditional spell-checking experience.

## Relation to ignore files

The functionality of vocabularies is similar to the existing concept of [ignore files](https://docs.vale.sh/checks/spelling#ignore-files).

The major differences are that vocabularies apply to multiple extension points (rather than just `spelling`), support regular expressions, and have built-in rules associated with them (`Vale.Terms` and `Vale.Avoid`).

In general, this means that ignore files are for style *creators* while vocabularies are for style *users*:

* If you’re developing or maintaining a style, you may still want to include a custom `spelling` rule—`MyStyle.Spelling`—that packages its own ignore files.
* As a user of styles, vocabularies should be able to replace the use of ignore files completely.

## Rules targeting vocabulary entries

In cases where you want to write a rule that needs to match against an otherwise-ignored token, you can add `vocab: false` to the rule definition. For example,

```yaml
extends: existence
message: Did you mean '%s'?
vocab: false
tokens:
  # "MonoDB" can be in a vocab
  - MongoDB
```

[Packages](https://docs.vale.sh/keys/packages) [MinAlertLevel](https://docs.vale.sh/keys/minalertlevel)

# MinAlertLevel

Learn about how to set the minimum alert level for Vale.

```ini
StylesPath = styles
MinAlertLevel = suggestion

[*.md]
BasedOnStyles = Vale
```

The `MinAlertLevel` key allows you to set the minimum alert level that Vale will report. The supported levels are `suggestion` (default), `warning`, and `error`.

`error`-level alerts will result in a [non-zero exit code](https://docs.vale.sh/topics/cli#return-codes), while `warning`- and `suggestion`-level alerts will not. This is useful for controlling which rules will fail CI builds.

## [Overriding](#overriding)

The `MinAlertLevel` key can be overridden from the command line using the `--minAlertLevel` flag:

```bash
vale --minAlertLevel=warning README.md
```

This allows you to, for example, show all alerts in your editor while only running `error`-level alerts in CI.

## [Editing](#editing)

You can edit the severity of a rule by modifying its `level` in your local `.vale.ini` file:

```ini
[*.md]
BasedOnStyles = Vale

Vale.Spelling = warning
```

Related: [Vocab](https://docs.vale.sh/keys/vocabularies) [IgnoredScopes](https://docs.vale.sh/keys/ignoredscopes)

# IgnoredScopes

Learn about how to ignore inline-level HTML tags.

```ini
StylesPath = styles

IgnoredScopes = code, tt

[*.md]
BasedOnStyles = Vale
```

`IgnoredScopes` specifies inline-level HTML tags to ignore. In other words, these tags may occur in an active scope (unlike `SkippedScopes`, which are skipped entirely) but their content still won’t raise any alerts.

By default, Vale ignores `code` and `tt` tags. For example, considering the following Markdown file:

```markdown
This is a sentence that contains inline `code`.
```

Vale will not raise any alerts for the content within the backticks, such as `code` in the example above.

See [Markup](https://docs.vale.sh/topics/scopes) for more information.

[MinAlertLevel](https://docs.vale.sh/keys/minalertlevel) [IgnoredClasses](https://docs.vale.sh/keys/ignoredclasses)

# IgnoredClasses

Learn about how to ignore HTML classes.

```ini
Copy

StylesPath = styles

IgnoredClasses = my-class, another-class

[*.md]
BasedOnStyles = Vale
```

`IgnoredClasses` specifies classes to ignore. These classes may appear on both inline- and block-level HTML elements.

[IgnoredScopes](https://docs.vale.sh/keys/ignoredscopes) [SkippedScopes](https://docs.vale.sh/keys/skippedscopes)

# SkippedScopes

Learn about how to ignore block-level HTML tags.

```ini
StylesPath = styles

SkippedScopes = script, style, pre

[*.md]
BasedOnStyles = Vale
```

`SkippedScopes` specifies block-level HTML tags to ignore. Any content in these scopes will be ignored.

By default, Vale ignores `script`, `style`, and `pre` tags. For example, considering the following Markdown file:

````markdown
This is a sentence that contains normal text.

```python
# This is a code block.
print("Hello, world!")
```

Another normal sentence.
````

Vale will not raise any alerts for the content within the code block.

See [Markup](https://docs.vale.sh/topics/scopes) for more information.

[IgnoredClasses](https://docs.vale.sh/keys/ignoredclasses) [BasedOnStyles](https://docs.vale.sh/keys/basedonstyles)

# BasedOnStyles

Learn how to enable a style for a specific file type.

```ini
StylesPath = styles

[*.md]
BasedOnStyles = Vale, MyStyle
```

`BasedOnStyles` specifies styles that should have all of their rules enabled.

If you only want to enable certain rules within a style, you can do so on an individual basis:

```ini
[*.md]

# Enables only this rule:
Style1.Rule = YES
```

You can also selectively disable rules from a style:

```ini
[*.md]
BasedOnStyles = Vale, MyStyle

Vale.Spelling = NO
```

[SkippedScopes](https://docs.vale.sh/keys/skippedscopes) [BlockIgnores](https://docs.vale.sh/keys/blockignores)

# BlockIgnores

Learn define custom block-level ignores in your Vale configuration.

{% hint style="info" %}
Heads up!

`BlockIgnores` are only supported in Markdown, reStructuredText, AsciiDoc, and Org Mode.
{% endhint %}

```ini
StylesPath = styles

[*.md]
BasedOnStyles = Vale

BlockIgnores = (?s) *({< file [^>]* >}.*?{</ ?file >})
```

`BlockIgnores` allow you to exclude certain block-level sections of text that don’t have an associated HTML tag that could be used with [`SkippedScopes`](https://docs.vale.sh/keys/skippedscopes).

The idea is to write a regular expression that captures the entire block in the first grouping. See this [regex101 session](https://regex101.com/r/mFM0kZ/1/) for a more thorough explanation.

[BasedOnStyles](https://docs.vale.sh/keys/basedonstyles) [TokenIgnores](https://docs.vale.sh/keys/tokenignores)

# TokenIgnores

Learn define custom inline-level ignores in your Vale configuration.

{% hint style="warning" %}
`TokenIgnores` are only supported in Markdown, reStructuredText, AsciiDoc, and Org Mode.
{% endhint %}

```ini
StylesPath = styles

[*.md]
BasedOnStyles = Vale

TokenIgnores = ($+[^\n$]+$+), (:math:`.*`)
```

`TokenIgnores` allow you to exclude certain inline-level sections of text that don’t have an associated HTML tag that could be used with [`IgnoredScopes`](https://docs.vale.sh/keys/ignoredscopes).

The idea is to write a regular expression that captures the entire token in the first grouping. See this [regex101 session](https://regex101.com/r/3Raecd/1) for a more thorough explanation.

Related:

* [BlockIgnores](https://docs.vale.sh/keys/blockignores)
* [CommentDelimiters](https://docs.vale.sh/keys/commentdelimiters)

# CommentDelimiters

Learn how to define custom comment delimiters.

`CommentDelimiters` allow you to override standard HTML comment delimiters (`<!-- foo -->`).

Custom comment delimiters are useful when using non-standard markup which do not allow HTML-style comments, such as MDX.

```ini
[formats]
mdx = md

[*.mdx]
BasedOnStyles = Vale

CommentDelimiters = {/*, */}
```

When `CommentDelimiters` are set, you can take full advantage of markup-based configuration to enable or disable specific rules within a section.

For instance, when using MDX:

```mdx
{/* vale off */}

This is some text ACT test

This is some text ACT test

{/* vale on */}

{/* vale vale.Redundancy = NO */}

This is some text ACT test

{/* vale vale.Redundancy = YES */}
```

Related keys: [TokenIgnores](https://docs.vale.sh/keys/tokenignores) [Transform](https://docs.vale.sh/keys/transform)

# Transform

Learn about how to add support for XML.

```ini
StylesPath = styles

[*.xml]
BasedOnStyles = Vale

Transform = docbook-xsl-snapshot/html/docbook.xsl
```

`Transform` specifies a version 1.0 XSL Transformation (XSLT) for converting to HTML.

See <https://vale.sh/docs/formats/xml> for more information.

<https://vale.sh/docs/keys/commentdelimiters> <https://vale.sh/docs/checks/existence>

# existence

Checks

existence

## existence

Learn about the existence extension point.

| Name         | Type    | Description                                                                                                         |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------- |
| `append`     | `bool`  | Adds `raw` to the end of `tokens`, assuming both are defined.                                                       |
| `ignorecase` | `bool`  | Makes all matches case-insensitive.                                                                                 |
| `nonword`    | `bool`  | Removes the default word boundaries (`\b`).                                                                         |
| `action`     | `array` | Options for correcting matches, see the [actions](https://docs.vale.sh/topics/actions) section.                     |
| `raw`        | `array` | A list of tokens to be concatenated into a pattern.                                                                 |
| `tokens`     | `array` | A list of tokens to be transformed into a non-capturing group.                                                      |
| `exceptions` | `array` | An array of strings to be ignored.                                                                                  |
| `vocab`      | `bool`  | If false, disables all active [vocabularies](https://docs.vale.sh/keys/vocabularies) for this rule (default: true). |

The most general extension point is existence. As its name implies, it looks for the “existence” of particular tokens.

```yaml
extends: existence
message: Consider removing '%s'
level: warning
ignorecase: true
tokens:
  - appears to be
  - arguably
```

These tokens can be anything from simple phrases (as in the above example) to regular expressions—e.g., [the number of spaces between sentences](https://github.com/errata-ai/vale/blob/master/testdata/styles/demo/Spacing.yml) or [the position of punctuation after quotes](https://github.com/errata-ai/Google/blob/master/Google/Quotes.yml).

### [tokens](#tokens)

{% hint style="info" %}
Heads up!

See [Vale Studio](https://studio.vale.sh/) for a live editor that can help you write and test your rules, including generating the compiled regular expression.
{% endhint %}

The most common entry point for this extension point is the `tokens` key, which is a list of strings or regular expressions to be transformed into a word-bounded, non-capturing group:

```yaml
tokens:
  - appears to be
  - arguably
```

Which, after compilation, becomes:

```regex
(?i)(?m)\b(?:appears to be|arguably)\b
```

This is a convenience feature to avoid having to write the same boilerplate for every token in a rule.

### [raw](#raw)

When you want more control over the regular expression, you can use the `raw` key instead:

```yaml
extends: existence
message: "Incorrect use of symbols in '%s'."
ignorecase: true
raw:
  - $[d]* ?(?:dollars|usd|us dollars)
```

This allows you to write more complex patterns without having to worry about any post-processing. Each entry in `raw` is concatenated with the previous entry, allowing for improved commenting and readability of complex patterns.

### [message](#message)

The `message` key is a string that will be used to generate the final message when a match is found. The (optional) `%s` placeholder will be replaced with the matched text.

[Transform](https://docs.vale.sh/keys/transform) [substitution](https://docs.vale.sh/checks/substitution)

# substitution

Learn about the substitution extension point.

| Name         | Type    | Description                                                               |
| ------------ | ------- | ------------------------------------------------------------------------- |
| `append`     | `bool`  | Adds `raw` to the end of `tokens`, assuming both are defined.             |
| `ignorecase` | `bool`  | Makes all matches case-insensitive.                                       |
| `nonword`    | `bool`  | Removes the default word boundaries (`\b`).                               |
| `swap`       | `map`   | A sequence of `observed: expected` pairs.                                 |
| `exceptions` | `array` | An array of strings to be ignored.                                        |
| `vocab`      | `bool`  | If false, disables all active vocabularies for this rule (default: true). |
| `capitalize` | `bool`  | Matches the capitalization of the source token.                           |

`substitution` associates a string with a preferred form.

```
yaml
Copy

extends: substitution
message: Consider using '%s' instead of '%s'
level: warning
ignorecase: false
# swap maps tokens in form of bad: good
swap:
  abundance: plenty
  accelerate: speed up
```

If we want to suggest the use of “plenty” instead of “abundance,” for example, we’d write:

```
yaml
Copy

swap:
  abundance: plenty
```

## Regex keys

The keys may also be regular expressions:

```
yaml
Copy

swap:
  '(?:give|gave) rise to': lead to
```

You can also reference capture groups for more dynamic substitutions:

```
yaml
Copy

swap:
  'within the (.*)?directory': in the $1 directory
```

## Multiple suggestions

In some cases, you may want to suggest multiple alternatives for a single token. You can do this by separating them with a pipe ("|"):

```
yaml
Copy

extends: substitution
# NOTE: We don't quote the first '%s':
message: Consider using %s instead of '%s.'
level: warning
# NOTE: The action is required.
action:
  name: replace
swap:
  # You can suggest multiple alternatives for a single token
  # by separating them with a pipe ("|").
  masterful: skilled|authoritative|commanding
```

In the CLI, this will render as a sentence with multiple suggestions:

![Multiple suggestions](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/ndXPk2UKcmhPFauXBQlf/pipe.png)

In LSP-based editors, the suggestions will be presented as a list of ‘Quick Fixes’. See the [LSP guide](https://docs.vale.sh/guides/lsp) for more information.

## message

`substitution` can have one or two `%s` format specifiers in its message. This allows us to do either of the following:

```
yaml
Copy

message: "Consider using '%s' instead of '%s'."
# or
message: "Consider using '%s'."
```

[existence](https://docs.vale.sh/checks/existence) [occurrence](https://docs.vale.sh/checks/occurrence)

# occurrence

Learn about the occurrence extension point.

| Name    | Type     | Description                                                         |
| ------- | -------- | ------------------------------------------------------------------- |
| `max`   | `int`    | The maximum amount of times `token` may appear in a given scope.    |
| `min`   | `int`    | The minimum amount of times `token` has to appear in a given scope. |
| `token` | `string` | The token of interest.                                              |

`occurrence` enforces the maximum or minimum number of times a particular token can appear in a given scope.

```yaml
extends: occurrence
message: 'More than 3 commas!'
level: error
# Here, we're counting the number of times a comma appears
# in a sentence.
#
# If it occurs more than 3 times, we'll flag it.
scope: sentence
max: 3
token: ','
```

In the example above, we’re limiting the number of commas per sentence.

## [message](#message)

The `message` key can contain an optional format specifier `%s` which will be populated with the number of occurrences:

```yaml
message: 'Titles should use fewer than 70 characters (found: %s).'
```

[substitution](https://docs.vale.sh/checks/substitution) [repetition](https://docs.vale.sh/checks/repetition)

# repetition

Learn about the repetition extension point.

| Name         | Type    | Description                                                               |
| ------------ | ------- | ------------------------------------------------------------------------- |
| `ignorecase` | `bool`  | Makes all matches case-insensitive.                                       |
| `alpha`      | `bool`  | Limits all matches to alphanumeric tokens.                                |
| `tokens`     | `array` | A list of tokens to be transformed into a non-capturing group.            |
| `exceptions` | `array` | An array of strings to be ignored.                                        |
| `vocab`      | `bool`  | If false, disables all active vocabularies for this rule (default: true). |

`repetition` looks for repeated occurrences of its tokens.

```yaml
extends: repetition
message: "'%s' is repeated!"
level: error
alpha: true
tokens:
  - '[^s.!?]+'
```

## [Vale.Repetition](#valerepetition)

Vale includes a [built-in implementation](https://docs.vale.sh/topics/styles#vale) of `repetition` that can be used to flag repeated words such as “the the” or “and and”. This rule will catch almost any instance of a repeated word, including across markup boundaries:

```markdown
See the Mermaid [Mermaid user guide][1].
```

[occurrence](https://docs.vale.sh/checks/occurrence) [consistency](https://docs.vale.sh/checks/consistency)

# consistency

Learn about the consistency extension point.

| Name         | Type    | Description                                                       |
| ------------ | ------- | ----------------------------------------------------------------- |
| `nonword`    | `bool`  | Removes the default word boundaries (`\b`).                       |
| `ignorecase` | `bool`  | Makes all matches case-insensitive.                               |
| `either`     | `array` | A map of `option 1: option 2` pairs of which only one may appear. |

`consistency` will ensure that a key and its value (e.g., “advisor” and “adviser”) don’t both occur in its scope.

```yaml
extends: consistency
message: "Inconsistent spelling of '%s'."
level: error
ignorecase: true

# We only want one of these to appear.
either:
  advisor: adviser
  centre: center
```

[repetition](https://docs.vale.sh/checks/repetition) [conditional](https://docs.vale.sh/checks/conditional)

# conditional

Learn about the conditional extension point.

| Name         | Type     | Description                                                               |
| ------------ | -------- | ------------------------------------------------------------------------- |
| `ignorecase` | `bool`   | Makes all matches case-insensitive.                                       |
| `first`      | `string` | The antecedent of the statement.                                          |
| `second`     | `string` | The consequent of the statement.                                          |
| `vocab`      | `bool`   | If false, disables all active vocabularies for this rule (default: true). |
| `exceptions` | `array`  | An array of strings to be ignored.                                        |

```yaml
extends: conditional
message: "'%s' has no definition"
level: error
scope: text
ignorecase: false
# Ensures that the existence of 'first'
# implies the existence of 'second'.
first: '\b([A-Z]{3,5})\b'
second: '(?:\b[A-Z][a-z]+ )+\(([A-Z]{3,5})\)'
# ... with the exception of these:
exceptions:
  - ABC
  - ADD
```

For example, consider the following text:

> According to Wikipedia, the World Health Organization (WHO) is a specialized agency of the United Nations that is concerned with international public health. We can now use WHO because it has been defined, but we can’t use DAFB because people may not know what it represents. We can use `DAFB` when it’s presented as code, though.

Using the above text with our example rule yields the following:

```bash
test.md:1:224:style.UnexpandedAcronyms:'DAFB' has no definition
```

`conditional` also takes an optional `exceptions` list. Any token listed as an exception won’t be flagged.

## [Lookarounds](#lookarounds)

Regular expression lookarounds can be used to restrict the capture of the rule, allowing for more complex conditional statements. For example, the following rule will flag any MDX-style import that is not used:

```yaml
extends: conditional
message: "'%s' has been imported but not used."
level: error
scope: raw
first: '(?<=import )(\w+)(?= from)'
second: '(?<=<)(\w+)'
```

See the [regex guide](https://docs.vale.sh/guides/regex) for more information.

[consistency](https://docs.vale.sh/checks/consistency) [capitalization](https://docs.vale.sh/checks/capitalization)

# capitalization

Learn about the capitalization extension point.

| Name         | Type     | Description                                                                                                          |
| ------------ | -------- | -------------------------------------------------------------------------------------------------------------------- |
| `match`      | `string` | `$title`, `$sentence`, `$lower`, `$upper`, or a pattern.                                                             |
| `style`      | `string` | AP or Chicago; only applies when match is set to `$title` (default: AP).                                             |
| `exceptions` | `array`  | An array of strings to be ignored.                                                                                   |
| `indicators` | `array`  | An array of suffixes that indicate the next token should be ignored.                                                 |
| `threshold`  | `float`  | The minimum proportion of words that must be (un)capitalized for a sentence to be considered correct (default: 0.8). |
| `prefix`     | `string` | A constant prefix to ignore during case conversion.                                                                  |
| `vocab`      | `bool`   | If false, disables all active vocabularies for this rule (default: true).                                            |

`capitalization` checks that the text in the specified scope matches the case of `match`.

```yaml
extends: capitalization
message: "'%s' should be in title case"
level: warning
scope: heading
# $title, $sentence, $lower, $upper, or a pattern.
match: $title
# AP or Chicago; only applies when match is set to
# $title.
style: AP
exceptions:
  - ABC
  - add
```

## [styles](#styles)

The `capitalization` extension point supports two styles: “AP” and “Chicago.”

The “AP” style enforces the rules of the Associated Press Stylebook:

* Capitalize the first word and the last word of the title.
* Capitalize “to” in infinitives.
* Do not capitalize articles, conjunctions, and prepositions of three letters or fewer.

The “Chicago” style enforces the rules of The Chicago Manual of Style:

* Capitalize the first word and the last word of the title.
* Do not capitalize articles (a, an, the), coordinating conjunctions (and, but, or, for, nor), and prepositions, regardless of length.

## [prefix](#prefix)

The `prefix` option allows you to specify a constant prefix to ignore during case conversion. For example,

```yaml
extends: capitalization
message: "'%s' should be sentence-cased."
scope: heading
match: $sentence
# sentence-cased, but allows for a common prefix:
#
# E.g.,
#
# a. This is my heading
prefix: '^[a-z]\.\s'
```

In this example, `^[a-z]\.\s` is used to ignore the common prefix.

## [message](#message)

`capitalization` can have one or two `%s` format specifiers in its message. This allows us to do either of the following:

```yaml
message: "Found: '%s'; expected: '%s'."
# or
message: "'%s' should use title-style capitalization."
```

[conditional](https://docs.vale.sh/checks/conditional) [metric](https://docs.vale.sh/checks/metric)

# metric

Learn about the metric extension point.

{% hint style="info" %}
Heads up!

When writing conditions, be sure to use floating-point numbers. For example, use `"== 8.0"` instead of `"== 8"`.
{% endhint %}

| Name        | Type     | Description                                                    |
| ----------- | -------- | -------------------------------------------------------------- |
| `formula`   | `string` | A formula of pre-defined variables to be evaluated.            |
| `condition` | `string` | A binary condition upon which `formula` will trigger an alert. |

`metric` enforces arbitrary formulas based on pre-defined, built-in variables.

```yaml
extends: metric
message: 'Try to keep the Flesch-Kincaid grade level (%s) below 8.'
link: |
  https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests

formula: |
  (0.39 * (words / sentences)) + (11.8 * (syllables / words)) - 15.59

condition: '> 8.0'
```

## [Variables](#variables)

The table below summarizes all available variables:

|       Variable       |                                    Description                                   |
| :------------------: | :------------------------------------------------------------------------------: |
|     `blockquote`     |                         The number of `blockquote` tags.                         |
|     `characters`     |                             The number of characters.                            |
|    `complex_words`   | The number of polysyllabic words without common suffixes (`es`, `ed`, `ing`, …). |
|    `heading.h{n}`    |    The number of headings at the specified level (for example, `heading.h1`).    |
|        `list`        |                         The number of `ol` and `ul` tags.                        |
|     `long_words`     |                 The number of words with more than 6 characters.                 |
|     `paragraphs`     |                             The number of paragraphs.                            |
| `polysyllabic_words` |                  The number of words with more than 2 syllables.                 |
|         `pre`        |                             The number of `pre` tags.                            |
|      `sentences`     |                             The number of sentences.                             |
|      `syllables`     |                             The number of syllables.                             |
|        `words`       |                               The number of words.                               |

Since the pre-defined variables are calculated using the entire document, all `metric`-based rules are [`summary`-scoped](https://docs.vale.sh/topics/scopes).

## [Operators](#operators)

In addition to using the variables listed above, a `formula` may also use the following operators:

|    Operator    |      Description      |
| :------------: | :-------------------: |
|       `+`      |        Addition       |
|       `-`      |      Subtraction      |
|       `*`      |     Multiplication    |
|       `/`      |        Division       |
| `math.sqrt(x)` |   Square root of `x`  |
|  `math.abs(x)` | Absolute value of `x` |

A `condition` may use one of `>`, `<`, `==`, `>=`, and `<=`.

## [message](#message)

The result of a `formula` will be compared to its `condition` and inserted into its `message` format specifier (`%s`).

[capitalization](https://docs.vale.sh/checks/capitalization) [spelling](https://docs.vale.sh/checks/spelling)

# spelling

Learn about the spelling extension point.

| Name           | Type     | Description                                                                                        |
| -------------- | -------- | -------------------------------------------------------------------------------------------------- |
| `custom`       | `bool`   | Turn off the default filters for acronyms, abbreviations, and numbers.                             |
| `filters`      | `array`  | An array of patterns to ignore during spell checking.                                              |
| `ignore`       | `string` | A relative path (from `StylesPath`) to a file consisting of one word per line to ignore.           |
| `dicpath`      | `string` | The location to look for `.dic` and `.aff` files. Can be absolute or relative to the `StylesPath`. |
| `dictionaries` | `array`  | An array of dictionaries to load.                                                                  |
| `append`       | `bool`   | Adds the array of dictionaries after the default Vale dictionary, instead of replacing it.         |

`spelling` implements spell checking based on Hunspell-compatible dictionaries.

```yaml
# Uses the built-in dictionary and filters.
extends: spelling
message: "Did you really mean '%s'?"
level: error
```

By default, `spelling` includes a custom, open-source [dictionary for American English](https://github.com/errata-ai/en_US-web).

## [Dictionaries](#dictionaries)

You may instead use the `dictionaries` key to list multiple custom dictionaries:

```yaml
extends: spelling
message: "'%s' is a typo!"
dictionaries:
  - en_US
  - en_medical
```

The `spelling` extension point will look for `en_US.{dic,aff}` and `en_medical.{dic,aff}` files in `<StylesPath>/config/dictionaries`.

You can also use the `DICPATH` environment variable or the `dicpath` key.

## [Filters](#filters)

Vale comes with a set of built-in filters, as described in the table below:

| Filter                    | Description                                         |
| ------------------------- | --------------------------------------------------- |
| `[A-Z]{1}[a-z]+[A-Z]+\w+` | Mixed-cased words (such as “MongoDB”).              |
| `[^a-zA-Z_']`             | Words containing non-word tokens (such as numbers). |
| `[A-Z]+$`                 | Upper-cased words.                                  |

You can also choose define you own filters either with or without the built-in ones enabled:

```yaml
extends: spelling
message: "Did you really mean '%s'?"
level: error
# This disables the built-in filters. If you omit this
# key or set it to false, custom filters (see below) are
# added on top of the built-in ones.
custom: true
# A "filter" is a regular expression specifying words
# to ignore during spell checking.
filters:
  # Ignore all words starting with 'py'.
  #
  # e.g., 'PyYAML'.
  - '[pP]y.*\b'
```

## [Ignore files](#ignore-files)

Ignore files are plain-text files that list words to be ignored during spell check (one case-insensitive entry per line). For example:

```
destructuring
transpiler
```

You can name these files anything you’d like and reference them relative to the active `<StylesPath>/config/ignore` directory.

```yaml
extends: spelling
message: "Did you really mean '%s'?"
level: error
ignore:
  - ignore1.txt
  - ignore2.txt
```

See [Vocabularies](https://docs.vale.sh/keys/vocabularies) for information on rule-agnostic terminology lists.

[metric](https://docs.vale.sh/checks/metric) [sequence](https://docs.vale.sh/checks/sequence)

# sequence

Learn about the sequence extension point.

| Name         | Type         | Description                                    |
| ------------ | ------------ | ---------------------------------------------- |
| `tokens`     | `[]NLPToken` | A list of tokens with associated NLP metadata. |
| `ignorecase` | `bool`       | Makes all matches case-insensitive.            |

While most extension points focus on writing *style*, `sequence` aims to support grammar-focused rules.

```yaml
extends: sequence

# `%[4]s` is like `%s`, but specifically refers to the
# 4th token in our sequence.
message: |
  The infinitive '%[4]s' after 'be' requires 'to'.
  Did you mean '%[2]s %[3]s *to* %[4]s'?"
tokens:
  - tag: MD
  - pattern: be
  - tag: JJ
  # The `|` notation means that we'll accept `VB`
  # or `VBN` in position 4.
  - tag: VB|VBN
```

Every `sequence`-based rule is required to have at least one `pattern` (such as `pattern: be`, shown above). This becomes the “anchor” of the sequence: we find all instances of the first pattern and then check that the left- and right-hand sides of the sequence match.

Each entry in a sequence is known as an `NLPToken` and has the following structure:

```yaml
# [optional]: A regular expression (required
# if `tag` isn't given).
pattern: '...'

# [optional]: If true, indicates that we
# *shouldn't* match this token.
negate: true # or false

# [optional]: A part-of-speech tag (required
# if `pattern` isn't given).
tag: '...'

# [optional]: An integer meaning that there may
# be up to `n` (3, in this case) tokens between
# this token and the next one.
skip: 3
```

`sequence`-based are [sentence-scoped](https://docs.vale.sh/topics/scopes). See [prose/tagging](https://github.com/jdkato/prose?tab=readme-ov-file#tagging) for a full list of supported part-of-speech tags.

[spelling](https://docs.vale.sh/checks/spelling) [script](https://docs.vale.sh/checks/script)

# script

Learn about the script extension point.

{% hint style="warning" %}
Heads up!

When using `script`-based rules, you're limited to the standard Go [regex syntax](https://pkg.go.dev/regexp/syntax).
{% endhint %}

| Name     | Type     | Description                                            |
| -------- | -------- | ------------------------------------------------------ |
| `script` | `string` | The [Tengo](https://tengolang.com/) script to execute. |

`script` allows for the creation of arbitrary logic-based rules using [Tengo](https://tengolang.com/), a Go-like scripting language.

```yaml
extends: script
message: 'Consider inserting a new section heading at this point.'
link: https://tengolang.com
scope: raw
script: MyScript.tengo
```

Where `MyScript.tengo` is a file containing the Tengo script to execute stored at `$StypesPath/config/scripts`.

````go
text := import("text")

matches := []
// at most 3 paragraphs per section
p_limit := 3

// Remove all instances of code blocks
// since we don't want to count inter-block
// newlines as a new paragraph.
document := text.re_replace("(?s) *(\n```.*?```\n)", scope, "")

count := 0
for line in text.split(document, "\n") {
    if text.has_prefix(line, "#") {
        count = 0 // New section; reset count
    } else if count > p_limit {
        start := text.index(scope, line)
        matches = append(matches, {begin: start, end: start + len(line)})
        count = 0
    } else if text.trim_space(line) == "" {
        count += 1
    }
}
````

{% stepper %}
{% step %}
Use Tengo’s [`text`](https://github.com/d5/tengo/blob/master/docs/stdlib-text.md) module, which provides a number of string- and regex-related utility functions.
{% endstep %}

{% step %}
Process the content in the `scope` variable. `scope` contains text based on the `scope: <scope>` setting for the rule. For more information, see [Scoping](https://docs.vale.sh/topics/scopes).
{% endstep %}

{% step %}
Populate the `matches` array with rule matches. Each match must be a map with the keys:

* `begin`: where the match begins in the content provided by the `scope` variable.
* `end`: where the match ends in the content provided by the `scope` variable.
  {% endstep %}
  {% endstepper %}

[sequence](https://docs.vale.sh/checks/sequence) [suggest](https://docs.vale.sh/fixes/suggest)

# suggest

Learn how to create dynamic suggestions for your rules.

```go
func suggest(match string) []string
```

`suggest` returns an array of suggested replacements for the matched text.

## [script](#script)

```yaml
action:
  name: suggest
  params:
    - scriptName.tengo
```

The `suggest` action allows you to define a custom suggestion script that will be executed for each match. The script should return an array of strings called `suggestions`.

Scripts are written in [Tengo](https://github.com/d5/tengo) and are stored in the `<StylesPath>/config/actions` directory.

Here’s an example script:

```go
text := import("text")

// `match` is provided by Vale and represents the rule's matched text.
made := text.re_replace(`([A-Z]\w+)([A-Z]\w+)`, match, `$1-$2`)

made = text.replace(made, "-", "_", 1)
made = text.to_lower(made)

// `suggestions` is required by Vale and represents the script's output.
suggestions := [made]
```

We would save this script as `CamelToSnake.tengo` and then reference it in our rule:

```yaml
extends: existence
message: "'%s' should be in snake_case."
nonword: true
level: error
action:
  name: suggest
  params:
    - CamelToSnake.tengo
tokens:
  - '[A-Z]\w+[A-Z]\w+'
```

## [spellings](#spellings)

```yaml
action:
  name: suggest
  params:
    - spellings
```

`spellings` returns the top 5 spelling suggestions for the matched text from all active dictionaries.

Suggestions are ordered by calculating the [Levenshtein distance](https://pkg.go.dev/github.com/adrg/strutil@v0.3.0/metrics#Levenshtein) between the matched text and the dictionary words.

[script](https://docs.vale.sh/checks/script) [replace](https://docs.vale.sh/fixes/replace)

# replace

Learn how to create static suggestions for your rules.

```go
func replace(match string) []string
```

`replace` returns an array of user-provided replacements.

```yaml
action:
  name: replace
  params:
    - option1
    - option2
    ...
```

Rules that extend `substitution` or `capitalization` will automatically populate the `params` array, so you can simply provide the `name`:

```yaml
action:
  name: replace
```

[suggest](https://docs.vale.sh/fixes/suggest) [remove](https://docs.vale.sh/fixes/remove)

# remove

## remove

Learn how to remove matches from your content.

```go
func remove(match string)
```

`remove` will remove the matched text of any rule.

```yaml
extends: existence
message: "Don't use an ellipsis in documentation."
nonword: true
action:
  name: remove
tokens:
  - '...'
```

[replace](https://docs.vale.sh/fixes/replace) [edit](https://docs.vale.sh/fixes/edit)

# edit

Learn how to make in-place edits to your matches.

```go
func edit(match string) string
```

`edit` will perform an in-place edit on the match string according to the provided parameters.

## [https://vale.sh/docs/fixers/edit#regex](#regex)

Replace the provided regex pattern with the given string.

```yaml
extends: existence
message: Consider removing '%s'
level: warning
action:
  name: edit
  params:
    - regex
    - '([A-Z]\w+)([A-Z]\w+)' # pattern
    - '$1-$2' # repl
tokens:
  - '([A-Z]\w+)([A-Z]\w+)'
```

This is equivalent to the following Go code:

```go
match = pattern.ReplaceAllString(match, repl)
```

## [https://vale.sh/docs/fixers/edit#trim\_right](#trim_right)

Trim the first parameter from the end of the matched text.

```yaml
extends: existence
message: "Don't use exclamation points in text."
nonword: true
action:
  name: edit
  params:
    - trim_right
    - '!'
tokens:
  - '\w+!(?:\s|$)'
```

## [https://vale.sh/docs/fixers/edit#trim\_left](#trim_left)

Trim the first parameter from the start of the matched text.

```yaml
extends: existence
message: "'%s' too many spaces."
level: warning
nonword: true
action:
  name: edit
  params:
    - trim_left
    - ' '
tokens:
  - '(?<=[a-z][.!?] ) [A-Z]'
```

[remove](https://docs.vale.sh/fixes/remove) [Front Matter](https://docs.vale.sh/formats/front-matter)

# Front Matter

Learn how Vale handles front matter.

Linting front matter fields is supported in Markdown, AsciiDoc, reStructuredText, MDX, and Org files.

There are 3 supported front matter types – YAML, TOML, and JSON:

![Front Matter Formats](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/CJ22fM232r8IGidk6aPy/formats.png)

Each field is dynamically assigned its own scope, allowing you to write rules that target specific ones:

```yaml
---
title: 'My document'
description: "A short summary of the document's purpose."
author: 'John Doe'
---
```

Using the example above, the generated scopes would be `text.frontmatter.title`, `text.frontmatter.description`, and `text.frontmatter.author`.

A rule can then use these in its `scope:` field:

```yaml
extends: capitalization
message: "'%s' should be in title case"
level: warning
scope: text.frontmatter.title
```

This rule would then only be applied to the `title` field in the front matter.

[Markdown](https://docs.vale.sh/formats/markdown)

# Markdown

Learn how Vale handles Markdown content.

[GitHub-Flavored Markdown](https://github.github.com/gfm) support is built in. The supported extensions are `.md`, `.mdown`, `.markdown`, and `.markdn`.

By default, Vale ignores:

* Indented blocks: Blocks starting with four or more spaces.
* Fenced blocks: Blocks surrounded by three or more backticks.
* Code spans: Text surrounded by backticks.
* URLs: See [URL handling](https://github.com/errata-ai/vale/issues/320) for more information.

## [Comments](#comments)

Vale supports comment-based configuration in Markdown files:

* Turn Vale off entirely:

```html
<!-- vale off -->

This text will be ignored.

<!-- vale on -->
```

* Turn off a specific rule:

```html
<!-- vale Style.Redundancy = NO -->

This is some text ACT test

<!-- vale Style.Redundancy = YES -->
```

* Turn off specific match(es) within a rule:

```html
<!-- vale Style.Redundancy["ACT test","OTHER"] = NO -->

This is some text ACT test

<!-- vale Style.Redundancy["ACT test","OTHER"] = YES -->
```

* Turn on or off specific styles:

```html
<!-- vale StyleName1 = YES -->
<!-- vale StyleName2 = NO -->
```

* Set styles (enabling them and switching off any other styles):

```html
<!-- vale style = StyleName1 -->
<!-- vale styles = StyleName1, StyleName2 -->
```

[Front Matter](https://docs.vale.sh/formats/front-matter) [AsciiDoc](https://docs.vale.sh/formats/asciidoc)

# AsciiDoc

Learn how Vale handles AsciiDoc content.

AsciiDoc is supported through the external program [Asciidoctor](https://asciidoctor.org/). See their [installation](https://docs.asciidoctor.org/asciidoctor/latest/install) instructions to get started. You’ll need to ensure that the `asciidoctor` executable is available in your `$PATH`.

The supported extensions are `.adoc`, `.asciidoc`, and `.asc`.

By default, Vale ignores:

* [Literals and source code](https://docs.asciidoctor.org/asciidoc/latest/syntax-quick-reference/#literals-and-source-code).
* URLs: See [URL handling](https://github.com/errata-ai/vale/issues/320) for more information.

## [Attributes](#attributes)

You can customize how `asciidoctor` is called by passing [document attributes](https://docs.asciidoctor.org/asciidoc/latest/attributes/document-attributes-ref/):

```ini
StylesPath = styles

[asciidoctor]
# attribute = value
#
# where 'YES' enables and 'NO' disables.

# enable
experimental = YES

# assign a specific value
attribute-missing = drop

[*.adoc]
BasedOnStyles = Vale
```

## [Comments](#comments)

Heads up!

Make sure the surround the inline passthrough statements with newlines, as shown below.

Vale supports comment-based configuration in AsciiDoc files:

* Turn Vale off entirely:

```adoc
pass:[<!-- vale off -->]

This text will be ignored.

pass:[<!-- vale on -->]
```

* Turn off a specific rule:

```adoc
pass:[<!-- vale Style.Redundancy = NO -->]

This is some text ACT test

pass:[<!-- vale Style.Redundancy = YES -->]
```

* Turn off specific match(es) within a rule:

```adoc
pass:[<!-- vale Style.Redundancy["ACT test","OTHER"] = NO -->]

This is some text ACT test

pass:[<!-- vale Style.Redundancy["ACT test","OTHER"] = YES -->]
```

* Turn on or off specific styles:

```adoc
pass:[<!-- vale StyleName1 = YES -->]
pass:[<!-- vale StyleName2 = NO -->]
```

* Set styles (enabling them and switching off any other styles):

```adoc
pass:[<!-- vale style = StyleName1 -->]
pass:[<!-- vale styles = StyleName1, StyleName2 -->]
```

# MDX

Learn how Vale handles MDX content.

[MDX](https://mdxjs.com/) is supported through the external program [`mdx2vast`](https://github.com/jdkato/mdx2vast). To get started, you’ll need to install the CLI:

```bash
npm install -g mdx2vast
```

You’ll need to ensure that the `mdx2vast` executable is available in your `$PATH` (this should happen automatically).

The supported extension is `.mdx`.

By default, Vale ignores:

* Fenced blocks: Blocks surrounded by three or more backticks.
* Code spans: Text surrounded by backticks.
* URLs: See [URL handling](https://github.com/jdkato/mdx2vast) for more information.
* JSX expressions and components.
* ESM imports and exports.

## [Comments](#comments)

Vale supports comment-based configuration in MDX files:

* Turn Vale off entirely:

```mdx
{/* vale off */}

This text will be ignored.

{/* vale on */}
```

* Turn off a specific rule:

```mdx
{/* vale Style.Redundancy = NO */}

This is some text ACT test

{/* vale Style.Redundancy = YES */}
```

* Turn off specific match(es) within a rule:

```mdx
{/* vale Style.Redundancy["ACT test","OTHER"] = NO */}

This is some text ACT test

{/* vale Style.Redundancy["ACT test","OTHER"] = YES */}
```

* Turn on or off specific styles:

```mdx
{/* vale StyleName1 = YES */}

{/* vale StyleName2 = NO */}
```

* Set styles (enabling them and switching off any other styles):

```mdx
{/* vale style = StyleName1 */}
{/* vale styles = StyleName1, StyleName2 */}
```

[AsciiDoc](https://docs.vale.sh/formats/asciidoc) [HTML](https://docs.vale.sh/formats/html)

# HTML

Learn how Vale handles HTML content.

HTML5 support is built in. The supported extensions are `.html`, `.htm`, `.shtml`, and `.xhtml`.

By default, Vale ignores `script`, `style`, `pre`, `code`, and `tt` tags, as well as URLs (see [URL handling](https://github.com/errata-ai/vale/issues/320) for more information).

## [Comments](#comments)

Vale supports comment-based configuration in HTML files:

* Turn Vale off entirely:

```html
<!-- vale off -->

This text will be ignored.

<!-- vale on -->
```

* Turn off a specific rule:

```html
<!-- vale Style.Redundancy = NO -->

This is some text ACT test

<!-- vale Style.Redundancy = YES -->
```

* Turn off specific match(es) within a rule:

```html
<!-- vale Style.Redundancy["ACT test","OTHER"] = NO -->

This is some text ACT test

<!-- vale Style.Redundancy["ACT test","OTHER"] = YES -->
```

* Turn on or off specific styles:

```html
<!-- vale StyleName1 = YES -->
<!-- vale StyleName2 = NO -->
```

* Set styles (enabling them and switching off any other styles):

```html
<!-- vale style = StyleName1 -->
<!-- vale styles = StyleName1, StyleName2 -->
```

# reStructuredText

Learn how Vale handles reStructuredText content.

reStructuredText is supported through the external program [`rst2html`](http://docutils.sourceforge.net/docs/user/tools.html#rst2html-py). To get started, you’ll need to install the [`docutils`](https://pypi.org/project/docutils/) package:

```bash
pip install docutils
```

You’ll need to ensure that the `rst2html` executable is available in your `$PATH` (this should happen automatically).

The supported extensions are `.rst` and `.rest`.

By default, Vale ignores:

* [Literal blocks](https://docutils.sourceforge.io/docs/user/rst/quickref.html#literal-blocks).
* [Inline literals](https://docutils.sourceforge.io/docs/user/rst/quickref.html#inline-markup).
* URLs: See [URL handling](https://github.com/errata-ai/vale/issues/320) for more information.

## [Comments](#comments)

Vale supports comment-based configuration in reStructuredText files:

* Turn Vale off entirely:

```rst
.. vale off

This text will be ignored.

.. vale on
```

* Turn off a specific rule:

```rst
.. vale Style.Redundancy = NO

This is some text ACT test

.. vale Style.Redundancy = YES
```

* Turn off specific match(es) within a rule:

```rst
.. vale Style.Redundancy["ACT test","OTHER"] = NO

This is some text ACT test

.. vale Style.Redundancy["ACT test","OTHER"] = YES
```

* Turn on or off specific styles:

```rst
.. vale StyleName1 = YES
.. vale StyleName2 = NO
```

* Set styles (enabling them and switching off any other styles):

```rst
.. vale style = StyleName1
.. vale styles = StyleName1, StyleName2
```

[HTML](https://docs.vale.sh/formats/html) [XML](https://docs.vale.sh/formats/xml)

# XML

Learn how Vale handles XML content.

XML is supported through the external program [`xsltproc`](http://xmlsoft.org/XSLT/xsltproc.html). To install, see:

* [Chocolatey](https://community.chocolatey.org/packages/xsltproc) (Windows): `choco install xsltproc`.
* [Homebrew](https://formulae.brew.sh/formula/libxslt) (macOS): `brew install libxslt`.
* Debian/Ubuntu/apt-based systems: `apt-get install xsltproc`.

You’ll need to ensure that the `xsltproc` executable is available in your `$PATH`.

The supported extension is `.xml`.

You also need to provide a version 1.0 XSL Transformation (XSLT) for converting to HTML:

{% code title=".vale.ini" %}

```ini
[*.xml]
Transform = docbook-xsl-snapshot/html/docbook.xsl
```

{% endcode %}

Once converted, Vale will follow the same rules as it does for [HTML](https://docs.vale.sh/formats/html).

Related formats: [reStructuredText](https://docs.vale.sh/formats/restructuredtext) [Org](https://docs.vale.sh/formats/org)

# Org

Learn how Vale handles Org content.

[Org](https://orgmode.org/) support is built in. The supported extension is `.org`.

By default, Vale ignores:

* [Code blocks](https://orgmode.org/org.html#Structure-of-Code-Blocks).
* [Literal examples](https://orgmode.org/org.html#Literal-Examples).
* [Code and verbatim strings](https://orgmode.org/org.html#Emphasis-and-Monospace-1).
* URLs: See [URL handling](https://orgmode.org/org.html#Structure-of-Code-Blocks) for more information.

## [Comments](#comments)

Vale supports comment-based configuration in Org files:

* Turn Vale off entirely:

```org
# vale off

This text will be ignored.

# vale on
```

* Turn off a specific rule:

```org
# vale Style.Redundancy = NO

This is some text ACT test

# vale Style.Redundancy = YES
```

* Turn off specific match(es) within a rule:

```org
# vale Style.Redundancy["ACT test","OTHER"] = NO

This is some text ACT test

# vale Style.Redundancy["ACT test","OTHER"] = YES
```

* Turn on or off specific styles:

```org
# vale StyleName1 = YES
# vale StyleName2 = NO
```

* Set styles (enabling them and switching off any other styles):

```org
# vale style = StyleName1
# vale styles = StyleName1, StyleName2
```

# DITA

Learn how Vale handles DITA content.

{% hint style="warning" %}
Due to the dependency on the third-party `dita` command, you'll likely experience worse performance with DITA files compared to other formats.
{% endhint %}

DITA is supported through the [DITA Open Toolkit](https://www.dita-ot.org/). You’ll need to follow the [installation instructions](https://www.dita-ot.org/dev/topics/installing-client.html), including the optional step of adding the absolute path for the `bin` directory to the `PATH` system variable.

The supported extension is `.dita`.

Vale ignores `<codeblock>`, `<tt>`, and `<codeph>` elements by default.

[Org](https://docs.vale.sh/formats/org) [Code](https://docs.vale.sh/formats/code)

# Code

Learn how Vale handles source code.

Vale supports linting source code comments in a number of languages (see below).

| Language   | Extensions                           | Scopes                                                                                                                                                                                                                                       |
| ---------- | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| C          | `.c`, `.h`                           | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| C#         | `.cs`, `.csx`                        | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| C++        | `.cpp`, `.cc`, `.cxx`, `.hpp`        | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| CSS        | `.css`                               | <p><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                                                                                  |
| Go         | `.go`                                | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| Haskell    | `.hs`                                | <p><code>--</code> (<code>text.comment.line.ext</code>),<br><code>{-</code> (<code>text.comment.block.ext</code>)</p>                                                                                                                        |
| Java       | `.java`, `.bsh`                      | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| JavaScript | `.js`                                | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| Julia      | `.jl`                                | <p><code>#</code> (<code>text.comment.line.ext</code>),<br><code>"..."</code> (<code>text.comment.line.ext</code>)<br><code>#=</code> (<code>text.comment.block.ext</code>),<br><code>"""</code> (<code>text.comment.block.ext</code>)</p>   |
| LESS       | `.less`                              | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| Lua        | `.lua`                               | <p><code>--</code> (<code>text.comment.line.ext</code>),<br><code>--\[\[</code> (<code>text.comment.block.ext</code>)</p>                                                                                                                    |
| Perl       | `.pl`, `.pm`, `.pod`                 | `#` (`text.comment.line.ext`)                                                                                                                                                                                                                |
| PHP        | `.php`                               | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>#</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p> |
| PowerShell | `.ps1`                               | <p><code>#</code> (<code>text.comment.line.ext</code>),<br><code><#...#></code> (<code>text.comment.line.ext</code>),<br><code><#</code> (<code>text.comment.block.ext</code>)</p>                                                           |
| Protobuf   | `.proto`                             | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| Python     | `.py`, `.py3`, `.pyw`, `.pyi`, `rpy` | <p><code>#</code> (<code>text.comment.line.ext</code>),<br><code>"""</code> (<code>text.comment.block.ext</code>)</p>                                                                                                                        |
| R          | `.r`, `.R`                           | `#` (`text.comment.line.ext`)                                                                                                                                                                                                                |
| Ruby       | `.rb`                                | <p><code>#</code> (<code>text.comment.line.ext</code>),<br><code>^=begin</code> (<code>text.comment.block.ext</code>)</p>                                                                                                                    |
| Rust       | `.rs`                                | `//` (`text.comment.line.ext`)                                                                                                                                                                                                               |
| Sass       | `.sass`                              | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| Scala      | `.scala`, `.sbt`                     | `//` (`text.comment.line.ext`)                                                                                                                                                                                                               |
| Swift      | `.swift`                             | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |
| TypeScript | `.ts`, `.tsx`                        | <p><code>//</code> (<code>text.comment.line.ext</code>),<br><code>/*...*/</code> (<code>text.comment.line.ext</code>),<br><code>/\*</code> (<code>text.comment.block.ext</code>)</p>                                                         |

## [Associations](#associations)

In many languages, it’s common for comments to contain *embedded markup* (e.g., Markdown, reStructuredText, etc.) within them. For example, consider the following Rust doc comment:

````rust
impl Person {
    /// Creates a person with the given name.
    ///
    /// # Examples
    ///
    /// ```
    /// // You can have rust code between fences
    /// // inside the comments If you pass --test
    /// // to `rustdoc`, it will even test it for
    /// // you!
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person {
            name: name.to_string(),
        }
    }
}
````

If the embedded markup is one of the supported formats, you can associate the `comment` scope with a `markup` type. This will allow you to lint the embedded markup as if it were a standalone file.

```ini
StylesPath = styles
MinAlertLevel = suggestion

[formats]
# Rust + Markdown
rs = md

[*.{rs,md}]
BasedOnStyles = Vale
```

Once a markup format has been assigned, you can make use of all the supported features of that format (such as ignore patterns and comment-based configuration) in your source code comments.

[DITA](https://docs.vale.sh/formats/dita) [LSP](https://docs.vale.sh/guides/lsp)

# LSP

Docs

Guides

LSP

## LSP

Get started with Vale's Language Server.

The Vale Language Server (`vale-ls`) is an implementation of the [Language Server Protocol (LSP)](https://microsoft.github.io/language-server-protocol/) that acts as a wrapper around a local installation of Vale, providing autocomplete, diagnostics, hover popups, and more, in many popular text editors and IDEs.

Some available integrations include:

* [CircleCI](https://circleci.com/developer/orbs/orb/circleci/vale)
* [Emacs](https://github.com/tpeacock19/flymake-vale)
* [GitHub Actions](https://github.com/errata-ai/vale-action)
* [Git Hooks](https://docs.vale.sh/integrations/pre-commit)
* [JetBrains](https://plugins.jetbrains.com/plugin/19613-vale-cli/docs)
* [Laravel](https://github.com/beyondcode/laravel-prose-linter)
* [Obsidian](https://github.com/ChrisChinchilla/obsidian-vale)
* [Oxygen XML](https://www.oxygenxml.com/doc/versions/23.1/ug-editor/topics/vale-linter-addon.html)
* [Sublime Text](https://packagecontrol.io/packages/LSP-vale-ls) LSP
* [Neovim](https://github.com/dense-analysis/ale) LSP
* [VS Code](https://github.com/chrischinchilla/vale-vscode) LSP
* [Qt Creator](https://wiki.qt.io/Setting_Up_Vale)
* [Zed](https://github.com/koozz/zed-vale) LSP

### [Configuration](#configuration)

The server supports the following `initializationParams`:

| Parameter       | Default | Description                                                                                                                                                                    |
| --------------- | ------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `installVale`   |  `true` | Automatically install and update Vale to a `vale_bin` folder in the same location as `vale-ls`. If `false`, the `vale` executable needs to be available on the user’s `$PATH`. |
| `filter`        |  `None` | An [output filter](https://vale.sh/manual/filter/) to apply when calling Vale.                                                                                                 |
| `configPath`    |  `None` | An absolute path to a `.vale.ini` file to be used as the default configuration.                                                                                                |
| `syncOnStartup` |  `true` | Runs `vale sync` upon starting the server.                                                                                                                                     |

To use the server, you’ll need to download the latest release from [GitHub](https://github.com/errata-ai/vale-ls/releases). See the Sublime Text [package](https://packagecontrol.io/packages/LSP-vale-ls) for an example of how to use the server.

[Code](https://docs.vale.sh/formats/code) [Regex](https://docs.vale.sh/guides/regex)

# Regex

Learn how to use regex in Vale.

Vale uses the [`regexp2`](https://github.com/dlclark/regexp2) library to process regular expressions in its rules. This library extends the capabilities of the standard Go [regexp](https://pkg.go.dev/regexp/syntax) package by supporting features like lookaheads, lookbehinds, and lazy quantifiers, which are missing in Go’s built-in regexp implementation.

This guide provides an overview of regex syntax supported by Vale, along with tips for writing regular expressions in [YAML](https://yaml.org/) files.

## [Syntax](#syntax)

For basic information on the supported syntax, see the [Go docs](https://pkg.go.dev/regexp/syntax). For the extended syntax provided by `regexp2`, see their [README](https://github.com/dlclark/regexp2?tab=readme-ov-file#compare-regexp-and-regexp2).

The most commonly used assertion constructs are:

* Positive lookahead: `(?=re)`
* Negative lookahead: `(?!re)`
* Positive lookbehind: `(?<=re)`
* Negative lookbehind: `(?<!re)`

This extended syntax is supported everywhere in Vale, except for `script`-based rules (which are limited to the standard Go regex syntax).

## [YAML](#yaml)

Wrap all regex in single (`'`) or double (`"`) quotes to avoid YAML interpreting special characters:

* Single quotes (`'`): Prevent YAML from interpreting any characters except single quotes themselves.
* Double quotes (`"`): Allow YAML to interpret escape sequences like `\n` and `\t`, so you’ll need to escape backslashes.

In general, this means that you should **prefer single quotes** for most cases:

```yaml
extends: existence
message: Consider removing '%s'
level: warning
# A typical rule with single quotes:
tokens:
  - '([A-Z]\w+)([A-Z]\w+)'
```

If you need to *use* a single quote in your regex, you can escape it with another single quote:

```yaml
extends: existence
message: Consider removing '%s'
level: warning
# A rule with a single quote in the regex:
tokens:
  - '([A-Z]\w+)([A-Z]\w+)''s'
```

## [Vale Studio](#vale-studio)

[Vale Studio](https://studio.vale.sh/) provides a rule editor that integrates with [regex101](https://regex101.com/) to allow you to inspect the compiled regex pattern and test it against sample text. This can be a helpful way to debug your regex patterns.

![Vale Studio](https://content.gitbook.com/content/EMH7s0sC5N9L8xSMXGwW/blobs/XtEeU99fYedU7hEZwzd1/studio.png)

## [Common Issues](#common-issues)

<details>

<summary>Word Boundaries</summary>

In regex, `\b` is a word boundary assertion that matches the position between a word character and a non-word character.

For example, the regex `\bfoo\b` will only match the word “foo” and not “foobar” or “foo-bar”.

By default, [`existence`](https://docs.vale.sh/checks/existence) and [`substitution`](https://docs.vale.sh/checks/substitution) rules in Vale will automatically add word boundaries to the beginning and end of each token.

To disable this behavior, set `nonword` to `true`:

```yaml
extends: existence
message: Consider removing '%s'
nonword: true
tokens:
  - some token
```

</details>

<details>

<summary>Scoping</summary>

For markup-based rules, Vale converts each document to HTML and applies a [scoping](https://docs.vale.sh/topics/scopes) system before running any rules.

This means that if you’re writing a rule that targets markup syntax or needs to match across block boundaries, the results may be different from what you expect.

If you like to apply a rule to the entire, unprocessed document, you can use `scope: raw`:

```yaml
extends: existence
message: Consider removing '%s'
scope: raw
tokens:
  - some token
```

</details>

# Hunspell

Learn how to create and use Hunspell-compatible dictionaries in Vale.

[Hunspell](https://hunspell.github.io/) is a spell-checking engine known for its flexibility and support for complex morphological rules. It powers spell-checking in popular applications like LibreOffice, Mozilla Firefox, and Google Chrome.

Vale uses Hunspell-compatible dictionaries to power its [own spell-checking](https://docs.vale.sh/checks/spelling) features. This guide will discuss the basics of creating and using these dictionaries.

You can find more thorough documentation at the [official repository](https://github.com/hunspell/hunspell?tab=readme-ov-file#documentation). There’s also a well-documented Python port of the library called [spylls](https://github.com/zverok/spylls).

## How does spell-checking in Vale work?

Vale doesn’t use Hunspell directly and doesn’t require it to be installed on your system.

Instead, Vale uses a pure-Go package to parse Hunspell-compatible dictionaries and check the spelling of words. This package supports a (growing) subset of Hunspell’s features.

A Hunspell-compatible dictionary consists of two files:

1. Affix (`.aff`) file: This file defines the morphological rules, including prefixes, suffixes, and other language-specific grammar rules that govern how words are formed.
2. Dictionary (`.dic`) file: This file contains the list of root words and their associated affix codes to specify valid transformations.

You can name these files whatever you like, so long as the `.aff` and `.dic` files are named consistently – for example, `en_US.aff` and `en_US.dic`.

Here’s a minimal example of a dictionary:

```
1
software/M
```

“1” is the number of words in the dictionary and `software/M` is the root word “software” with the affix code `M`. This means that we accept the word “software” and the variations derived from the affix code `M`.

Our affix file would look like this:

```
SET UTF-8

SFX M Y 1
SFX M   0     's         .
```

* `SFX M Y 1`: This line defines a suffix rule (`SFX`) for the affix code `M`. The `Y` indicates that the rule is [cross-productible](https://github.com/hunspell/hunspell/blob/874abbbe65e228df525023afe176b42df34a7a4f/man/hunspell.5#L527) and the `1` indicates that there is one rule.
* `SFX M 0 's .`: This line defines the rule itself. It says that if a word has the affix code `M`, we can add `'s` to the end of the word. The `0` indicates that no part of the base word is removed when applying this suffix. The `.` indicates that there are no conditions for applying this rule.

The end result is that the dictionary will accept both “software” and “software’s”. Other variations like “softwares” or “softwaring” will be rejected.

## Where can I find Hunspell dictionaries?

* [`wooorm/dictionaries`](https://github.com/wooorm/dictionaries?tab=readme-ov-file)
* [`LibreOffice/dictionaries`](https://github.com/LibreOffice/dictionaries)

[Firefox](https://addons.mozilla.org/en-US/firefox/language-tools) and [OpenOffice](https://extensions.openoffice.org/en/search?f%5B0%5D=field_project_tags%3A157) also provide Language Packs that include Hunspell dictionaries.

# Globbing

Learn how to use glob patterns in Vale.

[Glob](https://en.wikipedia.org/wiki/Glob_\(programming\)) patterns are used for matching file paths in a filesystem. They are commonly employed in command-line tools, scripting languages, and libraries to specify sets of filenames or directories.

This guide will cover the basics of using glob patterns in Vale.

## [Syntax](#syntax)

Vale supports the following glob syntax:

* `/` to separate path segments.
* `*` to match zero or more characters in a path segment.
* `?` to match on one character in a path segment.
* `**` to match zero or more directories.
* `[]` to declare a range of characters to match.
* `{}` to declare a set of patterns to match.
* `[!...]` to negate a range of characters to match.

Additionally, when using the `--glob` flag, you can use the `!` prefix to negate the *entire* pattern:

```sh
# Match all files except those with a `.md` or `.py` extension.
$ vale --glob='!**/*.{md,py}' path/to/files
```

## [Precedence](#precedence)

When evaluating glob patterns, the result of using the `--glob` flag is computed *first*, followed by any sections in the `.vale.ini` file.

For example, given the following `.vale.ini`:

```ini
StylesPath = styles

[*.md]
BasedOnStyles = Vale
```

And this directory structure:

```
cases/test/
├── a.md
├── b
│   └── b.md
└── c.md
```

We can then run Vale with the following command:

```bash
$ vale --glob='!**/b/*' .
 cases/test/c.md
 8:37  warning  Found 'Here'.  Test.Test

 cases/test/a.md
 8:37  warning  Found 'Here'.  Test.Test
```

You’ll notice that the `b.md` file is not included in the output because the `--glob` flag takes precedence over the `.vale.ini` file.

[Regex](https://docs.vale.sh/guides/regex) [Hunspell](https://docs.vale.sh/guides/hunspell)

# pre-commit

Use Vale with pre-commit, a Git Hooks framework.

[`pre-commit`](https://pre-commit.com/index.html) is a framework for managing and maintaining multi-language pre-commit hooks. It’s designed to be language-agnostic and can be used with any project.

To get started, here’s an example configuration that incorporates running `vale sync` prior to running Vale:

```yaml
repos:
  - repo: https://github.com/errata-ai/vale
    rev: 16d3a7f
    hooks:
      - id: vale
        name: vale sync
        pass_filenames: false
        args: [sync]
      - id: vale
        args: [--output=line, --minAlertLevel=error]
```

<https://github.com/errata-ai/vale-action> <https://plugins.jetbrains.com/plugin/19613-vale-cli/docs>

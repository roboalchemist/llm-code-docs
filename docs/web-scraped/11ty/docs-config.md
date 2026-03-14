# Source: https://www.11ty.dev/docs/config/

Title: Configuration

URL Source: https://www.11ty.dev/docs/config/

Markdown Content:
Configuration — Eleventy
===============

[Skip to navigation](https://www.11ty.dev/docs/config/#skip-nav)[Skip to main content](https://www.11ty.dev/docs/config/#skip-content)

[Build Awesome](https://www.kickstarter.com/projects/fontawesome/build-awesome-pro?ref=43ttgb)[Font Awesome](https://fontawesome.com/)[Web Awesome](https://webawesome.com/)[Podcast Awesome](https://www.podcastawesome.com/)[Blog Awesome](https://blog.fontawesome.com/)

*   [11ty](https://www.11ty.dev/)
*   [Get Started](https://www.11ty.dev/docs/)
*   [Blog](https://www.11ty.dev/blog/)
*   [Community](https://www.11ty.dev/docs/community/)
*   
Versions

    *   [`v3`Stable](https://www.11ty.dev/docs/)
    *   [`v2`](https://v2.11ty.dev/docs/)
    *   [`v1`](https://v1.11ty.dev/docs/)
    *   [`v0`](https://v0.11ty.dev/docs/)
    *   [History](https://www.11ty.dev/docs/versions/)
    *   [Firehose](https://www.11ty.dev/firehose/)

*   Search Search
*   [GitHub](https://github.com/11ty/eleventy/)
*   [YouTube](https://www.youtube.com/c/EleventyVideo)
*   [Mastodon](https://neighborhood.11ty.dev/@11ty)
*   [Bluesky](https://bsky.app/profile/11ty.dev)
*   [Discord](https://www.11ty.dev/blog/discord/)

[![Image 1: The possum is Eleventy’s mascot](https://www.11ty.dev/img/built/i65COKQqjG-790.svg)](https://www.kickstarter.com/projects/fontawesome/build-awesome-pro?ref=43ttgb)

[Blog](https://www.11ty.dev/blog/)

[**Eleventy is now Build Awesome**](https://www.11ty.dev/blog/build-awesome/)

[Versions](https://www.11ty.dev/docs/versions/)

Stable[`3.1.2`](https://github.com/11ty/eleventy/releases/tag/v3.1.2)Canary[`4.0.0-alpha.6`](https://github.com/11ty/eleventy/releases/tag/v4.0.0-alpha.6)

*   
Introduction
    *   [Get Started](https://www.11ty.dev/docs/)
    *   [Why Eleventy?](https://www.11ty.dev/#why-should-you-use-eleventy)
        *   [Performance](https://www.11ty.dev/docs/performance/)

    *   Learn
        *   [Glossary](https://www.11ty.dev/docs/glossary/)
        *   [Opening a Terminal](https://www.11ty.dev/docs/terminal-window/)
        *   [Installing JavaScript](https://www.11ty.dev/docs/javascript-runtime/)
        *   [CommonJS, ESM, TypeScript](https://www.11ty.dev/docs/cjs-esm/)

    *   [Starter Projects](https://www.11ty.dev/docs/starter/)
    *   [Tutorials](https://www.11ty.dev/docs/tutorials/)
        *   [Quick Tips](https://www.11ty.dev/docs/quicktips/)

*   
Community
    *   [How can I contribute?](https://www.11ty.dev/docs/community/)
    *   [Code of Conduct](https://www.11ty.dev/docs/code-of-conduct/)
    *   [Blog](https://www.11ty.dev/blog/)
    *   [Firehose](https://www.11ty.dev/firehose/)
    *   [11ty Bundle](https://11tybundle.dev/)
    *   [Leaderboards](https://www.11ty.dev/speedlify/)
    *   [Eleventy Meetup](https://11tymeetup.dev/)
    *   [11ty Conference](https://conf.11ty.dev/)

*   [Guide](https://www.11ty.dev/docs/projects/)

Guide
    *   [Get Started](https://www.11ty.dev/docs/)
    *   [Command Line Usage](https://www.11ty.dev/docs/usage/)
    *   [Add a Configuration File](https://www.11ty.dev/docs/config/)
    *   [Copy Files to Output](https://www.11ty.dev/docs/copy/)
    *   [Add CSS, JS, Fonts](https://www.11ty.dev/docs/assets/)
    *   [Importing Content](https://www.11ty.dev/docs/migrate/)
    *   [Configure Templates with Data](https://www.11ty.dev/docs/data-configuration/)
        *   [Permalinks](https://www.11ty.dev/docs/permalinks/)
        *   [Layouts](https://www.11ty.dev/docs/layouts/)
        *   [Collections](https://www.11ty.dev/docs/collections/)
            *   [Collections API](https://www.11ty.dev/docs/collections-api/)

        *   [Content Dates](https://www.11ty.dev/docs/dates/)
        *   [Create Pages From Data](https://www.11ty.dev/docs/pages-from-data/)
            *   [Pagination](https://www.11ty.dev/docs/pagination/)
            *   [Pagination Navigation](https://www.11ty.dev/docs/pagination/nav/)

    *   [Using Data in Templates](https://www.11ty.dev/docs/data/)
        *   [Eleventy Supplied Data](https://www.11ty.dev/docs/data-eleventy-supplied/)
        *   [Data Cascade](https://www.11ty.dev/docs/data-cascade/)
            *   [Front Matter Data](https://www.11ty.dev/docs/data-frontmatter/)
                *   [Custom Front Matter](https://www.11ty.dev/docs/data-frontmatter-customize/)

            *   [Template & Directory Data Files](https://www.11ty.dev/docs/data-template-dir/)
            *   [Global Data Files](https://www.11ty.dev/docs/data-global/)
            *   [Config Global Data](https://www.11ty.dev/docs/data-global-custom/)
            *   [Computed Data](https://www.11ty.dev/docs/data-computed/)

        *   [JavaScript Data Files](https://www.11ty.dev/docs/data-js/)
        *   [Custom Data File Formats](https://www.11ty.dev/docs/data-custom/)
        *   [Validate Data](https://www.11ty.dev/docs/data-validate/)

    *   [Template Languages](https://www.11ty.dev/docs/languages/)
        *   [HTML](https://www.11ty.dev/docs/languages/html/)
        *   [Markdown](https://www.11ty.dev/docs/languages/markdown/)
            *   [MDX](https://www.11ty.dev/docs/languages/mdx/)

        *   [JavaScript](https://www.11ty.dev/docs/languages/javascript/)
            *   [JSX](https://www.11ty.dev/docs/languages/jsx/)
            *   [TypeScript](https://www.11ty.dev/docs/languages/typescript/)

        *   [Custom](https://www.11ty.dev/docs/languages/custom/)
        *   [WebC](https://www.11ty.dev/docs/languages/webc/)
        *   [Nunjucks](https://www.11ty.dev/docs/languages/nunjucks/)
        *   [Liquid](https://www.11ty.dev/docs/languages/liquid/)
        *   [Handlebars](https://www.11ty.dev/docs/languages/handlebars/)
        *   [Mustache](https://www.11ty.dev/docs/languages/mustache/)
        *   [EJS](https://www.11ty.dev/docs/languages/ejs/)
        *   [HAML](https://www.11ty.dev/docs/languages/haml/)
        *   [Pug](https://www.11ty.dev/docs/languages/pug/)
        *   [Sass](https://www.11ty.dev/docs/languages/sass/)
        *   [Virtual Templates](https://www.11ty.dev/docs/virtual-templates/)
        *   [Overriding Languages](https://www.11ty.dev/docs/template-overrides/)

    *   Template Features
        *   [Ignore Files](https://www.11ty.dev/docs/ignores/)
        *   [Preprocess Content](https://www.11ty.dev/docs/config-preprocessors/)
        *   [Postprocess Content](https://www.11ty.dev/docs/transforms/)
        *   [Filters](https://www.11ty.dev/docs/filters/)
            *   [`url`](https://www.11ty.dev/docs/filters/url/)
            *   [`slugify`](https://www.11ty.dev/docs/filters/slugify/)
            *   [`log`](https://www.11ty.dev/docs/filters/log/)
            *   [`get*CollectionItem`](https://www.11ty.dev/docs/filters/collection-items/)
            *   [`inputPathToUrl`](https://www.11ty.dev/docs/filters/inputpath-to-url/)

        *   [Shortcodes](https://www.11ty.dev/docs/shortcodes/)
            *   [`getBundle`](https://www.11ty.dev/docs/plugins/bundle/)
            *   [`getBundleFileUrl`](https://www.11ty.dev/docs/plugins/bundle/)

    *   [Environment Variables](https://www.11ty.dev/docs/environment-vars/)
    *   [Internationalization (i18n)](https://www.11ty.dev/docs/i18n/)
    *   [Watch Files and Dev Servers](https://www.11ty.dev/docs/watch-serve/)
        *   [Eleventy Dev Server](https://www.11ty.dev/docs/dev-server/)
        *   [Vite](https://www.11ty.dev/docs/server-vite/)

    *   [Common Pitfalls](https://www.11ty.dev/docs/pitfalls/)
    *   [Advanced](https://www.11ty.dev/docs/advanced/)
        *   [Release History](https://www.11ty.dev/docs/versions/)
        *   [Programmatic API](https://www.11ty.dev/docs/programmatic/)
        *   [Configuration Events](https://www.11ty.dev/docs/events/)
        *   [Order of Operations](https://www.11ty.dev/docs/advanced-order/)

*   [Plugins](https://www.11ty.dev/docs/plugins/)

Plugins
    *   [Create or use Plugins](https://www.11ty.dev/docs/create-plugin/)
    *   [Image](https://www.11ty.dev/docs/plugins/image/)
    *   [Fetch](https://www.11ty.dev/docs/plugins/fetch/)
    *   [`<is-land>`](https://www.11ty.dev/docs/plugins/is-land/)
    *   [Render](https://www.11ty.dev/docs/plugins/render/)
    *   [Internationalization (i18n)](https://www.11ty.dev/docs/plugins/i18n/)
    *   [RSS](https://www.11ty.dev/docs/plugins/rss/)
    *   [Upgrade Helper](https://www.11ty.dev/docs/plugins/upgrade-help/)
    *   [Syntax Highlighting](https://www.11ty.dev/docs/plugins/syntaxhighlight/)
    *   [InputPath to URL](https://www.11ty.dev/docs/plugins/inputpath-to-url/)
    *   [Navigation](https://www.11ty.dev/docs/plugins/navigation/)
    *   [HTML `<base>`](https://www.11ty.dev/docs/plugins/html-base/)
    *   [Bundle](https://www.11ty.dev/docs/plugins/bundle/)
    *   [Id Attribute](https://www.11ty.dev/docs/plugins/id-attribute/)
    *   [Community Plugins](https://www.11ty.dev/docs/plugins/community/)
    *   [Retired Plugins](https://www.11ty.dev/docs/plugins/retired/)

*   [Services](https://www.11ty.dev/docs/services/)

Services
    *   [Deployment & Hosting](https://www.11ty.dev/docs/deployment/)
    *   [Using a CMS](https://www.11ty.dev/docs/cms/)
    *   [Runtime APIs](https://www.11ty.dev/docs/api-services/)
        *   [Screenshots](https://www.11ty.dev/docs/services/screenshots/)
        *   [OpenGraph Image](https://www.11ty.dev/docs/services/opengraph/)
        *   [IndieWeb Avatar](https://www.11ty.dev/docs/services/indieweb-avatar/)
        *   [Generator Image](https://www.11ty.dev/docs/services/generator/)
        *   [Hosting Image](https://www.11ty.dev/docs/services/builtwith/)
        *   [Sparklines](https://www.11ty.dev/docs/services/sparklines/)

Breadcrumbs: 

*   [Eleventy Documentation](https://www.11ty.dev/docs/)
*   [Guide](https://www.11ty.dev/docs/projects/)

Configuration
=============

On this page

*   [Default filenames](https://www.11ty.dev/docs/config/#default-filenames)
*   [Configuration Options](https://www.11ty.dev/docs/config/#configuration-options)
    *   [Input Directory](https://www.11ty.dev/docs/config/#input-directory)
    *   [Directory for Includes](https://www.11ty.dev/docs/config/#directory-for-includes)
    *   [Directory for Layouts (Optional)](https://www.11ty.dev/docs/config/#directory-for-layouts-optional)
    *   [Directory for Global Data Files](https://www.11ty.dev/docs/config/#directory-for-global-data-files)
    *   [Output Directory](https://www.11ty.dev/docs/config/#output-directory)
    *   [Default template engine for Markdown files](https://www.11ty.dev/docs/config/#default-template-engine-for-markdown-files)
    *   [Default template engine for HTML files](https://www.11ty.dev/docs/config/#default-template-engine-for-html-files)
    *   [Template Formats](https://www.11ty.dev/docs/config/#template-formats)
    *   [Enable Quiet Mode to Reduce Console Noise](https://www.11ty.dev/docs/config/#enable-quiet-mode-to-reduce-console-noise)
    *   [Deploy to a subdirectory with a Path Prefix](https://www.11ty.dev/docs/config/#deploy-to-a-subdirectory-with-a-path-prefix)
    *   [Change Base File Name for Data Files](https://www.11ty.dev/docs/config/#change-base-file-name-for-data-files)
    *   [Change File Suffix for Data Files](https://www.11ty.dev/docs/config/#change-file-suffix-for-data-files)
    *   [Transforms](https://www.11ty.dev/docs/config/#transforms)
    *   [Linters](https://www.11ty.dev/docs/config/#linters)
    *   [Data Filter Selectors](https://www.11ty.dev/docs/config/#data-filter-selectors)
    *   [TypeScript Type Definitions](https://www.11ty.dev/docs/config/#type-script-type-definitions)
    *   [Removed Features](https://www.11ty.dev/docs/config/#removed-features)
    *   [Documentation Moved to Dedicated Pages](https://www.11ty.dev/docs/config/#documentation-moved-to-dedicated-pages)

Configuration files are optional. Add an `eleventy.config.js` file to the root directory of your project (read more about [default configuration filenames](https://www.11ty.dev/docs/config/#default-filenames)) to configure Eleventy to your own project’s needs. It might look like this:

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-224-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-224-jscjs)

```js
export default async function(eleventyConfig) {
	// Configure Eleventy
};
```

```js
module.exports = async function(eleventyConfig) {
	// Configure Eleventy
};
```

There are a few different ways to [shape your configuration file](https://www.11ty.dev/docs/config-shapes/). Added in v3.0.0 Eleventy v3 added support for both ESM and Asynchronous callbacks.

*   Add [Filters](https://www.11ty.dev/docs/filters/).
*   Add [Shortcodes](https://www.11ty.dev/docs/shortcodes/).
*   Add [Custom Tags](https://www.11ty.dev/docs/custom-tags/).
*   Add [JavaScript Template Functions](https://www.11ty.dev/docs/languages/javascript/#javascript-template-functions)
*   Add custom [Collections](https://www.11ty.dev/docs/collections/) and use [Advanced Collection Filtering and Sorting](https://www.11ty.dev/docs/collections/#advanced-custom-filtering-and-sorting).
*   Add [Plugins](https://www.11ty.dev/docs/plugins/).

Is your config file getting big and hard to understand? You can [create a project-specific plugin](https://www.11ty.dev/docs/quicktips/local-plugin/) to better organize your code.

Default filenames#
------------------

[Jump to section titled: Default filenames#](https://www.11ty.dev/docs/config/#default-filenames)
We look for the following configuration files:

1.   `.eleventy.js`
2.   `eleventy.config.js`Added in v2.0.0
3.   `eleventy.config.mjs`Added in v3.0.0
4.   `eleventy.config.cjs`Added in v2.0.0

The first configuration file found is used. The others are ignored.

[Play Video: Additions to the default config filename list (Changelog №17)](https://www.11ty.dev/docs/config/ "Play Video")[Additions to the default config filename list (Changelog №17) `▶7m11s`](https://youtube.com/watch?v=hJAtWQ9nmKU&t=431)

Configuration Options#
----------------------

[Jump to section titled: Configuration Options#](https://www.11ty.dev/docs/config/#configuration-options)
### Input Directory#

[Jump to section titled: Input Directory#](https://www.11ty.dev/docs/config/#input-directory)
Controls the top level directory/file/glob that we’ll use to look for templates.

| Input Directory |  |
| --- | --- |
| _Object Key_ | `dir.input` |
| _Default Value_ | `.`_(current directory)_ |
| _Valid Options_ | Any valid directory. |
| _Configuration API_ | `eleventyConfig.setInputDirectory()`Added in v3.0.0 |
| _Command Line Override_ | `--input` |

#### Command Line#

[Jump to section titled: Command Line#](https://www.11ty.dev/docs/config/#command-line)

```bash
# The current directory
npx @11ty/eleventy --input=.

# A single file
npx @11ty/eleventy --input=README.md

# A glob of files
npx @11ty/eleventy --input=*.md

# A subdirectory
npx @11ty/eleventy --input=views
```

#### Configuration#

[Jump to section titled: Configuration#](https://www.11ty.dev/docs/config/#configuration-2)
Via named export (order doesn’t matter). Note that there are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-input-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-input-jscjs)

```js
export const config = {
  dir: {
    input: "views"
  }
};
```

```js
module.exports.config = {
  dir: {
    input: "views"
  }
};
```

Or via method (not available in plugins) Added in v3.0.0:

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-225-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-225-jscjs)

```js
export default function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
  eleventyConfig.setInputDirectory("views");
};
```

```js
module.exports = function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
  eleventyConfig.setInputDirectory("views");
};
```

### Directory for Includes#

[Jump to section titled: Directory for Includes#](https://www.11ty.dev/docs/config/#directory-for-includes)
The includes directory is meant for [Eleventy layouts](https://www.11ty.dev/docs/layouts/), include files, extends files, partials, or macros. These files will not be processed as full template files, but can be consumed by other templates.

| Includes Directory |  |
| --- | --- |
| _Object Key_ | `dir.includes` |
| _Default_ | `_includes` |
| _Valid Options_ | Any valid directory inside of `dir.input` (an empty string `""` is supported) |
| _Configuration API_ | `eleventyConfig.setIncludesDirectory()`Added in v3.0.0 |
| _Command Line Override_ | _None_ |

Via named export (order doesn’t matter). Note that there are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-includes-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-includes-jscjs)

```js
export const config = {
  dir: {
		// ⚠️ This value is relative to your input directory.
    includes: "my_includes"
  }
};
```

```js
module.exports.config = {
  dir: {
		// ⚠️ This value is relative to your input directory.
    includes: "my_includes"
  }
};
```

Or via method (not available in plugins) Added in v3.0.0:

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-226-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-226-jscjs)

```js
export default function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
	// This is relative to your input directory!
  eleventyConfig.setIncludesDirectory("my_includes");
};
```

```js
module.exports = function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
	// This is relative to your input directory!
  eleventyConfig.setIncludesDirectory("my_includes");
};
```

### Directory for Layouts (Optional)#

[Jump to section titled: Directory for Layouts (Optional)#](https://www.11ty.dev/docs/config/#directory-for-layouts-optional)
This configuration option is optional but useful if you want your [Eleventy layouts](https://www.11ty.dev/docs/layouts/) to live outside of the [Includes directory](https://www.11ty.dev/docs/config/#directory-for-includes). Just like the [Includes directory](https://www.11ty.dev/docs/config/#directory-for-includes), these files will not be processed as full template files, but can be consumed by other templates.

WARNING

This setting **only applies** to Eleventy's language-agnostic [layouts](https://www.11ty.dev/docs/layouts/) (when defined in front matter or data files).

When using `{% extends %}`, Eleventy will **still search the `_includes` directory**. See [this note about existing templating features](https://www.11ty.dev/docs/layout-chaining/#addendum-about-existing-templating-features).

| Includes Directory |  |
| --- | --- |
| _Object Key_ | `dir.layouts` |
| _Default_ | _The value in `dir.includes`_ |
| _Valid Options_ | Any valid directory inside of `dir.input` (an empty string `""` is supported) |
| _Configuration API_ | `eleventyConfig.setLayoutsDirectory()`Added in v3.0.0 |
| _Command Line Override_ | _None_ |

Via named export (order doesn’t matter). Note that there are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-layouts-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-layouts-jscjs)

```js
export const config = {
  dir: {
    // These are both relative to your input directory!
    includes: "_includes",
    layouts: "_layouts",
  }
};
```

```js
module.exports.config = {
  dir: {
    // These are both relative to your input directory!
    includes: "_includes",
    layouts: "_layouts",
  }
};
```

Or via method (not available in plugins) Added in v3.0.0:

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-227-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-227-jscjs)

```js
export default function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
	// This is relative to your input directory!
  eleventyConfig.setLayoutsDirectory("_layouts");
};
```

```js
module.exports = function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
	// This is relative to your input directory!
  eleventyConfig.setLayoutsDirectory("_layouts");
};
```

### Directory for Global Data Files#

[Jump to section titled: Directory for Global Data Files#](https://www.11ty.dev/docs/config/#directory-for-global-data-files)
Controls the directory inside which the global data template files, available to all templates, can be found. Read more about [Global Data Files](https://www.11ty.dev/docs/data-global/).

| Data Files Directory |  |
| --- | --- |
| _Object Key_ | `dir.data` |
| _Default_ | `_data` |
| _Valid Options_ | Any valid directory inside of `dir.input` |
| _Configuration API_ | `eleventyConfig.setDataDirectory()`Added in v3.0.0 |
| _Command Line Override_ | _None_ |

Via named export (order doesn’t matter). Note that there are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-data-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-data-jscjs)

```js
export const config = {
  dir: {
    // ⚠️ This value is relative to your input directory.
    data: "lore",
  }
};
```

```js
module.exports.config = {
  dir: {
    // ⚠️ This value is relative to your input directory.
    data: "lore",
  }
};
```

Or via method (not available in plugins) Added in v3.0.0:

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-228-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-228-jscjs)

```js
export default function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
  eleventyConfig.setDataDirectory("lore");
};
```

```js
module.exports = function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
  eleventyConfig.setDataDirectory("lore");
};
```

### Output Directory#

[Jump to section titled: Output Directory#](https://www.11ty.dev/docs/config/#output-directory)
Controls the directory inside which the finished templates will be written to.

| Output Directory |  |
| --- | --- |
| _Object Key_ | `dir.output` |
| _Default_ | `_site` |
| _Valid Options_ | Any string that will work as a directory name. Eleventy creates this if it doesn’t exist. |
| _Configuration API_ | `eleventyConfig.setOutputDirectory()`Added in v3.0.0 |
| _Command Line Override_ | `--output` |

#### Command Line#

[Jump to section titled: Command Line#](https://www.11ty.dev/docs/config/#command-line-2)

```bash
npx @11ty/eleventy --output=_site
```

#### Configuration#

[Jump to section titled: Configuration#](https://www.11ty.dev/docs/config/#configuration-3)
Via named export (order doesn’t matter). Note that there are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-output-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-output-jscjs)

```js
export const config = {
  dir: {
		output: "dist",
  }
};
```

```js
module.exports.config = {
  dir: {
		output: "dist",
  }
};
```

Or via method (not available in plugins) Added in v3.0.0:

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-229-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-229-jscjs)

```js
export default function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
  eleventyConfig.setOutputDirectory("dist");
};
```

```js
module.exports = function(eleventyConfig) {
	// Order matters, put this at the top of your configuration file.
  eleventyConfig.setOutputDirectory("dist");
};
```

### Default template engine for Markdown files#

[Jump to section titled: Default template engine for Markdown files#](https://www.11ty.dev/docs/config/#default-template-engine-for-markdown-files)
Markdown files run through this template engine before transforming to HTML.

| Markdown Template Engine |  |
| --- | --- |
| _Object Key_ | `markdownTemplateEngine` |
| _Default_ | `liquid` |
| _Valid Options_ | A valid [template engine short name](https://www.11ty.dev/docs/languages/) or `false` |
| _Command Line Override_ | _None_ |
| _Configuration API_ | `setMarkdownTemplateEngine`Pre-release only: v4.0.0-alpha.1 |

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-mdengine-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-mdengine-jscjs)

```js
export const config = {
  markdownTemplateEngine: "njk",
};
```

```js
module.exports.config = {
  markdownTemplateEngine: "njk",
};
```

There are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

### Default template engine for HTML files#

[Jump to section titled: Default template engine for HTML files#](https://www.11ty.dev/docs/config/#default-template-engine-for-html-files)
HTML templates run through this template engine before transforming to (better) HTML.

| HTML Template Engine |  |
| --- | --- |
| _Object Key_ | `htmlTemplateEngine` |
| _Default_ | `liquid` |
| _Valid Options_ | A valid [template engine short name](https://www.11ty.dev/docs/languages/) or `false` |
| _Command Line Override_ | _None_ |
| _Configuration API_ | `setHtmlTemplateEngine`Pre-release only: v4.0.0-alpha.1 |

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-htmlengine-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-htmlengine-jscjs)

```js
export const config = {
  htmlTemplateEngine: "njk",
};
```

```js
module.exports.config = {
  htmlTemplateEngine: "njk",
};
```

There are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

### Template Formats#

[Jump to section titled: Template Formats#](https://www.11ty.dev/docs/config/#template-formats)
Specify which types of templates should be transformed.

| Template Formats |  |
| --- | --- |
| _Object Key_ | `templateFormats` |
| _Default_ | `html,liquid,ejs,md,hbs,mustache,haml,pug,njk,11ty.js` |
| _Valid Options_ | Array of [template engine short names](https://www.11ty.dev/docs/languages/) |
| _Command Line Override_ | `--formats`_(accepts a comma separated string)_ |
| _Configuration API_ | `setTemplateFormats` and `addTemplateFormats` |

**Case sensitivity**: File extensions should be considered case insensitive, cross-platform. While macOS already behaves this way (by default), other operating systems require additional Eleventy code to enable this behavior.

#### Command Line#

[Jump to section titled: Command Line#](https://www.11ty.dev/docs/config/#command-line-3)`npx @11ty/eleventy --formats=html,liquid,njk`
#### Configuration File Static Export#

[Jump to section titled: Configuration File Static Export#](https://www.11ty.dev/docs/config/#configuration-file-static-export)

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-templatelangs-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-templatelangs-jscjs)

```js
export const config = {
  templateFormats: ["html", "liquid", "njk"],
};
```

```js
module.exports.config = {
  templateFormats: ["html", "liquid", "njk"],
};
```

There are many [different shapes of configuration file](https://www.11ty.dev/docs/config-shapes/).

#### Configuration API#

[Jump to section titled: Configuration API#](https://www.11ty.dev/docs/config/#configuration-api)

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-230-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-230-jscjs)

```js
export default function (eleventyConfig) {
	// Reset to this value
	eleventyConfig.setTemplateFormats("html,liquid,njk");

	// Additive to existing
	eleventyConfig.addTemplateFormats("pug,haml");

	// Or:
	// eleventyConfig.setTemplateFormats([ "html", "liquid", "njk" ]);
	// eleventyConfig.addTemplateFormats([ "pug", "haml" ]);
};
```

```js
module.exports = function (eleventyConfig) {
	// Reset to this value
	eleventyConfig.setTemplateFormats("html,liquid,njk");

	// Additive to existing
	eleventyConfig.addTemplateFormats("pug,haml");

	// Or:
	// eleventyConfig.setTemplateFormats([ "html", "liquid", "njk" ]);
	// eleventyConfig.addTemplateFormats([ "pug", "haml" ]);
};
```

### Enable Quiet Mode to Reduce Console Noise#

[Jump to section titled: Enable Quiet Mode to Reduce Console Noise#](https://www.11ty.dev/docs/config/#enable-quiet-mode-to-reduce-console-noise)
In order to maximize user-friendliness to beginners, Eleventy will show each file it processes and the output file. To disable this noisy console output, use quiet mode!

| Quiet Mode |  |
| --- | --- |
| _Default_ | `false` |
| _Valid Options_ | `true` or `false` |
| _Command Line Override_ | `--quiet` |

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-231-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-231-jscjs)

```js
export default function (eleventyConfig) {
	eleventyConfig.setQuietMode(true);
};
```

```js
module.exports = function (eleventyConfig) {
	eleventyConfig.setQuietMode(true);
};
```

The command line will override any setting in configuration:

```bash
npx @11ty/eleventy --quiet
```

### Deploy to a subdirectory with a Path Prefix#

[Jump to section titled: Deploy to a subdirectory with a Path Prefix#](https://www.11ty.dev/docs/config/#deploy-to-a-subdirectory-with-a-path-prefix)
If your site lives in a different subdirectory (particularly useful with GitHub pages), use pathPrefix to specify this. When paired with the [HTML `<base>` plugin](https://www.11ty.dev/docs/plugins/html-base/) it will transform any absolute URLs in your HTML to include this folder name and does **not** affect where things go in the output folder.

| Path Prefix |  |
| --- | --- |
| _Object Key_ | `pathPrefix` |
| _Default_ | `/` |
| _Valid Options_ | A prefix directory added to urls in HTML files |
| _Command Line Override_ | `--pathprefix` |

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#config-pathprefix-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#config-pathprefix-jscjs)

```js
import { HtmlBasePlugin } from "@11ty/eleventy";

export default function (eleventyConfig) {
	eleventyConfig.addPlugin(HtmlBasePlugin);
};

export const config = {
	pathPrefix: "/eleventy-base-blog/",
}
```

```js
module.exports = async function (eleventyConfig) {
	const { HtmlBasePlugin } = await import("@11ty/eleventy");

	eleventyConfig.addPlugin(HtmlBasePlugin);
};

module.exports.config = {
	pathPrefix: "/eleventy-base-blog/",
}
```

Deploy to https://11ty.github.io/eleventy-base-blog/ on GitHub pages without modifying your config. This allows you to use the same code-base to deploy to either GitHub pages or Netlify, like the [`eleventy-base-blog`](https://github.com/11ty/eleventy-base-blog) project does.

```bash
npx @11ty/eleventy --pathprefix=eleventy-base-blog
```

### Change Base File Name for Data Files#

[Jump to section titled: Change Base File Name for Data Files#](https://www.11ty.dev/docs/config/#change-base-file-name-for-data-files)
Added in v2.0.0 When using [Directory Specific Data Files](https://www.11ty.dev/docs/data-template-dir/), looks for data files that match the current folder name. You can override this behavior to a static string with the `setDataFileBaseName` method.

| File Suffix |  |
| --- | --- |
| _Configuration API_ | `setDataFileBaseName` |
| _Default_ | _Current folder name_ |
| _Valid Options_ | String |
| _Command Line Override_ | _None_ |

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-232-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-232-jscjs)

```js
export default function (eleventyConfig) {
	// Looks for index.json and index.11tydata.json instead of using folder names
	eleventyConfig.setDataFileBaseName("index");
};
```

```js
module.exports = function (eleventyConfig) {
	// Looks for index.json and index.11tydata.json instead of using folder names
	eleventyConfig.setDataFileBaseName("index");
};
```

### Change File Suffix for Data Files#

[Jump to section titled: Change File Suffix for Data Files#](https://www.11ty.dev/docs/config/#change-file-suffix-for-data-files)
Added in v2.0.0 When using [Template and Directory Specific Data Files](https://www.11ty.dev/docs/data-template-dir/), to prevent file name conflicts with non-Eleventy files in the project directory, we scope these files with a unique-to-Eleventy suffix. This suffix is customizable using the `setDataFileSuffixes` configuration API method.

| File Suffix |  |
| --- | --- |
| _Configuration API_ | `setDataFileSuffixes` |
| _Default_ | `[".11tydata", ""]` |
| _Valid Options_ | Array |
| _Command Line Override_ | _None_ |

For example, using `".11tydata"` will search for `*.11tydata.js` and `*.11tydata.json` data files. The empty string (`""`) here represents a file without a suffix—and this entry only applies to `*.json` data files.

This feature can also be used to disable Template and Directory Data Files altogether with an empty array (`[]`).

Read more about [Template and Directory Specific Data Files](https://www.11ty.dev/docs/data-template-dir/).

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-233-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-233-jscjs)

```js
export default function (eleventyConfig) {
	// e.g. file.json and file.11tydata.json
	eleventyConfig.setDataFileSuffixes([".11tydata", ""]);

	// e.g. file.11tydata.json
	eleventyConfig.setDataFileSuffixes([".11tydata"]);

	// No data files are used.
	eleventyConfig.setDataFileSuffixes([]);
};
```

```js
module.exports = function (eleventyConfig) {
	// e.g. file.json and file.11tydata.json
	eleventyConfig.setDataFileSuffixes([".11tydata", ""]);

	// e.g. file.11tydata.json
	eleventyConfig.setDataFileSuffixes([".11tydata"]);

	// No data files are used.
	eleventyConfig.setDataFileSuffixes([]);
};
```

_**Backwards Compatibility Note**_ (`v2.0.0`)
Prior to v2.0.0 this feature was exposed using a `jsDataFileSuffix` property in the configuration return object. When the `setDataFileSuffixes` method has not been used, Eleventy maintains backwards compatibility for old projects by using this property as a fallback.

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-234-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-234-jscjs)

```js
export default function (eleventyConfig) {
	return {
		jsDataFileSuffix: ".11tydata",
	};
};
```

```js
module.exports = function (eleventyConfig) {
	return {
		jsDataFileSuffix: ".11tydata",
	};
};
```

### Transforms#

[Jump to section titled: Transforms#](https://www.11ty.dev/docs/config/#transforms)
*   Documented moved to [Transforms](https://www.11ty.dev/docs/transforms/).

### Linters#

[Jump to section titled: Linters#](https://www.11ty.dev/docs/config/#linters)
Similar to Transforms, Linters are provided to analyze a template’s output without modifying it.

| Linters |  |
| --- | --- |
| _Configuration API_ | `addLinter` |
| _Object Key_ | _N/A_ |
| _Valid Options_ | Callback function |
| _Command Line Override_ | _None_ |

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-235-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-235-jscjs)

```js
export default function (eleventyConfig) {
	// Sync or async
	eleventyConfig.addLinter("linter-name", async function (content) {
		console.log(this.inputPath);
		console.log(this.outputPath);

		// Eleventy 2.0+ has full access to Eleventy’s `page` variable
		console.log(this.page.inputPath);
		console.log(this.page.outputPath);
	});
};
```

```js
module.exports = function (eleventyConfig) {
	// Sync or async
	eleventyConfig.addLinter("linter-name", async function (content) {
		console.log(this.inputPath);
		console.log(this.outputPath);

		// Eleventy 2.0+ has full access to Eleventy’s `page` variable
		console.log(this.page.inputPath);
		console.log(this.page.outputPath);
	});
};
```

**Linters Example: Use Inclusive Language**
Inspired by the [CSS Tricks post _Words to Avoid in Educational Writing_](https://css-tricks.com/words-avoid-educational-writing/), this linter will log a warning to the console when it finds a trigger word in a markdown file.

This example has been packaged as a plugin in [`eleventy-plugin-inclusive-language`](https://www.11ty.dev/docs/plugins/inclusive-language/).

**Filename**eleventy.config.js

```js
export default function (eleventyConfig) {
	eleventyConfig.addLinter(
		"inclusive-language",
		function (content, inputPath, outputPath) {
			let words =
				"simply,obviously,basically,of course,clearly,just,everyone knows,however,easy".split(
					","
				);

			// Eleventy 1.0+: use this.inputPath and this.outputPath instead
			if (inputPath.endsWith(".md")) {
				for (let word of words) {
					let regexp = new RegExp("\\b(" + word + ")\\b", "gi");
					if (content.match(regexp)) {
						console.warn(
							`Inclusive Language Linter (${inputPath}) Found: ${word}`
						);
					}
				}
			}
		}
	);
};
```

### Data Filter Selectors#

[Jump to section titled: Data Filter Selectors#](https://www.11ty.dev/docs/config/#data-filter-selectors)
Added in v1.0.0

A `Set` of [`lodash` selectors](https://lodash.com/docs/4.17.15#get) that allow you to include data from the data cascade in the output from `--to=json`, `--to=ndjson`.

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-236-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-236-jscjs)

```js
export default function (eleventyConfig) {
	eleventyConfig.dataFilterSelectors.add("page");
	eleventyConfig.dataFilterSelectors.delete("page");
};
```

```js
module.exports = function (eleventyConfig) {
	eleventyConfig.dataFilterSelectors.add("page");
	eleventyConfig.dataFilterSelectors.delete("page");
};
```

This will now include a `data` property in your JSON output that includes the `page` variable for each matching template.

### TypeScript Type Definitions#

[Jump to section titled: TypeScript Type Definitions#](https://www.11ty.dev/docs/config/#type-script-type-definitions)
This may enable some extra autocomplete features in your IDE (where supported).

eleventy.config.js

[ESM](https://www.11ty.dev/docs/config/#tab-id-237-jsesm)[CommonJS](https://www.11ty.dev/docs/config/#tab-id-237-jscjs)

```js
/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
export default function (eleventyConfig) {
	// …
};
```

```js
/** @param {import("@11ty/eleventy").UserConfig} eleventyConfig */
module.exports = function (eleventyConfig) {
	// …
};
```

*   Related: [GitHub #2091](https://github.com/11ty/eleventy/pull/2091) and [GitHub #3097](https://github.com/11ty/eleventy/issues/3097)

### Removed Features#

[Jump to section titled: Removed Features#](https://www.11ty.dev/docs/config/#removed-features)
#### Change exception case suffix for HTML files#

[Jump to section titled: Change exception case suffix for HTML files#](https://www.11ty.dev/docs/config/#change-exception-case-suffix-for-html-files)

Feature Removal

The `htmlOutputSuffix` feature was removed in Eleventy 3.0. You can read about the feature on the [v2 documentation](https://v2-0-1.11ty.dev/docs/config/#change-exception-case-suffix-for-html-files). Related: [GitHub #3327](https://github.com/11ty/eleventy/issues/3327).

### Documentation Moved to Dedicated Pages#

[Jump to section titled: Documentation Moved to Dedicated Pages#](https://www.11ty.dev/docs/config/#documentation-moved-to-dedicated-pages)
[](https://www.11ty.dev/docs/config/)

#### Copy Files to Output using Passthrough File Copy#

[Jump to section titled: Copy Files to Output using Passthrough File Copy#](https://www.11ty.dev/docs/config/#copy-files-to-output-using-passthrough-file-copy)
Files found (that don’t have a valid template engine) from opt-in file extensions in `templateFormats` will passthrough to the output directory. Read more about [Passthrough Copy](https://www.11ty.dev/docs/copy/).

#### Customize Front Matter Parsing Options#

[Jump to section titled: Customize Front Matter Parsing Options#](https://www.11ty.dev/docs/config/#customize-front-matter-parsing-options)
*   Documented at [Customize Front Matter Parsing](https://www.11ty.dev/docs/data-frontmatter-customize/).

#### Watch JavaScript Dependencies#

[Jump to section titled: Watch JavaScript Dependencies#](https://www.11ty.dev/docs/config/#watch-java-script-dependencies)
*   Documented at [Watch and Serve Configuration](https://www.11ty.dev/docs/watch-serve/).

#### Add Your Own Watch Targets#

[Jump to section titled: Add Your Own Watch Targets#](https://www.11ty.dev/docs/config/#add-your-own-watch-targets)
*   Documented at [Watch and Serve Configuration](https://www.11ty.dev/docs/watch-serve/).

#### Override Browsersync Server Options#

[Jump to section titled: Override Browsersync Server Options#](https://www.11ty.dev/docs/config/#override-browsersync-server-options)
*   Documented at [Watch and Serve Configuration](https://www.11ty.dev/docs/watch-serve/).

#### Transforms#

[Jump to section titled: Transforms#](https://www.11ty.dev/docs/config/#transforms-2)
*   Documented at [Transforms](https://www.11ty.dev/docs/transforms/).

* * *

### Other pages in _Eleventy Projects_

*   [Get Started](https://www.11ty.dev/docs/)
*   [Command Line Usage](https://www.11ty.dev/docs/usage/)
*   [Add a Configuration File](https://www.11ty.dev/docs/config/)
*   [Copy Files to Output](https://www.11ty.dev/docs/copy/)
*   [Add CSS, JS, Fonts](https://www.11ty.dev/docs/assets/)
*   [Importing Content](https://www.11ty.dev/docs/migrate/)
*   [Configure Templates with Data](https://www.11ty.dev/docs/data-configuration/)
    *   [Permalinks](https://www.11ty.dev/docs/permalinks/)
    *   [Layouts](https://www.11ty.dev/docs/layouts/)
    *   [Collections](https://www.11ty.dev/docs/collections/)
        *   [Collections API](https://www.11ty.dev/docs/collections-api/)

    *   [Content Dates](https://www.11ty.dev/docs/dates/)
    *   [Create Pages From Data](https://www.11ty.dev/docs/pages-from-data/)
        *   [Pagination](https://www.11ty.dev/docs/pagination/)
        *   [Pagination Navigation](https://www.11ty.dev/docs/pagination/nav/)

*   [Using Data in Templates](https://www.11ty.dev/docs/data/)
    *   [Eleventy Supplied Data](https://www.11ty.dev/docs/data-eleventy-supplied/)
    *   [Data Cascade](https://www.11ty.dev/docs/data-cascade/)
        *   [Front Matter Data](https://www.11ty.dev/docs/data-frontmatter/)
            *   [Custom Front Matter](https://www.11ty.dev/docs/data-frontmatter-customize/)

        *   [Template & Directory Data Files](https://www.11ty.dev/docs/data-template-dir/)
        *   [Global Data Files](https://www.11ty.dev/docs/data-global/)
        *   [Config Global Data](https://www.11ty.dev/docs/data-global-custom/)
        *   [Computed Data](https://www.11ty.dev/docs/data-computed/)

    *   [JavaScript Data Files](https://www.11ty.dev/docs/data-js/)
    *   [Custom Data File Formats](https://www.11ty.dev/docs/data-custom/)
    *   [Validate Data](https://www.11ty.dev/docs/data-validate/)

*   [Template Languages](https://www.11ty.dev/docs/languages/)
    *   [HTML](https://www.11ty.dev/docs/languages/html/)
    *   [Markdown](https://www.11ty.dev/docs/languages/markdown/)
        *   [MDX](https://www.11ty.dev/docs/languages/mdx/)

    *   [JavaScript](https://www.11ty.dev/docs/languages/javascript/)
        *   [JSX](https://www.11ty.dev/docs/languages/jsx/)
        *   [TypeScript](https://www.11ty.dev/docs/languages/typescript/)

    *   [Custom](https://www.11ty.dev/docs/languages/custom/)
    *   [WebC](https://www.11ty.dev/docs/languages/webc/)
    *   [Nunjucks](https://www.11ty.dev/docs/languages/nunjucks/)
    *   [Liquid](https://www.11ty.dev/docs/languages/liquid/)
    *   [Handlebars](https://www.11ty.dev/docs/languages/handlebars/)
    *   [Mustache](https://www.11ty.dev/docs/languages/mustache/)
    *   [EJS](https://www.11ty.dev/docs/languages/ejs/)
    *   [HAML](https://www.11ty.dev/docs/languages/haml/)
    *   [Pug](https://www.11ty.dev/docs/languages/pug/)
    *   [Sass](https://www.11ty.dev/docs/languages/sass/)
    *   [Virtual Templates](https://www.11ty.dev/docs/virtual-templates/)
    *   [Overriding Languages](https://www.11ty.dev/docs/template-overrides/)

*   [Template Features](https://www.11ty.dev/docs/config/)
    *   [Ignore Files](https://www.11ty.dev/docs/ignores/)
    *   [Preprocess Content](https://www.11ty.dev/docs/config-preprocessors/)
    *   [Postprocess Content](https://www.11ty.dev/docs/transforms/)
    *   [Filters](https://www.11ty.dev/docs/filters/)
        *   [`url`](https://www.11ty.dev/docs/filters/url/)
        *   [`slugify`](https://www.11ty.dev/docs/filters/slugify/)
        *   [`log`](https://www.11ty.dev/docs/filters/log/)
        *   [`get*CollectionItem`](https://www.11ty.dev/docs/filters/collection-items/)
        *   [`inputPathToUrl`](https://www.11ty.dev/docs/filters/inputpath-to-url/)

    *   [Shortcodes](https://www.11ty.dev/docs/shortcodes/)
        *   [`getBundle`](https://www.11ty.dev/docs/plugins/bundle/)
        *   [`getBundleFileUrl`](https://www.11ty.dev/docs/plugins/bundle/)

*   [Environment Variables](https://www.11ty.dev/docs/environment-vars/)
*   [Internationalization (i18n)](https://www.11ty.dev/docs/i18n/)
*   [Watch Files and Dev Servers](https://www.11ty.dev/docs/watch-serve/)
    *   [Eleventy Dev Server](https://www.11ty.dev/docs/dev-server/)
    *   [Vite](https://www.11ty.dev/docs/server-vite/)

*   [Common Pitfalls](https://www.11ty.dev/docs/pitfalls/)
*   [Advanced](https://www.11ty.dev/docs/advanced/)
    *   [Release History](https://www.11ty.dev/docs/versions/)
    *   [Programmatic API](https://www.11ty.dev/docs/programmatic/)
    *   [Configuration Events](https://www.11ty.dev/docs/events/)
    *   [Order of Operations](https://www.11ty.dev/docs/advanced-order/)

[**19.3k**](https://github.com/11ty/eleventy)[**Star Eleventy on GitHub!**](https://github.com/11ty/eleventy) This is an easy way to support our underrated project and help boost our rank on both GitHub and [jamstack.org](https://jamstack.org/generators/)’s list of site generators.

*   [Read the **Blog**](https://www.11ty.dev/blog/)
*   [Follow on **Mastodon**](https://neighborhood.11ty.dev/@11ty)
*   [Follow on **Bluesky**](https://bsky.app/profile/11ty.dev)
*   [Subscribe to the **Newsletter**](https://buttondown.email/11ty)
*   [Watch on **YouTube**](https://www.youtube.com/c/EleventyVideo)
*   [Star on **GitHub**](https://github.com/11ty/eleventy)
*   [Chat on **Discord**](https://www.11ty.dev/blog/discord/)
*   ~~**Twitter**~~

### **Sponsors**

[![Image 2: Open Collective Avatar for Privatejet.com](https://www.11ty.dev/img/built/qWEZjwKj95-66.png)](https://privatejet.com/)[![Image 3: Open Collective Avatar for Unabridged Software](https://www.11ty.dev/img/built/Cjvwp-116A-66.png)](https://www.unabridgedsoftware.com/)[![Image 4: Open Collective Avatar for Casino mit schneller auszahlung](https://www.11ty.dev/img/built/oGxGPCb_wc-66.png)](https://de.trustpilot.com/review/casino-schnelle-auszahlung.net)[![Image 5: Open Collective Avatar for Ok win](https://www.11ty.dev/img/built/TbradoSVLa-66.png)](https://okwingame.io/)[![Image 6: Open Collective Avatar for Fun88](https://www.11ty.dev/img/built/u7teF61XY2-66.png)](https://global.fun88.com/)[![Image 7: Open Collective Avatar for Guidebook.BetWinner](https://www.11ty.dev/img/built/UuMp5szMW--66.png)](https://guidebook.betwinner.com/)[![Image 8: Open Collective Avatar for Scire](https://www.11ty.dev/img/built/MobMBD_Nws-66.png)](https://scire.au/)[![Image 9: Open Collective Avatar for Bitcoin casino](https://www.11ty.dev/img/built/lbuBwHu7lE-66.png)](https://de.trustpilot.com/review/bitcoin-casino-online.net)[![Image 10: Open Collective Avatar for PayID Pokies](https://www.11ty.dev/img/built/aJ7aUWPRQq-66.png)](https://au.trustpilot.com/review/bestpayidpokies.net)[![Image 11: Open Collective Avatar for Antithesis](https://www.11ty.dev/img/built/ErhByygERT-66.png)](https://antithesis.com/)[![Image 12: Open Collective Avatar for Best Online Pokies in Australia](https://www.11ty.dev/img/built/mx5fPHfyUJ-66.png)](https://au.trustpilot.com/review/aussiepokies.net)[![Image 13: Open Collective Avatar for Ставки на спорт](https://www.11ty.dev/img/built/1BoDc9wYwn-66.png)](https://betking.com.ua/sports-book/)[![Image 14: Open Collective Avatar for nejlepsiceskacasina.com](https://www.11ty.dev/img/built/_SNdRr9Qw0-66.png)](https://nejlepsiceskacasina.com/)[![Image 15: Open Collective Avatar for FBPostLikes](https://www.11ty.dev/img/built/0E76mjhf2N-66.png)](https://www.fbpostlikes.com/)[![Image 16: Open Collective Avatar for Pintura](https://www.11ty.dev/img/built/BC8y6qmc2B-66.png)](https://pqina.nl/pintura/)[![Image 17: Open Collective Avatar for ESLint](https://www.11ty.dev/img/built/d-IxivSbC--66.png)](https://eslint.org/)

### [**×746 Supporters**](https://opencollective.com/11ty)

[![Image 18: Open Collective Avatar for Unabridged Software](https://www.11ty.dev/img/built/Cjvwp-116A-66.png)](https://www.unabridgedsoftware.com/)[![Image 19: Open Collective Avatar for Pintura](https://www.11ty.dev/img/built/BC8y6qmc2B-66.png)](https://pqina.nl/pintura/)[![Image 20: Open Collective Avatar for Nathan Smith](https://www.11ty.dev/img/built/eI2AYn2zUF-66.png)](https://sonspring.com/)[![Image 21: Open Collective Avatar for ESLint](https://www.11ty.dev/img/built/d-IxivSbC--66.png)](https://eslint.org/)[![Image 22: Open Collective Avatar for Monarch Air Group](https://www.11ty.dev/img/built/3KCcBZabuw-66.png)](https://monarchairgroup.com/)[![Image 23: Open Collective Avatar for Scire](https://www.11ty.dev/img/built/MobMBD_Nws-66.png)](https://scire.au/)[![Image 24: Open Collective Avatar for Rob Dodson](https://www.11ty.dev/img/built/QM1fpudxiK-66.png)](https://opencollective.com/rob-dodson)[![Image 25: Open Collective Avatar for Screen recorder for Mac](https://www.11ty.dev/img/built/bUZGB8ZSO6-66.png)](https://www.movavi.com/screen-recorder-mac/)[![Image 26: Open Collective Avatar for Mercury Jets](https://www.11ty.dev/img/built/0QFe-H5i-8-66.png)](https://www.mercuryjets.com/)[![Image 27: Open Collective Avatar for Antithesis](https://www.11ty.dev/img/built/ErhByygERT-66.png)](https://antithesis.com/)[![Image 28: Open Collective Avatar for Steady](https://www.11ty.dev/img/built/wsNJXrCpUr-66.png)](https://opencollective.com/steady)[![Image 29: Open Collective Avatar for nejlepsiceskacasina.com](https://www.11ty.dev/img/built/_SNdRr9Qw0-66.png)](https://nejlepsiceskacasina.com/)[![Image 30: Open Collective Avatar for Getform.io](https://www.11ty.dev/img/built/wsx31INM9z-66.png)](https://getform.io/)[![Image 31: Open Collective Avatar for OCEG](https://www.11ty.dev/img/built/2aDIpz4KaJ-66.png)](https://www.oceg.org/)[![Image 32: Open Collective Avatar for Tyler Gaw](https://www.11ty.dev/img/built/PsYeSXkLDP-66.png)](https://tylergaw.com/)[![Image 33: Open Collective Avatar for Screen recorder for Mac](https://www.11ty.dev/img/built/gMoEVh8Uiq-66.png)](https://www.movavi.com/screen-recorder-mac/)[![Image 34: Open Collective Avatar for Ігрові автомати](https://www.11ty.dev/img/built/LvCTM10bSM-66.png)](https://casino.ua/casino/slots/)[![Image 35: Open Collective Avatar for Flatirons Development](https://www.11ty.dev/img/built/8HjOIYXDco-66.png)](https://flatironsdevelopment.com/)[![Image 36: Open Collective Avatar for Ariel Salminen](https://www.11ty.dev/img/built/nF3syuArh1-66.png)](https://arielsalminen.com/)[![Image 37: Open Collective Avatar for Guidebook.BetWinner](https://www.11ty.dev/img/built/UuMp5szMW--66.png)](https://guidebook.betwinner.com/)[![Image 38: Open Collective Avatar for Katie Sylor-Miller](https://www.11ty.dev/img/built/K0Y0MOA3-N-66.png)](https://opencollective.com/katie-sylor-miller)[![Image 39: Open Collective Avatar for Melanie Sumner](https://www.11ty.dev/img/built/wIGgXx6h9M-66.png)](https://opencollective.com/melanie-sumner)[![Image 40: Open Collective Avatar for Mike Aparicio](https://www.11ty.dev/img/built/DREl_gg_wr-66.png)](https://mikeaparicio.com/)[![Image 41: Open Collective Avatar for Peter deHaan](https://www.11ty.dev/img/built/zLhWlzdB5Q-66.png)](https://about.me/peterdehaan)[![Image 42: Open Collective Avatar for Route4Me Route Planner](https://www.11ty.dev/img/built/FzOxqojzsV-66.png)](https://route4me.com/)[![Image 43: Open Collective Avatar for Jérôme Coupé](https://www.11ty.dev/img/built/PnStZIbcVK-66.png)](https://www.webstoemp.com/)[![Image 44: Open Collective Avatar for Mat Marquis](https://www.11ty.dev/img/built/NS06PblEGa-66.png)](https://hire.wil.to/)[![Image 45: Open Collective Avatar for Playfortuneforfun.com](https://www.11ty.dev/img/built/bQonhAl0oC-66.png)](https://playfortuneforfun.com/)[![Image 46: Open Collective Avatar for Nicolas](https://www.11ty.dev/img/built/e7h1CuC2vk-66.png)](https://nicolas-hoizey.com/)[![Image 47: Open Collective Avatar for Ashur Cabrera](https://www.11ty.dev/img/built/NcppY43IAo-66.png)](https://ashur.cab/rera)[![Image 48: Open Collective Avatar for Ben Nash](https://www.11ty.dev/img/built/kk3NTuJsli-66.png)](https://www.bennash.com/)[![Image 49: Open Collective Avatar for Lauris Consulting](https://www.11ty.dev/img/built/TjLhjlmwrV-66.png)](https://lauris-webdev.com/)[![Image 50: Open Collective Avatar for Philip Borenstein](https://www.11ty.dev/img/built/uiu3SlDtRu-66.png)](https://pborenstein.com/)[![Image 51: Open Collective Avatar for Mark Buskbjerg](https://www.11ty.dev/img/built/UQ0apalw-S-66.png)](https://markbuskbjerg.dk/)[![Image 52: Open Collective Avatar for Paul Everitt](https://www.11ty.dev/img/built/goiJfARbzu-66.png)](https://opencollective.com/paul-everitt)[![Image 53: Open Collective Avatar for Jenn Schiffer](https://www.11ty.dev/img/built/IzZbJnFGnG-66.png)](https://jennmoney.biz/)[![Image 54: Open Collective Avatar for Tim Giles](https://www.11ty.dev/img/built/0tdKgINKou-66.png)](https://www.tgiles.dev/)[![Image 55: Open Collective Avatar for Fershad Irani](https://www.11ty.dev/img/built/MhX7JmRL3m-66.png)](https://www.fershad.com/)[![Image 56: Open Collective Avatar for Eric Bailey](https://www.11ty.dev/img/built/IDAOfKWSve-66.png)](https://ericwbailey.design/)[![Image 57: Open Collective Avatar for Josh Crain](https://www.11ty.dev/img/built/MVazrAK6DJ-66.png)](https://joshcrain.io/)[![Image 58: Open Collective Avatar for Alejandro Rodríguez](https://www.11ty.dev/img/built/2CMD_d63PF-66.png)](https://opencollective.com/arcxyz)[![Image 59: Open Collective Avatar for Max Böck](https://www.11ty.dev/img/built/slrzLYWGvX-66.png)](https://mxb.dev/)[![Image 60: Open Collective Avatar for Sam](https://www.11ty.dev/img/built/Z4x5YEFgM6-66.png)](https://opencollective.com/user-3b6553b5)[![Image 61: Open Collective Avatar for Aaron Hans](https://www.11ty.dev/img/built/DgATprs8pL-66.png)](https://opencollective.com/aaron-hans)[![Image 62: Open Collective Avatar for Stephanie Eckles](https://www.11ty.dev/img/built/dSPdz2fjYM-66.png)](https://thinkdobecreate.com/)[![Image 63: Open Collective Avatar for Matt Hobbs](https://www.11ty.dev/img/built/FhVS39COk3-66.png)](https://nooshu.com/)[![Image 64: Open Collective Avatar for Higby](https://www.11ty.dev/img/built/WoM2ucFBqh-66.png)](https://www.higby.io/)[![Image 65: Open Collective Avatar for Alex Russell](https://www.11ty.dev/img/built/pqP00aOpUz-66.png)](https://infrequently.org/)[![Image 66: Open Collective Avatar for Ben Myers](https://www.11ty.dev/img/built/y-JQ2BRZOs-66.png)](https://benmyers.dev/)[![Image 67: Open Collective Avatar for Alex Zappa](https://www.11ty.dev/img/built/hcbAIkx-Ge-66.png)](https://alex.zappa.dev/)[![Image 68: Open Collective Avatar for Rich Holman](https://www.11ty.dev/img/built/4KpRNL1s9I-66.png)](https://opencollective.com/rich-holman)[![Image 69: Open Collective Avatar for Dan Ryan](https://www.11ty.dev/img/built/yENJdvDk6w-66.png)](https://dryan.com/)[![Image 70: Open Collective Avatar for Michel van der Kroef](https://www.11ty.dev/img/built/cqvp22_JCa-66.png)](https://neckam.nl/)[![Image 71: Open Collective Avatar for Henry Desroches](https://www.11ty.dev/img/built/ReQlqeJ1JI-66.png)](https://henry.codes/)[![Image 72: Open Collective Avatar for Mike Stilling](https://www.11ty.dev/img/built/8-WdMfg9kx-66.png)](https://opencollective.com/mike-stilling)[![Image 73: Open Collective Avatar for Horacio Gonzalez](https://www.11ty.dev/img/built/WOmQ5epxy4-66.png)](https://opencollective.com/lostinbrittany)[![Image 74: Open Collective Avatar for Ryan Swaney](https://www.11ty.dev/img/built/TnDsFb0YCp-66.png)](https://opencollective.com/ryan-swaney)[![Image 75: Open Collective Avatar for Heather Buchel](https://images.opencollective.com/heather-buchel/b983990/avatar.png)](https://opencollective.com/heather-buchel)[![Image 76: Open Collective Avatar for Cthos](https://www.11ty.dev/img/built/R6PHpVeSax-66.png)](https://alextheward.com/)[![Image 77: Open Collective Avatar for mortendk](https://www.11ty.dev/img/built/-zcpYYT07X-66.png)](https://morten.dk/)[![Image 78: Open Collective Avatar for Angelique Weger](https://www.11ty.dev/img/built/T83wYfiEtr-66.png)](https://angeliqueweger.com/)[![Image 79: Open Collective Avatar for Privatejet.com](https://www.11ty.dev/img/built/qWEZjwKj95-66.png)](https://privatejet.com/)[![Image 80: Open Collective Avatar for Kyosuke Nakamura](https://www.11ty.dev/img/built/hEbvUjXjsY-66.png)](https://opencollective.com/kyosuke)[![Image 81: Open Collective Avatar for Bryce Wray](https://www.11ty.dev/img/built/3Jo9x1pFy5-66.png)](https://www.brycewray.com/)[![Image 82: Open Collective Avatar for Noel Forte](https://www.11ty.dev/img/built/RyFknwn9v2-66.png)](https://forte.is/)[![Image 83: Open Collective Avatar for John Meyerhofer](https://www.11ty.dev/img/built/rXJ5CSQK_i-66.png)](https://opencollective.com/john-meyerhofer)[![Image 84: Open Collective Avatar for Makoto Kawasaki](https://www.11ty.dev/img/built/D95kFrkXIb-66.png)](https://makotokw.com/)[![Image 85: Open Collective Avatar for Richard Hemmer](https://www.11ty.dev/img/built/A6r0BYiNGK-66.png)](https://opencollective.com/richard-hemmer)[![Image 86: Open Collective Avatar for Nick Nisi](https://www.11ty.dev/img/built/73Hk1Sipu1-66.png)](https://nicknisi.com/)[![Image 87: Open Collective Avatar for Hans Gerwitz](https://www.11ty.dev/img/built/6z9ngP6bqW-66.png)](https://hans.gerwitz.com/)[![Image 88: Open Collective Avatar for Ivo Herrmann](https://www.11ty.dev/img/built/TJM-kWzEjA-66.png)](https://ivoherrmann.com/)[![Image 89: Open Collective Avatar for shawn j sandy](https://www.11ty.dev/img/built/NRdDyeEorl-66.png)](https://opencollective.com/shawn-j-sandy)[![Image 90: Open Collective Avatar for Cory Dransfeldt](https://www.11ty.dev/img/built/KDSaeqiHNy-66.png)](https://opencollective.com/coryd)[![Image 91: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fjohnhall.codes%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fjohnhall.codes%2F/)](https://johnhall.codes/)[![Image 92: Open Collective Avatar for Miriam Suzanne](https://www.11ty.dev/img/built/YxHH1tIFbe-66.png)](https://oddbird.net/)[![Image 93: Open Collective Avatar for Bentley Davis](https://www.11ty.dev/img/built/QBBvK8xd8x-66.png)](https://bentleydavis.com/)[![Image 94: Open Collective Avatar for Vincent Falconi](https://www.11ty.dev/img/built/PEsWVJJWzs-66.png)](https://www.vincentfalconi.com/)[![Image 95: Open Collective Avatar for Martin Schneider](https://www.11ty.dev/img/built/JjYhLWuoL0-66.png)](https://martinschneider.me/)[![Image 96: Open Collective Avatar for Frontend Weekly Tokyo](https://www.11ty.dev/img/built/pRXq-7FgY4-66.png)](https://frontendweekly.tokyo/)[![Image 97: Open Collective Avatar for Matthew Hallonbacka](https://www.11ty.dev/img/built/i6cR3Pp3Su-66.png)](https://mallonbacka.com/)[![Image 98: Open Collective Avatar for Jens Grochtdreis](https://www.11ty.dev/img/built/a1JMi4h3SW-66.png)](https://opencollective.com/jens-grochtdreis)[![Image 99: Open Collective Avatar for John SJ Anderson](https://www.11ty.dev/img/built/Rrrp3wLkvf-66.png)](https://genehack.org/)[![Image 100: Open Collective Avatar for Kristof Michiels](https://www.11ty.dev/img/built/WsP426f6nF-66.png)](https://krs.tf/)[![Image 101: Open Collective Avatar for Kasper Storgaard](https://www.11ty.dev/img/built/Vgd9aYiZod-66.png)](https://opencollective.com/kasper-storgaard)[![Image 102: Open Collective Avatar for Kevin Healy-Clarke](https://www.11ty.dev/img/built/HV0QG2GaFh-66.png)](https://kevinhealyclarke.co.uk/)[![Image 103: Open Collective Avatar for Andy Bell](https://www.11ty.dev/img/built/IiDuxTy8bC-66.png)](https://hankchizljaw.com/)[![Image 104: Open Collective Avatar for David A. Herron](https://www.11ty.dev/img/built/nRxyQu-XYp-66.png)](https://www.david-herron.com/)[![Image 105: Open Collective Avatar for Alesandro Ortiz](https://www.11ty.dev/img/built/n72dBUyk9_-66.png)](https://alesandroortiz.com/)[![Image 106: Open Collective Avatar for Paul Robert Lloyd](https://www.11ty.dev/img/built/BiFiIHCw1c-66.png)](https://paulrobertlloyd.com/)[![Image 107: Open Collective Avatar for Andrea Vaghi](https://www.11ty.dev/img/built/3q3IMMayo3-66.png)](https://www.andreavaghi.dev/)[![Image 108: Open Collective Avatar for Joe Lamyman](https://www.11ty.dev/img/built/aar4OHOcqP-66.png)](https://joelamyman.co.uk/)[![Image 109: Open Collective Avatar for Alistair Shepherd](https://www.11ty.dev/img/built/kSH7U8cxwV-66.png)](https://alistairshepherd.uk/)[![Image 110: Open Collective Avatar for Luke Bonaccorsi](https://www.11ty.dev/img/built/TU1l7LJzhV-66.png)](https://lukeb.co.uk/)[![Image 111: Open Collective Avatar for Brett Nelson](https://www.11ty.dev/img/built/6gypf2lc7Q-66.png)](https://wipdeveloper.com/)[![Image 112: Open Collective Avatar for Jesse Heady](https://www.11ty.dev/img/built/iiBhcuvOYd-66.png)](https://jesseheady.com/)[![Image 113: Open Collective Avatar for Melanie Richards](https://www.11ty.dev/img/built/444I5oJZFw-66.png)](http://melanie-richards.com/)[![Image 114: Open Collective Avatar for Wes Ruvalcaba](https://www.11ty.dev/img/built/b0VzPAuVuF-66.png)](https://opencollective.com/wesruv)[![Image 115: Open Collective Avatar for Ara Abcarians](https://www.11ty.dev/img/built/eds5Qh3iwQ-66.png)](https://itsmeara.com/)[![Image 116: Open Collective Avatar for Yuhei Yasuda](https://www.11ty.dev/img/built/7ye2IDyKbp-66.png)](https://yuheiy.com/)[![Image 117: Open Collective Avatar for Devin Clark](https://www.11ty.dev/img/built/hK2NwjOC6H-66.png)](https://opencollective.com/devin-clark)[![Image 118: Open Collective Avatar for Manuel](https://www.11ty.dev/img/built/B8slbpdWuK-66.png)](https://opencollective.com/manuel-matuzovic)[![Image 119: Open Collective Avatar for Joachim Kliemann](https://www.11ty.dev/img/built/L3mFTO2pzF-66.png)](https://opencollective.com/joachim-kliemann)[![Image 120: Open Collective Avatar for Ken Hawkins](https://www.11ty.dev/img/built/Af4lqD81Eo-66.png)](https://allaboutken.com/)[![Image 121: Open Collective Avatar for Bryan Robinson](https://www.11ty.dev/img/built/j91eUfRJl2-66.png)](https://opencollective.com/bryan-robinson)[![Image 122: Open Collective Avatar for Todd Libby](https://www.11ty.dev/img/built/VcbkvglcF1-66.png)](https://opencollective.com/todd-libby)[![Image 123: Open Collective Avatar for Eric Portis](https://www.11ty.dev/img/built/rJp9GqAh9A-66.png)](https://opencollective.com/eric-portis)[![Image 124: Open Collective Avatar for Dimitrios Grammatikogiannis](https://www.11ty.dev/img/built/jFSXiKETyT-66.png)](https://dgrammatiko.online/)[![Image 125: Open Collective Avatar for Benjamin Geese](https://www.11ty.dev/img/built/dcs66y1r-B-66.png)](https://benjamingeese.de/)[![Image 126: Open Collective Avatar for William Riley](https://www.11ty.dev/img/built/u7h3sqBSVm-66.png)](https://splitinfinities.com/)[![Image 127: Open Collective Avatar for Dorin Vancea](https://www.11ty.dev/img/built/x8w8aJcRzN-66.png)](https://dorinvancea.com/)[![Image 128: Open Collective Avatar for Saneef Ansari](https://www.11ty.dev/img/built/GFWfnU3I80-66.png)](https://saneef.com/)[![Image 129: Open Collective Avatar for Raphael Höser](https://www.11ty.dev/img/built/Vjjf_NElrJ-66.png)](https://hoeser.dev/)[![Image 130: Open Collective Avatar for Nikita Dubko](https://www.11ty.dev/img/built/_F-P_XEWkz-66.png)](https://mefody.dev/)[![Image 131: Open Collective Avatar for Michelle Barker](https://www.11ty.dev/img/built/2DGHoCId3C-66.png)](https://opencollective.com/michelle-barker)[![Image 132: Open Collective Avatar for Chris Burnell](https://www.11ty.dev/img/built/8m4hIDDshg-66.png)](https://chrisburnell.com/)[![Image 133: Open Collective Avatar for Colin Fahrion](https://www.11ty.dev/img/built/C9VCrMo0jY-66.png)](https://opencollective.com/colin-fahrion)[![Image 134: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdanburzo.ro%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fdanburzo.ro%2F/)](https://danburzo.ro/)[![Image 135: Open Collective Avatar for Jon Kuperman](https://www.11ty.dev/img/built/go0oS6P220-66.png)](https://jonkuperman.com/)[![Image 136: Open Collective Avatar for Luc Poupard](https://www.11ty.dev/img/built/xnPuch_ElH-66.png)](https://www.kloh.ch/)[![Image 137: Open Collective Avatar for James Steinbach](https://www.11ty.dev/img/built/CQKunEbus4-66.png)](https://jamessteinbach.com/)[![Image 138: Open Collective Avatar for Cheap VPS](https://www.11ty.dev/img/built/dw_vlSmpz6-66.png)](https://vpsdime.com/)[![Image 139: Open Collective Avatar for Marco Zehe](https://www.11ty.dev/img/built/EOzUPnpiaR-66.png)](https://opencollective.com/marco-zehe)[![Image 140: Open Collective Avatar for Dana Byerly](https://www.11ty.dev/img/built/EntixyRl9H-66.png)](https://danabyerly.com/)[![Image 141: Open Collective Avatar for Oisín Quinn](https://www.11ty.dev/img/built/T5EXP6ABIP-66.png)](https://oisin.io/)[![Image 142: Open Collective Avatar for SignpostMarv](https://www.11ty.dev/img/built/k2v76MSRBK-66.png)](https://opencollective.com/signpostmarv)[![Image 143: Open Collective Avatar for Josh Vickerson](https://www.11ty.dev/img/built/RuWPCNf5i6-66.png)](https://www.joshvickerson.com/)[![Image 144: Open Collective Avatar for Patrick Byrne](https://www.11ty.dev/img/built/-raIxYZdWd-66.png)](https://opencollective.com/user-559626bc)[![Image 145: Open Collective Avatar for Marcus Relacion](https://www.11ty.dev/img/built/9MV-m7OA4R-66.png)](https://www.marcusrelacion.com/)[![Image 146: Open Collective Avatar for Cory Birdsong](https://www.11ty.dev/img/built/eWJP1VTc-N-66.png)](https://birdsong.dev/)[![Image 147: Open Collective Avatar for Dave letorey](https://www.11ty.dev/img/built/XF5pSlxirY-66.png)](https://letorey.co.uk/)[![Image 148: Open Collective Avatar for Ryan Trimble](https://www.11ty.dev/img/built/BBAjvyEnvc-66.png)](https://www.ryantrimble.com/)[![Image 149: Open Collective Avatar for Aram ZS](https://www.11ty.dev/img/built/yfMR5hVlO1-66.png)](https://aramzs.xyz/)[![Image 150: Open Collective Avatar for Frank Reding](https://www.11ty.dev/img/built/TgyQKt0fiq-66.png)](https://opencollective.com/user-a2e5f55d)[![Image 151: Open Collective Avatar for Sia Karamalegos](https://www.11ty.dev/img/built/o3X_bqcFc3-66.png)](https://sia.codes/)[![Image 152: Open Collective Avatar for Ed Spencer](https://www.11ty.dev/img/built/mSBAXwR58A-66.png)](https://edspencer.me.uk/)[![Image 153: Open Collective Avatar for Patrick Grey](https://www.11ty.dev/img/built/F6WiSJ7WTE-66.png)](https://risingsky.co.uk/)[![Image 154: Open Collective Avatar for Incognito](https://www.11ty.dev/img/built/yAnzJWpNrI-66.png)](https://opencollective.com/user-58d6db26)[![Image 155: Open Collective Avatar for Barry Pollard](https://www.11ty.dev/img/built/PaoDIojRvn-66.png)](https://www.tunetheweb.com/)[![Image 156: Open Collective Avatar for Patrick Fulton](https://www.11ty.dev/img/built/SZI7Ps7Z5j-66.png)](https://opencollective.com/patrick-fulton1)[![Image 157: Open Collective Avatar for Incognito](https://www.11ty.dev/img/built/r8RhxwhckA-66.png)](https://opencollective.com/incognito-81ff86a6)[![Image 158: Open Collective Avatar for Patrick O'Brien](https://www.11ty.dev/img/built/F-pb4nDfpW-66.png)](https://opencollective.com/patrick-obrien)[![Image 159: Open Collective Avatar for Rob Sterlini](https://www.11ty.dev/img/built/7yuhBpjR_2-66.png)](https://robsterlini.co.uk/)[![Image 160: Open Collective Avatar for Adam DJ Brett](https://www.11ty.dev/img/built/5QE8XD2mdE-66.png)](https://adamdjbrett.com/)[![Image 161: Open Collective Avatar for Kathleen Fitzpatrick](https://www.11ty.dev/img/built/Por0vddrkM-66.png)](https://opencollective.com/kathleen-fitzpatrick)[![Image 162: Open Collective Avatar for Lea Rosema](https://www.11ty.dev/img/built/jPm1xZrzMs-66.png)](https://opencollective.com/lea-rosema)[![Image 163: Open Collective Avatar for Mark Llobrera](https://www.11ty.dev/img/built/jHr-sKfV5t-66.png)](https://opencollective.com/mark-llobrera)[![Image 164: Open Collective Avatar for Nic Chan](https://www.11ty.dev/img/built/idpxINM6kh-66.png)](https://opencollective.com/nic-chan)[![Image 165: Open Collective Avatar for Chris](https://www.11ty.dev/img/built/hnjhQG24QF-66.png)](https://www.chrisswithinbank.net/)[![Image 166: Open Collective Avatar for Greg G](https://www.11ty.dev/img/built/t4OoG0jsUG-66.png)](https://opencollective.com/hellogreg)[![Image 167: Open Collective Avatar for Scott McCracken](https://www.11ty.dev/img/built/bZ8uHs57Np-66.png)](https://scottmccracken.net/)[![Image 168: Open Collective Avatar for Tanner Dolby](https://www.11ty.dev/img/built/9-uJbuby7E-66.png)](https://tannerdolby.com/)[![Image 169: Open Collective Avatar for CelineDesign](https://www.11ty.dev/img/built/pQagEjPYFp-66.png)](https://www.celinedesign.com/)[![Image 170: Open Collective Avatar for Dave Rupert](https://www.11ty.dev/img/built/UA8VCWzEwr-66.png)](https://daverupert.com/)[![Image 171: Open Collective Avatar for Christian Miles](https://www.11ty.dev/img/built/OZs6Gm-dnF-66.png)](https://cjlm.ca/)[![Image 172: Open Collective Avatar for Bob Monsour](https://www.11ty.dev/img/built/E8bKJZJnE8-66.png)](https://www.bobmonsour.com/)[![Image 173: Open Collective Avatar for Mehis](https://www.11ty.dev/img/built/Zz3QBEYhEl-66.png)](https://github.com/TotallyMehis/)[![Image 174: Open Collective Avatar for Jeremy](https://www.11ty.dev/img/built/_r5bATNRE9-66.png)](https://www.jeremycaldwell.me/)[![Image 175: Open Collective Avatar for cro.media](https://www.11ty.dev/img/built/EzE0X3FSsa-66.png)](https://cro.media/)[![Image 176: Open Collective Avatar for JC](https://www.11ty.dev/img/built/Gx8fkVcGx_-66.png)](https://jcletousey.dev/en/)[![Image 177: Open Collective Avatar for Lene](https://www.11ty.dev/img/built/6DHpZHxazZ-66.png)](https://www.lenesaile.com/)[![Image 178: Open Collective Avatar for Brett DeWoody](https://www.11ty.dev/img/built/NWu6jOdKOd-66.png)](https://opencollective.com/brett-dewoody)[![Image 179: Open Collective Avatar for jpoehnelt](https://www.11ty.dev/img/built/U-gxqLz_8c-66.png)](https://justin.poehnelt.com/)[![Image 180: Open Collective Avatar for Ben Hyrman](https://www.11ty.dev/img/built/dbfSchziZ2-66.png)](https://opencollective.com/ben-hyrman)[![Image 181: Open Collective Avatar for Ximenav Vf.](https://www.11ty.dev/img/built/OSCw2q3V77-66.png)](https://ximenavf.com/)[![Image 182: Open Collective Avatar for Flaki](https://www.11ty.dev/img/built/QR0zIV-TnT-66.png)](https://flak.is/)[![Image 183: Open Collective Avatar for Heydon Pickering](https://www.11ty.dev/img/built/hPDmDKDVjf-66.png)](https://opencollective.com/heydon-pickering)[![Image 184: Open Collective Avatar for Phil Hawksworth](https://www.11ty.dev/img/built/ABNN7svhDr-66.png)](https://opencollective.com/phil-hawksworth)[![Image 185: Open Collective Avatar for Zearin](https://www.11ty.dev/img/built/ZP6GVIGpwt-66.png)](https://opencollective.com/zearin)[![Image 186: Open Collective Avatar for dan leatherman](https://www.11ty.dev/img/built/d_KcS04uzE-66.png)](https://danleatherman.com/)[![Image 187: Open Collective Avatar for John Meguerian](https://www.11ty.dev/img/built/Snxs8GqSa9-66.png)](https://opencollective.com/john-meguerian)[![Image 188: Open Collective Avatar for Keenan Payne](https://www.11ty.dev/img/built/NeqsEoVUst-66.png)](https://keenanpayne.com/)[![Image 189: Open Collective Avatar for Tianyu Ge](https://www.11ty.dev/img/built/g8JuVktfCY-66.png)](https://opencollective.com/tianyu-ge)[![Image 190: Open Collective Avatar for Ставки на спорт](https://www.11ty.dev/img/built/1BoDc9wYwn-66.png)](https://betking.com.ua/sports-book/)[![Image 191: Open Collective Avatar for Simon Cox](https://www.11ty.dev/img/built/0liiy7-s8t-66.png)](https://www.simoncox.com/)[![Image 192: Open Collective Avatar for King Billy Slots](https://www.11ty.dev/img/built/YkyePnjAKa-66.png)](https://opencollective.com/king-billy-slots1)[![Image 193: Open Collective Avatar for Oscar](https://www.11ty.dev/img/built/eIMJ1fV_tl-66.png)](https://opencollective.com/ovl)[![Image 194: Open Collective Avatar for Ingo Steinke](https://www.11ty.dev/img/built/okzSCHvvSz-66.png)](https://www.ingo-steinke.com/)[![Image 195: Open Collective Avatar for Matthew Tole](https://www.11ty.dev/img/built/Ca0d4Fystb-66.png)](https://opencollective.com/matthew-tole)[![Image 196: Open Collective Avatar for Ned Zimmerman](https://www.11ty.dev/img/built/qOFZ0q42LJ-66.png)](https://bight.dev/)[![Image 197: Open Collective Avatar for Richard Herbert](https://images.opencollective.com/richard-herbert/9b47657/avatar.png)](https://opencollective.com/richard-herbert)[![Image 198: Open Collective Avatar for Kayce Basques](https://www.11ty.dev/img/built/Oin0JiM_Th-66.png)](https://kayce.basqu.es/)[![Image 199: Open Collective Avatar for Cecilie Vennevik](https://www.11ty.dev/img/built/S0_9Pqroe3-66.png)](https://www.cvennevik.no/)[![Image 200: Open Collective Avatar for Robin Rendle](https://www.11ty.dev/img/built/0ecBO3mcjC-66.png)](https://opencollective.com/robin-rendle)[![Image 201: Open Collective Avatar for Raymond Camden](https://www.11ty.dev/img/built/m7XckrlSP5-66.png)](https://www.raymondcamden.com/)[![Image 202: Open Collective Avatar for Søren Birkemeyer](https://www.11ty.dev/img/built/L5sd6hUs3Z-66.png)](https://annualbeta.com/)[![Image 203: Open Collective Avatar for cocopon](https://www.11ty.dev/img/built/rtuZtaJUSz-66.png)](https://cocopon.me/)[![Image 204: Open Collective Avatar for Iva Tech](https://www.11ty.dev/img/built/TTncNkK1l5-66.png)](https://ivatech.dev/)[![Image 205: Open Collective Avatar for Jay Cuthrell](https://www.11ty.dev/img/built/gJBuQPfhxJ-66.png)](https://fudge.org/)[![Image 206: Open Collective Avatar for Ryan Gittings](https://www.11ty.dev/img/built/bEU8IWANAL-66.png)](https://gittings.studio/)[![Image 207: Open Collective Avatar for Mark Hernandez](https://www.11ty.dev/img/built/WlZ3RmxoyC-66.png)](https://www.lion-byte.com/)[![Image 208: Open Collective Avatar for Andrew Harvard](https://www.11ty.dev/img/built/6Pt5xOwP-E-66.png)](https://opencollective.com/andrew-harvard)[![Image 209: Open Collective Avatar for Kelson Vibber](https://www.11ty.dev/img/built/cS3MO2qidc-66.png)](https://kvibber.com/)[![Image 210: Open Collective Avatar for Tobias Fedder](https://www.11ty.dev/img/built/W1srFwOqke-66.png)](https://tfedder.de/)[![Image 211: Open Collective Avatar for Gaston Rampersad](https://www.11ty.dev/img/built/oKjB9DXvSM-66.png)](https://opencollective.com/gastonrampersad)[![Image 212: Open Collective Avatar for Ivan Buncic](https://www.11ty.dev/img/built/4MCslbq-xv-66.png)](https://ivanbuncic.com/)[![Image 213: Open Collective Avatar for Richmond Insulation](https://www.11ty.dev/img/built/wyaqQSVjSb-66.png)](https://www.centralvainsulation.com/)[![Image 214: Open Collective Avatar for Brian Koser](https://www.11ty.dev/img/built/BTgKMRjqSr-66.png)](https://opencollective.com/brian-koser)[![Image 215: Open Collective Avatar for Ainsley Ellis](https://www.11ty.dev/img/built/HDuGU6WKyC-66.png)](https://www.ains.me/)[![Image 216: Open Collective Avatar for David Hayes](https://www.11ty.dev/img/built/dy_OCpjmmX-66.png)](https://drhayes.io/)[![Image 217: Open Collective Avatar for Kevin Yank](https://www.11ty.dev/img/built/tFdXD40ECE-66.png)](https://opencollective.com/kevin-yank)[![Image 218: Open Collective Avatar for Eric Gallager](https://www.11ty.dev/img/built/kmTPROJIsP-66.png)](https://www.nhhousedemcaucus.com/team/rep-eric-gallager)[![Image 219: Open Collective Avatar for Eric Carlisle](https://www.11ty.dev/img/built/segdDp6Ynq-66.png)](https://opencollective.com/eric-carlisle)[![Image 220: Open Collective Avatar for quinnanya](https://www.11ty.dev/img/built/Cy-c4InPEb-66.png)](https://opencollective.com/quinnanya)[![Image 221: Open Collective Avatar for Nick Colley](https://www.11ty.dev/img/built/U1sjK2Nyct-66.png)](https://nickcolley.co.uk/)[![Image 222: Open Collective Avatar for Mark Boulton](https://www.11ty.dev/img/built/6aNZoB1-cB-66.png)](https://opencollective.com/mark-boulton)[![Image 223: Open Collective Avatar for Vadim Makeev](https://www.11ty.dev/img/built/QNJYtxBgGn-66.png)](https://opencollective.com/pepelsbey)[![Image 224: Open Collective Avatar for Christian Alder](https://www.11ty.dev/img/built/fUFEDD31rL-66.png)](https://www.aldr.dev/)[![Image 225: Open Collective Avatar for David Darnes](https://www.11ty.dev/img/built/DcHSuYIAdy-66.png)](https://darn.es/)[![Image 226: Open Collective Avatar for Luke Mitchell](https://www.11ty.dev/img/built/wRiXT7ZuXr-66.png)](https://www.interroban.gg/)[![Image 227: Open Collective Avatar for Sachin Sancheti](https://www.11ty.dev/img/built/VbcY6fHpL3-66.png)](https://opencollective.com/sachin-sancheti)[![Image 228: Open Collective Avatar for Takuya Fukuju](https://www.11ty.dev/img/built/g9xKaLEKNd-66.png)](https://opencollective.com/chalkygames123)[![Image 229: Open Collective Avatar for Richmond Concrete](https://www.11ty.dev/img/built/6w0Ejl6LIi-66.png)](https://www.richmondconcretepros.com/)[![Image 230: Open Collective Avatar for Dan Ott](https://www.11ty.dev/img/built/DSsM8y-k9f-66.png)](https://dtott.com/)[![Image 231: Open Collective Avatar for Paul Welsh](https://www.11ty.dev/img/built/4d1nmNRlvb-66.png)](https://www.nonbreakingspace.co.uk/)[![Image 232: Open Collective Avatar for Nicolas](https://www.11ty.dev/img/built/MYV9o10Hkc-66.png)](https://thejollyteapot.com/)[![Image 233: Open Collective Avatar for RxDB](https://www.11ty.dev/img/built/6TSDNjn0Wn-66.png)](https://rxdb.info/?utm_source=opencollective&utm_medium=banner&utm_campaign=opencollective_sponsor&utm_content=logo)[![Image 234: Open Collective Avatar for Aaron Gustafson](https://www.11ty.dev/img/built/_G96c0SZtf-66.png)](https://www.aaron-gustafson.com/)[![Image 235: Open Collective Avatar for Andreas Kapp](https://www.11ty.dev/img/built/J6Z8i_NGny-66.png)](https://opencollective.com/andreas-kapp)[![Image 236: Open Collective Avatar for Chris Peckham](https://www.11ty.dev/img/built/roBjnfJrzt-66.png)](https://opencollective.com/chris-peckham)[![Image 237: Open Collective Avatar for Tom](https://www.11ty.dev/img/built/z8ZEdSyHaM-66.png)](https://tomquinonero.com/)[![Image 238: Open Collective Avatar for Ben Brignell](https://www.11ty.dev/img/built/Gm8R6o0LOG-66.png)](https://benbrignell.com/)[![Image 239: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbikes.emilyhorsman.com%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fbikes.emilyhorsman.com%2F/)](https://bikes.emilyhorsman.com/)[![Image 240: Open Collective Avatar for Kyle Mitofsky](https://www.11ty.dev/img/built/HmQz9SMhEy-66.png)](https://opencollective.com/kyle-mitofsky)[![Image 241: Open Collective Avatar for Juan Miguel](https://www.11ty.dev/img/built/7sqbXjInLK-66.png)](https://www.apirocket.io/)[![Image 242: Open Collective Avatar for IT Flashcards](https://www.11ty.dev/img/built/_7ZlRcCQc7-66.png)](https://www.itflashcards.com/)[![Image 243: Open Collective Avatar for Anna E. Cook](https://www.11ty.dev/img/built/_W72Qo0VaI-66.png)](https://opencollective.com/anna-e-cook)[![Image 244: Open Collective Avatar for Jonathan Weckerle](https://www.11ty.dev/img/built/s6ss6kmSrm-66.png)](https://webworker.berlin/)[![Image 245: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflorianboegner.com%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fflorianboegner.com%2F/)](https://florianboegner.com/)[![Image 246: Open Collective Avatar for Ana Rodrigues](https://www.11ty.dev/img/built/DsOUZMVh1X-66.png)](https://ohhelloana.blog/)[![Image 247: Open Collective Avatar for Nicolas Friedli](https://www.11ty.dev/img/built/esDDEWPN4t-66.png)](https://nicolasfriedli.ch/)[![Image 248: Open Collective Avatar for Matt DeCamp](https://www.11ty.dev/img/built/PPDXLYumuI-66.png)](https://decamp.dev/)[![Image 249: Open Collective Avatar for Reach Digital](https://www.11ty.dev/img/built/0Yvuq6Sbe8-66.png)](https://www.reachdigital.nl/)[![Image 250: Open Collective Avatar for Ross Kinney](https://www.11ty.dev/img/built/T_p4I7wPmw-66.png)](https://opencollective.com/ross-kinney)[![Image 251: Open Collective Avatar for beeps](https://www.11ty.dev/img/built/k_lfX-kD16-66.png)](https://beeps.website/)[![Image 252: Open Collective Avatar for Harris Lapiroff](https://www.11ty.dev/img/built/lnVWvnlygL-66.png)](https://chromamine.com/)[![Image 253: Open Collective Avatar for Eric T Grubaugh](https://www.11ty.dev/img/built/PVsziB1EsD-66.png)](https://opencollective.com/eric-t-grubaugh)[![Image 254: Open Collective Avatar for Kilian Finger](https://www.11ty.dev/img/built/rEm-bG4XT1-66.png)](https://www.kilianfinger.com/)[![Image 255: Open Collective Avatar for Khalid Abuhakmeh](https://www.11ty.dev/img/built/JNNWOpXx7--66.png)](https://www.khalidabuhakmeh.com/)[![Image 256: Open Collective Avatar for Marty McGuire](https://www.11ty.dev/img/built/IrbJeDdqr_-66.png)](https://opencollective.com/schmartissimo)[![Image 257: Open Collective Avatar for Keith Kurson](https://www.11ty.dev/img/built/AWXqmOC4El-66.png)](https://opencollective.com/keith-kurson)[![Image 258: Open Collective Avatar for Rahul Gupta](https://www.11ty.dev/img/built/tkzPwEtYCZ-66.png)](https://opencollective.com/rahul-gupta2)[![Image 259: Open Collective Avatar for Nathan Bottomley](https://www.11ty.dev/img/built/X4trEZmnp1-66.png)](https://gunsandfrocks.com/)[![Image 260: Open Collective Avatar for Zacky Ma](https://www.11ty.dev/img/built/4xHZ4uxOI4-66.png)](https://marchbox.com/)[![Image 261: Open Collective Avatar for box464](https://www.11ty.dev/img/built/TtRXbP0S1n-66.png)](https://opencollective.com/box464)[![Image 262: Open Collective Avatar for Sam Baldwin](https://www.11ty.dev/img/built/1YQm_kUuCC-66.png)](https://sambaldwin.info/)[![Image 263: Open Collective Avatar for Sami Määttä](https://www.11ty.dev/img/built/sDbteeFBd_-66.png)](https://opencollective.com/sami-maatta)[![Image 264: Open Collective Avatar for Stephen Bell](https://www.11ty.dev/img/built/JA6oRMUqSh-66.png)](https://steedgood.com/)[![Image 265: Open Collective Avatar for Jeffrey A Morgan](https://www.11ty.dev/img/built/ANAiVAqWUP-66.png)](https://jam1401.dev/)[![Image 266: Open Collective Avatar for Evan Harrison](https://www.11ty.dev/img/built/YVSoYSEyvu-66.png)](https://www.evan-harrison.com/)[![Image 267: Open Collective Avatar for Jon Roobottom](https://www.11ty.dev/img/built/yIbsK1_KKC-66.png)](https://roobottom.com/)[![Image 268: Open Collective Avatar for Christopher Salmon](https://www.11ty.dev/img/built/nxRoe3aj5J-66.png)](https://windowswebdev.io/)[![Image 269: Open Collective Avatar for Stefan Brechbühl](https://www.11ty.dev/img/built/DL-Ll4E5L--66.png)](https://stebre.ch/)[![Image 270: Open Collective Avatar for Mike](https://www.11ty.dev/img/built/ks79zsTag7-66.png)](https://opencollective.com/mike83)[![Image 271: Open Collective Avatar for Marco Solazzi](https://www.11ty.dev/img/built/IS8nLph9jq-66.png)](https://marco.solazzi.me/)[![Image 272: Open Collective Avatar for Chris Ruppel](https://www.11ty.dev/img/built/SVv_kojePS-66.png)](https://opencollective.com/chris-ruppel)[![Image 273: Open Collective Avatar for Wayne and Layne](https://www.11ty.dev/img/built/umzifA1TGy-66.png)](https://www.wayneandlayne.com/)[![Image 274: Open Collective Avatar for Ryan](https://www.11ty.dev/img/built/VdVcl7nGQR-66.png)](https://ryanmulligan.dev/)[![Image 275: Open Collective Avatar for Jason Garber](https://www.11ty.dev/img/built/RehkOw1umc-66.png)](https://sixtwothree.org/)[![Image 276: Open Collective Avatar for Josiah](https://www.11ty.dev/img/built/HWIPYJWWMT-66.png)](https://opencollective.com/josiah2)[![Image 277: Open Collective Avatar for Nate Moore](https://www.11ty.dev/img/built/jm68T5FpvH-66.png)](https://opencollective.com/nmoodev)[![Image 278: Open Collective Avatar for Andy Stevenson](https://www.11ty.dev/img/built/v-0uPV1QAa-66.png)](https://opencollective.com/andy-stevenson)[![Image 279: Open Collective Avatar for Brian Louis Ramirez](https://www.11ty.dev/img/built/XYWi1t7zRw-66.png)](https://blr.design/)[![Image 280: Open Collective Avatar for Automatio AI](https://www.11ty.dev/img/built/znP4JTOftm-66.png)](https://automatio.ai/)[![Image 281: Open Collective Avatar for John](https://www.11ty.dev/img/built/MWKcoYPTPj-66.png)](https://velvetcache.org/)[![Image 282: Open Collective Avatar for Dieter Peirs](https://www.11ty.dev/img/built/-2pC9NPlRa-66.png)](https://opencollective.com/dieter-peirs)[![Image 283: Open Collective Avatar for Alexander Wunschik](https://www.11ty.dev/img/built/N7ZdNyTqOQ-66.png)](https://www.wunschik.it/)[![Image 284: Open Collective Avatar for Casino mit schneller auszahlung](https://www.11ty.dev/img/built/oGxGPCb_wc-66.png)](https://de.trustpilot.com/review/casino-schnelle-auszahlung.net)[![Image 285: Open Collective Avatar for Bitcoin casino](https://www.11ty.dev/img/built/lbuBwHu7lE-66.png)](https://de.trustpilot.com/review/bitcoin-casino-online.net)[![Image 286: Open Collective Avatar for Fun88](https://www.11ty.dev/img/built/u7teF61XY2-66.png)](https://global.fun88.com/)[![Image 287: Open Collective Avatar for Best Online Pokies in Australia](https://www.11ty.dev/img/built/mx5fPHfyUJ-66.png)](https://au.trustpilot.com/review/aussiepokies.net)[![Image 288: Open Collective Avatar for PayID Pokies](https://www.11ty.dev/img/built/aJ7aUWPRQq-66.png)](https://au.trustpilot.com/review/bestpayidpokies.net)[![Image 289: Open Collective Avatar for FBPostLikes](https://www.11ty.dev/img/built/0E76mjhf2N-66.png)](https://www.fbpostlikes.com/)[![Image 290: Open Collective Avatar for Ok win](https://www.11ty.dev/img/built/TbradoSVLa-66.png)](https://okwingame.io/)[![Image 291: Open Collective Avatar for Cita d.o.o.](https://www.11ty.dev/img/built/UZ0en7SnTj-66.png)](https://www.silvestar.codes/)[![Image 292: Open Collective Avatar for Shane Holloway](https://www.11ty.dev/img/built/CN0OYb1AbS-66.png)](https://shaneholloway.com/)[![Image 293: Open Collective Avatar for Aleksandr Zapparov](https://www.11ty.dev/img/built/LreaYfMWUQ-66.png)](https://zapparov.dev/)[![Image 294: Open Collective Avatar for Mark Mayo](https://www.11ty.dev/img/built/B2Yd09X-_V-66.png)](https://opencollective.com/mark-mayo)[![Image 295: Open Collective Avatar for bengo](https://www.11ty.dev/img/built/kcs-nCAcrQ-66.png)](https://bengo.is/)[![Image 296: Open Collective Avatar for Daniel Saunders](https://www.11ty.dev/img/built/ez8-1o75YK-66.png)](https://opencollective.com/daniel-saunders)[![Image 297: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Featon-works.com%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Featon-works.com%2F/)](https://eaton-works.com/)[![Image 298: Open Collective Avatar for Flemming Meyer](https://www.11ty.dev/img/built/bU3oOK1mnC-66.png)](https://fokus.design/)[![Image 299: Open Collective Avatar for Brian Zerangue](https://www.11ty.dev/img/built/AP-wp7KBHM-66.png)](https://opencollective.com/brian-zerangue)[![Image 300: Open Collective Avatar for Hawk Ticehurst](https://www.11ty.dev/img/built/4Xy_M5Ra7F-66.png)](https://opencollective.com/hawk-ticehurst)[![Image 301: Open Collective Avatar for MasalPu](https://www.11ty.dev/img/built/5wVMj7aric-66.png)](https://masalpu.com/)[![Image 302: Open Collective Avatar for John Kemp-Cruz](https://www.11ty.dev/img/built/n6O2gdI7lp-66.png)](https://opencollective.com/john-kemp-cruz)[![Image 303: Open Collective Avatar for Veronica Explains](https://www.11ty.dev/img/built/6VIE-qZTIL-66.png)](https://vkc.sh/)[![Image 304: Open Collective Avatar for John J. Mills](https://www.11ty.dev/img/built/T1ZwRF3yTD-66.png)](https://opencollective.com/john-j-mills)[![Image 305: Open Collective Avatar for Joshua Ray](https://www.11ty.dev/img/built/XrCbDDjCu0-66.png)](https://ollomedia.com/)[![Image 306: Open Collective Avatar for Stuart Robson](https://www.11ty.dev/img/built/QLslqWOL_Q-66.png)](https://opencollective.com/sturobson)[![Image 307: Open Collective Avatar for Curt Hasselschwert](https://www.11ty.dev/img/built/IqymD2oMb7-66.png)](https://opencollective.com/curt-hasselschwert)[![Image 308: Open Collective Avatar for Yahor Mikhnevich](https://www.11ty.dev/img/built/mlYQDVfEqd-66.png)](https://opencollective.com/yahor-mikhnevich)[![Image 309: Open Collective Avatar for Travis Briggs](https://www.11ty.dev/img/built/7q6GeFY1xR-66.png)](https://travisbriggs.com/)[![Image 310: Open Collective Avatar for David Luhr](https://www.11ty.dev/img/built/3oxrLKija6-66.png)](https://luhr.co/)[![Image 311: Open Collective Avatar for Matt Stein](https://www.11ty.dev/img/built/lu4Jdo8vj8-66.png)](https://mattstein.com/)[![Image 312: Open Collective Avatar for Softermii](https://www.11ty.dev/img/built/kyJ1iq0um5-66.png)](https://www.softermii.com/)[![Image 313: Open Collective Avatar for Rob Anderson](https://www.11ty.dev/img/built/zautg4GgYX-66.png)](https://www.r0b.io/)[![Image 314: Open Collective Avatar for VoloshchenkoAl](https://www.11ty.dev/img/built/QJw2Hp9-gW-66.png)](https://github.com/VoloshchenkoAl)[![Image 315: Open Collective Avatar for Hunter Miller](https://www.11ty.dev/img/built/vr-9daIgFJ-66.png)](https://opencollective.com/hunter-miller)[![Image 316: Open Collective Avatar for Andrew Shell](https://www.11ty.dev/img/built/rVVxTYlieC-66.png)](https://blog.andrewshell.org/)[![Image 317: Open Collective Avatar for Lewis Nyman](https://www.11ty.dev/img/built/yjOdTjcvxu-66.png)](https://opencollective.com/lewis-nyman)[![Image 318: Open Collective Avatar for Andrew Chou](https://www.11ty.dev/img/built/GJGI-AeBSL-66.png)](https://andrew.nonetoohappy.buzz/)[![Image 319: Open Collective Avatar for Schepp](https://www.11ty.dev/img/built/WtGqwkmdGB-66.png)](https://schepp.dev/)[![Image 320: Open Collective Avatar for Ricky de Laveaga](https://www.11ty.dev/img/built/5Xt5fO3MbK-66.png)](https://rdela.com/)[![Image 321: Open Collective Avatar for IgAnony](https://www.11ty.dev/img/built/ulLUdnq4Xn-66.png)](https://iganony.net/)[![Image 322: Open Collective Avatar for Daniel Rafaj](https://www.11ty.dev/img/built/H2YsWORSa9-66.png)](https://github.com/danielstaleiny)[![Image 323: Open Collective Avatar for Johan Bové](https://www.11ty.dev/img/built/0foGlM6wQK-66.png)](https://johanbove.info/)[![Image 324: Open Collective Avatar for Grant Smith](https://www.11ty.dev/img/built/c0uBWfQwo0-66.png)](https://www.transition-creative.co.uk/)[![Image 325: Open Collective Avatar for chriskirknielsen](https://www.11ty.dev/img/built/vYuhBQSqXF-66.png)](https://chriskirknielsen.com/)[![Image 326: Open Collective Avatar for Ray Villalobos](https://www.11ty.dev/img/built/3S4kNIlJ6f-66.png)](https://opencollective.com/ray-villalobos)[![Image 327: Open Collective Avatar for Maël Brunet](https://www.11ty.dev/img/built/01ZSfydoZ3-66.png)](https://opencollective.com/mael-brunet)[![Image 328: Open Collective Avatar for Joel Goodman](https://www.11ty.dev/img/built/MnhAJEuBsl-66.png)](https://opencollective.com/joel-goodman)[![Image 329: Open Collective Avatar for Jonathan Wright](https://images.opencollective.com/jonathan-wright/a1adea5/avatar.png)](https://opencollective.com/jonathan-wright)[![Image 330: Open Collective Avatar for Peter Antonius](https://www.11ty.dev/img/built/427TJDN43R-66.png)](https://antonius.me/)[![Image 331: Open Collective Avatar for Dave Powers](https://www.11ty.dev/img/built/85W70IjHFe-66.png)](https://davepowers.me/)[![Image 332: Open Collective Avatar for legjobbmagyarcasino.com](https://www.11ty.dev/img/built/1vvzCsUYLb-66.png)](https://legjobbmagyarcasino.com/)[![Image 333: Open Collective Avatar for Chudovo](https://www.11ty.dev/img/built/NRBpwMUeBj-66.png)](https://chudovo.com/)[![Image 334: Open Collective Avatar for Tixie Salander](https://www.11ty.dev/img/built/QeYBHwfaJU-66.png)](https://tixie.name/)[![Image 335: Open Collective Avatar for alistairtweedie](https://www.11ty.dev/img/built/VZAV2dFUQx-66.png)](https://opencollective.com/alistair-tweedie)[![Image 336: Open Collective Avatar for Sami Singh](https://www.11ty.dev/img/built/nn0cPWvJXf-66.png)](https://httpster.io/)[![Image 337: Open Collective Avatar for Trey Piepmeier](https://www.11ty.dev/img/built/90Hmd68nD8-66.png)](https://treypiepmeier.com/)[![Image 338: Open Collective Avatar for Pelle Wessman](https://www.11ty.dev/img/built/AVYrptayKp-66.png)](https://voxpelli.com/)[![Image 339: Open Collective Avatar for Jeremias Menichelli](https://www.11ty.dev/img/built/JVNXyslEFl-66.png)](https://jeremenichelli.io/)[![Image 340: Open Collective Avatar for Marek ‘saji’ Augustynowicz](https://www.11ty.dev/img/built/LrXPBrG0kb-66.png)](https://opencollective.com/saji)[![Image 341: Open Collective Avatar for Buy YouTube Subscribers from SocialWick](https://www.11ty.dev/img/built/ULSIqO_guB-66.png)](https://www.socialwick.com/youtube/subscribers)[![Image 342: Open Collective Avatar for Jon Plummer](https://www.11ty.dev/img/built/rs45UPtDdz-66.png)](https://jonplummer.com/)[![Image 343: Open Collective Avatar for Daniel Ritzenthaler](https://www.11ty.dev/img/built/iW1nTWBQg4-66.png)](https://opencollective.com/daniel-ritzenthaler)[![Image 344: Open Collective Avatar for Discount Agent](https://www.11ty.dev/img/built/4UlgrnpnS5-66.png)](https://discountagent.co.uk/)[![Image 345: Open Collective Avatar for Stefan Burke](https://www.11ty.dev/img/built/Hcuas6rcYP-66.png)](https://chobble.com/)[![Image 346: Open Collective Avatar for Claudia R](https://www.11ty.dev/img/built/yboBiDgDxh-66.png)](https://opencollective.com/claudia-rndrs)[![Image 347: Open Collective Avatar for Grady Thompson](https://www.11ty.dev/img/built/kMKAcGq4jl-66.png)](https://www.gradyt.com/)[![Image 348: Open Collective Avatar for Mike](https://www.11ty.dev/img/built/PYEnC_ol47-66.png)](https://opencollective.com/mikeproulx)[![Image 349: Open Collective Avatar for Chris McLeod](https://www.11ty.dev/img/built/w846qo9ySQ-66.png)](https://opencollective.com/chris-mcleod)[![Image 350: Open Collective Avatar for Rowdy Rabouw](https://www.11ty.dev/img/built/7cYhKwRy68-66.png)](https://opencollective.com/rowdy-rabouw)[![Image 351: Open Collective Avatar for Kevin C. Tofel](https://www.11ty.dev/img/built/upu1vV_oVT-66.png)](https://opencollective.com/kevin-c-tofel)[![Image 352: Open Collective Avatar for Celebian](https://www.11ty.dev/img/built/Gpe-Pa03NE-66.png)](https://celebian.com/)[![Image 353: Open Collective Avatar for Thomas Rigby](https://www.11ty.dev/img/built/a4YqOKU4Wt-66.png)](https://thomasrigby.com/)[![Image 354: Open Collective Avatar for Matt Obee](https://www.11ty.dev/img/built/__43EVHUkD-66.png)](https://bsky.app/profile/obee.me)[![Image 355: Open Collective Avatar for Austin Carr](https://www.11ty.dev/img/built/5ZJ0kMIG_s-66.png)](https://opencollective.com/user-656cc0f2)[![Image 356: Open Collective Avatar for Chris Collins](https://www.11ty.dev/img/built/CaAOFxSW9e-66.png)](https://www.chriscollins.me/)[![Image 357: Open Collective Avatar for Eben Gilkenson](https://www.11ty.dev/img/built/quLqd13Afl-66.png)](https://opencollective.com/eben-gilkenson)[![Image 358: Open Collective Avatar for Greg Wolanski](https://www.11ty.dev/img/built/1GFOxv-kU1-66.png)](https://gregwolanski.com/?ref=opencollective.com)[![Image 359: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fthomasclausen.dk](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fthomasclausen.dk/)](https://thomasclausen.dk/)[![Image 360: Open Collective Avatar for Nathan Knowler](https://www.11ty.dev/img/built/qboKv_8K47-66.png)](https://knowler.dev/)[![Image 361: Open Collective Avatar for Nove Casino](https://www.11ty.dev/img/built/Q1UpFVPUIt-66.png)](https://novecasino.net/)[![Image 362: Open Collective Avatar for Brennan Kenneth Brown](https://www.11ty.dev/img/built/nT_wkD149--66.png)](https://berryhouse.ca/)[![Image 363: Open Collective Avatar for irishlucky.com](https://www.11ty.dev/img/built/KP2nkUzjuh-66.png)](https://irishlucky.com/)[![Image 364: Open Collective Avatar for Vienna.com.ua](https://www.11ty.dev/img/built/Uf5Ps4ckuI-66.png)](https://vienna.com.ua/)[![Image 365: Open Collective Avatar for Mymoneycomparison.com](https://www.11ty.dev/img/built/3aC0nmyEMg-66.png)](https://www.mymoneycomparison.com/)[![Image 366: Open Collective Avatar for TWT S](https://www.11ty.dev/img/built/QPVeQfHZhG-66.png)](https://targetedwebtraffic.com/our-services)[![Image 367: Open Collective Avatar for slovenskecasino.net](https://www.11ty.dev/img/built/wD1al9UJBB-66.png)](https://slovenskecasino.net/)[![Image 368: Open Collective Avatar for Casino Magyar](https://www.11ty.dev/img/built/ej2YW3Xj9x-66.png)](https://kaszinomagyar.net/)[![Image 369: Open Collective Avatar for UnAIMyText](https://www.11ty.dev/img/built/Vn50x51bNc-66.png)](https://unaimytext.com/)[![Image 370: Open Collective Avatar for YouTube Downloader](https://www.11ty.dev/img/built/LoSLRhR_xN-66.png)](https://orbitdownloader.com/youtube-downloader)[![Image 371: Open Collective Avatar for Network Tools](https://www.11ty.dev/img/built/S9zFmus7b6-66.png)](https://gf.dev/)[![Image 372: Open Collective Avatar for Calculators](https://www.11ty.dev/img/built/QYz-0WHGUc-66.png)](https://calculator.now/)[![Image 373: Open Collective Avatar for Wallpapers.Com](https://www.11ty.dev/img/built/2beKKziFkM-66.png)](https://wallpapers.com/)[![Image 374: Open Collective Avatar for baginstore](https://www.11ty.dev/img/built/6LYJDXgXd9-66.png)](https://www.baginstore.com/)[![Image 375: Open Collective Avatar for Casino ohne oasis](https://www.11ty.dev/img/built/V_yGTe6Pqo-66.png)](https://de.trustpilot.com/review/onlinecasinoohneoasis.me)[![Image 376: Open Collective Avatar for ViewSnapStories](https://www.11ty.dev/img/built/khTN8FSc3P-66.png)](https://viewsnapstories.com/)[![Image 377: Open Collective Avatar for Horoskopi](https://www.11ty.dev/img/built/Ydmv5fX4EW-66.png)](https://horoskopishqip.com/)[![Image 378: Open Collective Avatar for elfontario.ca](https://www.11ty.dev/img/built/RldOQxGdHJ-66.png)](https://elfontario.ca/)[![Image 379: Open Collective Avatar for FameViso | Instagram Growth Agency](https://www.11ty.dev/img/built/roytSDKbnn-66.png)](https://fameviso.com/)

*   [Edit this page](https://github.com/11ty/11ty-website/tree/main/src/docs/config.md)
*   [Accessibility](https://www.11ty.dev/docs/accessibility/)
*   [Credits](https://www.11ty.dev/docs/credits/)
*   [Firehose](https://www.11ty.dev/firehose/)
*   [Style Guide](https://www.11ty.dev/styleguide/)

*   **Built With**
*   _Eleventy v4.0.0_
*   **Statistics**
*   [19.3k Stars](https://github.com/11ty/eleventy/ "19297")
*   16.8M Downloads

*   **Awesomeverse**
*   [Font Awesome](https://fontawesome.com/)
*   [Web Awesome](https://webawesome.com/)
*   [Podcast Awesome](https://www.podcastawesome.com/)
*   [Blog Awesome](https://blog.fontawesome.com/)

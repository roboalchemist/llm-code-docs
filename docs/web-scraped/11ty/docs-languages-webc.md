# Source: https://www.11ty.dev/docs/languages/webc/

Title: WebC

URL Source: https://www.11ty.dev/docs/languages/webc/

Markdown Content:
Breadcrumbs:

*   [Eleventy Documentation](https://www.11ty.dev/docs/)
*   [Guide](https://www.11ty.dev/docs/projects/)
*   [Template Languages](https://www.11ty.dev/docs/languages/)

![Image 1: Logo for WebC](https://www.11ty.dev/img/built/PjwkLHHTs2-200.png)

On this page

*   [Why use WebC](https://www.11ty.dev/docs/languages/webc/#why-use-web-c)
    *   [Performance](https://www.11ty.dev/docs/languages/webc/#performance)
    *   [Compatible with Standards](https://www.11ty.dev/docs/languages/webc/#compatible-with-standards)
    *   [Authoring](https://www.11ty.dev/docs/languages/webc/#authoring)

*   [Resources](https://www.11ty.dev/docs/languages/webc/#resources)
*   [Installation](https://www.11ty.dev/docs/languages/webc/#installation)
    *   [Syntax highlighting](https://www.11ty.dev/docs/languages/webc/#syntax-highlighting)

*   [Usage](https://www.11ty.dev/docs/languages/webc/#usage)
    *   [Add a new .webc file](https://www.11ty.dev/docs/languages/webc/#add-a-new-webc-file)
    *   [Non-traditional WebC usage](https://www.11ty.dev/docs/languages/webc/#non-traditional-web-c-usage)

*   [WebC Reference](https://www.11ty.dev/docs/languages/webc/#web-c-reference)
    *   [HTML-only components](https://www.11ty.dev/docs/languages/webc/#html-only-components)
    *   [Asset bundling](https://www.11ty.dev/docs/languages/webc/#asset-bundling)
    *   [webckeep](https://www.11ty.dev/docs/languages/webc/#webckeep)
    *   [webcnokeep](https://www.11ty.dev/docs/languages/webc/#webcnokeep)
    *   [webcimport](https://www.11ty.dev/docs/languages/webc/#webcimport)
    *   [webcif](https://www.11ty.dev/docs/languages/webc/#webcif)
    *   [webcelseif and webcelse](https://www.11ty.dev/docs/languages/webc/#webcelseif-and-webcelse)
    *   [webcfor Loops](https://www.11ty.dev/docs/languages/webc/#webcfor-loops)
    *   [Slots](https://www.11ty.dev/docs/languages/webc/#slots)
    *   [Attributes and webcroot](https://www.11ty.dev/docs/languages/webc/#attributes-and-webcroot)
    *   [Props (Properties)](https://www.11ty.dev/docs/languages/webc/#props-properties)
    *   [Dynamic attributes and properties](https://www.11ty.dev/docs/languages/webc/#dynamic-attributes-and-properties)
    *   [@attributes](https://www.11ty.dev/docs/languages/webc/#attributes)
    *   [@html](https://www.11ty.dev/docs/languages/webc/#html)
    *   [@raw](https://www.11ty.dev/docs/languages/webc/#raw)
    *   [@text](https://www.11ty.dev/docs/languages/webc/#text)
    *   [webcis](https://www.11ty.dev/docs/languages/webc/#webcis)
    *   [webcscoped](https://www.11ty.dev/docs/languages/webc/#webcscoped)
    *   [Using JavaScript to Setup your Component](https://www.11ty.dev/docs/languages/webc/#using-java-script-to-setup-your-component)
    *   [Using Template Syntax to Generate Content](https://www.11ty.dev/docs/languages/webc/#using-template-syntax-to-generate-content)
    *   [Using JavaScript to Generate Content](https://www.11ty.dev/docs/languages/webc/#using-java-script-to-generate-content)
    *   [webcraw](https://www.11ty.dev/docs/languages/webc/#webcraw)
    *   [webcignore](https://www.11ty.dev/docs/languages/webc/#webcignore)
    *   [Server-only comments](https://www.11ty.dev/docs/languages/webc/#server-only-comments)
    *   [Custom Transforms](https://www.11ty.dev/docs/languages/webc/#custom-transforms)
    *   [Helper Functions](https://www.11ty.dev/docs/languages/webc/#helper-functions)
    *   [Subtleties and Limitations](https://www.11ty.dev/docs/languages/webc/#subtleties-and-limitations)

*   [Eleventy + WebC Features](https://www.11ty.dev/docs/languages/webc/#eleventy-web-c-features)
    *   [Front Matter](https://www.11ty.dev/docs/languages/webc/#front-matter)
    *   [Defining Components](https://www.11ty.dev/docs/languages/webc/#defining-components)
    *   [Official WebC Components](https://www.11ty.dev/docs/languages/webc/#official-web-c-components)
    *   [Eleventy Data Cascade](https://www.11ty.dev/docs/languages/webc/#eleventy-data-cascade)
    *   [CSS and JS (Bundler mode)](https://www.11ty.dev/docs/languages/webc/#css-and-js-bundler-mode)
    *   [Asset bucketing](https://www.11ty.dev/docs/languages/webc/#asset-bucketing)
    *   [Use with is-land](https://www.11ty.dev/docs/languages/webc/#use-with-is-land)

*   [From the Community](https://www.11ty.dev/docs/languages/webc/#from-the-community)

| Type | Value |
| --- | --- |
| Eleventy Name | `webc` |
| File Extension | `*.webc` |
| npm | [`@11ty/webc`](https://www.npmjs.com/package/@11ty/webc) and [`@11ty/eleventy-plugin-webc`](https://www.npmjs.com/package/@11ty/eleventy-plugin-webc) |
| GitHub | [`11ty/webc`](https://github.com/11ty/webc) and [`11ty/eleventy-plugin-webc`](https://github.com/11ty/eleventy-plugin-webc) |

Why use WebC?
-------------

[Jump to section titled: Why use WebC?](https://www.11ty.dev/docs/languages/webc/#why-use-web-c)
*   Brings first-class **components** to Eleventy. 
    *   Expand any HTML element (including custom elements) to HTML with defined conventions from web standards.
    *   This means that Web Components created with WebC are compatible with server-side rendering (without duplicating author-written markup)
    *   WebC components are [Progressive Enhancement friendly](https://www.youtube.com/watch?v=p0wDUK0Z5Nw).

### Performance

[Jump to section titled: Performance](https://www.11ty.dev/docs/languages/webc/#performance)
*   Create streamlined component-driven, cache-friendly page-specific JavaScript and CSS bundles. Users will only load the code they need to render that page (or that [island](https://www.11ty.dev/docs/plugins/is-land/)). 
    *   Easily [configurable boundaries](https://www.11ty.dev/docs/languages/webc/#asset-bucketing) for critical component CSS and JavaScript.
    *   Works great with [is-land](https://www.11ty.dev/docs/plugins/is-land/) for web component hydration.

*   Get first-class **incremental builds** (for page templates, components, and Eleventy layouts) when [used with `--incremental`](https://www.11ty.dev/docs/usage/#incremental-for-partial-incremental-builds)
*   Streaming friendly (stream on the Edge 👀)

### Compatible with Standards

[Jump to section titled: Compatible with Standards](https://www.11ty.dev/docs/languages/webc/#compatible-with-standards)
*   Uses [`parse5`](https://github.com/inikulin/parse5) to parse WebC HTML as modern browsers do (a nod to [@DasSurma’s](https://twitter.com/DasSurma/status/1559159122964127744) work with [Vite](https://twitter.com/patak_dev/status/1564265006627176449) here)
*   Shadow DOM and Declarative Shadow DOM friendly (easily switch components between Light DOM and Shadow DOM)

[Jump to section titled: Authoring](https://www.11ty.dev/docs/languages/webc/#authoring)
*   Encourages no-quirks mode HTML authoring (and a doctype is optional). WebC throws a helpful error if encounters quirks mode markup.
*   Easily scope component CSS (or use your own scoping utility).
*   Tired of importing components? Use global or per-page no-import components.
*   Async-friendly: All configuration extensions/hooks into WebC are async-friendly out of the box.
*   For more complex templating needs, render any existing Eleventy template syntax (Liquid, markdown, Nunjucks, etc.) inside of WebC.

Resources
---------

[Jump to section titled: Resources](https://www.11ty.dev/docs/languages/webc/#resources)
Installation
------------

[Jump to section titled: Installation](https://www.11ty.dev/docs/languages/webc/#installation)

Note that WebC support in Eleventy is **not bundled** with core! You must install the officially supported Eleventy plugin and the plugin **requires Eleventy v2.0.0** or newer.

It’s on [npm at `@11ty/eleventy-plugin-webc`](https://www.npmjs.com/package/@11ty/eleventy-plugin-webc)!

`npm install @11ty/eleventy-plugin-webc`

To add support for `.webc` files in Eleventy, add the plugin in your Eleventy configuration file:

eleventy.config.js

```
import pluginWebc from "@11ty/eleventy-plugin-webc";

export default function(eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc);
};
```

```
const pluginWebc = require("@11ty/eleventy-plugin-webc");

module.exports = function(eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc);
};
```

**Full options list** (defaults shown)
eleventy.config.js

```
import pluginWebc from "@11ty/eleventy-plugin-webc";

export default function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc, {
		// Glob to find no-import global components
		// (The default changed from `false` in Eleventy WebC v0.7.0)
		components: "_components/**/*.webc",

		// Adds an Eleventy WebC transform to process all HTML output
		useTransform: false,

		// Additional global data used in the Eleventy WebC transform
		transformData: {},

		// Options passed to @11ty/eleventy-plugin-bundle
		bundlePluginOptions: {},
	});
};
```

```
const pluginWebc = require("@11ty/eleventy-plugin-webc");

module.exports = function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc, {
		// Glob to find no-import global components
		// (The default changed from `false` in Eleventy WebC v0.7.0)
		components: "_components/**/*.webc",

		// Adds an Eleventy WebC transform to process all HTML output
		useTransform: false,

		// Additional global data used in the Eleventy WebC transform
		transformData: {},

		// Options passed to @11ty/eleventy-plugin-bundle
		bundlePluginOptions: {},
	});
};
```

View the [full options list for the Bundle plugin](https://www.11ty.dev/docs/plugins/bundle/). As an example, you can use the [`transforms` array to modify bundle content with postcss](https://www.11ty.dev/docs/plugins/bundle/#postprocess-the-bundle-output).

### Syntax highlighting

[Jump to section titled: Syntax highlighting](https://www.11ty.dev/docs/languages/webc/#syntax-highlighting)
Because WebC _is_ HTML you can configure your editor to treat `.webc` files as HTML, this should correctly syntax highlight your WebC files. Your editor of choice should have some documentation on how to get this working.

Usage
-----

[Jump to section titled: Usage](https://www.11ty.dev/docs/languages/webc/#usage)
There are a few different ways to use WebC in Eleventy:

### Add a new `.webc` file

[Jump to section titled: Add a new .webc file](https://www.11ty.dev/docs/languages/webc/#add-a-new-webc-file)
Adding the plugin will enable support for `.webc` files in your Eleventy project. Just make a new `.webc` HTML file in your Eleventy input directory and Eleventy will process it for you! Notably, `.webc` files will operate [WebC in bundler mode](https://github.com/11ty/webc#aggregating-css-and-js), aggregating the CSS and JS in use on each individual page to create a bundle of the assets in use on the page.

WebC uses an HTML parser to process input files: use any HTML here!

**Filename**my-page.webc

```
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title>WebC Example</title>
	</head>
	<body>
		WebC *is* HTML.
	</body>
</html>
```

### Non-traditional WebC usage

[Jump to section titled: Non-traditional WebC usage](https://www.11ty.dev/docs/languages/webc/#non-traditional-web-c-usage)
#### Use the Render plugin

[Jump to section titled: Use the Render plugin](https://www.11ty.dev/docs/languages/webc/#use-the-render-plugin)
Using Eleventy’s built-in [Render plugin](https://www.11ty.dev/docs/plugins/render/) allows you to render WebC inside of an existing Liquid, Nunjucks, or 11ty.js template.

```
{% renderTemplate "webc" %}
<my-custom-component></my-custom-component>
{% endrenderTemplate %}
```

```
{% renderTemplate "webc" %}
<my-custom-component></my-custom-component>
{% endrenderTemplate %}
```

```
export default async function () {
	let content = await this.renderTemplate(
		`<my-custom-component></my-custom-component>`,
		"webc"
	);
	return content;
};
```

```
module.exports = async function () {
	let content = await this.renderTemplate(
		`<my-custom-component></my-custom-component>`,
		"webc"
	);
	return content;
};
```

#### Pre-process HTML input as WebC

[Jump to section titled: Pre-process HTML input as WebC](https://www.11ty.dev/docs/languages/webc/#pre-process-html-input-as-web-c)
You can use the configuration option to change the default HTML preprocessor (from `liquid`) to `webc`. This might look like `htmlTemplateEngine: "webc"`. Read more on the [Eleventy documentation: Default Template Engine for HTML Files](https://www.11ty.dev/docs/config/#default-template-engine-for-html-files).

#### Post-process HTML output as WebC

[Jump to section titled: Post-process HTML output as WebC](https://www.11ty.dev/docs/languages/webc/#post-process-html-output-as-web-c)
This is a (last-resort?) catch-all option to let WebC process `.html` output files in your project (skipping any `.webc` input files to avoid double-processing templates). This feature makes use of [Eleventy transforms](https://www.11ty.dev/docs/config/#transforms) and is most useful when you want to get up and running with WebC on an existing project quickly.

A few drawbacks to the transform method:

1.   This is the slowest build-performance method to implement WebC in a project, so try the other methods first!
2.   The WebC Eleventy transform operates with [bundler mode disabled](https://www.11ty.dev/docs/languages/webc/#css-and-js-bundler-mode), which means that processes WebC but _does not_ aggregate component JS or CSS. ([Upvote this enhancement request](https://github.com/11ty/eleventy-plugin-webc/issues/55))

The transform is disabled by default, you will need to use the `useTransform` option to enable it.
eleventy.config.js

```
import pluginWebc from "@11ty/eleventy-plugin-webc";

export default function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc, {
		useTransform: true,
	});
};
```

```
const pluginWebc = require("@11ty/eleventy-plugin-webc");

module.exports = function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc, {
		useTransform: true,
	});
};
```

WebC Reference
--------------

[Jump to section titled: WebC Reference](https://www.11ty.dev/docs/languages/webc/#web-c-reference)
**Note:** All `webc:` attributes are removed from the rendered output HTML.

### HTML-only components

[Jump to section titled: HTML-only components](https://www.11ty.dev/docs/languages/webc/#html-only-components)
*   _Related: [Defining Components in WebC](https://www.11ty.dev/docs/languages/webc/#defining-components)_

When a component has only content HTML (no CSS or JavaScript) it will ignore the host component tag in the output HTML. This enables HTML-only components to have zero overhead HTML. _(You can opt-out of this behavior with `webc:keep`.)_

Expand for Example

WebC components are not limited to custom element name restrictions (e.g. `my-component`) here. You can use `p`, `blockquote`, `h1`, `img`, or any valid HTML tag name.

**Filename**page.webc

```
<!DOCTYPE html>
<title>WebC Example</title>
<my-component></my-component>
```

**Filename**components/my-component.webc

`Components don’t need a root element, y’all.`
Outputs:

**Filename**_site/page.html

```
<!DOCTYPE html>
<html>
	<head>
		<title>WebC Example</title>
	</head>
	<body>
		Components don’t need a root element, y’all.
	</body>
</html>
```

### Asset bundling

[Jump to section titled: Asset bundling](https://www.11ty.dev/docs/languages/webc/#asset-bundling)
For components that are _not_ HTML-only (they _do_ have CSS or JS), WebC will include the component tag in the output markup (e.g. `<my-component>`) (for styling or client scripting). _(You can opt-out of this behavior with `webc:nokeep`.)_

Expand for Example

WebC components are not limited to custom element name restrictions (e.g. `my-component`) here. You can use `p`, `blockquote`, `h1`, `img`, or any valid HTML tag name.

**Filename**page.webc

```
<!DOCTYPE html>
<title>WebC Example</title>
<my-component></my-component>
```

**Filename**components/my-component.webc

```
Components don’t need a root element, y’all.
<style>
	/* Hi */
</style>
```

Outputs:

**Filename**_site/page.html

```
<!DOCTYPE html>
<html>
	<head>
		<title>WebC Example</title>
	</head>
	<body>
		<my-component>Components don’t need a root element, y’all.</my-component>
	</body>
</html>
```

Eleventy runs WebC in Bundler mode. That means that when it finds `<style>`, `<link rel="stylesheet">`, or `<script>` elements in component definitions, they are removed from the output markup and _their content_ is aggregated together for re-use in asset bundles on the page. Read more about [CSS and JS in WebC](https://www.11ty.dev/docs/languages/webc/#css-and-js-bundler-mode). _(You can opt-out of this behavior with `webc:keep`.)_

### `webc:keep`

[Jump to section titled: webc:keep](https://www.11ty.dev/docs/languages/webc/#webckeep)
With an [HTML-only component](https://www.11ty.dev/docs/languages/webc/#html-only-components), you can use `webc:keep` on the host component to keep the tag around:

`<html-only-component webc:keep></html-only-component>`
You can also use `webc:keep` to opt-out of [asset bundling](https://www.11ty.dev/docs/languages/webc/#asset-bundling) for individual elements inside of a component definition:

```
<style webc:keep></style>
<script webc:keep></script>
```

You can also use `webc:keep` to save a [`<slot>`](https://www.11ty.dev/docs/languages/webc/#slots) for use in a client-side custom element.

### `webc:nokeep`

[Jump to section titled: webc:nokeep](https://www.11ty.dev/docs/languages/webc/#webcnokeep)
With an CSS/JS component (not an [HTML-only component](https://www.11ty.dev/docs/languages/webc/#html-only-components)), you can use `webc:nokeep` on the host component to drop the tag:

`<css-js-component webc:nokeep></css-js-component>`
### `webc:import`

[Jump to section titled: webc:import](https://www.11ty.dev/docs/languages/webc/#webcimport)
WebC will expand any component it finds using known components. You can also use `webc:import` to inline import a component definition. This import path is relative to the component file path. WebC checks for circular component dependencies and throws an error if one is encountered.

*   _Related: [Defining Components in WebC](https://www.11ty.dev/docs/languages/webc/#defining-components) (global or scoped)_

`<any-tag-name webc:import="./components/my-component.webc"></any-tag-name>`
Added in @11ty/webc@0.6.2 You can import directly from an installed npm package. Eleventy will begin to supply WebC components with existing plugins. The Syntax Highlighter (`4.2.0` or newer) supplies one that you can use today:

```
<syntax-highlight
	language="js"
	webc:import="npm:@11ty/eleventy-plugin-syntaxhighlight"
>
	function myFunction() { return true; }
</syntax-highlight>
```

This uses the component tag name (`syntax-highlight`) to look for a WebC component at `node_modules/@11ty/eleventy-plugin-syntaxhighlight/syntax-highlight.webc` and imports it for use on this node. This works with a tag name override via `webc:is` too.

### `webc:if`

[Jump to section titled: webc:if](https://www.11ty.dev/docs/languages/webc/#webcif)
Added in @11ty/webc@0.7.1

Use `webc:if` to conditionally render elements. Accepts arbitrary JavaScript (and is async-friendly). Similar to dynamic attributes, this also has access to component attributes and properties.

```
<div webc:if="true">This will render</div>
<div webc:if="false">This will not render</div>
<div webc:if="myAsyncHelper()">
	If the helper promise resolves to a truthy value, this will render
</div>
```

You can use `webc:type="js"`_(WebC v0.7.1+)_ to use JavaScript for more complex conditional logic (read more below).

### `webc:elseif` and `webc:else`

[Jump to section titled: webc:elseif and webc:else](https://www.11ty.dev/docs/languages/webc/#webcelseif-and-webcelse)
Added in @11ty/webc@0.10.0

Adjacent siblings of `webc:if` can use `webc:elseif=""` and `webc:else` for additional conditional logic.

```
<div webc:if="false">This will not render</div>
<!-- interspersing comments works ok -->
<div webc:elseif="true">This will render</div>
<div webc:else>This will not render</div>
```

### `webc:for` Loops

[Jump to section titled: webc:for Loops](https://www.11ty.dev/docs/languages/webc/#webcfor-loops)
Added in @11ty/webc@0.10.0

Use `webc:for` to loop over data with HTML. It works with Objects and any [Iterable](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators#built-in_iterables) (String, Array, Map, Set, etc).

The syntax should feel similar to JavaScript’s `for` statement.

#### Arrays (or any other Iterable)

[Jump to section titled: Arrays (or any other Iterable)](https://www.11ty.dev/docs/languages/webc/#arrays-or-any-other-iterable)
```
<!-- renders three div elements -->
<div webc:for="item of [1, 2, 3]" @text="item"></div>

<!-- access the loop index (zero-indexed) -->
<div webc:for="(item, index) of [1, 2, 3]" @text="index"></div>

<!-- name these whatever you’d like -->
<div webc:for="myItem of [1, 2, 3]" @text="myItem"></div>
<div webc:for="(myItem, myIndex) of [1, 2, 3]" @text="myIndex"></div>

<!-- any iterable -->
<div webc:for="item of new Set([1, 2, 3])" @text="item"></div>
```

#### Objects

[Jump to section titled: Objects](https://www.11ty.dev/docs/languages/webc/#objects)
Note the use of `in` instead of `of`.

```
<!-- renders two div elements -->
<div webc:for="key in { a: 1, b: 2 }" @text="key"></div>

<!-- access the value -->
<div webc:for="(key, value) in { a: 1, b: 2 }" @text="value"></div>

<!-- access the loop index (zero-indexed) -->
<div webc:for="(key, value, index) in { a: 1, b: 2 }" @text="index"></div>

<!-- name these whatever you’d like -->
<div
	webc:for="(myKey, myValue, myIndex) in { a: 1, b: 2 }"
	@text="myIndex"
></div>

<!-- use `Object.values` or `Object.keys`, sure -->
<div webc:for="value of Object.values({ a: 1, b: 2 })"></div>
<div webc:for="key of Object.keys({ a: 1, b: 2 })"></div>
```

#### Nesting `webc:for`

[Jump to section titled: Nesting webc:for](https://www.11ty.dev/docs/languages/webc/#nesting-webcfor)
Loops can be nested but access to outer scope from the inner loop doesn't work currently. More at [issue #175](https://github.com/11ty/webc/issues/175).

### Slots

[Jump to section titled: Slots](https://www.11ty.dev/docs/languages/webc/#slots)
Child content optionally precompiles using `<slot>` and `[slot]` too. This example is using an [HTML-only component](https://www.11ty.dev/docs/languages/webc/#html-only-components).

**Filename**page.webc

```
<my-component></my-component>
<my-component>This is the default slot</my-component>
```

**Filename**components/my-component.webc

`<p><slot>Fallback slot content</slot></p>`
Compiles to:

```
<p>Fallback slot content</p>
<p>This is the default slot</p>
```

If your WebC component wants to _output_ a `<slot>` tag in the compiled markup (for use in client JavaScript), use the [`webc:keep` attribute](https://www.11ty.dev/docs/languages/webc/#webckeep) (e.g. `<slot webc:keep>`).

Per web component standard conventions, if your component file contains _no content markup_ (e.g. empty or only `<style>`/`<script>`), `<slot></slot>` is implied and the default slot content will be included automatically. If the WebC component file does contain content markup, the content passed in as the default slot requires `<slot>` to be included.

#### Named slots

[Jump to section titled: Named slots](https://www.11ty.dev/docs/languages/webc/#named-slots)
This works with named slots (e.g. `<span slot="named-slot">`) too.

Expand for Example
**Filename**page.webc

```
<my-component>
	This is the default slot.
	<strong slot="named-slot">This is a named slot</strong>
	This is also the default slot.
</my-component>
```

**Filename**components/my-component.webc

`<p><slot name="named-slot"></slot></p>`
Compiles to:

`<p><strong>This is a named slot.</strong></p>`

### Attributes and `webc:root`

[Jump to section titled: Attributes and webc:root](https://www.11ty.dev/docs/languages/webc/#attributes-and-webcroot)
**Filename**page.webc

`<my-component class="sr-only"></my-component>`
Inside of your component definition, you can add attributes to the outer host component using `webc:root`:

**Filename**components/my-component.webc

`<template webc:root class="another-class"> Some component content </template>`
`class` and `style` attribute values are _merged_ as expected between the host component and the `webc:root` element.

Comparing WebC Attribute Data Types

1.   [Attributes](https://www.11ty.dev/docs/languages/webc/#attributes-and-webcroot): HTML attribute strings.
2.   [Properties](https://www.11ty.dev/docs/languages/webc/#props-(properties)): server-only private HTML attribute strings (not rendered to output).
3.   [Dynamic Attributes and Properties](https://www.11ty.dev/docs/languages/webc/#dynamic-attributes-and-properties): evaluate as JavaScript (any data type, not just strings).

#### Override the host component tag

[Jump to section titled: Override the host component tag](https://www.11ty.dev/docs/languages/webc/#override-the-host-component-tag)
You can use `webc:root="override"` to override the host component tag name! This isn’t very useful for HTML-only components (which leave out the host component tag), but is very useful when your component has style/scripts.

**Filename**components/my-component.webc

```
<button webc:root="override">Some component content</button>
<style>
	/* Hi */
</style>
```

*   Added in @11ty/webc@0.9.0 Previously, the above used to be accomplished by using `webc:root` and `webc:keep` together on an element.

#### Nesting

[Jump to section titled: Nesting](https://www.11ty.dev/docs/languages/webc/#nesting)
It’s worth noting also that `webc:root` can be nested inside of other content—it does not need to exist at the top level of the component definition. (Framework folks love things deeply nested in `div`s, right?)

**Filename**components/my-component.webc

```
<div>
	<div>
		<template webc:root="override" class="another-class">
			Some component content
		</template>
	</div>
</div>
```

### Props (Properties)

[Jump to section titled: Props (Properties)](https://www.11ty.dev/docs/languages/webc/#props-properties)
Make any attribute into a prop by prefixing it with `@`. Props are server-only “private” attributes that don’t end up in the output HTML (they are private to WebC). They are identical to attributes except that they are filtered from the output HTML.

**Filename**page.webc

`<my-component @prop="Hello"></my-component>`
**Filename**components/my-component.webc

```
<p @text="prop"></p>
<!-- outputs <p>Hello</p> -->
```

*   In the HTML specification, attribute names are lower-case. Added in @11ty/webc@0.8.0 Attribute or property names with dashes are converted to camelcase for JS (e.g. `<my-component @prop-name="test">` can be used like `@text="propName"`). More at [issue #71](https://github.com/11ty/webc/issues/71).

Comparing WebC Attribute Data Types

1.   [Attributes](https://www.11ty.dev/docs/languages/webc/#attributes-and-webcroot): HTML attribute strings.
2.   [Properties](https://www.11ty.dev/docs/languages/webc/#props-(properties)): server-only private HTML attribute strings (not rendered to output).
3.   [Dynamic Attributes and Properties](https://www.11ty.dev/docs/languages/webc/#dynamic-attributes-and-properties): evaluate as JavaScript (any data type, not just strings).

### Dynamic attributes and properties

[Jump to section titled: Dynamic attributes and properties](https://www.11ty.dev/docs/languages/webc/#dynamic-attributes-and-properties)
Make any attribute or property dynamic (using JavaScript for the value instead of a string) by prefixing it with a colon (`:`). You have access to host component attributes, props, and page data here!

**Filename**page.webc

```
<avatar-image
	src="my-image.jpeg"
	alt="Zach is documenting this project"
	:@dynamic-prop="'hello'"
></avatar-image>
```

**Filename**components/avatar-image.webc

`<img :src="src" :alt="alt" class="avatar-image" />`
*   Added in @11ty/webc@0.9.0 The `:@` dynamic property prefix was added in WebC v0.9.0.
*   In the HTML specification, attribute names are lower-case. Added in @11ty/webc@0.8.0 Attribute or property names with dashes are converted to camelcase for JS (e.g. `<my-component @prop-name="test">` can be used like `@text="propName"`). More at [#71](https://github.com/11ty/webc/issues/71).

*   The only currently supported `webc:*` configuration attribute that supports dynamic values is [`webc:bucket`](https://www.11ty.dev/docs/languages/webc/#asset-bucketing). More to come here: [#143](https://github.com/11ty/webc/issues/143)[#148](https://github.com/11ty/webc/issues/148)

Comparing WebC Attribute Data Types

1.   [Attributes](https://www.11ty.dev/docs/languages/webc/#attributes-and-webcroot): HTML attribute strings.
2.   [Properties](https://www.11ty.dev/docs/languages/webc/#props-(properties)): server-only private HTML attribute strings (not rendered to output).
3.   [Dynamic Attributes and Properties](https://www.11ty.dev/docs/languages/webc/#dynamic-attributes-and-properties): evaluate as JavaScript (any data type, not just strings).

### `@attributes`

[Jump to section titled: @attributes](https://www.11ty.dev/docs/languages/webc/#attributes)
Added in @11ty/webc@0.9.0 You can use `@attributes` to render all of the attributes (including on host component) to the current node.

**Filename**components/avatar-image.webc

```
<!-- will render all attributes including `src` and `alt` from the host component -->
<img @attributes class="avatar-image" />
```

You can use this to render an arbitrary object as attributes too (note the parentheses to avoid JavaScript parsing as a [`block`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block) + [`label`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)):

`<img @attributes="({ myattribute: 'myValue'})" />`
### `@html`

[Jump to section titled: @html](https://www.11ty.dev/docs/languages/webc/#html)
We surface a special `@html`[prop](https://www.11ty.dev/docs/languages/webc/#props-(properties)) to override any tag content with custom JavaScript.

```
<template @html="'Template HTML'"></template>
<template @html="dataProperty"></template>
```

```
<!-- webc:nokeep will replace the outer element -->
<template @html="'Template HTML'" webc:nokeep></template>
```

*   Content returned from the `@html` prop will be processed as WebC—return any WebC content here! Added in @11ty/webc@0.5.0

*   Using `webc:raw` will prevent processing the result as WebC Added in @11ty/webc@0.6.0
*   Use `@raw` as an alias for `webc:raw @html`Added in @11ty/webc@0.7.1

```
<!-- No reprocessing as WebC (useful in Eleventy layouts) -->
<!-- Where `myHtmlContent` is a variable holding an arbitrary HTML string -->
<template @raw="myHtmlContent" webc:nokeep></template>
```

### `@raw`

[Jump to section titled: @raw](https://www.11ty.dev/docs/languages/webc/#raw)
Added in @11ty/webc@0.7.1

As noted in [`@html`](https://www.11ty.dev/docs/languages/webc/#@html), you can use `@raw` as an alias for `webc:raw @html`.

### `@text`

[Jump to section titled: @text](https://www.11ty.dev/docs/languages/webc/#text)
Added in @11ty/webc@0.6.0

We provide a special `@text`[prop](https://www.11ty.dev/docs/languages/webc/#props-(properties)) to override any tag content with custom JavaScript. The entire value returned here will be escaped!

```
<p @text="dataProperty"></p>

<!-- When dataProperty contains `<p>This is text</p>`, this renders: -->
<p>&lt;p&gt;This is text&lt;/p&gt;</p>
```

```
<!-- webc:nokeep will replace the outer element -->
<p @text="dataProperty" webc:nokeep></p>
```

*   Content returned from the `@text` prop will **not** be processed as WebC.

### `webc:is`

[Jump to section titled: webc:is](https://www.11ty.dev/docs/languages/webc/#webcis)
Remap a component to another component name.

```
<div webc:is="my-component"></div>

<!-- equivalent to -->
<my-component></my-component>
```

### `webc:scoped`

[Jump to section titled: webc:scoped](https://www.11ty.dev/docs/languages/webc/#webcscoped)
We include a lightweight mechanism (`webc:scoped`) to scope component CSS. Selectors are prefixed with a new component class name. The class name is based on a hash of the style content (for fancy de-duplication of identical component styles).

Expand for example
**Filename**page.webc

`<my-component>Default slot</my-component>`
If you use `:host` it will be replaced with that class selector.

**Filename**components/my-component.webc

```
<style webc:scoped>
	:host {
		color: blue;
	}
	:host:defined {
		color: rebeccapurple;
	}
</style>
```

This outputs:

`<my-component class="wcl2xedjk">Default slot</my-component>`
and aggregates the following CSS to [the bundle](https://www.11ty.dev/docs/languages/webc/#asset-bundling):

```
.wcl2xedjk {
	color: blue;
}
.wcl2xedjk:defined {
	color: rebeccapurple;
}
```

_**CSS bundling opinion alert**:_ Some folks recommend using Declarative Shadow DOM for component style encapsulation. This is a great method! It has 2 major drawbacks:

1.   The progressive enhancement story requires [ubiquitous browser support](https://caniuse.com/declarative-shadow-dom) before using it for content in the critical rendering path.
2.   It requires `<style>` duplication in each instance of the component.

Just be aware of these tradeoffs. And remember that you can use both methods in WebC!

#### `webc:scoped="my-prefix"`

[Jump to section titled: webc:scoped="my-prefix"](https://www.11ty.dev/docs/languages/webc/#webcscopedmy-prefix)
You can also specify an attribute value to `webc:scoped` to hard code your own component prefix (e.g. `<style webc:scoped="my-prefix">`). This allows the CSS to look a bit more friendly and readable. We will automatically check for duplicate values in your component tree and throw an error if collisions occur.

### Using JavaScript to Setup your Component

[Jump to section titled: Using JavaScript to Setup your Component](https://www.11ty.dev/docs/languages/webc/#using-java-script-to-setup-your-component)
Added in @11ty/webc@0.9.0 You can now also use `<script webc:setup>` to run arbitrary JavaScript and provide data and markup to your component. Any top level variables declared here are available in your component as local data.

This is similar to using [JavaScript as a custom Eleventy Front Matter type](https://www.11ty.dev/docs/data-frontmatter-customize/#example-use-javascript-in-your-front-matter), although data in `webc:setup` is scoped to the component and _does not_ flow back up in the Data Cascade.

**Note:** This JavaScript is run _only once_ per build, even if the component is used in multiple instances. Therefore, there is no access inside the `<script webc:setup>` tag to instance-specific data such as attributes, props, or slots.

**Filename**components/my-component.webc

```
<script webc:setup>
	const myHtml = "<my-webc-component></my-webc-component>";

	function alwaysBlue() {
		return "blue";
	}
</script>

<div @html="myHtml"></div>
<div @raw="myHtml"></div>
<!-- @raw does not reprocess as WebC -->
<div @html="alwaysBlue()"></div>
```

Works with `var`, `let`, `const`, `function`, `Array`, and `Object`[destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

*   Uses the [`node-retrieve-globals` package](https://github.com/zachleat/node-retrieve-globals/).

### Using Template Syntax to Generate Content

[Jump to section titled: Using Template Syntax to Generate Content](https://www.11ty.dev/docs/languages/webc/#using-template-syntax-to-generate-content)
The [Custom Transforms feature](https://github.com/11ty/webc#custom-transforms) (e.g. `webc:type`) in the Eleventy WebC plugin has been wired up to the [Eleventy Render plugin](https://www.11ty.dev/docs/plugins/render/) to allow you to use existing Eleventy template syntax inside of WebC.

**Note:** The `webc:type="11ty"` feature is exclusive to the **Eleventy** WebC plugin and is not available in non-Eleventy independent WebC.

Use `webc:type="11ty"` with the `11ty:type` attribute to specify a [valid template syntax](https://www.11ty.dev/docs/plugins/render/#rendertemplate-paired-shortcode).

**Filename**my-page.webc

```
---
frontmatterdata: "Hello from Front Matter"
---
<template webc:type="11ty" 11ty:type="liquid,md">
{% assign t = "Liquid in WebC" %}
## {{ t }}

_{{ frontmatterdata }}_
</template>
```

*   You have full access to the data cascade here (note `frontmatterdata` is [set in front matter](https://www.11ty.dev/docs/languages/webc/#front-matter) above).
*   Added in @11ty/webc@0.5.0 Content returned from custom transforms on `<template>` (or `webc:is="template"`) nodes will be processed as WebC—return any WebC content here!

### Using JavaScript to Generate Content

[Jump to section titled: Using JavaScript to Generate Content](https://www.11ty.dev/docs/languages/webc/#using-java-script-to-generate-content)
You can also transform individual element content using `webc:type`. In addition to `webc:type="11ty"`, there are three more bundled types:

1.   `webc:type="js"`Added in @11ty/webc@0.7.1
2.   `webc:type="render"` (superseded by `webc:type="js"`)
3.   `webc:type="css:scoped"` (internal for `webc:scoped`—but overridable!)

#### JavaScript Render Functions: `webc:type="js"` and `webc:type="render"`

[Jump to section titled: JavaScript Render Functions: webc:type="js" and webc:type="render"](https://www.11ty.dev/docs/languages/webc/#java-script-render-functions-webctypejs-and-webctyperender)
Added in @11ty/webc@0.7.1 Run any arbitrary server JavaScript in WebC. Outputs the result of the very last statement executed in the script. Async-friendly (return a promise and we’ll resolve it).

**Filename**page.webc

```
<img
	src="my-image.jpeg"
	alt="An excited Zach is trying to finish this documentation"
/>
```

**Filename**components/img.webc

```
<script webc:type="js" webc:root>
	if (!alt) {
		throw new Error("oh no you didn’t");
	}
	`<img src="${src}" alt="${alt}">`;
</script>
```

Expand to see this example with `webc:type="render"`
```
<script webc:type="render">
	export default function() {
		if(!this.alt) {
			throw new Error("oh no you didn’t");
		}
		// Free idea: use the Eleventy Image plugin to return optimized markup
		return `<img src="${this.src}" alt="${this.alt}">`;
	}
</script>
```

Or use a JavaScript render function to generate some CSS:

**Filename**page.webc

```
<style webc:is="add-banner-to-css" @license="MIT licensed">
	p {
		color: rebeccapurple;
	}
</style>
```

**Filename**components/add-banner-to-css.webc

```
<template webc:is="style" webc:root="override">
	<script webc:type="js">
		export default function({ license }) {
			return `/* ${license} */`;
		}
	</script>
	<slot></slot>
</template>
```

Expand to see this example with `webc:type="render"`
```
<template webc:is="style" webc:root="override">
	<script webc:type="render">
		export default function() {
			return `/* ${this.license} */`;
		}
	</script>
	<slot></slot>
</template>
```

Expand to see another example of a more complex conditional using `webc:type="js"`
Note that you can also use `webc:if`!

```
<script webc:type="js">
export default function({ src, alt }) {
	if (alt) {
		return `<img src="${src}" alt="${alt}">`;
	} else {
		return `<a href="${src}">Your image didn’t have an alt so you get this link instead.</a>`;
	}
}
</script>
```

Bonus tips:

*   You can use `webc:scoped webc:is="style" webc:type="js"` (or `webc:type="render"`) to generate scoped CSS using JavaScript! Read more at [`webc:scoped`](https://www.11ty.dev/docs/languages/webc/#webcscoped).
*   You have access to the component attributes and props in the render function (which is covered in another section!).
*   Added in @11ty/webc@0.9.0 Using `webc:type="js"` has an implied `webc:is="template"` to return content that will be reprocessed as WebC (HTML). You can override this with your own `webc:is` attribute to generate a different tag (e.g. `webc:is="script"` or `webc:is="style"`).
*   Added in @11ty/webc@0.9.0 Using `webc:type="js"` has an implied `webc:nokeep` to skip outputting the outer node. You can add `webc:keep` to override this behavior.

[Jump to section titled: Extra data for JavaScript Render Functions](https://www.11ty.dev/docs/languages/webc/#extra-data-for-java-script-render-functions)
*   `webc.attributes`: Added in @11ty/webc@0.9.0 an object literal representing the current element’s attributes.
*   `webc.renderAttributes`: Added in @11ty/webc@0.9.0 a method to render _public_ attributes to a string.
*   `webc.filterPublicAttributes`: Added in @11ty/webc@0.10.1 a method to filter `webc.attributes`, returning an object with only _public_ attributes. Usage: `webc.filterPublicAttributes(webc.attributes)`
*   `webc.escapeText`: Added in @11ty/webc@0.10.1 encodes all characters that have to be escaped in HTML text (via the [`entities` package](https://github.com/fb55/entities/blob/b6cd547c8088b55a18b2ef449bc9dc8f9c294f0c/src/escape.ts#L126))
*   `webc.escapeAttribute`: Added in @11ty/webc@0.10.1 encodes all characters that have to be escaped in HTML attributes (via the [`entities` package](https://github.com/fb55/entities/blob/b6cd547c8088b55a18b2ef449bc9dc8f9c294f0c/src/escape.ts#L111))

Read more at [Issue #104](https://github.com/11ty/webc/issues/104).

Expand to see an `img` component example
One might imagine an `<img>` component definition that merges and re-uses all host component attributes correctly like this:

**Filename**components/img.webc

```
<script webc:type="js" webc:root="override">
	`<img ${webc.renderAttributes(webc.attributes)}>`;
</script>
```

### `webc:raw`

[Jump to section titled: webc:raw](https://www.11ty.dev/docs/languages/webc/#webcraw)
Use `webc:raw` to opt-out of WebC template processing for all child content of the current node. Notably, attributes on the current node will be processed. This works well with `<template>`!

**Filename**components/my-component.webc

```
<template webc:raw>
	Leave me out of this.
	<style>
		p {
			color: rebeccapurple;
		}
	</style>
</template>
```

*   Related: [`@raw` property](https://www.11ty.dev/docs/languages/webc/#@raw)

### `webc:ignore`

[Jump to section titled: webc:ignore](https://www.11ty.dev/docs/languages/webc/#webcignore)
Added in @11ty/webc@0.9.0 Use `webc:ignore` to completely ignore a node and not process or output anything to do with it. Useful for server-side comments or documentation on a component.

**Filename**components/my-component.webc

```
<template webc:ignore>
	Here’s how you might use this component:

	<my-component>Nothing in here will be processed</my-component>
</template>
```
[Jump to section titled: Server-only comments](https://www.11ty.dev/docs/languages/webc/#server-only-comments)
Added in @11ty/webc@0.10.0

Instead of an HTML comment that will show up in rendered output, you can add one or more dashes to the beginning/end to tell WebC to strip this from the output. Great for server-side comments.

**Filename**components/my-component.webc

```
<!--- WebC will remove this --->
<!-- This will *not* be removed and is rendered to the output -->
<!------- WebC will remove this, too ------->
```

### Custom Transforms

[Jump to section titled: Custom Transforms](https://www.11ty.dev/docs/languages/webc/#custom-transforms)
This plugin provides a few transforms out of the box: `webc:type="js"`, `webc:type="render"`, `webc:type="css:scoped"`, and `webc:type="11ty"`.

However, adding your own [`webc:type` Custom Transform](https://github.com/11ty/webc#custom-transforms)**directly** to WebC is not yet available in the Eleventy WebC plugin! If this is something folks would like to see added, [please let us know](https://neighborhood.11ty.dev/@11ty)!

Do note that you **can**[add your own custom template engine](https://www.11ty.dev/docs/languages/custom/) which would be available via `webc:type="11ty"` (e.g. `<style webc:type="11ty" 11ty:type="sass">`).

### Helper Functions

[Jump to section titled: Helper Functions](https://www.11ty.dev/docs/languages/webc/#helper-functions)
WebC [Helpers](https://github.com/11ty/webc#helper-functions) are JavaScript functions available in dynamic attributes, `@html`, `@raw`, and render functions.

#### Eleventy-provided Helpers

[Jump to section titled: Eleventy-provided Helpers](https://www.11ty.dev/docs/languages/webc/#eleventy-provided-helpers)
Added in @11ty/eleventy-plugin-webc@0.5.0 Included with Eleventy WebC, [JavaScript template functions](https://www.11ty.dev/docs/languages/javascript/#javascript-template-functions) and [Universal Filters](https://www.11ty.dev/docs/filters/) are provided automatically as WebC Helpers.

This includes [`url`, `slugify`, `log`, and others](https://www.11ty.dev/docs/filters/#eleventy-provided-filters)!

```
<!-- Use the  Eleventy provided `url` universal filter -->
<a :href="url('/local-path/')">My Link</a>
```

#### Supply your own Helper

[Jump to section titled: Supply your own Helper](https://www.11ty.dev/docs/languages/webc/#supply-your-own-helper)
eleventy.config.js

```
export default function (eleventyConfig) {
	// via Universal Filter
	eleventyConfig.addFilter("alwaysRed", () => "Red");

	// or via JavaScript Template Function directly
	eleventyConfig.addJavaScriptFunction("alwaysBlue", () => "Blue");

	// Don’t forget to add the WebC plugin in your config file too!
};
```

```
module.exports = function (eleventyConfig) {
	// via Universal Filter
	eleventyConfig.addFilter("alwaysRed", () => "Red");

	// or via JavaScript Template Function directly
	eleventyConfig.addJavaScriptFunction("alwaysBlue", () => "Blue");

	// Don’t forget to add the WebC plugin in your config file too!
};
```

```
<div @html="alwaysRed()"></div>
<div @html="alwaysBlue()"></div>

<!-- renders as: -->
<div>Red</div>
<div>Blue</div>
```

### Subtleties and Limitations

[Jump to section titled: Subtleties and Limitations](https://www.11ty.dev/docs/languages/webc/#subtleties-and-limitations)
#### Void elements

[Jump to section titled: Void elements](https://www.11ty.dev/docs/languages/webc/#void-elements)
Custom elements (per specification) are not supported as void elements: they require both a starting and ending tag.

Practically speaking, this means a WebC component cannot be self-closing. You can workaround this limitation using [`webc:is`](https://www.11ty.dev/docs/languages/webc/#webcis) (e.g. `<img webc:is="my-component">`).

#### `<head>` Components

[Jump to section titled: Components](https://www.11ty.dev/docs/languages/webc/#components)
There are a few wrinkles when using an HTML parser with custom elements. Notably, the parser tries to force custom element children in the `<head>` over to the `<body>`. To workaround this limitation, use [`webc:is`](https://www.11ty.dev/docs/languages/webc/#webcis).

Expand for a few example workarounds
```
<head webc:is="my-custom-head">
	<!-- this is slot content, yes you can use named slots here too -->
</head>
```

```
<head>
	<!-- <my-custom-head> is not allowed here but
			 <meta webc:is="my-custom-head> is -->
	<meta webc:is="my-custom-head" />
	<title webc:is="my-custom-title">Default Title</title>
</head>
```

#### `<table>` Components

[Jump to section titled: Components](https://www.11ty.dev/docs/languages/webc/#components-2)
Due to WebC's use of the parse5 library, all WebC files to be processed undergo parsing and tokenization in the same way a web browser would parse them. For this reason, putting a `<table>` tag in a custom WebC element and it's `<tr>` and `<td>` tags in a slot to be inserted into the table will cause the `<tr>` and `<td>` elements to be removed upon initial parsing and all internals of the table to be placed as a sibling to itself. This is caused by the parse5 library believing the `<tr>` and `<td>` tags are orphaned.

To workaround this limitation, use [`webc:is`](https://www.11ty.dev/docs/languages/webc/#webcis) for the `<table>`, `<tr>`, and `<td>` elements.

Expand for an example workaround
The above example assumes the existence of `_includes/my-layout.webc` (an [Eleventy layout](https://www.11ty.dev/docs/layouts/)).

**Filename**_includes/my-layout.webc

```
...
<my-table>
	<x webc:is="tr">
		<x webc:is="td">
			My Table Content
		</x>
	</x>
</my-table>
...
```

**Filename**components/my-table.webc

 ```html  ``` 

#### Rendering Modes

[Jump to section titled: Rendering Modes](https://www.11ty.dev/docs/languages/webc/#rendering-modes)
There are two different rendering modes in Eleventy: `page` and `component`. We attempt to guess the rendering mode that you’d like based on the markup you supply. The `page` rendering mode is for rendering full HTML pages. The `component` rendering mode is for fragments of HTML. Most of the time you won’t need to worry about this distinction but it is included in the documentation for completeness.

*   `page` is used when the markup starts with `<!doctype` (or `<!DOCTYPE`) or `<html` (WebC forces no-quirks parsing).
*   `component` is used otherwise.

#### Differences from HTML parsing

[Jump to section titled: Differences from HTML parsing](https://www.11ty.dev/docs/languages/webc/#differences-from-html-parsing)
Added in @11ty/webc@0.9.0 WebC processes content inside of both `<template>` and `<noscript>` tags. The HTML parser treats these as plaintext.

Eleventy + WebC Features
------------------------

[Jump to section titled: Eleventy + WebC Features](https://www.11ty.dev/docs/languages/webc/#eleventy-web-c-features)
### Front Matter

[Jump to section titled: Front Matter](https://www.11ty.dev/docs/languages/webc/#front-matter)
WebC in Eleventy works automatically with standard Eleventy conventions for [front matter](https://www.11ty.dev/docs/data-frontmatter/) (though front matter in Eleventy is _optional_).

**Filename**with-front-matter.webc

```
---
layout: "my-layout.webc"
---
WebC *is* HTML.
```

Expand to see an example `my-layout.webc`
The above example assumes the existence of `_includes/my-layout.webc` (an [Eleventy layout](https://www.11ty.dev/docs/layouts/)).

**Filename**_includes/my-layout.webc

```
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title>WebC Example</title>
	</head>
	<body @raw="content"></body>
</html>
```

*   Read more about the WebC properties: [`@raw`](https://www.11ty.dev/docs/languages/webc/#@raw)Added in @11ty/webc@0.7.1 and [`@html`](https://www.11ty.dev/docs/languages/webc/#@html).

_Notable note_: front matter (per standard Eleventy conventions) is supported in page-level templates only (`.webc` files in your input directory) and not in components (see below).

### Defining Components

[Jump to section titled: Defining Components](https://www.11ty.dev/docs/languages/webc/#defining-components)
Components are the magic of WebC and there are a few ways to define components in WebC:

1.   Use global no-import components specified in your config file.
2.   Specify a glob of no-import components at a directory or template level in the data cascade.
3.   You can use [`webc:import`](https://www.11ty.dev/docs/languages/webc/#webcimport) inside of your components to import another component directly.

Notably, WebC components can have any valid HTML tag name! They are not restricted to the same naming limitations as custom elements (which require a dash in the name).

#### Global no-import Components

[Jump to section titled: Global no-import Components](https://www.11ty.dev/docs/languages/webc/#global-no-import-components)
Use the `components` property in the options passed to `addPlugin` in your Eleventy configuration file to specify project-wide WebC component files available for use in any page.

We accept:

*   String (file path or glob)
*   Array (of file paths or globs) [Added in @11ty/eleventy-plugin-webc@0.9.2](https://github.com/11ty/eleventy-plugin-webc/releases/tag/v0.9.2)
*   [`npm:` prefix aliases](https://www.11ty.dev/docs/languages/webc/#webcimport)[Added in @11ty/eleventy-plugin-webc@0.9.2](https://github.com/11ty/eleventy-plugin-webc/releases/tag/v0.9.2)

eleventy.config.js

```
import pluginWebc from "@11ty/eleventy-plugin-webc";

export default function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc, {
		// Glob to find no-import global components
		// This path is relative to the project-root!
		// The default value is shown:
		components: "_components/**/*.webc",

		// or an Array (Eleventy WebC v0.9.2+)
		components: [
			"_components/**/*.webc",
			"npm:@11ty/is-land/*.webc",
			"npm:@11ty/eleventy-plugin-syntaxhighlight/*.webc",
		],
	});
};
```

```
const pluginWebc = require("@11ty/eleventy-plugin-webc");

module.exports = function (eleventyConfig) {
	eleventyConfig.addPlugin(pluginWebc, {
		// Glob to find no-import global components
		// This path is relative to the project-root!
		// The default value is shown:
		components: "_components/**/*.webc",

		// or an Array (Eleventy WebC v0.9.2+)
		components: [
			"_components/**/*.webc",
			"npm:@11ty/is-land/*.webc",
			"npm:@11ty/eleventy-plugin-syntaxhighlight/*.webc",
		],
	});
};
```

Notably, the path for `components` is relative to your project root (**not** your [project’s `input` directory](https://www.11ty.dev/docs/config/#input-directory)).

The file names of components found in the glob determine the global tag name used in your project (e.g. `_components/my-component.webc` will give you access to `<my-component>`).

#### Declaring Components in Front Matter

[Jump to section titled: Declaring Components in Front Matter](https://www.11ty.dev/docs/languages/webc/#declaring-components-in-front-matter)
You can also use and configure specific components in front matter (or, via any part of the data cascade—scoped to a folder or a template) by assigning a glob (or array of globs) to the property at `webc.components`:

**Filename**my-directory/my-page.webc

```
---
layout: "my-layout.webc"
webc:
  components: "./webc/*.webc"
---

<my-webc-component>WebC *is* HTML.</my-webc-component>
```

WARNING

By default these paths are relative to the template file. If you’re setting this in the data cascade in a directory data file that will apply multiple child folders deep, it might be better to:

1.   Use the global no-import components option.
2.   Use `~/` as a prefix (e.g. `~/my-directory/webc/*.webc`) to alias to the project’s root directory.

### Official WebC Components

[Jump to section titled: Official WebC Components](https://www.11ty.dev/docs/languages/webc/#official-web-c-components)
The following plugins offer official WebC components for use in your projects:

*   `@11ty/is-land` supplies `<is-land>`
    *   Example: `<is-land webc:import="npm:@11ty/is-land">`
    *   Read more at [Use with `is-land`](https://www.11ty.dev/docs/languages/webc/#use-with-is-land)

*   `@11ty/eleventy-plugin-syntaxhighlight` supplies `<syntax-highlight>`
    *   Example: `<syntax-highlight language="js" webc:import="npm:@11ty/eleventy-plugin-syntaxhighlight">`
    *   Read more at [Syntax Highlighting Plugin](https://www.11ty.dev/docs/plugins/syntaxhighlight/#syntax-highlight-source-code)

*   `@11ty/eleventy-img` supplies `<eleventy-image>`
    *   Added in Image v3.1.0
    *   Example: `<img webc:is="eleventy-image" webc:import="npm:@11ty/eleventy-img">`
    *   Read more at [the Image WebC component](https://www.11ty.dev/docs/plugins/image-webc/).

### Eleventy Data Cascade

[Jump to section titled: Eleventy Data Cascade](https://www.11ty.dev/docs/languages/webc/#eleventy-data-cascade)
To access **global data** from the Data Cascade, you can use `$data` variable in your component's javascript. For example:

For example, if you have this in `_data/site.json`:

```
{
  "title": "My Site Title"
}
```

In an internal webc component, that is in a sub-folder such as `src/_includes/components/*`, you can access that data via:

`<h1 @text="$data.site.title"></h1>`
In a top-level webc component, such as a layout file or other *.webc files in the Eleventy input folder, you can access global data variables directly without `$data`:

`<h1 @text="site.title"></h1>`
### CSS and JS (Bundler mode)

[Jump to section titled: CSS and JS (Bundler mode)](https://www.11ty.dev/docs/languages/webc/#css-and-js-bundler-mode)
Eleventy WebC will bundle any specific page’s assets (CSS and JS used by components on the page). These are automatically rolled up when a component uses `<script>`, `<script src>`, `<style>`, or `<link rel="stylesheet">`. You can use this to implement component-driven Critical CSS.

Note on **Declarative Shadow DOM**: elements inside of [declarative shadow root](https://web.dev/declarative-shadow-dom/) template (`<template shadowrootmode>` or the deprecated `<template shadowroot>`) are left as is and **not bundled**.

**Filename**_components/my-webc-component.webc

```
<style>
	/* This is component CSS */
</style>
<script>
	/* This is component JS */
</script>

<!-- Local file references work too -->
<link rel="stylesheet" href="my-file.css" />
<script src="my-file.js"></script>
```

As shown above this also includes `<link rel="stylesheet">` and `<script src>` when the URLs point to files on the file system ([remote URL sources are not yet supported](https://github.com/11ty/webc/issues/15)).

You can opt-out of bundling on a per-element basis [using `webc:keep`](https://www.11ty.dev/docs/languages/webc/#webckeep).

**Filename**_includes/layout.webc

```
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title>WebC Example</title>

		<!-- inline bundles -->
		<style @raw="getBundle('css')" webc:keep></style>
		<script @raw="getBundle('js')" webc:keep></script>

		<!-- or write your bundle to a file -->
		<link rel="stylesheet" :href="getBundleFileUrl('css')" webc:keep />
		<script :src="getBundleFileUrl('js')" webc:keep></script>
	</head>
	<body @raw="content"></body>
</html>
```

*   Added in @11ty/eleventy-plugin-webc@0.9.0 Eleventy WebC uses the [Bundle Plugin](https://www.11ty.dev/docs/plugins/bundle/#using-with-webc) behind the scenes to implement bundling. `getBundle('css')` and `getBundle('js')` can now be used instead of `getCss(page.url)` and `getJs(page.url)` respectively.
*   Added in @11ty/webc@0.8.0`webc:keep` is required on `<style>` and `<script>` in your layout files to prevent re-bundling the bundles.
*   Added in @11ty/webc@0.8.0 The `getCss` and `getJs` helpers are now available to all WebC templates without restriction. Previous versions required them to be used in an _Eleventy Layout_ file.
*   `@raw` was Added in @11ty/webc@0.7.1. Previous versions can use `webc:raw @html`.

#### Bundle Code Ordering

[Jump to section titled: Bundle Code Ordering](https://www.11ty.dev/docs/languages/webc/#bundle-code-ordering)
The order of the code in these bundles is determined by the dependency order of the components, from most specific to least specific!

Expand to see an example
Say we have an `index.webc` page that uses a `header.webc` component.

**Filename**index.webc

```
<style>
	/* index.webc */
</style>
<header></header>
```

**Filename**_components/header.webc

```
<style>
	/* header.webc */
</style>
```

The CSS bundle will look like:

```
/* header.webc */
/* index.webc */
```

#### Access Bundles in other Template Engines

[Jump to section titled: Access Bundles in other Template Engines](https://www.11ty.dev/docs/languages/webc/#access-bundles-in-other-template-engines)
You can access these bundles in other templates types too (`.njk`, `.liquid`, etc.).

Added in @11ty/eleventy-plugin-webc@0.9.0 Eleventy WebC uses the [Bundle Plugin](https://www.11ty.dev/docs/plugins/bundle/#using-with-webc) behind the scenes to implement bundling. This plugin provides `getBundle` and `getBundleFileUrl` universal shortcodes for use in any template type (including WebC as shown above).

_WebC v0.8.0 and older:_ Check out the deprecated (but still in place for backwards compatibility) `webcGetCss` and `webcGetJs` universal filters for bundle output.
**Filename**_includes/layout.njk

```
<style>{{ page.url | webcGetCss | safe }}</style>
<script>{{ page.url | webcGetJs | safe }}</script>
<!-- write to a file -->
<link rel="stylesheet" href="{% getBundleFileUrl "css" %}">
```

**Filename**_includes/layout.liquid

```
<style>{{ page.url | webcGetCss }}</style>
<script>{{ page.url | webcGetJs }}</script>
```

### Asset bucketing

[Jump to section titled: Asset bucketing](https://www.11ty.dev/docs/languages/webc/#asset-bucketing)
There is an additional layer of bundling here that you can use that we call Bucketing. Components can use `webc:bucket` to output to any arbitrary bucket name.

In this component, we have component code that outputs to two separate buckets:

**Filename**_components/my-webc-component.webc

```
<style>
	/* This CSS is put into the default bucket */
</style>
<script>
	/* This JS is put into the default bucket */
</script>
<style webc:bucket="defer">
	/* This CSS is put into the `defer` bucket */
</style>
<script webc:bucket="defer">
	/* This JS is put into the `defer` bucket */
</script>
```

When `<my-webc-component>` is used on a page, it will roll the assets to the page-specific bucket bundles for CSS and JavaScript.

Then you can output those bucket bundles anywhere on your page like this (here we’re using an Eleventy layout file):

**Filename**_includes/layout.webc

```
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8" />
		<title>WebC Example</title>
		<!-- Default bucket -->
		<style @raw="getBundle('css')" webc:keep></style>
		<script @raw="getBundle('js')" webc:keep></script>
	</head>
	<body>
		<template @raw="content" webc:nokeep></template>

		<!-- `defer` bucket -->
		<style @raw="getBundle('css', 'defer')" webc:keep></style>
		<script @raw="getBundle('js', 'defer')" webc:keep></script>
	</body>
</html>
```

*   Added in @11ty/webc@0.8.0`webc:keep` is required on `<style>` and `<script>` in your layout files to prevent re-bundling the bundles.
*   Added in @11ty/webc@0.9.1`:webc:bucket` (dynamic attribute) is supported to set this value via JavaScript. [#120](https://github.com/11ty/webc/issues/120)

#### Cascading Asset Buckets

[Jump to section titled: Cascading Asset Buckets](https://www.11ty.dev/docs/languages/webc/#cascading-asset-buckets)
[Added in @11ty/webc@0.9.1](https://github.com/11ty/webc/releases/tag/v0.9.1) Additionally `webc:bucket` can be added to any tag and will cascade to all child content.

Consider this WebC page:

**Filename**index.webc

```
<!-- has an implied webc:bucket="default" -->
<my-component></my-component>

<div webc:bucket="defer">
	<!-- each of these have webc:bucket="defer" -->
	<!-- (including any nested components inside, too) -->
	<footnote-references></footnote-references>

	<my-footer></my-footer>
</div>
```

Setting `webc:bucket` now cascades to all of the children as if they had `webc:bucket="defer"` assigned to each of them individually. All assets used in those components will now be rolled up into the `defer` bucket.

##### Conflicts and hoisting

What happens when a component is used in multiple distinct buckets?

**Filename**index.webc

```
<!-- has an implied webc:bucket="default" -->
<my-component></my-component>

<div webc:bucket="defer">
	<my-component></my-component>
</div>
```

When duplicates and conflicts occur, WebC will hoist the component code to find the nearest shared bucket for you. In the above example, the CSS and JS for `<my-component>` will be loaded in the `default` bucket and only in the `default` bucket.

### Use with `is-land`

[Jump to section titled: Use with is-land](https://www.11ty.dev/docs/languages/webc/#use-with-is-land)
You can also use this out of the box with Eleventy’s [`is-land` component for web component hydration](https://www.11ty.dev/docs/plugins/is-land/).

At the component level, components can declare their own is-land loading conditions.

**Filename**index.webc

```
<is-land on:visible webc:import="npm:@11ty/is-land">
	<template data-island>
		<!-- CSS -->
		<style webc:keep>
			/* This CSS applies on:visible */
		</style>
		<link rel="stylesheet" href="arbitrary.css" webc:keep />

		<!-- JS -->
		<script type="module" webc:keep>
			console.log("This JavaScript runs on:visible");
		</script>
		<script type="module" src="arbitrary.js" webc:keep></script>
	</template>
</is-land>
```
[Jump to section titled: From the Community](https://www.11ty.dev/docs/languages/webc/#from-the-community)
×57 resources via **[11tybundle.dev](https://11tybundle.dev/)** curated by [![Image 2: Favicon for v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.bobmonsour.com%2F](https://v1.indieweb-avatar.11ty.dev/https%3A%2F%2Fwww.bobmonsour.com%2F/)Bob Monsour](https://www.bobmonsour.com/).

**_Expand to see 52 more resources._**

* * *

Template Languages:

*   [HTML `*.html`](https://www.11ty.dev/docs/languages/html/)
*   [Markdown `*.md`](https://www.11ty.dev/docs/languages/markdown/)
*   [WebC `*.webc`](https://www.11ty.dev/docs/languages/webc/)
*   [JavaScript `*.11ty.js`](https://www.11ty.dev/docs/languages/javascript/)
*   [Liquid `*.liquid`](https://www.11ty.dev/docs/languages/liquid/)
*   [Nunjucks `*.njk`](https://www.11ty.dev/docs/languages/nunjucks/)
*   [Handlebars `*.hbs`](https://www.11ty.dev/docs/languages/handlebars/)
*   [Mustache `*.mustache`](https://www.11ty.dev/docs/languages/mustache/)
*   [EJS `*.ejs`](https://www.11ty.dev/docs/languages/ejs/)
*   [Haml `*.haml`](https://www.11ty.dev/docs/languages/haml/)
*   [Pug `*.pug`](https://www.11ty.dev/docs/languages/pug/)
*   [TypeScript `*.ts`](https://www.11ty.dev/docs/languages/typescript/)
*   [JSX `*.jsx`](https://www.11ty.dev/docs/languages/jsx/)
*   [MDX `*.mdx`](https://www.11ty.dev/docs/languages/mdx/)
*   [Sass `*.scss`](https://www.11ty.dev/docs/languages/sass/)
*   [Custom `*.*`](https://www.11ty.dev/docs/languages/custom/)

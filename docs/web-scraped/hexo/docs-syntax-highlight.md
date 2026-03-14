# Source: https://hexo.io/docs/syntax-highlight

Title: Syntax Highlighting

URL Source: https://hexo.io/docs/syntax-highlight

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Hexo
Docs
API
News
Plugins
Themes
About
Search
English
English
正體中文
简体中文
Русский
한국어
Português (Brasil)
ภาษาไทย
日本語
Español
Syntax Highlighting

Hexo has two built-in syntax highlight libraries, highlight.js and prismjs. This tutorial shows you how to integrate Hexo’s built-in syntax highlight into your template.

How to use code block in posts

Hexo supports two ways to write code block: Tag Plugin - Code Block and Tag Plugin - Backtick Code Block:

{% codeblock [title] [lang:language] [url] [link text] [additional options] %}
code snippet
{% endcodeblock %}

{% code [title] [lang:language] [url] [link text] [additional options] %}
code snippet
{% endcode %}

```[language] [title] [url] [link text] [additional options]
code snippet
```

The third syntax is Markdown’s fenced code block syntax, and Hexo extends it to support more features. Check out Tag Plugin Docs to find out the options available.

Tip: Hexo support posts written in any format, so long the corresponding renderer plugin is installed. It can be in markdown, ejs, swig, nunjucks, pug, asciidoc, etc. Regardless of the format used, those three code block syntax will always be available.

Configuration

below v7.0.0:

# _config.yml

highlight:
  enable: true
  auto_detect: false
  line_number: true
  line_threshold: 0
  tab_replace: ""
  exclude_languages:
    - example
  wrap: true
  hljs: false
prismjs:
  enable: false
  preprocess: true
  line_number: true
  line_threshold: 0
  tab_replace: ""

v7.0.0+:

# _config.yml

syntax_highlighter: highlight.js
highlight:
  auto_detect: false
  line_number: true
  line_threshold: 0
  tab_replace: ""
  exclude_languages:
    - example
  wrap: true
  hljs: false
prismjs:
  preprocess: true
  line_number: true
  line_threshold: 0
  tab_replace: ""

The YAML above is Hexo’s default configuration.

Disabled

below v7.0.0:

# _config.yml

highlight:
  enable: false
prismjs:
  enable: false

v7.0.0+:

# _config.yml

syntax_highlighter: # empty

When both highlight.enable and prismjs.enable are false (below v7.0.0) or syntax_highlighter is empty (v7.0.0+), the output HTML of the code block is controlled by the corresponding renderer. For example, marked.js (used by hexo-renderer-marked, the default markdown renderer of Hexo) will add the language code to the class of <code>:

```yaml
hello: hexo
```

<pre>
  <code class="yaml">hello: hexo</code>
</pre>

When no built-in syntax highlight is enabled, you can either install third-party syntax-highlight plugin, or use a browser-side syntax highlighter (e.g. highlight.js and prism.js both support running in browser).

Highlight.js

below v7.0.0:

# _config.yml

highlight:
  enable: true
  auto_detect: false
  line_number: true
  line_threshold: 0
  tab_replace: "  "
  exclude_languages:
    - example
  wrap: true
  hljs: false
prismjs:
  enable: false

v7.0.0+:

# _config.yml

syntax_highlighter: highlight.js
highlight:
  auto_detect: false
  line_number: true
  line_threshold: 0
  tab_replace: "  "
  exclude_languages:
    - example
  wrap: true
  hljs: false

highlight.js is enabled by default and used as server-side highlighting in Hexo; it needs to be disabled if you prefer to run highlight.js on browser-side.

Server-side means, the syntax highlight is generated during hexo generate or hexo server.

auto_detect

auto_detect is a highlight.js feature that detects language of the code block automatically.

Tip: When you want to use “sublanguage highlight”, enable auto_detect and don’t mark language when writing code block.

Warning!

auto_detect is very resource-intensive. Do not enable it unless you really need “sublanguage highlight” or prefer not to mark language when writing code block.

line_number

highlight.js does not support line number.

Hexo adds line number by wrapping output inside <figure> and <table>:

<figure class="highlight yaml">
  <table>
    <tbody>
      <tr>
        <td class="gutter">
          <pre><span class="line">1</span><br></pre>
        </td>
        <td class="code">
          <pre><span class="line"><span class="attr">hello:</span><span class="string">hexo</span></span><br></pre>
        </td>
      </tr>
    </tbody>
  </table>
</figure>

It is not the behavior of highlight.js and requires custom CSS for <figure> and <table> elements; some themes have built-in support.

You might also notice that all class has no hljs- prefixed, we will revisit it later part.

line_threshold (+6.1.0)

Accepts an optional threshold to only show line numbers as long as the numbers of lines of the code block exceed such threshold. Default is 0.

tab_replace

Replace tabs inside code block with given string. By default it is 2 spaces.

exclude_languages (+6.1.0)

Only wrap with <pre><code class="lang"></code></pre> and will not render all tags(span, and br) in content if are languages match this option.

wrap

Hexo wraps the output inside <figure> and <table> to support line number. You need to disable both line_number and wrap to revert to highlight.js‘s behavior:

<pre><code class="yaml">
<span class="comment"># _config.yml</span>
<span class="attr">hexo:</span> <span class="string">hexo</span>
</code></pre>

Warning!

Because line_number feature relies on wrap, you can’t disable wrap with line_number enabled: If you set line_number to true, wrap will be automatically enabled.

hljs

When hljs is set to true, all the HTML output will have class prefixed with hljs- (regardless wrap is enabled or not):

<pre><code class="yaml hljs">
<span class="hljs-comment"># _config.yml</span>
<span class="hljs-attr">hexo:</span> <span class="hljs-string">hexo</span>
</code></pre>

Tip: When line_number is set to false, wrap is set to false and hljs is set to true, you can then use highlight.js theme directly in your site.

PrismJS

below v7.0.0:

# _config.yml

highlight:
  enable: false
prismjs:
  enable: true
  preprocess: true
  line_number: true
  line_threshold: 0
  tab_replace: ""

v7.0.0+:

# _config.yml

syntax_highlighter: prismjs
prismjs:
  preprocess: true
  line_number: true
  line_threshold: 0
  tab_replace: ""

Prismjs is disabled by default. You should set highlight.enable to false (below v7.0.0) or set syntax_highlighter to prismjs (v7.0.0+) before enabling prismjs.

preprocess

Hexo’s built-in prismjs supports both browser-side (preprocess set to false) and server-side (preprocess set to true).

When use server-side mode (set preprocess to true), you only need to include prismjs theme (css stylesheet) in your website. When use browser-side (set preprocess to false), you have to include the javascript library as well.

Prismjs is designed to be used in browser, thus under preprocess mode only limited prismjs plugin is supported:

Line Numbers: Only prism-line-numbers.css is required, No need to include prism-line-numbers.js in your website. Hexo will generate required HTML mark up mark up for you.
Show Languages: Hexo will always have data-language attribute added as long as language is given for the code block.
Any other prism plugins that don’t need special HTML markup are supported as well, but you will have to include JavaScript required by those plugins.

All prism plugins are supported if preprocess is set to false. Here are a few things you should still pay attention to:

Line Numbers: Hexo won’t generate required HTML mark up when preprocess is set to false. Requires both prism-line-numbers.css and prism-line-numbers.js.
Show Languages: Hexo will always have data-language attribute added as long as language is given for the code block.
Line Highlight: Both Hexo Tag Plugin - Code Block and Tag Plugin - Backtick Code Block supports Line Highlight syntax (mark option). When mark option is given, Hexo will generate the corresponding HTML markup.
line_number

With both preprocess and line_number set to true, you just need to include prism-line-numbers.css to make line-numbering work. If you set both preprocess and line_number to false, you will need both prism-line-numbers.css and prism-line-numbers.js.

line_threshold (+6.1.0)

Accepts an optional threshold to only show line numbers as long as the numbers of lines of the code block exceed such threshold. Default is 0.

tab_replace

Replace \t inside code block with given string. By default it is 2 spaces.

Other useful information
Highlight.js
PrismJS

The source codes behind Hexo’s syntax highlighting are available in:

Highlight.js Utility Functions
PrismJS Utility Functions
Tag Plugin - Code Block
Tag Plugin - Backtick Code Block
Last updated: 2026-03-12
PREV
NEXT
Contents
How to use code block in posts
Configuration
Disabled
Highlight.js
auto_detect
line_number
line_threshold (+6.1.0)
tab_replace
exclude_languages (+6.1.0)
wrap
hljs
PrismJS
preprocess
line_number
line_threshold (+6.1.0)
tab_replace
Other useful information
Back to Top
Getting Started
Overview
Setup
Configuration
Commands
Migration
Basic Usage
Writing
Front-matter
Tag Plugins
Asset Folders
Data Files
Server
Generating
Deployment
GitHub Pages
GitLab Pages
One-Command Deployment
Customization
Permalinks
Themes
Templates
Variables
Helpers
Internationalization (i18n)
Syntax Highlight
Plugins
Miscellaneous
Troubleshooting
Contributing
© 2026 Hexo
Documentation licensed under CC BY 4.0.
  
Docs
API
News
Plugins
Themes
About
GitHub
Getting Started
Overview
Setup
Configuration
Commands
Migration
Basic Usage
Writing
Front-matter
Tag Plugins
Asset Folders
Data Files
Server
Generating
Deployment
GitHub Pages
GitLab Pages
One-Command Deployment
Customization
Permalinks
Themes
Templates
Variables
Helpers
Internationalization (i18n)
Syntax Highlight
Plugins
Miscellaneous
Troubleshooting
Contributing
English
English
正體中文
简体中文
Русский
한국어
Português (Brasil)
ภาษาไทย
日本語
Español

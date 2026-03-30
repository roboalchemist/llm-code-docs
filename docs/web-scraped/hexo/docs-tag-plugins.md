# Source: https://hexo.io/docs/tag-plugins

Title: Tag Plugins

URL Source: https://hexo.io/docs/tag-plugins

Published Time: 2026-03-12T00:23:04.147Z

Markdown Content:
Tag Plugins | Hexo
===============

[Hexo](https://hexo.io/)
========================

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)[](https://github.com/hexojs/hexo)

English

[](https://hexo.io/docs/tag-plugins)

Tag Plugins
===========

[](https://github.com/hexojs/site/edit/master/source/docs/tag-plugins.md "Improve this doc")

Tag plugins are different from post tags. They are ported from Octopress and provide a useful way for you to quickly add specific content to your posts.

Although you can write your posts in any format, the tag plugins will always be available and syntax remains the same.

_Tag plugins should not be wrapped inside Markdown syntax, e.g. `[]({% post\_path lorem-ipsum %})` is not supported._

[](https://hexo.io/docs/tag-plugins#Block-Quote "Block Quote")Block Quote[](https://hexo.io/docs/tag-plugins#Block-Quote)
-------------------------------------------------------------------------------------------------------------------------

Perfect for adding quotes to your post, with optional author, source and title information.

**Alias:** quote

{% blockquote [author[, source]] [link] [source_link_title] %}

content

{% endblockquote %}

### [](https://hexo.io/docs/tag-plugins#Examples "Examples")Examples[](https://hexo.io/docs/tag-plugins#Examples)

**No arguments. Plain blockquote.**

{% blockquote %}

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque hendrerit lacus ut purus iaculis feugiat. Sed nec tempor elit, quis aliquam neque. Curabitur sed diam eget dolor fermentum semper at eu lorem.

{% endblockquote %}

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque hendrerit lacus ut purus iaculis feugiat. Sed nec tempor elit, quis aliquam neque. Curabitur sed diam eget dolor fermentum semper at eu lorem.

**Quote from a book**

{% blockquote David Levithan, Wide Awake %}

Do not just seek happiness for yourself. Seek happiness for all. Through kindness. Through mercy.

{% endblockquote %}

> Do not just seek happiness for yourself. Seek happiness for all. Through kindness. Through mercy.
>
> **David Levithan**Wide Awake

**Quote from Twitter**

{% blockquote @DevDocs https://twitter.com/devdocs/status/356095192085962752 %}

NEW: DevDocs now comes with syntax highlighting. http://devdocs.io

{% endblockquote %}

> NEW: DevDocs now comes with syntax highlighting. [http://devdocs.io](http://devdocs.io/)
>
> **@DevDocs**[twitter.com/devdocs/status/356095192085962752](https://twitter.com/devdocs/status/356095192085962752)

**Quote from an article on the web**

{% blockquote Seth Godin http://sethgodin.typepad.com/seths_blog/2009/07/welcome-to-island-marketing.html Welcome to Island Marketing %}

Every interaction is both precious and an opportunity to delight.

{% endblockquote %}

> Every interaction is both precious and an opportunity to delight.
>
> **Seth Godin**[Welcome to Island Marketing](http://sethgodin.typepad.com/seths_blog/2009/07/welcome-to-island-marketing.html)

[](https://hexo.io/docs/tag-plugins#Code-Block "Code Block")Code Block[](https://hexo.io/docs/tag-plugins#Code-Block)
---------------------------------------------------------------------------------------------------------------------

A useful feature for adding code snippets to your post.

**Alias:** code

{% codeblock [title] [lang:language] [url] [link text] [additional options] %}

code snippet

{% endcodeblock %}

Specify additional options in `option:value` format, e.g. `line_number:false first_line:5`.

| Extra Options | Description | Default |
| --- | --- | --- |
| `line_number` | Show line number | `true` |
| `line_threshold` | Only show line numbers as long as the numbers of lines of the code block exceed such threshold. | `0` |
| `highlight` | Enable code highlighting | `true` |
| `first_line` | Specify the first line number | `1` |
| `mark` | Line highlight specific line(s), each value separated by a comma. Specify the number range using a dash Example: `mark:1,4-7,10` will mark lines 1, 4 to 7 and 10. |  |
| `wrap` | Wrap the code block in [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table) | `true` |

### [](https://hexo.io/docs/tag-plugins#Examples-1 "Examples")Examples[](https://hexo.io/docs/tag-plugins#Examples-1)

**A plain code block**

{% codeblock %}

alert('Hello World!');

{% endcodeblock %}

alert('Hello World!');

**Specifying the language**

{% codeblock lang:objc %}

[rectangle setX: 10 y: 10 width: 20 height: 20];

{% endcodeblock %}

[rectangle setX: 10 y: 10 width: 20 height: 20];

**Adding a caption to the code block**

{% codeblock Array.map %}

array.map(callback[, thisArg])

{% endcodeblock %}

Array.map

array.map(callback[, thisArg])

**Adding a caption and a URL**

{% codeblock _.compact http://underscorejs.org/#compact Underscore.js %}

_.compact([0, 1, false, 2, '', 3]);

=> [1, 2, 3]

{% endcodeblock %}

_.compact[Underscore.js](http://underscorejs.org/#compact)

\_.compact([0, 1, false, 2, '', 3]);

=> [1, 2, 3]

[](https://hexo.io/docs/tag-plugins#Backtick-Code-Block "Backtick Code Block")Backtick Code Block[](https://hexo.io/docs/tag-plugins#Backtick-Code-Block)
---------------------------------------------------------------------------------------------------------------------------------------------------------

This is identical to using a code block, but instead uses three backticks to delimit the block.

`` [language] [title] [url] [link text] code snippet ``
[](https://hexo.io/docs/tag-plugins#Pull-Quote "Pull Quote")Pull Quote[](https://hexo.io/docs/tag-plugins#Pull-Quote)
---------------------------------------------------------------------------------------------------------------------

To add pull quotes to your posts:

{% pullquote [class] %}

content

{% endpullquote %}

[](https://hexo.io/docs/tag-plugins#jsFiddle-deleted-in-v7-0-0 "jsFiddle (deleted in v7.0.0)")jsFiddle (deleted in `v7.0.0`)[](https://hexo.io/docs/tag-plugins#jsFiddle-deleted-in-v7-0-0)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> The tag was removed in Hexo 7.0.0. We have provided a plugin [hexo-tag-embed](https://github.com/hexojs/hexo-tag-embed) for backward compatibility with your existing posts.

To embed a jsFiddle snippet:

{% jsfiddle shorttag [tabs] [skin] [width] [height] %}

[](https://hexo.io/docs/tag-plugins#Gist-deleted-in-v7-0-0 "Gist (deleted in v7.0.0)")Gist (deleted in `v7.0.0`)[](https://hexo.io/docs/tag-plugins#Gist-deleted-in-v7-0-0)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Please use [hexo-tag-embed](https://github.com/hexojs/hexo-tag-embed) instead if you use `v7.0.0+`.

To embed a Gist snippet:

{% gist gist_id [filename] %}

[](https://hexo.io/docs/tag-plugins#iframe "iframe")iframe[](https://hexo.io/docs/tag-plugins#iframe)
-----------------------------------------------------------------------------------------------------

To embed an iframe:

{% iframe url [width] [height] %}

[](https://hexo.io/docs/tag-plugins#Image "Image")Image[](https://hexo.io/docs/tag-plugins#Image)
-------------------------------------------------------------------------------------------------

Inserts an image with specified size.

{% img [class names] /path/to/image [width] [height] '"title text" "alt text"' %}

[](https://hexo.io/docs/tag-plugins#Link "Link")Link[](https://hexo.io/docs/tag-plugins#Link)
---------------------------------------------------------------------------------------------

Inserts a link with `target="_blank"` attribute.

{% link text url [external] [title] %}

[](https://hexo.io/docs/tag-plugins#Include-Code "Include Code")Include Code[](https://hexo.io/docs/tag-plugins#Include-Code)
-----------------------------------------------------------------------------------------------------------------------------

Inserts code snippets in `source/downloads/code` folder. The folder location can be specified through the `code_dir` option in the config.

{% include_code [title] [lang:language] [from:line] [to:line] path/to/file %}

### [](https://hexo.io/docs/tag-plugins#Examples-2 "Examples")Examples[](https://hexo.io/docs/tag-plugins#Examples-2)

**Embed the whole content of test.js**

{% include_code lang:javascript test.js %}

**Embed line 3 only**

{% include_code lang:javascript from:3 to:3 test.js %}

**Embed line 5 to 8**

{% include_code lang:javascript from:5 to:8 test.js %}

**Embed line 5 to the end of file**

{% include_code lang:javascript from:5 test.js %}

**Embed line 1 to 8**

{% include_code lang:javascript to:8 test.js %}

[](https://hexo.io/docs/tag-plugins#YouTube-deleted-in-v7-0-0 "YouTube (deleted in v7.0.0)")YouTube (deleted in `v7.0.0`)[](https://hexo.io/docs/tag-plugins#YouTube-deleted-in-v7-0-0)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Please use [hexo-tag-embed](https://github.com/hexojs/hexo-tag-embed) instead if you use `v7.0.0+`.

Inserts a YouTube video.

{% youtube video_id [type] [cookie] %}

### [](https://hexo.io/docs/tag-plugins#Examples-3 "Examples")Examples[](https://hexo.io/docs/tag-plugins#Examples-3)

**Embed a video**

{% youtube lJIrF4YjHfQ %}

**Embed a playlist**

{% youtube PL9hW1uS6HUfscJ9DHkOSoOX45MjXduUxo 'playlist' %}

**Enable privacy-enhanced mode**

YouTube’s cookie is not used in this mode.

{% youtube lJIrF4YjHfQ false %}

{% youtube PL9hW1uS6HUfscJ9DHkOSoOX45MjXduUxo 'playlist' false %}

[](https://hexo.io/docs/tag-plugins#Vimeo-deleted-in-v7-0-0 "Vimeo (deleted in v7.0.0)")Vimeo (deleted in `v7.0.0`)[](https://hexo.io/docs/tag-plugins#Vimeo-deleted-in-v7-0-0)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Please use [hexo-tag-embed](https://github.com/hexojs/hexo-tag-embed) instead if you use `v7.0.0+`.

Inserts a responsive or specified size Vimeo video.

{% vimeo video_id [width] [height] %}

[](https://hexo.io/docs/tag-plugins#Include-Posts "Include Posts")Include Posts[](https://hexo.io/docs/tag-plugins#Include-Posts)
---------------------------------------------------------------------------------------------------------------------------------

Include links to other posts.

{% post_path filename %}

{% post_link filename [title] [escape] %}

You can ignore permalink and folder information, like languages and dates, when using this tag.

For instance: `{% post_link how-to-bake-a-cake %}`.

This will work as long as the filename of the post is `how-to-bake-a-cake.md`, even if the post is located at `source/posts/2015-02-my-family-holiday` and has permalink `2018/en/how-to-bake-a-cake`.

You can customize the text to display, instead of displaying the post’s title.

Post’s title and custom text are escaped by default. You can use the `escape` option to disable escaping.

For instance:

**Display title of the post.**

`{% post_link hexo-3-8-released %}`

[Hexo 3.8.0 Released](https://hexo.io/news/2018/10/19/hexo-3-8-released/ "Hexo 3.8.0 Released")
**Display custom text.**

`{% post_link hexo-3-8-released 'Link to a post' %}`

[Link to a post](https://hexo.io/news/2018/10/19/hexo-3-8-released/ "Hexo 3.8.0 Released")
**Escape title.**

{% post_link hexo-4-released 'How to use <b> tag in title' %}
[How to use <b> tag in title](https://hexo.io/news/2019/10/14/hexo-4-released/ "Hexo 4.0.0 Released")
**Do not escape title.**

{% post_link hexo-4-released '<b>bold</b> custom title' false %}
[**bold** custom title](https://hexo.io/news/2019/10/14/hexo-4-released/ "Hexo 4.0.0 Released")
[](https://hexo.io/docs/tag-plugins#Include-Assets "Include Assets")Include Assets[](https://hexo.io/docs/tag-plugins#Include-Assets)
-------------------------------------------------------------------------------------------------------------------------------------

Include post assets, to be used in conjunction with [`post_asset_folder`](https://hexo.io/docs/asset-folders).

{% asset_path filename %}

{% asset_img [class names] slug [width] [height] [title text [alt text]] %}

{% asset_link filename [title] [escape] %}

### [](https://hexo.io/docs/tag-plugins#Embed-image "Embed image")Embed image[](https://hexo.io/docs/tag-plugins#Embed-image)

_hexo-renderer-marked 3.1.0+ can (optionally) resolves the post’s path of an image automatically, refer to [this section](https://hexo.io/docs/asset-folders#Embedding-an-image-using-markdown) on how to enable it._

“foo.jpg” is located at `http://example.com/2020/01/02/hello/foo.jpg`.

**Default (no option)**

`{% asset_img foo.jpg %}`

<img src="/2020/01/02/hello/foo.jpg" />

**Custom class**

`{% asset_img post-image foo.jpg %}`

<img src="/2020/01/02/hello/foo.jpg" class="post-image" />

**Display size**

`{% asset_img foo.jpg 500 400 %}`

<img src="/2020/01/02/hello/foo.jpg" width="500" height="400" />

**Title & Alt**

`{% asset_img foo.jpg "lorem ipsum'dolor'" %}`

<img src="/2020/01/02/hello/foo.jpg" title="lorem ipsum" alt="dolor" />

[](https://hexo.io/docs/tag-plugins#URL "URL")URL[](https://hexo.io/docs/tag-plugins#URL)
-----------------------------------------------------------------------------------------

### [](https://hexo.io/docs/tag-plugins#url-for-7-0-0 "url_for (7.0.0+)")url_for (7.0.0+)[](https://hexo.io/docs/tag-plugins#url-for-7-0-0)

Returns a url with the root path prefixed. Output is encoded automatically.

{% url_for text path [relative] %}

**Examples:**

_config.yml

root: /blog/ # example

{% url_for blog index.html %}

<a href="/blog/index.html">blog</a>

Relative link, follows `relative_link` option by default

e.g. post/page path is ‘/foo/bar/index.html’

_config.yml

relative_link: true

{% url_for blog index.html %}

<a href="../../index.html">blog</a>

You could also disable it to output a non-relative link, even when `relative_link` is enabled and vice versa.

{% url_for blog index.html false %}

<a href="/index.html">blog</a>

### [](https://hexo.io/docs/tag-plugins#full-url-for-7-0-0 "full_url_for (7.0.0+)")full_url_for (7.0.0+)[](https://hexo.io/docs/tag-plugins#full-url-for-7-0-0)

Returns a url with the `config.url` prefixed. Output is encoded automatically.

{% full_url_for text path %}

**Examples:**

_config.yml

url: https://example.com/blog # example

{% full_url_for index /a/path %}

<a href="https://example.com/blog/a/path">index</a>

[](https://hexo.io/docs/tag-plugins#Raw "Raw")Raw[](https://hexo.io/docs/tag-plugins#Raw)
-----------------------------------------------------------------------------------------

If certain content is causing processing issues in your posts, wrap it with the `raw` tag to avoid rendering errors.

{% raw %}

content

{% endraw %}

[](https://hexo.io/docs/tag-plugins#Post-Excerpt "Post Excerpt")Post Excerpt[](https://hexo.io/docs/tag-plugins#Post-Excerpt)
-----------------------------------------------------------------------------------------------------------------------------

Use text placed before the  tag as an excerpt for the post. `excerpt:` value in the [front-matter](https://hexo.io/docs/front-matter#Settings-amp-Their-Default-Values), if specified, will take precedent.

**Examples:**

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.

<!-- more -->

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Last updated: 2026-03-12[Prev](https://hexo.io/docs/front-matter "Front-matter")[Next](https://hexo.io/docs/asset-folders "Asset Folders")

**Contents**

1. [Block Quote](https://hexo.io/docs/tag-plugins#Block-Quote)
    1.   [Examples](https://hexo.io/docs/tag-plugins#Examples)

2. [Code Block](https://hexo.io/docs/tag-plugins#Code-Block)
    1.   [Examples](https://hexo.io/docs/tag-plugins#Examples-1)

3. [Backtick Code Block](https://hexo.io/docs/tag-plugins#Backtick-Code-Block)
4. [Pull Quote](https://hexo.io/docs/tag-plugins#Pull-Quote)
5. [jsFiddle (deleted in v7.0.0)](https://hexo.io/docs/tag-plugins#jsFiddle-deleted-in-v7-0-0)
6. [Gist (deleted in v7.0.0)](https://hexo.io/docs/tag-plugins#Gist-deleted-in-v7-0-0)
7. [iframe](https://hexo.io/docs/tag-plugins#iframe)
8. [Image](https://hexo.io/docs/tag-plugins#Image)
9. [Link](https://hexo.io/docs/tag-plugins#Link)
10. [Include Code](https://hexo.io/docs/tag-plugins#Include-Code)
    1.   [Examples](https://hexo.io/docs/tag-plugins#Examples-2)

11. [YouTube (deleted in v7.0.0)](https://hexo.io/docs/tag-plugins#YouTube-deleted-in-v7-0-0)
    1.   [Examples](https://hexo.io/docs/tag-plugins#Examples-3)

12. [Vimeo (deleted in v7.0.0)](https://hexo.io/docs/tag-plugins#Vimeo-deleted-in-v7-0-0)
13. [Include Posts](https://hexo.io/docs/tag-plugins#Include-Posts)
14. [Include Assets](https://hexo.io/docs/tag-plugins#Include-Assets)
    1.   [Embed image](https://hexo.io/docs/tag-plugins#Embed-image)

15. [URL](https://hexo.io/docs/tag-plugins#URL)
    1.   [url_for (7.0.0+)](https://hexo.io/docs/tag-plugins#url-for-7-0-0)
    2.   [full_url_for (7.0.0+)](https://hexo.io/docs/tag-plugins#full-url-for-7-0-0)

16. [Raw](https://hexo.io/docs/tag-plugins#Raw)
17. [Post Excerpt](https://hexo.io/docs/tag-plugins#Post-Excerpt)

[Back to Top](https://hexo.io/docs/tag-plugins#)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

 © 2026 [Hexo](https://github.com/hexojs/hexo/graphs/contributors)

 Documentation licensed under [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/).

[![Image 1](https://www.netlify.com/img/global/badges/netlify-dark.svg)](https://www.netlify.com/)[](https://twitter.com/hexojs)[](https://github.com/hexojs/hexo)

[Docs](https://hexo.io/docs/)[API](https://hexo.io/api/)[News](https://hexo.io/news/)[Plugins](https://hexo.io/plugins/)[Themes](https://hexo.io/themes/)[About](https://hexo.io/about/)*   [GitHub](https://github.com/hexojs/hexo)

**Getting Started**[Overview](https://hexo.io/docs/)[Setup](https://hexo.io/docs/setup)[Configuration](https://hexo.io/docs/configuration)[Commands](https://hexo.io/docs/commands)[Migration](https://hexo.io/docs/migration)**Basic Usage**[Writing](https://hexo.io/docs/writing)[Front-matter](https://hexo.io/docs/front-matter)[Tag Plugins](https://hexo.io/docs/tag-plugins)[Asset Folders](https://hexo.io/docs/asset-folders)[Data Files](https://hexo.io/docs/data-files)[Server](https://hexo.io/docs/server)[Generating](https://hexo.io/docs/generating)**Deployment**[GitHub Pages](https://hexo.io/docs/github-pages)[GitLab Pages](https://hexo.io/docs/gitlab-pages)[One-Command Deployment](https://hexo.io/docs/one-command-deployment)**Customization**[Permalinks](https://hexo.io/docs/permalinks)[Themes](https://hexo.io/docs/themes)[Templates](https://hexo.io/docs/templates)[Variables](https://hexo.io/docs/variables)[Helpers](https://hexo.io/docs/helpers)[Internationalization (i18n)](https://hexo.io/docs/internationalization)[Syntax Highlight](https://hexo.io/docs/syntax-highlight)[Plugins](https://hexo.io/docs/plugins)**Miscellaneous**[Troubleshooting](https://hexo.io/docs/troubleshooting)[Contributing](https://hexo.io/docs/contributing)

English
